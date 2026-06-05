# Obsidian Capture Policy

이 문서는 승찬님 환경에서 Hermes/OMA/Codex 작업 후 Obsidian에 무엇을 기록하고, 무엇을 기록하지 않을지 정하는 운영 기준입니다.

## 핵심 원칙

Obsidian은 작업 결과와 재사용 지식을 기록하는 곳이지, Hermes의 작업 지침 자체를 저장하는 곳이 아닙니다.

- 작업 진행/검증/남은 일 → `1. Project`
- 재사용 가능한 개념/패턴/운영법 → `3. Resource`
- 기술 단어/제품명/프로토콜명/필드명/라이브러리명 → `4. Archive/Dictionary`
- Hermes의 행동 지침/라우팅 규칙/완료 기준 → 이 저장소(`hermes-agent-team-kr`) 또는 Hermes skill/reference

## `1. Project` 기록 기준

`1. Project/<project>/`는 실제 진행 중인 개발·운영·설정·디버깅 작업만 둡니다.

기록 대상:

- 목표, 작업 체크리스트, 검증 결과, 다음 조치
- 프로젝트별 기능/워크스트림 진행 노트
- 작업 결과와 연결되는 Resource/Dictionary 링크

금지/주의:

- `PM - <project>.md` 중심 구조를 만들지 않습니다.
- `전체 흐름 및 간트.md` 같은 generic whole-Gantt 파일을 만들지 않습니다.
- 숫자 접두어(`00`, `01`, `02`)나 `과거기록` 같은 접두어를 붙이지 않습니다.
- Vault 운영 지침, Hermes 행동 규칙, 작성 기준 자체를 Project로 만들지 않습니다.

## `3. Resource` 기록 기준

프로젝트 중 발견한 재사용 가능한 지식을 작성합니다.

기록 대상:

- 개념 설명
- 구현/설정 패턴
- 운영 체크리스트
- 반복 가능한 디버깅 패턴
- 프로젝트 밖에서도 다시 쓸 수 있는 기술 지식

메타데이터:

- 프로젝트 진행 중 필요한 개념 지식을 `3. Resource`에 작성한다면 frontmatter `project:`에 작업 중인 프로젝트명을 추가합니다.
- 여러 프로젝트와 직접 관련된 개념이면 `project:`를 리스트로 작성합니다.
- 프로젝트와 무관한 일반 지식이면 `project:`를 비워두거나 생략합니다.

예시:

- Harbor 외부 DB 전환 원리
- Harbor prepare/runtime config 구조
- argparse 반복 옵션 패턴
- Hermes skill/subagent 라우팅 개념

## `4. Archive/Dictionary` 기록 기준

기술 단어 자체를 짧게 정의합니다.

기록 대상:

- 제품명: Harbor, Obsidian, PostgreSQL
- 라이브러리/모듈명: argparse
- 프로토콜/표준명: OCI Registry
- 메타데이터 필드명: project
- 일반 기술 용어: Runtime Config, CLI, Frontmatter

기본 형식:

```markdown
---
def-type: atomic
aliases:
  - <alias>
---
# <Term>
<짧은 정의>

## 관련 용어
- [[Related Term]]

## 관련 리소스
- [[Related Resource]]
```

## 지침의 위치

다음은 Obsidian에 새 노트로 남기지 않습니다.

- Hermes가 어떤 순서로 Obsidian을 갱신해야 하는지
- `1. Project`, `3. Resource`, `4. Archive/Dictionary` 캡처 완료 기준
- OMA/Codex/Hermes 라우팅 기준
- 에이전트가 반복해서 따라야 할 작업 절차

이런 내용은 다음 위치에 둡니다.

- 이 저장소의 `docs/*.md`
- Hermes skill `hermes-agent-team-kr`
- 필요한 경우 `~/.hermes/skills/.../references/*.md`

## 완료 전 감사 체크리스트

Obsidian 갱신이 필요한 작업을 마치기 전 확인합니다.

1. 실제 프로젝트 진행이 있었는가?
   - 예: `1. Project/<project>/`의 기능/워크스트림 노트 갱신
   - 아니오: Project 노트를 만들지 않음
2. 재사용 가능한 개념이 생겼는가?
   - 예: `3. Resource` 생성/보강
   - 프로젝트 작업에서 나온 개념이면 Resource frontmatter `project:`에 해당 프로젝트 추가
3. 새 기술 단어가 나왔는가?
   - 예: `4. Archive/Dictionary` 생성/보강
4. 지침/행동 규칙 변경인가?
   - 예: Obsidian이 아니라 `hermes-agent-team-kr` 또는 Hermes skill/reference에 반영
5. 대표 노트를 읽어 실제 반영을 확인했는가?
6. Obsidian 파일을 바꿨다면 LiveSync를 실행했는가?
