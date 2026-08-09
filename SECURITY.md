# Security Policy

## Supported Scope

This repository is primarily a knowledge and automation project, not a production
inference service. The most relevant security concerns are:

- accidental publication of credentials
- accidental publication of private assets
- unsafe automation defaults
- repository workflows that overclaim or overwrite data

## Reporting a Vulnerability

If you discover a security issue:

1. Do not post secrets publicly in an issue.
2. Describe the issue with enough detail to reproduce it safely.
3. State whether the problem affects:
   - local scripts
   - GitHub workflows
   - documentation
   - sync contracts

## Secrets Handling

Never commit:

- API keys
- session tokens
- Notion tokens
- private cookies
- account exports containing personal data

## Automation Safety

Scheduled workflows should:

- validate before publishing
- avoid destructive behavior by default
- make generated changes reviewable
- avoid pretending that external writes succeeded without verification
