<a href="https://github.com/VoltAgent/awesome-codex-subagents">
  <img width="1500" height="500" alt="awesome-codex-subagents" src="https://github.com/user-attachments/assets/35f56654-e3e7-4023-a7d5-acd5215455de" />
</a>

<br />

<div align="center">
  <strong>Codex 하위 에이전트 136개를 카테고리별로 정리한 컬렉션</strong>
</div>

<br />

<div align="center">

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Subagent Count](https://img.shields.io/badge/subagents-136-blue?style=classic)
[![Last update](https://img.shields.io/github/last-commit/VoltAgent/awesome-codex-subagents?label=Last%20update&style=classic)](https://github.com/VoltAgent/awesome-codex-subagents)
[![Discord](https://img.shields.io/discord/1361559153780195478.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://s.voltagent.dev/discord)

</div>

# Awesome Codex Subagents (한국어 안내)

이 저장소는 [Codex 하위 에이전트](https://developers.openai.com/codex/subagents) 설정 파일(`.toml`)을 모아둔 컬렉션입니다. 각 에이전트는 특정 역할(백엔드 개발, 코드 리뷰, 인프라 운영, 리서치 등)에 맞춰 설계되어 있습니다.

## 설치

Codex 하위 에이전트는 아래 경로 중 하나에 배치해 사용할 수 있습니다.

- 전역 설치: `~/.codex/agents/` (모든 프로젝트에서 사용)
- 프로젝트 설치: `.codex/agents/` (현재 프로젝트에서만 사용, 전역보다 우선)

### 빠른 설치 스크립트

```bash
chmod +x ./install-subagents.sh
./install-subagents.sh --global
```

프로젝트 로컬 설치:

```bash
./install-subagents.sh --project
```

특정 카테고리만 설치:

```bash
./install-subagents.sh --project --category 04-quality-security
```

특정 에이전트만 설치:

```bash
./install-subagents.sh --agent reviewer.toml --global
```

### 수동 설치

1. 이 저장소를 클론합니다.
2. 원하는 `.toml` 파일을 선택합니다.
3. 파일을 `~/.codex/agents/` 또는 `.codex/agents/`로 복사합니다.
4. Codex 세션을 새로고침하거나 재시작합니다.

예시:

```bash
mkdir -p ~/.codex/agents
cp categories/01-core-development/backend-developer.toml ~/.codex/agents/

mkdir -p .codex/agents
cp categories/04-quality-security/reviewer.toml .codex/agents/
```

## 하위 에이전트 파일 구조

각 하위 에이전트는 Codex의 기본 TOML 형식을 사용합니다.

```toml
name = "subagent-name"
description = "When this agent should be invoked"
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"

[instructions]
text = """
You are a [role description and expertise areas]...

[Agent-specific checklists, patterns, and guidelines]...
"""
```

### 모델 가이드

- `gpt-5.4`: 보안 리뷰, 아키텍처 검토, 복잡한 의사결정처럼 깊은 추론이 필요한 작업
- `gpt-5.3-codex-spark`: 빠른 검색/분석, 경량 조사, 신속한 반복 작업

### 샌드박스 가이드

- `read-only`: 분석/검토 중심 작업 (파일 수정 없음)
- `workspace-write`: 코드/문서 수정이 필요한 작업

## 카테고리

- [01. Core Development](categories/01-core-development/README.md)
- [02. Language Specialists](categories/02-language-specialists/README.md)
- [03. Infrastructure](categories/03-infrastructure/README.md)
- [04. Quality & Security](categories/04-quality-security/README.md)
- [05. Data & AI](categories/05-data-ai/README.md)
- [06. Developer Experience](categories/06-developer-experience/README.md)
- [07. Specialized Domains](categories/07-specialized-domains/README.md)
- [08. Business & Product](categories/08-business-product/README.md)
- [09. Meta Orchestration](categories/09-meta-orchestration/README.md)
- [10. Research & Analysis](categories/10-research-analysis/README.md)

## 권장 사용 순서

1. 문제 성격(개발/인프라/리뷰/리서치)을 먼저 정합니다.
2. 해당 카테고리의 README에서 적합한 에이전트를 고릅니다.
3. `read-only` 에이전트로 먼저 진단하고, 필요할 때만 `workspace-write` 에이전트를 사용합니다.

## 라이선스

이 저장소는 MIT 라이선스를 따릅니다. 자세한 내용은 [LICENSE](LICENSE)를 확인하세요.
