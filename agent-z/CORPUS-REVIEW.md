# Corpus Review — Claude Assessment

Reviewed: 2026-05-27
Reviewer: Claude (strategic design role)
Branch: agent-z/corpus-seed-v1

## Overall assessment

The seed corpus has a clean structure and the right instincts. The source index identifies the correct priority sources. The approval playbook is the strongest piece — the grant-fit scoring rubric, pre-review blocker checklist, and category-specific strategy sections give Agent Z actionable decision logic rather than generic advice. The application template reconstruction is useful but incomplete (needs the actual YAML).

The main gap is that the corpus is mostly *about* the process but contains almost no *examples of the process in action*. Agent Z cannot learn approval patterns from descriptions of patterns alone — it needs actual grants (approved and declined) with committee reasoning attached.

## What was added in this review

1. `zcg-wishlist.md` — extracted verbatim from the ZCG homepage. Critical for grant-fit scoring.
2. `zcg-grant-process.md` — full official process from the selection page.
3. `zcg-committee.md` — committee member profiles with reviewer perspective notes.
4. `zcg-rfp-program.md` — RFP and RFI submission path details.
5. `zcg-funding-overview.md` — financial context, treasury size, previously funded projects.
6. `02-grant-examples/` — directory with README, one completed example (ZeWiF), one declined example (Zenith 2025). These demonstrate the normalised format.
7. `03-meeting-minutes/` — directory with README listing all known 2026 minute URLs and extraction format.
8. `04-governance-zips/` — directory with funding mechanism summary.

## Priority gaps remaining

### 1. Bulk grant issue export (highest priority)

The single most impactful improvement. Agent Z needs 20-30 normalised grant files covering:
- 5+ approved technical grants
- 5+ approved regional/community grants
- 5+ declined grants with reasons
- 3+ completed grants showing successful milestone execution
- 2+ withdrawn or modified grants showing the revision process

GPT should use the GitHub API (authenticated to avoid rate limits) to export all issues from `ZcashCommunityGrants/zcashcommunitygrants`, then normalise each into the front-matter format defined in `working-notes/agent-z-corpus-next-steps.md`.

### 2. Meeting minutes content (high priority)

The URLs are listed but no content is scraped. Each meeting's grant decisions and reasoning are the training signal for anticipating committee feedback. GPT should scrape each URL and extract structured decisions.

### 3. Actual GitHub issue template YAML (medium priority)

The reconstructed template is good but the real YAML has exact field names, required/optional flags, and dropdown options. This should be fetched from the repo's `.github/ISSUE_TEMPLATE/` directory.

### 4. Forum thread examples (medium priority)

The forum post is a required step. Agent Z needs 3-5 examples of good forum posts accompanying grant applications to learn the tone, structure, and community interaction patterns.

### 5. Monthly update examples (medium priority)

Users will eventually need help writing milestone updates. Agent Z needs 3-5 examples of actual monthly updates posted to forum threads.

### 6. Non-technical guidance content (low priority, broken URL)

The source index references `forum.zcashcommunity.com/t/zcg-grants-guidance-for-non-technical-applications/52214` but the official process page links to `/t/guidance-for-non-technical-grant-applicants/49679` which returns 404. The correct URL needs to be found and the content scraped.

### 7. ZCG dashboard CSV export (low priority for v0)

The Google Sheets dashboard has detailed financial data. A CSV snapshot would let Agent Z reference specific grant amounts and payout timelines. Not critical for v0 but important for v1.

## Structural recommendations

### Separate primary sources from derived analysis

The approval playbook (`zcg-approval-playbook.md`) mixes primary source facts with derived tactical advice. This is fine for Agent Z's skill definitions, but the corpus should clearly distinguish:
- Primary source material (what ZCG actually says) in `01-official-process/`
- Derived analysis and tactical patterns in a new `05-analysis/` directory
- Agent Z skill definitions (what the agent should do) in a separate `skills/` directory outside the corpus

The playbook should be moved to `05-analysis/` or split into a primary-source component and a derived-analysis component.

### Add a corpus freshness tracker

ZCG process can change. Each file has a `collected_date` in the header, which is good. Add a top-level `FRESHNESS.md` that lists every file and its last-verified date so stale content can be identified and refreshed.

### Add a NEAR stub directory

The v0 scope is Zcash-first, but the repo structure should anticipate NEAR expansion. Create `agent-z/corpus/near/` with a README explaining it's Phase 3 and listing the sources we already indexed (NEAR House of Stake, NEAR Intents, Ironclaw docs) from our previous knowledge base work.

## Verdict

The seed corpus is a solid v0 foundation. The approval playbook and application template give Agent Z enough to be useful for basic grant-fit assessment right now. The priority for the next iteration is bulk grant examples and meeting minutes — those are what turn Agent Z from a process explainer into a genuine grants companion.
