# Contributing (한국어 안내)

기여해 주셔서 감사합니다. 이 저장소는 Codex 하위 에이전트(`.toml`)를 모으는 컬렉션이며, 실무에 바로 쓸 수 있는 명확한 역할 정의를 목표로 합니다.

## 새 에이전트 추가

1. `categories/`에서 적절한 카테고리를 선택합니다.
2. 새 에이전트 `.toml` 파일을 추가합니다.
3. 아래 문서를 함께 업데이트합니다.
   - `README.md`
   - `categories/<category>/README.md`
4. 기존 에이전트와 이름/역할이 겹치지 않는지 확인합니다.
5. PR 설명에 추가 이유와 기대 효과를 적습니다.

## 기존 에이전트 개선

1. 역할 범위를 명확히 유지합니다.
2. Codex 기본 TOML 형식을 유지합니다.
3. 동작이 달라졌다면 관련 README 설명도 같이 수정합니다.
4. PR에 변경 전/후 차이와 의도를 요약합니다.

## 필수 필드

모든 에이전트 파일에는 다음 필드가 있어야 합니다.

- `name`
- `description`
- `developer_instructions`

자주 사용하는 선택 필드:

- `model`
- `model_reasoning_effort`
- `sandbox_mode`
- `mcp_servers`

## 작성 가이드

`developer_instructions`는 실행 가능한 지침이어야 합니다. 아래 항목을 권장합니다.

- Working mode
- Focus on
- Quality checks
- Return
- Do not ... unless explicitly requested by the parent agent.

피해야 할 내용:

- 지원되지 않는 도구/플랫폼을 전제로 한 지시
- 근거 없는 과도한 역할 확장
- "항상 모든 작업을 수행" 같은 범위 무제한 지시

## 모델/샌드박스 권장

- 기본 모델은 `gpt-5.4` 권장
- 경량 검색/합성 작업은 `gpt-5.3-codex-spark` 고려
- 리뷰/리서치는 기본 `read-only`
- 실제 파일 변경이 필요할 때만 `workspace-write`

## PR 전 체크리스트

- [ ] 에이전트 TOML 파일을 추가/수정했다.
- [ ] 메인 `README.md`를 업데이트했다.
- [ ] 해당 카테고리 `README.md`를 업데이트했다.
- [ ] 링크와 파일 경로를 점검했다.
- [ ] `name` 중복 여부를 확인했다.
- [ ] 변경 이유와 기대 효과를 PR 본문에 작성했다.

## 스타일 가이드

- 문장은 간결하고 명확하게 작성합니다.
- 마케팅 문구보다 작업 지침 중심으로 작성합니다.
- 모호한 표현 대신 검증 가능한 행동 지시를 사용합니다.

## 라이선스

기여물은 저장소 라이선스(MIT) 조건을 따릅니다.
