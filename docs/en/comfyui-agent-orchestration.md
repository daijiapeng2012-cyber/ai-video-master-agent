# Agent Orchestration for ComfyUI

Yes, ComfyUI can be automated with agents, but the useful target is **not**
"let an agent click around the interface blindly."

The better pattern is:

1. the agent builds a structured execution plan
2. the plan chooses a workflow family
3. a thin adapter maps that plan into ComfyUI graph parameters
4. review and retry remain explicit

## Why the UI feels hard

ComfyUI is powerful because it exposes graph-level control, but that also means:

- too many node choices
- too many runtime combinations
- too many hidden assumptions in community workflows
- easy drift between "looks cool" and "actually reusable"

An agent helps most at the layer above the graph:

- select the right workflow family
- bind references and constraints
- choose model route
- define retry policy
- generate a small execution contract

## Recommended architecture

### Layer 1: Knowledge and routing

Use `ai-video-master-agent` for:

- ability selection
- case-backed reasoning
- stage-aware planning
- evidence boundaries

### Layer 2: Plan generation

Generate a compact plan with fields like:

- task goal
- workflow family
- input references
- duration / aspect ratio / output target
- model route
- control assets
- review gates
- fallback strategy

### Layer 3: ComfyUI adapter

A thin execution adapter should:

- choose a saved workflow template
- inject prompt, references, checkpoint, LoRA, and settings
- launch the graph
- record output paths and runtime state

### Layer 4: Review loop

The review loop should stay outside the graph:

- validate files exist
- capture review notes
- decide retry vs revise vs approve

## What should be automated first

Good first automation targets:

1. workflow-family selection
2. prompt and reference binding
3. seed / checkpoint / LoRA preset routing
4. export of an execution plan
5. deterministic retry policy

Do **not** start with:

- full free-form node synthesis from scratch
- blind UI clicking as the primary strategy
- giant end-to-end graphs with no intermediate checks

## Workflow families

A practical agent usually does better by choosing among workflow families than by
inventing graphs every time.

Example families:

- `text_to_video_base`
- `image_to_video_reference`
- `character_consistency_ref`
- `dialogue_performance_branch`
- `clean_plate_fix`
- `relight_pass`

## Repository support

This repository now includes:

- a ComfyUI handoff exporter
- a planning schema for agent-generated ComfyUI execution plans
- a starter script that builds a reviewable plan JSON

Use these as the bridge between knowledge and execution.
