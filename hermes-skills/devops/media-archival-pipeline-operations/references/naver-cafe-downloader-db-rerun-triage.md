# Naver Cafe Downloader DB timeout rerun triage

Use this when FastAPI/Hermes reports `Naver_Cafe_Downloader` stopped because `CommonDatabase` could not connect to PostgreSQL, e.g. `Postgres Connection Error: connection to server at "192.168.50.20", port 25432 failed: timeout expired`.

## Fast verification sequence

1. Confirm current NAS/network reachability before touching the downloader:
   ```bash
   date
   ping -c 2 -W 2000 192.168.50.20 || true
   nc -vz -w 5 192.168.50.20 25432 || true
   route get 192.168.50.20 2>/dev/null | sed -n '1,12p' || true
   ```
2. Exercise the same PostgreSQL credentials from the project runtime, not just the TCP port:
   ```bash
   cd /Users/iseungchan/Project/Python/Naver_Cafe_Downloader
   python3 - <<'PY'
   import psycopg2, time
   t=time.time()
   conn=psycopg2.connect(host='192.168.50.20', port=25432, user='navercafe', password='navercafe', dbname='navercafe', connect_timeout=5)
   cur=conn.cursor()
   cur.execute('select now(), current_database(), current_user')
   print('postgres_query=', cur.fetchone())
   cur.execute("select count(*) from information_schema.tables where table_name='naver_download_log'")
   print('naver_download_log_table_count=', cur.fetchone()[0])
   conn.close()
   print(f'postgres_ok elapsed={time.time()-t:.2f}s')
   PY
   ```
3. Check for stale downloader processes and obvious project file handles:
   ```bash
   ps ax -o pid,etime,command | egrep 'Naver_Cafe_Downloader|main_cli\.py|chromedriver|Google Chrome.*--user-data-dir|playwright' | egrep -v 'egrep|@playwright/mcp|playwright-mcp' || true
   lsof +D /Users/iseungchan/Project/Python/Naver_Cafe_Downloader 2>/dev/null | sed -n '1,80p' || true
   ```
4. Check target mount status without deep-recursing the NAS tree:
   ```bash
   df -h /Users/iseungchan/NAS_Shares/sync/Python/NaverCafe || true
   stat -f 'path=%N type=%HT mode=%Sp size=%z mtime=%Sm' /Users/iseungchan/NAS_Shares/sync/Python/NaverCafe /Users/iseungchan/Project/Python/Naver_Cafe_Downloader/cookies.pkl 2>/dev/null || true
   ```

## Rerun command

After DB probe succeeds and no stale downloader process is active:

```bash
mkdir -p /Users/iseungchan/Project/Python/Naver_Cafe_Downloader/logs
LOG=/Users/iseungchan/Project/Python/Naver_Cafe_Downloader/logs/rerun_$(date +%Y%m%d_%H%M%S).log
cd /Users/iseungchan/Project/Python/Naver_Cafe_Downloader \
  && python3 -u main_cli.py chodan chyeonz friendshipping super__rim 2>&1 | tee "$LOG"
```

Verify completion:

```bash
ps ax -o pid,etime,command | egrep 'Naver_Cafe_Downloader|main_cli\.py' | egrep -v 'egrep' || true
python3 - <<'PY'
from pathlib import Path
p=max(Path('/Users/iseungchan/Project/Python/Naver_Cafe_Downloader/logs').glob('rerun_*.log'), key=lambda x: x.stat().st_mtime)
text=p.read_text(errors='replace')
print('log=', p)
for needle in ['Postgres Connection Error','db_connection_error',' - ERROR - ']:
    print(f'{needle}: {text.count(needle)}')
print(text[text.rfind('--- Summary ---'):])
PY
```

## Interpretation

- If `ping`, `nc`, and the psycopg2 query succeed, treat the original DB timeout as transient and rerun the same scoped job.
- `Mobile article API unauthorized (401)` and `Fallback login redirect: https://nid.naver.com/...` during rerun indicate Naver article/session authorization problems, not PostgreSQL failure. The current CLI may still finish with `Errors: 0` and `New Posts: 0` because these are skipped, not fatal.
- On the NAS SMB mount, broad `find`, full-tree `lsof`, and directory iteration can hang or time out. Prefer mount/stat checks and concrete paths from logs over deep scans.
