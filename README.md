# Agent Z

**Agent Z** is a Zcash-first grants companion agent designed to run on [IronClaw](https://docs.ironclaw.com). It helps applicants assess grant fit, draft stronger proposals, and navigate the Zcash Community Grants process.

## What Agent Z does

- Assesses whether an idea fits the ZCG funding criteria and wishlist.
- Identifies risks, weak points, and missing elements before submission.
- Drafts GitHub grant applications and companion forum posts.
- Recommends grant category, milestone structure, and budget breakdown.
- Reviews drafts for likely committee objections.
- Helps write monthly milestone updates.
- Refuses trading advice, price predictions, wallet/private-key handling, impersonation, astroturfing, and governance manipulation.

## What Agent Z does not do

Agent Z is not a trading assistant, financial advisor, wallet agent, private-key handler, automatic poster, or governance manipulator. It is a pre-submission reviewer and drafting companion.

## Architecture

Agent Z is a domain-specific agent deployed on IronClaw. IronClaw provides the agent runtime (chat interface, memory, skills engine, security). Agent Z provides the specialisation: identity files, grant-writing skills, and a curated corpus of ZCG process knowledge, grant precedents, and committee reasoning patterns.

## Repo structure

```text
agent-z/
  prompts/              Agent Z system prompt and drafting modes
  corpus/
    zcash/
      00-source-index/  Master source list with URLs and priorities
      01-official-process/  ZCG process, wishlist, committee, templates
      02-grant-examples/    Normalised approved/declined/completed grants
      03-meeting-minutes/   Committee meeting minutes and decision patterns
      04-governance-zips/   ZIP-1014, 1015, 1016 funding mechanism context
  working-notes/        Internal planning and next-step tracking
  manifest.json         File inventory and project metadata
  CORPUS-REVIEW.md      Claude's corpus assessment and gap analysis
```

## Current status

Seed corpus (v0). The official ZCG process, wishlist, committee profiles, funding overview, and grant-fit scoring rubric are in place. Bulk grant examples and meeting minutes are the next priority.

## Division of responsibility

- **Niall**: integrator and shipping decision-maker.
- **GPT**: corpus collection, formatting, scraping, markdown structuring, bulk data cleaning.
- **Claude**: strategic design, skill definitions, mission configs, identity files, prompt architecture, MVP scoping.

## MVP target

**Agent Z v0.1 — ZCG Grant Fit + Drafting Assistant**

User describes an idea → Agent asks 2-3 targeted questions → Agent produces a grant-fit score, wishlist alignment, risks, recommended category, milestone plan, budget structure, GitHub application draft, and forum post draft.

## Data sources

All corpus data is from public sources: the ZCG website, GitHub grant applications, Zcash Community Forum, ZCG meeting minutes, and Zcash Improvement Proposals. See `agent-z/corpus/zcash/00-source-index/source-index.md` for the full list.
