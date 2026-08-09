#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "knowledge_base"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def require_keys(items: Iterable[dict], required: set[str], label: str) -> list[str]:
    errors: list[str] = []
    for index, item in enumerate(items):
        missing = sorted(required - set(item))
        if missing:
            errors.append(f"{label}[{index}] missing keys: {', '.join(missing)}")
    return errors


def main() -> int:
    errors: list[str] = []

    abilities_path = KB / "abilities" / "seed_abilities.json"
    abilities = load_json(abilities_path)
    if not isinstance(abilities, list):
        errors.append("seed_abilities.json must be a JSON list")
        abilities = []

    ability_required = {
        "ability_id",
        "name",
        "category",
        "status",
        "stages",
        "summary",
        "template",
        "source_case_urls",
    }
    errors.extend(require_keys(abilities, ability_required, "ability"))

    ability_ids = set()
    for item in abilities:
        ability_id = item.get("ability_id")
        if ability_id in ability_ids:
            errors.append(f"duplicate ability_id: {ability_id}")
        ability_ids.add(ability_id)

    case_required = {
        "title",
        "source",
        "url",
        "published_at",
        "captured_date",
        "content_types",
        "stages",
        "credibility",
        "summary",
        "template",
        "evidence_boundary",
    }

    case_dir = KB / "cases"
    case_files = sorted(case_dir.glob("*.json"))
    if not case_files:
        errors.append("no case JSON files found")

    seen_urls = set()
    for case_file in case_files:
        cases = load_json(case_file)
        if not isinstance(cases, list):
            errors.append(f"{case_file.name} must be a JSON list")
            continue
        errors.extend(require_keys(cases, case_required, case_file.name))
        for item in cases:
            url = item.get("url")
            if url in seen_urls:
                errors.append(f"duplicate case url: {url}")
            seen_urls.add(url)
            for ability_id in item.get("ability_links", []):
                if ability_id not in ability_ids:
                    errors.append(
                        f"{case_file.name} references unknown ability_id: {ability_id}"
                    )

    if errors:
        print("Knowledge base validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Knowledge base validation passed.")
    print(f"Abilities: {len(abilities)}")
    print(f"Case files: {len(case_files)}")
    print(f"Unique case URLs: {len(seen_urls)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
