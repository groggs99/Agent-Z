# ZCG Meeting Minutes Archive

Status: directory stub. Full minutes need export from forum.
Collected date: 2026-05-27

## Purpose

ZCG meeting minutes reveal committee reasoning patterns, common objections, approval criteria in practice, and priority shifts over time. This is the highest-value corpus for training Agent Z to anticipate committee feedback.

## Known meeting minute URLs (2026)

- 2026-05-11: https://forum.zcashcommunity.com/t/zcash-community-grants-meeting-minutes-5-11-2026/55677
- 2026-04-27: https://forum.zcashcommunity.com/t/zcash-community-grants-meeting-minutes-april-27-2026/55555
- 2026-04-13: https://forum.zcashcommunity.com/t/zcash-community-grants-meeting-minutes-4-13-2026/55349
- 2026-03-30: https://forum.zcashcommunity.com/t/zcash-community-grants-meeting-minutes-3-30-2026/55196
- 2026-03-02: https://forum.zcashcommunity.com/t/zcash-community-grants-meeting-minutes-1-3-26/54874
- 2026-02-02: https://forum.zcashcommunity.com/t/zcash-community-grants-meeting-minutes-2-3-2026/54548
- 2026-01-19: https://forum.zcashcommunity.com/t/zcash-community-grants-meeting-minutes-1-19-2026/54383

## Normalised format per meeting

```yaml
date:
source_url:
collected_date:
grants_discussed:
  - grant_name:
    issue_number:
    action: approved | declined | deferred | revision_requested
    reasoning_summary:
    conditions:
committee_present:
key_themes:
agent_z_lessons:
```

## Next step

GPT should scrape each URL, extract the full text, and normalise into the format above. Older minutes (2025 and earlier) should also be collected — search the forum for the meeting-minutes tag or category.

## What to extract

For each meeting, the most valuable information is:
1. Which grants were discussed and what the committee decided.
2. Why they decided what they decided — the specific reasoning.
3. Any recurring objections or patterns across meetings.
4. Any changes to process, priorities, or wishlist items announced.
