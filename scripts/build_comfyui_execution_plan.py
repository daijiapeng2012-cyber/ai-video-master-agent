#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def build_plan(goal: str, workflow_family: str) -> dict:
    return {
        "plan_id": "plan_comfyui_demo_001",
        "goal": goal,
        "workflow_family": workflow_family,
        "model_route": {
            "checkpoint_family": "video_or_reference_first",
            "lora_stack": [],
            "reason": "Prefer a controlled starter route before graph expansion."
        },
        "inputs": {
            "prompt": "subject + action + camera move + environment response + ending state",
            "negative_prompt": "uncontrolled drift, extra limbs, broken continuity, random camera jumps",
            "references": [
                {
                    "id": "REF-CHAR-001",
                    "role": "character_anchor",
                    "path_or_url": "reference://character_anchor"
                },
                {
                    "id": "REF-LOC-001",
                    "role": "location_anchor",
                    "path_or_url": "reference://location_anchor"
                }
            ]
        },
        "controls": {
            "aspect_ratio": "16:9",
            "duration_target": "5-8s",
            "seed_policy": "lock_seed_on_probe_then_branch",
            "control_assets": [
                "reference_images",
                "camera_path_if_available"
            ]
        },
        "outputs": {
            "target_type": "preview_video_or_keyframe_sequence",
            "expected_paths": [
                "output/comfyui/run_001/preview.mp4",
                "output/comfyui/run_001/review_notes.md"
            ]
        },
        "review": {
            "gates": [
                "file_exists",
                "aspect_ratio_match",
                "subject_identity_holds",
                "camera_motion_matches_intent",
                "ending_state_is_visible"
            ]
        },
        "retry_policy": {
            "max_retries": 2,
            "change_after_first_failure": "adjust workflow family inputs or reference binding, not random prompt churn"
        }
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--goal", default="Generate a controlled AI video task plan for ComfyUI")
    parser.add_argument("--workflow-family", default="image_to_video_reference")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(build_plan(args.goal, args.workflow_family), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
