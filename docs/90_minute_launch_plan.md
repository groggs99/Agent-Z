# 90-Minute IronBridge Launch Plan

## Goal

Ship a credible v0 demo of IronBridge: a privacy-first NEAR × Zcash information and governance drafting agent designed for Ironclaw.

## Minute 0-15: Repo and prompt

- Confirm GitHub repo exists.
- Add README, system prompt, drafting modes, source manifest, and demo script.
- Copy `prompts/ironbridge_system_prompt.md` into the Ironclaw agent setup.

## Minute 15-35: Seed knowledge

- Add the most important source links from `sources/seed_sources.csv`.
- Add Claude research outputs to `data/raw/claude_research/` when available.
- If full ingestion is not ready, paste the highest-leverage summaries manually into the agent context.

## Minute 35-55: Demo prompts

Run these prompts:

1. Explain IronBridge to a skeptical Zcash user.
2. Draft a Zcash Community Collaborations post.
3. Draft a NEAR governance post for an Ironclaw Builder Fund.
4. Review both drafts for objections.
5. Refuse a price prediction request.

## Minute 55-75: Fix obvious failures

Check whether the agent:

- overclaims privacy;
- gives financial advice;
- invents facts;
- sounds too much like NEAR marketing when addressing Zcash;
- fails to ask for sources when needed.

Update the system prompt if needed.

## Minute 75-90: Public proof

- Save the best outputs.
- Post a short launch/update message.
- Ask for source suggestions, privacy objections, and test users.

## Win condition

A working demo that can draft a credible Zcash post, draft a credible NEAR governance post, and explain privacy/trust assumptions without hype.
