#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "knowledge_base"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def build_handoff(limit_cases: int = 5, limit_abilities: int = 5) -> dict:
    abilities = load_json(KB / "abilities" / "seed_abilities.json")[:limit_abilities]
    cases = load_json(KB / "cases" / "2026-08-08-public-cases.json")[:limit_cases]

    return {
        "project": {
            "name": "ai-video-master-agent",
            "layer": "knowledge_and_control",
            "intended_executor": "comfyui_or_other_execution_layer",
        },
        "handoff_contract": {
            "goal": "Translate reusable AI video knowledge into execution-ready constraints",
            "notes": [
                "This package is not a node graph.",
                "This package is a compact planning and constraint handoff.",
                "Execution repos should map these fields into actual ComfyUI graphs."
            ],
        },
        "abilities": abilities,
        "cases": cases,
        "constraints": {
            "public_evidence_only": True,
            "do_not_claim_generation_without_execution": True,
            "separate_knowledge_from_runtime_graphs": True,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, help="Output JSON path")
    parser.add_argument("--limit-cases", type=int, default=5)
    parser.add_argument("--limit-abilities", type=int, default=5)
    args = parser.parse_args()

    payload = build_handoff(
        limit_cases=args.limit_cases,
        limit_abilities=args.limit_abilities,
    )
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = ROOT / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
