# Agent Z — Corpus and Configuration

This directory contains everything that makes Agent Z a domain-specific grants companion: the system prompt, the knowledge corpus, and working notes.

## Directory structure

```text
prompts/                Agent Z system prompt and drafting modes
corpus/
  zcash/
    00-source-index/    Master source list with URLs and priorities
    01-official-process/  ZCG process, wishlist, committee, templates, scoring
    02-grant-examples/    Normalised approved/declined/completed grants
    03-meeting-minutes/   Committee meeting minutes and decision patterns
    04-governance-zips/   ZIP-1014, 1015, 1016 funding mechanism context
working-notes/          Internal planning and next-step tracking
manifest.json           File inventory and project metadata
CORPUS-REVIEW.md        Claude's corpus assessment and gap analysis
```

## Corpus status

Seed corpus (v0). The official ZCG process, wishlist, committee profiles, and grant-fit scoring rubric are complete. See `CORPUS-REVIEW.md` for the full gap analysis and priority next steps.

## Important caveat

This is not a full scrape. It is a curated seed corpus and approval playbook. The next step is bulk collection of complete GitHub issues, forum threads, meeting minutes, and ZCG dashboard exports.

## Corpus rules

1. Preserve source URLs and collection dates on every file.
2. Replace seed summaries with full source exports when available.
3. Keep primary source material separate from derived approval-pattern notes.
4. Separate facts, derived patterns, tactical guidance, and stale/unverified notes.
