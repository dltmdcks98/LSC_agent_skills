---
name: media-archival-pipeline-operations
description: "Operate end-to-end personal media archival pipelines: SNS crawling, downloader jobs, Immich organization, Plex libraries, and metadata databases."
version: 1.0.0
metadata:
  hermes:
    tags: [media, archival, sns-crawler, immich, plex, metadata, fastapi, docker]
---

# Media Archival Pipeline Operations

Use this skill for end-to-end media collection and library maintenance: social/SNS crawlers, FastAPI download jobs, Immich album/tag organization, Plex media servers and custom metadata providers, and backing metadata databases.

## System map

- **Acquisition**: SNS crawler/download jobs, browser/session recovery, target-account status, rate limits, login/challenge failures, yt-dlp/browser impersonation dependencies, macOS headed vs FastAPI/Docker headless execution choices, and run progress.
- **Organization**: Immich albums/tags derived from folders, captions, EXIF/IPTC subjects, cron-triggered album orchestration, and duplicate cleanup.
- **Serving**: Plex library refreshes, custom metadata provider behavior, local assets, poster/background cache, Docker/VPN/gluetun topology, and provider smoke tests.
- **Metadata**: SQLite/Postgres/app databases, external source refreshes, title/genre/cast/actor normalization, cache repair, migration cleanup, and enrichment jobs.

## Operating principles

1. Inspect live configuration before acting: project config, containers, cron jobs, DB targets, API endpoints, and active queues.
2. Prefer config-driven orchestration over one-off scripts when the project already has a FastAPI/cron/control plane.
3. Separate acquisition failures from organization/serving failures; do not debug Plex cache when the crawler never downloaded the asset.
4. Preserve safety gates for destructive operations: deletions, migrations, duplicate cleanup, archive sweeps, and queue resets.
5. Verify from the user-facing system: Immich API/UI state, Plex item/provider state, database rows, and job logs.

## Procedure: triage a broken pipeline

1. Identify the layer: crawler/download, metadata DB, Immich, Plex, or notification/reporting.
2. Check recent logs and active/stalled jobs.
3. Validate configuration and credentials without exposing secrets.
4. Run the smallest safe probe that exercises the failing path.
5. Apply targeted fix or resume command.
6. Re-check downstream visibility and report exact counts/IDs only when read from tools.

## Procedure: planned maintenance

- Snapshot or back up mutable DBs before schema repair or bulk cleanup.
- Estimate capacity and impact before duplicate removal or archive migration.
- Use dry runs where available.
- Stagger cron jobs when resources compete for browser profiles, DB connections, GPU/CPU, or network bandwidth.
- Send/verify Mattermost or other notifications only after the job's state is known.

## Pitfalls

- Naver Cafe Downloader DB timeouts can be transient: first verify NAS reachability, PostgreSQL TCP, and an actual psycopg2 query from `/Users/iseungchan/Project/Python/Naver_Cafe_Downloader`; if clean, rerun the scoped board CLI and verify the rerun log has no DB errors. See `references/naver-cafe-downloader-db-rerun-triage.md`.
- Browser profile stale locks can masquerade as downloader failure.
- TikTok may behave differently under FastAPI/Docker/headless versus macOS headed runs; when bot checks are the blocker, run TikTok locally/headed and keep unrelated Instagram/X jobs in FastAPI if they are stable.
- A venv that only contains `yt-dlp[curl-cffi]` fixes the downloader subprocess but may not run the full crawler; full local execution also needs runtime imports such as requests, Playwright, psycopg2, atproto, metadata/image libraries, and Playwright browsers.
- API/server outages can create misleading missed-history gaps; distinguish data absence from collection failure.
- Plex and Immich may cache stale posters, summaries, or tags after backend repair; verify cache invalidation separately.
- DB URI mismatch is common in MCP/container contexts; always verify current database/schema.

## References

- `references/immich-nas-memory-heap-oom.md` — Immich on NAS memory/heap OOM triage: distinguish Docker OOMKilled from Node/V8 heap OOM, verify split workers and effective env, inspect `system_metadata` job config, lower job concurrency, and avoid relying on unconfirmed v3.0.0 memory improvements.
- `references/tiktok-ytdlp-impersonation-curl-cffi.md` — troubleshooting pattern for TikTok/SNS_Crawler yt-dlp `--impersonate chrome-136:macos-15` failures caused by missing `curl_cffi`, with project-local `.venv` fix and verification.

## Source consolidation notes

This umbrella absorbs `sns-crawler-operations`, `immich-media-organization`, `plex-media-server`, and `metadata-database-maintenance` as lanes of one media archival pipeline class.
