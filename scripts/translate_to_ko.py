#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE_PATH = ROOT / ".translation-cache-ko.json"


def load_cache() -> dict[str, str]:
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    return {}


def save_cache(cache: dict[str, str]) -> None:
    CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def make_translator(cache: dict[str, str]):
    def translate(text: str) -> str:
        if not text.strip():
            return text
        if text in cache:
            return cache[text]

        placeholders: dict[str, str] = {}

        def protect(pattern: str, src: str) -> str:
            def repl(match: re.Match[str]) -> str:
                key = f"__PH_{len(placeholders)}__"
                placeholders[key] = match.group(0)
                return key

            return re.sub(pattern, repl, src)

        safe = text
        safe = protect(r"`[^`]+`", safe)
        safe = protect(r"https?://[^\s)\]]+", safe)

        chunks: list[str] = []
        current = ""
        for segment in re.split(r"(\n\s*\n)", safe):
            if len(current) + len(segment) > 2200 and current:
                chunks.append(current)
                current = segment
            else:
                current += segment
        if current:
            chunks.append(current)

        translated_parts: list[str] = []
        for chunk in chunks:
            if not chunk.strip():
                translated_parts.append(chunk)
                continue
            q = urllib.parse.quote(chunk)
            url = (
                "https://translate.googleapis.com/translate_a/single"
                f"?client=gtx&sl=en&tl=ko&dt=t&q={q}"
            )
            last_error: Exception | None = None
            for attempt in range(5):
                try:
                    with urllib.request.urlopen(url, timeout=20) as response:
                        payload = json.loads(response.read().decode("utf-8"))
                    translated_parts.append("".join(item[0] for item in payload[0]))
                    last_error = None
                    break
                except Exception as error:  # pragma: no cover
                    last_error = error
                    time.sleep(0.6 * (attempt + 1))
            if last_error is not None:
                raise RuntimeError(f"Translation failed: {last_error}") from last_error

        result = "".join(translated_parts)
        for key, value in placeholders.items():
            result = result.replace(key, value)

        cache[text] = result
        return result

    return translate


def translate_markdown(content: str, translate) -> str:
    lines = content.splitlines(keepends=True)
    output: list[str] = []
    buffer: list[str] = []
    in_fence = False

    def flush() -> None:
        nonlocal buffer
        if not buffer:
            return
        output.append(translate("".join(buffer)))
        buffer = []

    for line in lines:
        if line.lstrip().startswith("```"):
            flush()
            in_fence = not in_fence
            output.append(line)
            continue
        if in_fence:
            output.append(line)
        else:
            buffer.append(line)

    flush()
    return "".join(output)


def translate_toml(content: str, translate) -> str:
    desc_match = re.search(r'^description\s*=\s*"(.*)"\s*$', content, flags=re.MULTILINE)
    if desc_match:
        original = desc_match.group(1)
        translated = translate(original).replace('"', '\\"')
        replacement = f'description = "{translated}"'
        content = content[: desc_match.start()] + replacement + content[desc_match.end() :]

    dev_match = re.search(
        r'developer_instructions\s*=\s*"""\n(.*?)\n"""', content, flags=re.DOTALL
    )
    if dev_match:
        original = dev_match.group(1)
        translated = translate(original).strip("\n")
        replacement = f'developer_instructions = """\n{translated}\n"""'
        content = content[: dev_match.start()] + replacement + content[dev_match.end() :]

    return content


def main() -> None:
    cache = load_cache()
    translate = make_translator(cache)

    md_files = [ROOT / "README.md", ROOT / "CONTRIBUTING.md"]
    md_files.extend(sorted((ROOT / "categories").glob("*/README.md")))

    for md_file in md_files:
        source = md_file.read_text(encoding="utf-8")
        md_file.write_text(translate_markdown(source, translate), encoding="utf-8")
        print(f"translated md: {md_file.relative_to(ROOT)}")

    toml_files = sorted((ROOT / "categories").glob("**/*.toml"))
    for toml_file in toml_files:
        source = toml_file.read_text(encoding="utf-8")
        toml_file.write_text(translate_toml(source, translate), encoding="utf-8")
        print(f"translated toml: {toml_file.relative_to(ROOT)}")

    save_cache(cache)
    print(f"done: {len(md_files)} markdown, {len(toml_files)} toml")


if __name__ == "__main__":
    main()
