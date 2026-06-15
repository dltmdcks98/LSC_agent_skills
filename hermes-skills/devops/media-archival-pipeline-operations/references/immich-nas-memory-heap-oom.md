# Immich NAS memory / Node heap OOM triage

Use when Immich on the user's NAS repeatedly exits/restarts and RAM limits are suspected.

## Diagnostic pattern

1. Check container state and limits:
   ```bash
   ssh -p 1048 dltmdcks98@192.168.50.20 '
     /usr/local/bin/docker ps -a --format "{{.Names}}\t{{.Image}}\t{{.Status}}" | grep -i immich
     /usr/local/bin/docker stats --no-stream --format "{{.Name}}\t{{.MemUsage}}\t{{.MemPerc}}" | grep -i immich
     for c in immich_server immich_microservices; do
       /usr/local/bin/docker inspect "$c" --format "name={{.Name}} restart={{.RestartCount}} oom={{.State.OOMKilled}} exit={{.State.ExitCode}} mem={{.HostConfig.Memory}}"
     done
   '
   ```
2. Distinguish Docker/cgroup OOM from Node/V8 heap OOM:
   - Docker OOM: `.State.OOMKilled=true`, kernel/container `oom` events.
   - Node heap OOM: logs show `FATAL ERROR: Reached heap limit Allocation failed - JavaScript heap out of memory` and `api worker exited with code null`; `.State.OOMKilled` may remain false.
3. Verify actual compose/env, not just files:
   ```bash
   docker inspect immich_server --format '{{range .Config.Env}}{{println .}}{{end}}' | sort
   cd /volume1/docker/immich && docker compose config
   ```
   Immich docs note env changes require container recreate, not just restart.
4. Check whether split workers are active:
   - API container: `IMMICH_WORKERS_INCLUDE=api`
   - Microservices container: `IMMICH_WORKERS_EXCLUDE=api`
5. Inspect Immich system config from Postgres without printing secrets:
   - `system_metadata` table contains `system-config` JSON.
   - Look for `job` concurrency, `library.scan.cronExpression`, `machineLearning.urls`, OCR/smart search/face settings.
6. If `system-config` has no `job` key, the app uses defaults from `/usr/src/app/server/dist/config.js` inside the container.

## v2.7.5 default concurrency observed

From `/usr/src/app/server/dist/config.js`:

- `backgroundTask`: 5
- `smartSearch`: 2
- `metadataExtraction`: 5
- `faceDetection`: 2
- `search`: 5
- `sidecar`: 5
- `library`: 5
- `migration`: 5
- `thumbnailGeneration`: 3
- `videoConversion`: 1
- `notification`: 5
- `ocr`: 1
- `workflow`: 5
- `editor`: 2

For low-memory NAS, recommend lowering high-resource and broad queues first: `metadataExtraction`, `library`, `thumbnailGeneration`, `smartSearch`, `faceDetection`, `search`, `sidecar`, `migration`, `workflow`, `editor` to 1–2.

## Current user's NAS-specific observations from one incident

- Compose path: `/volume1/docker/immich`.
- Containers used split workers: `immich_server` and `immich_microservices` from `ghcr.io/immich-app/immich-server:release`.
- v2.7.5 was running.
- Remote ML URL was configured to `http://192.168.50.30:3003`; local ML container was not present.
- Logs showed Node/V8 heap OOM in the API worker, not Docker OOMKilled.
- Large DB indexes were logged at startup: `face_index` around 1.1M rows and `clip_index` around 1.8M rows.
- Latest public releases showed v2.7.5; v3.0.0 was only mentioned as upcoming and not as a confirmed memory fix.

## Recommended low-memory profile

Prefer UI/API-supported System Settings changes when possible. Direct DB edits should be treated as last resort and backed up first.

- Job concurrency:
  - `metadataExtraction`: 1
  - `library`: 1
  - `thumbnailGeneration`: 1
  - `smartSearch`: 1
  - `faceDetection`: 1
  - `search`: 1–2
  - `sidecar`, `migration`, `workflow`, `editor`, `backgroundTask`, `notification`: 1–2
  - `videoConversion` and `ocr`: keep 1
- Library scan cron: relax from frequent scans (e.g. every 6h) to 12h/daily if load persists.
- `NODE_OPTIONS=--max-old-space-size=...` is a heap cap/tuning knob, not a primary memory-reduction fix. Lowering it can make API crash earlier if workload still needs memory; raising it may avoid V8 OOM but uses more RAM within the container limit. Tune only after concurrency reduction.

## Verification after changes

- Recreate containers if env/compose changed:
  ```bash
  cd /volume1/docker/immich
  docker compose up -d --force-recreate
  ```
- Verify:
  ```bash
  docker compose ps
  docker stats --no-stream | grep -i immich
  docker logs --since 10m immich_server | grep -E 'FATAL ERROR|heap out of memory|Starting api worker' || true
  docker logs --since 10m immich_microservices | grep -E 'Missing lock|Lock mismatch|could not renew lock|FATAL ERROR' || true
  ```
