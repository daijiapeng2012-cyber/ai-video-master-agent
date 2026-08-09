# ComfyUI Bridge

This directory is reserved for lightweight integration contracts between the
knowledge layer and ComfyUI-based execution.

## Current state

The repository currently exports a compact JSON handoff package via:

```bash
python3 scripts/export_comfyui_handoff.py --output examples/comfyui_handoff.sample.json
```

## Design rule

Do not commit giant workflow JSON dumps here by default.

Prefer:

- small mapping examples
- field contracts
- handoff schemas
- execution notes

Keep runtime-specific graphs in a separate execution repository unless there is
a clear reason to version them here.
