# SNS/TikTok yt-dlp impersonation dependency troubleshooting

Use this when SNS_Crawler/TikTok logs show yt-dlp errors like:

```text
YoutubeDLError: Impersonate target "chrome-136:macos-15" is not available.
Use --list-impersonate-targets to see available targets.
```

## Durable lesson

This error usually means yt-dlp is present but its impersonation backend is missing or unavailable. For TikTok, `--impersonate chrome-136:macos-15` requires a yt-dlp build/environment with `curl_cffi` support.

Do not assume this is “macOS system Python” or solve it by installing another global Python. Prefer a project-local venv so downloader behavior is deterministic.

## Probe

```bash
cd /Users/iseungchan/Project/Python/SNS_Crawler
/usr/local/bin/python3 - <<'PY'
import sys
print(sys.executable)
try:
    import yt_dlp
    print(yt_dlp.version.__version__, yt_dlp.__file__)
except Exception as e:
    print(repr(e))
PY
/usr/local/bin/python3 -m yt_dlp --list-impersonate-targets | sed -n '1,120p'
```

If the target list shows `curl_cffi (unavailable)` or lacks `Chrome-136 Macos-15`, create/update a project venv.

## Fix pattern

The TikTok crawler already resolves yt-dlp in this order:

1. `SNS_Crawler/venv/bin/yt-dlp`
2. `SNS_Crawler/.venv/bin/yt-dlp`
3. PATH `yt-dlp`
4. current interpreter `python -m yt_dlp`

So install the known-good downloader into `.venv`:

```bash
cd /Users/iseungchan/Project/Python/SNS_Crawler
uv venv .venv --python 3.13
uv pip install --python .venv/bin/python 'yt-dlp[curl-cffi]'
.venv/bin/yt-dlp --list-impersonate-targets | awk 'tolower($0) ~ /chrome-136/ && tolower($0) ~ /macos-15/ {print}'
```

This is enough when the crawler itself runs under an existing Python but calls `.venv/bin/yt-dlp` as a subprocess.

## Full local macOS execution

If the user runs the whole crawler with `.venv/bin/python run.py ...`, install the crawler runtime dependencies too. A downloader-only venv will fail early with imports such as `ModuleNotFoundError: No module named 'requests'` or missing `psycopg2`.

Known runtime set from the macOS headed TikTok path:

```bash
cd /Users/iseungchan/Project/Python/SNS_Crawler
uv pip install --python .venv/bin/python \
  requests \
  playwright \
  playwright-stealth \
  psycopg2-binary \
  atproto \
  pillow \
  piexif \
  instaloader \
  'yt-dlp[curl-cffi]'
.venv/bin/python -m playwright install chromium
.venv/bin/python run.py --help
```

For TikTok bot-check issues, prefer the macOS headed run:

```bash
.venv/bin/python run.py --platform tiktok --sync --headless False
# or narrow the test:
.venv/bin/python run.py --platform tiktok --user <account> --sync --headless False
```

Keep FastAPI for platforms that remain stable there (for example Instagram):

```bash
curl -X POST http://localhost:8000/api/v1/sns-crawler/trigger/instagram \
  -H 'Content-Type: application/json' \
  -d '{"user":"all","sync":true}'
```

Verify the crawler will use the project-local yt-dlp:

```bash
PYTHONPATH=/Users/iseungchan/Project/Python/SNS_Crawler /usr/local/bin/python3 - <<'PY'
import configparser
from modules.tiktok_browser import TikTokBrowserCrawler
c = TikTokBrowserCrawler(configparser.ConfigParser(), db=None)
print(c.yt_dlp_cmd)
PY
```

Expected:

```text
['/Users/iseungchan/Project/Python/SNS_Crawler/.venv/bin/yt-dlp']
```

## Verification

Run a simulate probe and ensure the old impersonation error is absent:

```bash
.venv/bin/yt-dlp --simulate --no-warnings --impersonate chrome-136:macos-15 'https://www.tiktok.com/@<user>/video/<post_id>'
```

For TikTok extractor regressions where the latest stable still fails, test the current master before waiting for the next release:

```bash
uv pip install --python .venv/bin/python --force-reinstall \
  'yt-dlp[default,curl-cffi] @ git+https://github.com/yt-dlp/yt-dlp.git@master'
.venv/bin/python - <<'PY'
import importlib.metadata as m
print(m.distribution('yt-dlp').read_text('direct_url.json'))
PY
```

In this user's SNS_Crawler, the shared dependency file is `/Users/iseungchan/Project/Python/requirements.txt`, not a per-project `SNS_Crawler/requirements.txt`. FastAPI builds copy that file via Docker Compose `additional_contexts.python_project`, so after changing it reinstall both the local `.venv` and the FastAPI runtime/container image.

TikTok cookie use can be non-deterministic: the same master build may succeed with Playwright-exported cookies in one attempt and fail with `Unexpected response from webpage request` or `Unable to extract universal data` in another. If the browser scan already discovered public post URLs, a pragmatic downloader fallback is to retry yt-dlp without `--cookies` for those specific extractor errors.

This may still fail for TikTok auth/rate/captcha reasons, but it should not fail with “Impersonate target ... is not available.”

## Reporting

Tell the user: the durable fix is project-local `yt-dlp[curl-cffi]`, not a new global macOS Python install. If an existing long-running crawler process was started before the venv existed, restart/retrigger that crawler so it resolves the new yt-dlp path.