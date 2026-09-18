# LSC Agent Skills Codex Instructions

This file is a Codex copy adapted from `.agent/HERMES_POLICIES.md`. Keep the Hermes policy source read-only.

- This repository manages Codex TOML subagents, OMA `.agents`, and external Product Manager Skills material.
- For role or routing changes, inspect `docs/agent-routing-map.md`, `docs/hermes-skill-bridge.md`, and `docs/obsidian-capture-policy.md` together.
- Changes under `categories/**/*.toml` can affect global and project Codex CLI installation; validate agent names, roles, safety rules, and installation paths.
- Changes under `.agents/` can affect Antigravity, Claude Code, Codex CLI, Gemini CLI, and other consumers; preserve cross-agent compatibility.
- Preserve attribution, licensing, and external-source boundaries under `external/Product-Manager-Skills`; do not rewrite external or submodule material without scope.
