# Architecture

## One-line summary

AI Video Master Agent = `radar` + `knowledge base` + `skills` + `execution interface`

## Layers

### 1. Radar Layer

Input:

- public tutorials
- official changelogs
- public workflow writeups
- reproducible case studies

Output:

- structured case entries
- evidence boundaries
- candidate reusable patterns

### 2. Knowledge Layer

Input:

- curated high-signal cases

Output:

- abilities
- categories
- stages
- templates

### 3. Skill Layer

Input:

- user intent
- current knowledge base
- repository rules

Output:

- routing decisions
- upgrade decisions
- execution handoff strategy

### 4. Execution Interface Layer

This repository does not render media directly.

Instead, it provides stable knowledge to an execution repository such as
`ai-video-supervisor`, where prompts, manifests, review states, and handoffs are
managed against actual project runs.

## Main design rules

1. Public evidence first.
2. Cases are not automatically abilities.
3. Notion is not the only durable store.
4. The execution layer must remain separate from the knowledge layer.
5. Changelogs can prove parameter constraints without proving visual quality.
