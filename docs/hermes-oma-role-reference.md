# OMA Role Reference

## `oma-academic-writer`

- Path: `.agents/skills/oma-academic-writer/SKILL.md`

## `oma-architecture`

- Path: `.agents/skills/oma-architecture/SKILL.md`
- Description: Architecture specialist for software/system design, module and service boundaries, tradeoff analysis, and stakeholder synthesis. Uses context-aware methods such as diagnostic routing, design-twice comparison, ATAM-style risk analysis, CBAM-style prioritization, and ADR-style decision records.

## `oma-backend`

- Path: `.agents/skills/oma-backend/SKILL.md`
- Description: Backend specialist for APIs, databases, authentication with clean architecture (Repository/Service/Router pattern). Use for API, endpoint, REST, database, server, migration, and auth work.

## `oma-brainstorm`

- Path: `.agents/skills/oma-brainstorm/SKILL.md`
- Description: Design-first ideation that explores user intent, constraints, and approaches before any planning or implementation. Use for brainstorming, ideation, exploring concepts, and evaluating approaches.

## `oma-coordination`

- Path: `.agents/skills/oma-coordination/SKILL.md`
- Description: Guide for coordinating PM, Frontend, Backend, Mobile, and QA agents on complex projects via CLI. Use for manual step-by-step coordination and workflow guidance.

## `oma-db`

- Path: `.agents/skills/oma-db/SKILL.md`
- Description: Database specialist for SQL, NoSQL, and vector database modeling, schema design, normalization, indexing, transactions, integrity, concurrency control, backup, capacity planning, data standards, anti-pattern review, and compliance-aware database design. Use for database, schema, ERD, table design, document model, vector index design, RAG retrieval architecture, migration, query tuning, glossary, capacity estimation, backup strategy, database anti-pattern remediation work, and ISO 27001, ISO 27002, or ISO 22301-aware database recommendations.

## `oma-debug`

- Path: `.agents/skills/oma-debug/SKILL.md`
- Description: Bug diagnosis and fixing specialist - analyzes errors, identifies root causes, provides fixes, and writes regression tests. Use for bug, debug, error, crash, traceback, exception, and regression work.

## `oma-deepsec`

- Path: `.agents/skills/oma-deepsec/SKILL.md`

## `oma-design`

- Path: `.agents/skills/oma-design/SKILL.md`

## `oma-dev-workflow`

- Path: `.agents/skills/oma-dev-workflow/SKILL.md`
- Description: Use when setting up or optimizing developer workflows in a monorepo, managing mise tasks, git hooks, CI/CD pipelines, database migrations, or release automation. Invoke for development environment setup, build automation, testing workflows, and release coordination.

## `oma-docs`

- Path: `.agents/skills/oma-docs/SKILL.md`
- Description: Verify documentation references against the current codebase and propose updates for diff-affected docs. Use to check if docs still match reality (broken file paths, CLI commands, config keys, env vars, scripts) and to surface docs that may need updating after code changes.

## `oma-frontend`

- Path: `.agents/skills/oma-frontend/SKILL.md`
- Description: Frontend specialist for React, Next.js, TypeScript with FSD-lite architecture, shadcn/ui, and design system alignment. Use for UI, component, page, layout, CSS, Tailwind, and shadcn work.

## `oma-hwp`

- Path: `.agents/skills/oma-hwp/SKILL.md`

## `oma-image`

- Path: `.agents/skills/oma-image/SKILL.md`
- Description: Multi-vendor AI image generation with authentication-aware parallel dispatch. Routes to Codex (gpt-image-2 via ChatGPT OAuth), Antigravity (gemini-2.5-flash-image aka nano-banana via `agy` CLI + Gemini Code Assist), and Pollinations (flux/zimage, free with signup). Use for image generation, image creation, visual asset generation, and AI art.

## `oma-market`

- Path: `.agents/skills/oma-market/SKILL.md`
- Description: Market research skill for pain-point extraction, trend detection, competitor positioning, and discovery across community sources (Reddit, HN, Bluesky, Mastodon, GitHub Issues, web). Routes via oma-search transport, deterministic CLI compute, intent-auto SWOT/Porter's 5F/PESTEL frameworks. Use for market research, pain point analysis, trend detection, competitor research, user complaints, voice-of-customer, 시장조사, 사용자 페인, 트렌드, 경쟁구도.

## `oma-mobile`

- Path: `.agents/skills/oma-mobile/SKILL.md`
- Description: Mobile specialist for Flutter, React Native, and Swift native iOS development. Use for mobile app, Flutter, Dart, React Native, Swift, SwiftUI, iOS, Android, Riverpod, swift-openapi-generator, and widget work.

## `oma-observability`

- Path: `.agents/skills/oma-observability/SKILL.md`
- Description: Intent-based observability + traceability router across layers, boundaries, and signals. Routes to vendor-specific skills via category taxonomy; owns transport tuning, meta-observability, incident forensics. Use for observability, traceability, telemetry, APM, RUM, metrics, logs, traces, profiles, SLO, incident forensics, tracing architecture work.

## `oma-orchestrator`

- Path: `.agents/skills/oma-orchestrator/SKILL.md`
- Description: Automated multi-agent orchestrator that spawns CLI subagents in parallel, coordinates via MCP Memory, and monitors progress. Use for orchestration, parallel execution, and automated multi-agent workflows.

## `oma-pdf`

- Path: `.agents/skills/oma-pdf/SKILL.md`

## `oma-pm`

- Path: `.agents/skills/oma-pm/SKILL.md`
- Description: Product manager that decomposes requirements into actionable tasks with priorities and dependencies. Use for planning, requirements, specification, scope, prioritization, task breakdown, and ISO 21500, ISO 31000, or ISO 38500-aligned planning recommendations.

## `oma-qa`

- Path: `.agents/skills/oma-qa/SKILL.md`
- Description: Quality assurance specialist for security, performance, accessibility, comprehensive testing, and quality standard alignment. Use for test, review, security audit, OWASP, coverage, lint work, and ISO/IEC 25010 or ISO/IEC 29119-aligned QA recommendations.

## `oma-recap`

- Path: `.agents/skills/oma-recap/SKILL.md`
- Description: Analyze conversation histories from multiple AI tools (Claude, Codex, Qwen, Cursor, Antigravity) and generate themed daily/period work summaries. Filter by date or time window.

## `oma-scholar`

- Path: `.agents/skills/oma-scholar/SKILL.md`

## `oma-scm`

- Path: `.agents/skills/oma-scm/SKILL.md`
- Description: SCM (software configuration management) and Git: branching, merges, conflicts, worktrees, baselines, audit readiness, plus Conventional Commits and safe staging.

## `oma-search`

- Path: `.agents/skills/oma-search/SKILL.md`
- Description: Intent-based search router with trust scoring. Routes queries to optimal channels (Context7 docs, native web search, gh/glab code search, Serena local) and attaches domain trust labels. Use for search, find, lookup, reference, docs, code search, and web research.

## `oma-skill-creator`

- Path: `.agents/skills/oma-skill-creator/SKILL.md`

## `oma-slide`

- Path: `.agents/skills/oma-slide/SKILL.md`
- Description: HTML presentation deck generator and multi-format exporter. Generates distinctive, animation-rich HTML decks at a fixed 1920×1080 stage, then deterministically validates, bundles, and exports them to PDF/PNG/PPTX via the `oma slide` CLI. Use for slide, deck, presentation, slides, pptx, keynote, 슬라이드, 발표자료, プレゼン, 幻灯片 requests. Produces self-contained single-file HTML with keyboard/touch nav, speaker notes, and print-to-PDF support.

## `oma-tf-infra`

- Path: `.agents/skills/oma-tf-infra/SKILL.md`
- Description: Infrastructure-as-code specialist for multi-cloud provisioning using Terraform across any provider (AWS, GCP, Azure, Oracle Cloud). Use for terraform plan/apply, state management, compute, databases, storage, networking, IAM, OIDC, cost optimization, policy-as-code, ISO/IEC 42001 AI controls, ISO 22301 continuity, and ISO/IEC/IEEE 42010 architecture documentation.

## `oma-translator`

- Path: `.agents/skills/oma-translator/SKILL.md`
- Description: Context-aware translation that preserves tone, style, and natural word order. Use when translating UI strings, documentation, marketing copy, or any multilingual content. Infers register, domain, and style from the source text and surrounding codebase context.

## `oma-video`

- Path: `.agents/skills/oma-video/SKILL.md`
- Description: Short-form, explainer, and demo video generation via a key-optional 3-tier router. Composes scripts, oma-voice narration, oma-image/oma-slide/stock visuals, key-free captions, and a vendored Remotion compositor into reproducible run directories. Routes three modes — shorts/reels (9:16), explainer (16:9 README/code/data), and demo/walkthrough (screen capture, incl. supervised headed web-app capture of any URL). Use for video, shorts, reels, short-form, demo, explainer, walkthrough, screencast, web capture, video generation, 영상, 숏폼, 쇼츠, 릴스, 데모, 설명 영상.

## `oma-voice`

- Path: `.agents/skills/oma-voice/SKILL.md`
