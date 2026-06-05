# Hermes Skill Bridge

이 문서는 `Hermes Agent Team KR` 저장소를 Hermes Agent에서 활용하는 기준입니다.

## 기본 원칙

- Hermes는 실행 허브입니다. Mattermost, memory, MCP, Obsidian, cron, session_search를 유지합니다.
- OMA `.agents/`는 역할형 작업 기준의 원본입니다.
- Codex TOML subagents는 세부 전문 역할을 Codex CLI에 위임할 때 선택합니다.
- OMA CLI를 Hermes 위의 또 다른 오케스트레이터로 상시 실행하지 않습니다. 필요 시 `oma doctor`, `oma link`, `oma verify` 같은 보조 명령만 사용합니다.

## Hermes skill 변환 기준

Hermes local skill `hermes-agent-team-kr`는 이 저장소를 다음 순서로 사용합니다.

1. 작업 유형을 OMA role로 분류
2. 해당 OMA skill의 checklist/workflow를 참고
3. 필요한 경우 Codex TOML subagent를 선택
4. Hermes `delegate_task` 또는 Codex CLI로 위임
5. QA/debug/SCM/docs 단계로 검증

## 작업 유형별 기본 OMA role

| 작업 | OMA 기준 |
|---|---|
| 요구사항 정리/일정/작업 분해 | `oma-pm` |
| 아키텍처/경계/ADR | `oma-architecture` |
| FastAPI/API/백엔드 | `oma-backend` |
| DB/schema/migration/query | `oma-db` |
| React/Next/UI | `oma-frontend` |
| iOS/Flutter/mobile | `oma-mobile` |
| Docker/CI/CD/인프라 | `oma-dev-workflow`, `oma-tf-infra`, `oma-observability` |
| 버그/장애 원인 분석 | `oma-debug` |
| 보안/성능/접근성/코드 리뷰 | `oma-qa`, `oma-deepsec` |
| 문서 drift/README/Obsidian 보조 | `oma-docs` |
| Git/Gitea/GitHub/커밋 | `oma-scm` |

## 승찬님 환경 보정

- Obsidian 작업은 Obsidian 전용 subagent/skill을 우선 고려합니다.
- FastAPI는 오케스트레이터, 도메인 로직은 별도 Python 프로젝트로 분리하는 구조를 우선합니다.
- 공통 모듈 수정 전 영향 범위를 먼저 검토합니다.
- 완료 보고 전 실제 런타임/테스트/명령 결과를 확인합니다.
- Git 커밋 메시지는 한국어로 작성합니다.
- 명시 없는 Docker/FastAPI 재시작은 보류하고 영향도를 먼저 보고합니다.

## 적용 검증

- `git status --short`
- `find .agents/skills -maxdepth 2 -name SKILL.md | wc -l`
- `find categories -name '*.toml' | wc -l`
- Hermes에서는 새 세션에서 `skill_view(name='hermes-agent-team-kr')`로 로드 확인
