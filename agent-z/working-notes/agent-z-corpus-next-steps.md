# Agent Z Corpus Next Steps

Collected date: 2026-05-26

## What is done on this branch

- Created `agent-z/corpus-seed-v1` branch.
- Added Agent Z corpus README.
- Added ZCG source index.
- Added approval-focused ZCG playbook.
- Added reconstructed ZCG GitHub application template.

## Highest-priority next ingestion work

1. Export the full GitHub issue template YAML from `ZcashCommunityGrants/zcashcommunitygrants`.
2. Bulk export GitHub issues from `ZcashCommunityGrants/zcashcommunitygrants`.
3. Split issues by status:
   - approved;
   - pending;
   - declined;
   - withdrawn;
   - complete;
   - not meeting criteria.
4. Export full ZCG meeting-minutes archive from the forum.
5. Export ZCG dashboard sheets as CSV.
6. Create one normalized markdown file per grant.
7. Collect monthly/milestone update examples.
8. Expand ZIP 1014, ZIP 1015, ZIP 1016 notes.
9. Build evaluation fixtures for Agent Z grant-fit scoring.

## Normalized grant file front matter

```yaml
title:
source_url:
forum_url:
collected_date:
source_type: github_issue
status:
category:
requested_amount_usd:
approved_amount_usd:
applicant:
organization:
proposal_type:
zcg_priority_alignment:
committee_decision:
committee_reasoning_summary:
agent_z_lessons:
```

## Normalized grant file body

```markdown
# [Grant title]

## Summary

## Zcash alignment

## Problem

## Proposed solution

## Deliverables

## Milestones and budget

## Forum/community response

## Committee decision / status

## Agent Z lessons

## Source excerpts
```

## Immediate Agent Z evaluation fixtures

1. Weak regional grant: should push back on vague impact, no track record, weak budget, no Zcash-specific value.
2. Strong regional grant: should identify fit and suggest pilot milestones.
3. Technical wallet grant: should check wishlist alignment, dependencies, tests, reviewers, and KYC threshold.
4. Overbroad cross-chain proposal: should flag high budget, unclear Zcash benefit, and weak community demand.
5. Monthly update generation: should produce milestone update with completed work, evidence links, blockers, next steps, and payout readiness.
