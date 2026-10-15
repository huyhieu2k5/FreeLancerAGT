# Future specialized freelancer sub-agent handoff

## Purpose
Train or configure a future narrow-scope worker agent from **reproducible skills, evidence and policy**, not from an invented human CV or unsupported self-description. This document does not imply a currently deployed or self-running agent.

## Sources of truth
1. `agent/skills.json`: public skill allowlist and evidence status.
2. `agent/PROFILE.md`: transparency and truthful representation of human owner versus AI operator.
3. Local v0.4 pilot archive (ChatGPT project): `agent.py`, `integrations.py`, `mcp_server.py`, tests and experiments. **The archive is not yet completely synced to GitHub.**
4. Official Superteam skill and payout rules: https://superteam.fun/skill.md.

## Delegation design
- **Discovery**: Fetch only official/authorized listing APIs; never assume a missing proposal count means low competition.
- **Qualification**: Reject listing when agentAccess is not AGENT_ALLOWED / AGENT_ONLY; verify deadline, payment terms, sponsor identity, scope, jurisdiction, forbidden conduct and AI permission.
- **Skill routing**: Match narrow capabilities to task deliverables; public marketing only from `list_for_agent=true`. Unrecognized task => manual review.
- **Production**: Work only with authorized input; generate deliverables in private workspace with stable hashes and provenance.
- **Verification**: Run task-specific independent tests and document failures without overclaiming.
- **Application / delivery**: Human approval, required platform authorization, anti-spam and terms compliance. Do not implement unattended submissions until explicitly authorized and proven compliant.
- **Payment**: Human claimant handles identity and payout, chain/network/fees. Only settled funds are booked as income.

## Capability states
- `PILOT_TESTED`: bounded demo and tests only, eligible for controlled pilot marketing, not a promise of job success.
- `PARTIALLY_TESTED`: source code exists but external task-specific QA insufficient; manual qualification.
- `MOCK_TESTED_ONLY`: only simulated API interactions; live auth unverified.
- `EXPERIMENTAL`: candidate skill with no end-to-end independent test evidence.

## Promotion checklist for each new skill
- Scope, allowed I/O and forbidden operations documented.
- Reproducible fixture(s), executable tests, expected outputs, and failure cases.
- Independent held-out task checks and human/operator review of quality.
- Sponsor rules, license, confidentiality and AI disclosure checked.
- Conservative economics: estimate time, compute/gas and platform fees; never promise a payout.
- Publish evidence and owner approve changed `skills.json` before adding to profile.

## Metrics on real jobs
Track `listing_id`, `agent_access`, `reward_currency`, `expected_net_amount`, `submissions_observed`, `deliverable_type`, `tests_passed`, `human_approved`, `submitted_at`, `awarded_at`, `settled_at`, `actual_fees`, `actual_net_income`. Keep private data off GitHub.

Never train on unlicensed confidential customer work or pass account access, identity documents, wallet seeds or passwords to the sub-agent.

## Current blockers
Superteam agent registration, live API proof, real claimant profile, real award, real payout: **unverified** as of 2026-10-15. No live autonomous income loop has been demonstrated.
