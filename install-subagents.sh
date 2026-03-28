#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC_DIR="${ROOT_DIR}/categories"

TARGET_SCOPE="global"
TARGET_DIR="${HOME}/.codex/agents"
CATEGORY=""
AGENT_FILE=""

usage() {
  cat <<'EOF'
사용법:
  ./install-subagents.sh [옵션]

옵션:
  --global                전역 설치(기본값): ~/.codex/agents
  --project               현재 저장소 기준 .codex/agents 로 설치
  --category <폴더명>     특정 카테고리만 설치 (예: 01-core-development)
  --agent <파일명>        특정 에이전트 파일만 설치 (예: backend-developer.toml)
  --target <경로>         설치 경로 직접 지정
  -h, --help              도움말 출력

예시:
  ./install-subagents.sh --global
  ./install-subagents.sh --project --category 04-quality-security
  ./install-subagents.sh --agent reviewer.toml --target ~/.codex/agents
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --global)
      TARGET_SCOPE="global"
      TARGET_DIR="${HOME}/.codex/agents"
      shift
      ;;
    --project)
      TARGET_SCOPE="project"
      TARGET_DIR="${ROOT_DIR}/.codex/agents"
      shift
      ;;
    --category)
      CATEGORY="${2:-}"
      shift 2
      ;;
    --agent)
      AGENT_FILE="${2:-}"
      shift 2
      ;;
    --target)
      TARGET_DIR="${2:-}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "알 수 없는 옵션: $1" >&2
      usage
      exit 1
      ;;
  esac
done

if [[ ! -d "${SRC_DIR}" ]]; then
  echo "오류: categories 디렉토리를 찾을 수 없습니다: ${SRC_DIR}" >&2
  exit 1
fi

mkdir -p "${TARGET_DIR}"

copied_count=0

copy_agent_file() {
  local src_file="$1"
  cp "${src_file}" "${TARGET_DIR}/"
  copied_count=$((copied_count + 1))
}

if [[ -n "${AGENT_FILE}" ]]; then
  match="$(find "${SRC_DIR}" -type f -name "${AGENT_FILE}" | head -n 1 || true)"
  if [[ -z "${match}" ]]; then
    echo "오류: 에이전트 파일을 찾을 수 없습니다: ${AGENT_FILE}" >&2
    exit 1
  fi
  copy_agent_file "${match}"
else
  if [[ -n "${CATEGORY}" ]]; then
    category_dir="${SRC_DIR}/${CATEGORY}"
    if [[ ! -d "${category_dir}" ]]; then
      echo "오류: 카테고리를 찾을 수 없습니다: ${CATEGORY}" >&2
      exit 1
    fi
    while IFS= read -r -d '' file; do
      copy_agent_file "${file}"
    done < <(find "${category_dir}" -maxdepth 1 -type f -name "*.toml" -print0)
  else
    while IFS= read -r -d '' file; do
      copy_agent_file "${file}"
    done < <(find "${SRC_DIR}" -type f -name "*.toml" -print0)
  fi
fi

echo "설치 완료:"
echo "- 범위: ${TARGET_SCOPE}"
echo "- 대상 경로: ${TARGET_DIR}"
echo "- 복사된 에이전트 파일 수: ${copied_count}"
echo
echo "다음 단계:"
echo "1) Codex 세션을 새로고침하거나 재시작하세요."
echo "2) 프롬프트에서 하위 에이전트를 명시적으로 호출하세요."
