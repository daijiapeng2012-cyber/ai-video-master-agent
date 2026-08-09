# Notion Sync Contract

This repository is designed to work with, but not depend entirely on, Notion.

## Current mapped sources

See [`config/notion_sources.json`](../../config/notion_sources.json).

## Rules

1. Each case should exist as an independent record.
2. Each durable ability should exist as an independent ability record.
3. A write receipt is not enough; fetch-back and final verification are required.
4. The system page should remain structural, not a daily dump target.
5. This repository keeps a local versioned representation of the same knowledge.

## Source of truth model

- Git repository: versioned local truth for public and reusable knowledge
- Notion: operational database and collaboration surface

## Sync expectation

Future sync tooling should:

- read schema first
- deduplicate by original URL first
- verify writes by readback
- never claim success from create receipts alone
