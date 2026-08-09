# ComfyUI Integration

ComfyUI is one of the strongest open-source execution environments for AI image
and video workflows. This repository does not try to replace it.

Instead, `ai-video-master-agent` is meant to improve what gets sent into a
ComfyUI-based pipeline.

## Division of responsibility

### This repository does

- collect public workflow evidence
- structure reusable abilities
- define routing logic
- create exportable handoff packages
- generate human-readable weekly updates

### ComfyUI does

- actual node-graph execution
- local or remote inference orchestration
- image/video generation and transformation
- checkpoint / LoRA / control asset wiring

## Why this split is useful

ComfyUI is powerful, but a node graph alone does not solve:

- whether a workflow should exist at all
- when a pattern is stable enough to reuse
- how to separate a case from a durable ability
- how to keep a weekly public research trail
- how to preserve source evidence and method boundaries

This repository fills those gaps.

## Handoff model

The intended bridge is:

1. cases and abilities are curated locally
2. a specific goal is matched to reusable abilities
3. a compact handoff package is exported
4. a ComfyUI operator or downstream executor maps the package into a graph

## Handoff package shape

Use:

```bash
python3 scripts/export_comfyui_handoff.py --output examples/comfyui_handoff.sample.json
```

The exported package includes:

- repository metadata
- selected abilities
- linked cases
- stage coverage
- generation constraints
- review notes

This is meant to be small, inspectable, and execution-friendly.

## Practical guidance

- keep ComfyUI-specific graph logic outside the core knowledge base
- keep reusable method rules inside the knowledge base
- let execution repos own node graphs and runtime wiring
- let this repository own evidence, ability naming, and weekly synthesis
