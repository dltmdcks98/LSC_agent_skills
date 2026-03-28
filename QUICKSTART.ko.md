# 빠른 시작 (한국어)

이 저장소를 클론한 뒤 바로 Codex 하위 에이전트를 쓰려면 아래만 실행하세요.

```bash
chmod +x ./install-subagents.sh
./install-subagents.sh --global
```

프로젝트 로컬 설치를 원하면:

```bash
./install-subagents.sh --project
```

특정 카테고리만 설치:

```bash
./install-subagents.sh --project --category 04-quality-security
```

특정 에이전트 하나만 설치:

```bash
./install-subagents.sh --agent reviewer.toml --global
```

설치 후 Codex 세션을 새로고침/재시작하면 하위 에이전트를 바로 사용할 수 있습니다.
