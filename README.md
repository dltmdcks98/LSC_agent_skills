# LSC Agent Skills

승찬님 환경에서 **Hermes Agent + Codex Subagents + oh-my-agent(OMA)** 를 함께 쓰기 위한 한국어 에이전트 팀 저장소입니다.

기존 `codex-subagent-kr`의 Codex TOML subagent 컬렉션을 유지하면서, [`first-fluke/oh-my-agent`](https://github.com/first-fluke/oh-my-agent)의 `.agents/` 기반 역할형 skill/workflow 체계를 병합했습니다.

## 구성

| 영역 | 경로 | 용도 |
|---|---|---|
| Codex Subagents KR | `categories/**/*.toml` | Codex CLI 전역/프로젝트 subagent 설치용 한국어 TOML 에이전트 |
| OMA portable agents | `.agents/` | Antigravity, Claude Code, Codex CLI, Gemini CLI, Cursor 등에서 공유 가능한 역할형 agent/skill/workflow 원본 |
| Product Manager Skills | `external/Product-Manager-Skills` | PRD, 우선순위, 스토리맵, discovery 등 PM 산출물 작성용 외부 skill 라이브러리 |
| Hermes bridge docs | `docs/hermes-skill-bridge.md` | Hermes skill로 변환해서 사용하는 운영 방식 |
| Agent routing map | `docs/agent-routing-map.md` | 작업 유형별 OMA skill ↔ Codex subagent 매핑 |
| Obsidian capture policy | `docs/obsidian-capture-policy.md` | Project/Resource/Dictionary 기록 대상과 Hermes 지침 위치 기준 |

## 왜 이름을 바꿨나

이 저장소는 더 이상 Codex 전용 한국어 번역 모음만이 아니라, 승찬님이 Hermes에서 실제로 쓰는 **멀티 에이전트 작업 기준 저장소**입니다.

- Hermes: Mattermost/메모리/MCP/Obsidian/cron/skill 중심 실행 허브
- OMA `.agents`: 역할형 agent, workflow, checklist의 공용 원본
- Codex Subagents: 세부 전문 역할을 Codex CLI에 위임할 때 쓰는 TOML 에이전트 풀
- Product Manager Skills: PRD/우선순위/스토리맵/discovery 요청에서 참조하는 PM 방법론 라이브러리

따라서 활용 목적에 맞춰 저장소 표기명을 `LSC Agent Skills`로 정리했습니다.

## 빠른 사용

### Codex subagent 설치

```bash
chmod +x ./install-subagents.sh
./install-subagents.sh --global
./install-subagents.sh --project --category 04-quality-security
./install-subagents.sh --agent reviewer.toml --global
```

설치 위치:

- 전역: `~/.codex/agents/`
- 프로젝트: `.codex/agents/`

### OMA `.agents` 활용

```bash
# OMA CLI를 쓰는 경우
oma link
oma doctor

# Hermes에서는 직접 CLI를 먼저 쓰기보다,
# 등록된 Hermes skill `lsc-agent-skills`를 통해 역할 선택/위임 기준으로 사용합니다.
```

### Product Manager Skills 참조

```bash
# submodule 포함 clone/update
git submodule update --init --recursive

# PM skill catalog 확인
sed -n '1,120p' external/Product-Manager-Skills/catalog/skills-index.yaml
```

Hermes에서 “PRD 써줘”, “기능 우선순위 잡아줘”, “스토리맵 만들어줘” 같은 요청을 받으면 `docs/product-manager-skills-reference.md`를 기준으로 `oma-pm`/business-product subagent와 Product-Manager-Skills의 원본 skill을 함께 참조합니다.

## 권장 Hermes 운영 흐름

1. 작업을 받으면 Hermes가 `lsc-agent-skills` skill을 기준으로 작업 유형을 분류합니다.
2. 계획/요구사항은 `oma-pm` 관점으로 먼저 정리합니다.
3. PRD/우선순위/스토리맵/discovery 요청은 `docs/product-manager-skills-reference.md`를 열어 Product-Manager-Skills의 해당 skill을 참조합니다.
4. 구현은 도메인에 따라 `oma-backend`, `oma-frontend`, `oma-mobile`, `oma-db`, `oma-tf-infra` 기준을 적용합니다.
5. 세부 전문성이 필요하면 `categories/**/*.toml`의 Codex subagent를 선택해 Codex CLI에 위임합니다.
6. 리뷰/검증은 `oma-qa`, `oma-debug`, `oma-scm`, `oma-docs` 기준으로 마무리합니다.

## 병합 출처

- Codex subagent KR 기반: 기존 이 저장소의 `categories/**/*.toml`
- OMA 병합 기준: `first-fluke/oh-my-agent` commit `47803d7`
- 병합된 OMA 경로: `.agents/`
- Product Manager Skills: `deanpeters/Product-Manager-Skills`, 경로 `external/Product-Manager-Skills`

## 규모

- Codex TOML subagents: 137개
- OMA skills: 31개
- Product Manager Skills: upstream submodule catalog 기준 47개 skill + 6개 command
- OMA workflows/rules/agents: `.agents/workflows`, `.agents/rules`, `.agents/agents`

## 문서

- [Hermes skill bridge](docs/hermes-skill-bridge.md)
- [Agent routing map](docs/agent-routing-map.md)
- [Product Manager Skills reference](docs/product-manager-skills-reference.md)
- [Obsidian capture policy](docs/obsidian-capture-policy.md)

## 라이선스

이 저장소의 기존 Codex subagent 자료는 기존 라이선스를 따릅니다. 병합된 oh-my-agent 자료는 upstream MIT 라이선스와 출처를 유지합니다. `external/Product-Manager-Skills`는 upstream의 CC BY-NC-SA 4.0 계열 라이선스와 출처를 유지하는 외부 참조 자료입니다.
