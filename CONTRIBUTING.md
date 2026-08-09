# Contributing

Thanks for contributing to `ai-video-master-agent`.

中文贡献说明见：[`docs/zh-CN/contributing.md`](./docs/zh-CN/contributing.md)

## What We Accept

We welcome contributions in these areas:

- public-source AI video cases
- reusable ability definitions
- documentation improvements
- schema improvements
- weekly digest quality
- sync tooling and repository automation

## What We Do Not Accept

- private or paywalled material without a clear public fallback
- credentials, tokens, or account-specific configuration
- unverifiable claims about model outputs
- media dumps with no knowledge structure
- vague prompt collections with no reusable logic

## Contribution Principles

1. Prefer public, traceable sources.
2. Separate facts, inferences, and recommendations.
3. Do not claim a model or tool was used unless it actually was.
4. Do not promote a one-off trick into a durable ability without evidence.
5. Keep execution-layer claims out of the knowledge layer unless they are verified.

## Repository Workflow

### Cases

When adding a case:

1. Use a public, readable source.
2. Record the original URL.
3. Add a concise method summary.
4. Add a reusable template.
5. State the evidence boundary.
6. Link to existing abilities when appropriate.

### Abilities

When adding an ability:

1. Use a stable `ability_id` in snake_case.
2. Keep the ability definition minimal and reusable.
3. State the applicable stages.
4. Link back to the source case URLs.
5. Avoid tool-specific hype unless the rule is genuinely durable.

## Before Opening a Pull Request

Run:

```bash
python3 scripts/validate_knowledge_base.py
python3 scripts/generate_weekly_digest.py --date 2026-08-09
```

Then review:

- duplicated case URLs
- missing required fields
- broken cross-links between cases and abilities
- overclaimed evidence
- English/Chinese doc consistency when relevant

## Pull Request Expectations

A good pull request should explain:

- what changed
- why it changed
- what evidence supports it
- whether this affects weekly reports, schemas, or sync logic

## Style

- Keep docs clear and direct.
- Prefer precise nouns over hype.
- Keep code simple and scriptable.
- Keep the knowledge base auditable.
