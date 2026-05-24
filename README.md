# IronBridge

**IronBridge** is a privacy-first NEAR × Zcash ecosystem research and governance drafting agent designed to run on Ironclaw.

Its purpose is to help NEAR and Zcash users understand collaboration opportunities, draft better forum/governance/grant posts, and surface relevant context before proposing work.

## v0 Scope

IronBridge v0 is deliberately narrow:

- Answer questions about NEAR, Zcash, Ironclaw, NEAR Intents, governance, grants, and ecosystem collaboration.
- Draft Zcash forum posts and ZCG-style grant outlines.
- Draft NEAR governance discussion posts and HSP-style outlines.
- Review drafts for likely objections, weak claims, missing evidence, privacy concerns, and community-fit issues.
- Refuse trading advice, price predictions, wallet/private-key handling, impersonation, astroturfing, and governance manipulation.

## Why this exists

NEAR has agent infrastructure and chain abstraction through Intents. Zcash has a privacy-first community and a culture that is naturally cautious about cloud-hosted AI tools. Ironclaw creates a potential bridge: an auditable, privacy-first agent runtime that can help users participate more effectively without asking them to trust a generic cloud chatbot.

## Repo structure

```text
agent/                  Agent identity and operating rules
prompts/                System prompt and drafting modes
sources/                Source manifests and seed corpus list
data/raw/claude_research/  Drop research notes here
data/processed/         Generated chunks for ingestion
docs/                   Launch plan and public-facing notes
evals/                  Demo script and evaluation tests
scripts/                Corpus build and check scripts
```

## v0 Launch Goal

A working Ironclaw agent that can:

1. Explain Ironclaw to a skeptical Zcash user.
2. Draft a credible Zcash Community Collaborations post.
3. Draft a NEAR governance discussion post for an Ironclaw Builder Fund.
4. Review both drafts for objections and weak assumptions.
5. Refuse financial advice and manipulative governance requests.

## Non-goals

IronBridge is not a trading assistant, financial advisor, wallet agent, private-key handler, automatic poster, or governance manipulator.

## Status

Initial scaffold. Claude research and additional primary sources should be added to `data/raw/claude_research/` and `sources/source_manifest_template.csv`.
