# AI Video Master Agent

[中文说明](./README.zh-CN.md) | [English Docs](./docs/en/) | [中文文档](./docs/zh-CN/)

`ai-video-master-agent` is an open-source knowledge-and-control repository for AI video production.

It is designed to turn scattered prompts, public case studies, and model-specific tips into a maintainable project with:

- reusable `skills/`
- a structured `knowledge_base/`
- weekly public `reports/`
- automation-ready `scripts/`
- a clean interface to an execution layer such as [`ai-video-supervisor`](../ai-video-supervisor/README.md)

This repository does **not** claim to render images or videos by itself. Its job is to organize methods, evidence, routing rules, and production knowledge into a system that can be reviewed, versioned, and continuously improved.

## Why This Repo Exists

Most AI video workflows fail in one of two ways:

1. They remain prompt piles with no durable knowledge layer.
2. They mix research, prompt craft, production status, and media outputs into one unmaintainable folder.

This repository separates those concerns:

- `knowledge_base/` stores reusable abilities and public case evidence.
- `skills/` defines how the agent should think, filter, route, and upgrade methods.
- `reports/weekly/` turns ongoing scanning into public updates.
- `automation/` documents the ongoing maintenance contract.
- `scripts/` makes validation and digest generation reproducible.

## Repository Scope

### Included

- public-source AI video cases
- reusable ability definitions
- agent routing rules
- weekly digest generation
- Notion sync contract and local source-of-truth files
- multilingual documentation

### Not Included

- direct image rendering
- direct video rendering
- private credentials or tokens
- private media assets
- claims that an external model was used when it was not

## Repository Structure

```text
ai-video-master-agent/
  .github/
  automation/
  config/
  data/
  docs/
    en/
    zh-CN/
  knowledge_base/
    abilities/
    cases/
    schemas/
  reports/
    weekly/
  scripts/
  skills/
  CHANGELOG.md
  CONTRIBUTING.md
  CODE_OF_CONDUCT.md
  LICENSE
  README.md
  README.zh-CN.md
  SECURITY.md
```

## Core Components

### 1. Skills

`skills/` contains repository-local operating instructions for the AI Video Master Agent.

Current core skills:

- `ai-video-master-director`
- `ai-video-radar-librarian`

These are responsible for deciding:

- when to reuse an existing ability
- when to add a case
- when to promote a pattern into a durable ability
- when to hand work off to the execution layer

### 2. Knowledge Base

`knowledge_base/` is the repository's local truth source for reusable knowledge.

It currently stores:

- `abilities/seed_abilities.json`
- `cases/*.json`
- schema definitions for both

This layer is intentionally Git-friendly and can be mirrored into Notion later, but Notion is **not** treated as the only source of truth.

### 3. Weekly Reports

`reports/weekly/` contains public-facing weekly summaries.

A good weekly report should capture:

- newly added cases
- newly added abilities
- recurring workflow patterns
- evidence boundaries

### 4. Execution Interface

This repository is the **knowledge/control** layer.

[`ai-video-supervisor`](../ai-video-supervisor/README.md) remains the **execution** layer.

Recommended flow:

1. `ai-video-master-agent` discovers and solidifies rules.
2. `ai-video-supervisor` uses those rules in actual shot packages, prompts, reviews, and handoffs.
3. Stable lessons flow back into this repository as upgraded abilities and docs.

## Built-in Seed

Current seed content includes:

- 10 public AI video cases
- 10 reusable abilities
- 2 core skill definitions
- weekly digest generation
- knowledge base validation
- multilingual documentation scaffolding
- GitHub community health files

## Quick Start

```bash
cd /Users/jiapeng/Projects/AIGC/ai-video-master-agent
python3 scripts/validate_knowledge_base.py
python3 scripts/generate_weekly_digest.py --date 2026-08-09
```

Generated output example:

- [`reports/weekly/2026-W32.md`](./reports/weekly/2026-W32.md)

## Documentation

- [Architecture](./docs/en/architecture.md)
- [Weekly Update Workflow](./docs/en/weekly-update-workflow.md)
- [Notion Sync Contract](./docs/en/notion-sync-contract.md)
- [Reference Projects](./docs/en/reference-projects.md)
- [Roadmap](./docs/en/roadmap.md)

Chinese mirrors:

- [架构说明](./docs/zh-CN/architecture.md)
- [周更工作流](./docs/zh-CN/weekly-update-workflow.md)
- [Notion 同步合同](./docs/zh-CN/notion-sync-contract.md)
- [参考项目](./docs/zh-CN/reference-projects.md)
- [路线图](./docs/zh-CN/roadmap.md)

## Open Source

This project is released under the [MIT License](./LICENSE).

The intent is to make the repository:

- easy to fork
- easy to audit
- easy to keep updating weekly
- safe to separate from private production folders

## Continuous Update Model

This repository is intended to be updated continuously through:

- daily or periodic case ingestion
- weekly digest generation
- ability upgrades when patterns stabilize
- documentation refinement
- GitHub Actions validation and scheduled digest generation

## Publishing Guidance

When publishing this as a dedicated GitHub repository, push:

- `README*`
- `docs/`
- `skills/`
- `knowledge_base/`
- `reports/weekly/`
- `scripts/`
- community health files under `.github/`

Do **not** publish:

- private drafts
- local credentials
- private assets
- internal tokens
- unverified production outputs
