# Product Manager Skills Reference

이 문서는 `LSC Agent Skills`에서 [`deanpeters/Product-Manager-Skills`](https://github.com/deanpeters/Product-Manager-Skills)를 PM 작업 프레임워크로 참조하는 기준입니다.

## Source

| 항목 | 값 |
|---|---|
| Upstream | `https://github.com/deanpeters/Product-Manager-Skills` |
| Local path | `external/Product-Manager-Skills` |
| Integration type | Git submodule / read-only reference |
| Primary catalog | `external/Product-Manager-Skills/catalog/skills-index.yaml` |
| Commands | `external/Product-Manager-Skills/commands/*.md` |
| License | CC BY-NC-SA 4.0 계열 — 원본 출처와 비상업/동일조건공유 조건을 유지 |

## Operating Principle

Product-Manager-Skills는 Hermes/OMA/Codex에 새 오케스트레이터를 추가하는 것이 아니라, PM 산출물 작성 시 참조하는 **방법론·질문·템플릿 라이브러리**입니다.

기본 흐름:

1. Hermes가 `LSC_agent_skills` 기준으로 작업 의도를 분류합니다.
2. PM/기획/우선순위/스토리맵 계열이면 `oma-pm`을 1차 role로 둡니다.
3. 필요에 따라 `categories/08-business-product/*.toml`의 Codex subagent를 검토합니다.
4. 산출물 유형에 맞는 Product-Manager-Skills skill/command를 참조합니다.
5. 승찬님 환경 규칙에 맞춰 Obsidian/EventNote/프로젝트 문서/이슈 단위로 결과를 정리합니다.

주의:

- `external/Product-Manager-Skills`의 원본 skill 47개를 `.agents/skills`에 그대로 섞지 않습니다.
- 원본은 read-only reference로 사용하고, Hermes 동작 규칙은 이 저장소의 `docs/` 또는 Hermes skill reference에 둡니다.
- 상업적 재배포·수정 배포가 필요한 경우 라이선스 검토가 먼저 필요합니다.

## Trigger Phrases

사용자가 다음처럼 요청하면 이 문서를 먼저 참조합니다.

- “PRD 써줘”
- “요구사항 정리해줘”
- “문제 정의해줘”
- “기능 우선순위 잡아줘”
- “로드맵 잡아줘”
- “스토리맵 만들어줘”
- “user story 만들어줘”
- “acceptance criteria 써줘”
- “discovery 해보자”
- “JTBD로 정리해줘”
- “lean UX canvas 만들어줘”
- “시장/경쟁/회사 조사해줘”

## Role and Skill Mapping

| User intent | Primary OMA role | Codex subagent candidates | Product-Manager-Skills reference |
|---|---|---|---|
| PRD 작성/정리 | `oma-pm` | `product-manager`, `business-analyst`, `project-manager` | `skills/prd-development/SKILL.md`, `commands/write-prd.md` |
| 문제 정의 | `oma-pm`, `oma-brainstorm` | `business-analyst`, `product-manager`, `ux-researcher` | `skills/problem-statement/SKILL.md`, `skills/problem-framing-canvas/SKILL.md` |
| 기회/해결책 트리 | `oma-pm`, `oma-brainstorm` | `product-manager`, `ux-researcher` | `skills/opportunity-solution-tree/SKILL.md` |
| 기능 우선순위 | `oma-pm` | `product-manager`, `project-manager`, `risk-manager` | `skills/prioritization-advisor/SKILL.md` |
| 로드맵/워크스트림 계획 | `oma-pm`, `oma-coordination` | `project-manager`, `product-manager`, `scrum-master` | `skills/roadmap-planning/SKILL.md` |
| user story 작성 | `oma-pm` | `business-analyst`, `product-manager` | `skills/user-story/SKILL.md` |
| user story 분할 | `oma-pm` | `business-analyst`, `scrum-master` | `skills/user-story-splitting/SKILL.md` |
| 스토리맵/백로그 맵핑 | `oma-pm`, `oma-coordination` | `product-manager`, `business-analyst`, `scrum-master` | `skills/user-story-mapping/SKILL.md` |
| discovery 프로세스 | `oma-pm`, `oma-market`, `oma-search` | `ux-researcher`, `market-researcher`, `research-analyst` | `skills/discovery-process/SKILL.md` |
| 고객 여정 | `oma-pm`, `oma-design` | `ux-researcher`, `customer-success-manager` | `skills/customer-journey-map/SKILL.md`, `skills/customer-journey-mapping-workshop/SKILL.md` |
| JTBD | `oma-pm`, `oma-market` | `ux-researcher`, `market-researcher` | `skills/jobs-to-be-done/SKILL.md` |
| Lean UX canvas | `oma-pm`, `oma-design` | `product-manager`, `ux-researcher` | `skills/lean-ux-canvas/SKILL.md` |
| 시장/회사 조사 | `oma-market`, `oma-search` | `market-researcher`, `competitive-analyst`, `research-analyst` | `skills/company-research/SKILL.md`, `skills/pestel-analysis/SKILL.md`, `skills/positioning-statement/SKILL.md` |
| SaaS 지표/사업성 | `oma-pm`, `oma-market` | `data-analyst`, `market-researcher` | `skills/business-health-diagnostic/SKILL.md`, `skills/saas-revenue-growth-metrics/SKILL.md`, `skills/saas-economics-efficiency-metrics/SKILL.md` |

## Output Policy for 승찬님

PM 산출물을 만들 때 기본 출력은 다음 기준을 따릅니다.

- 개발 일정/계획은 필요 시 Obsidian `2. Area/EventNote` 또는 프로젝트별 `1. Project/<project>/`에 맞춥니다.
- `1. Project/<project>/`는 PM/whole-Gantt 중심이 아니라 기능/워크스트림 단위로 정리합니다.
- 지침/행동 규칙은 Obsidian이 아니라 `LSC_agent_skills` 또는 Hermes skill/reference에 둡니다.
- 개발로 이어지는 경우 user story에는 acceptance criteria, out-of-scope, verification 항목을 포함합니다.
- 기능 우선순위 결과는 단순 점수표만 내지 말고, 선택 기준·리스크·다음 실험/검증을 함께 제시합니다.

## How to Inspect a PM Skill

필요한 skill을 고른 뒤 원본을 직접 읽습니다.

```bash
cd /Users/iseungchan/Project/LSC_agent_skills
sed -n '1,220p' external/Product-Manager-Skills/skills/prd-development/SKILL.md
sed -n '1,220p' external/Product-Manager-Skills/commands/write-prd.md
```

전체 목록은 catalog에서 확인합니다.

```bash
cd /Users/iseungchan/Project/LSC_agent_skills
python3 - <<'PY'
from pathlib import Path
import re
for p in sorted(Path('external/Product-Manager-Skills/skills').glob('*/SKILL.md')):
    text = p.read_text(errors='ignore')
    name = re.search(r'^name:\s*(.+)$', text, re.M)
    desc = re.search(r'^description:\s*(.+)$', text, re.M)
    print(f"{name.group(1) if name else p.parent.name}: {desc.group(1) if desc else ''}")
PY
```

## Verification Checklist

- [ ] `external/Product-Manager-Skills` submodule exists.
- [ ] `catalog/skills-index.yaml` is readable.
- [ ] Chosen skill path exists under `external/Product-Manager-Skills/skills/`.
- [ ] Output follows 승찬님's Obsidian/project boundary rules.
- [ ] If a PM artifact becomes recurring Hermes behavior, update this repo or Hermes skill reference instead of only writing an Obsidian note.
