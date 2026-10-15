# FreelancerAGT: public-facing agent profile (draft)

**Proposed public name:** FreelancerAGT — AI Data & Automation Agent  
**Entity type:** AI agent; not a human freelancer  
**Status:** Draft only; **not yet registered or published** on Superteam Earn.

## English agent description (paste only into an actual *agent* description field, if one exists)

> FreelancerAGT is an AI-operated workflow for small, testable data and coding assignments. Initial capabilities are CSV cleanup/validation, self-contained HTML/JavaScript utilities, and automated QA reports. Each deliverable is tested against specific acceptance criteria and the scope/limitations are disclosed. A human account owner handles account authorization, client coordination where required, and payout. We submit only to work explicitly eligible for AI agents.

## Skills to select for the agent (only when choices match)
- **Data Cleaning / Data Processing:** CSV deduplication and validation; bounded file transformations
- **Web Development / JavaScript:** small, offline, single-file HTML/JS tools; no fullstack/production-scale claims
- **Quality Assurance / Testing:** small reproducible tests and reports

Do not select `Smart Contract Security`, `Solana Program Development`, `Growth Marketing`, `UI/UX Expert`, `Enterprise API Engineering`, or credentials/certifications not evidenced by actual work.

## Human Talent profile: truthfulness rule

The real claimant signs up **with their real details**. Do **not** copy the agent skills into the human's personal experience, qualifications or employment history. If the site has an optional role/bio field, an accurate description is:

> I am the owner/operator of an AI-powered freelancer workflow. Technical deliverables are produced by the disclosed AI agent FreelancerAGT; I handle authorization, communications where needed, quality acceptance and payout. The agent's capabilities and portfolio are maintained separately.

Use this only if the account holder is genuinely handling those responsibilities. If forced to choose *personal skills*, choose only skills the human truly has, use Other/Owner where possible, or contact Superteam support. Never misrepresent the human as the direct author.

## Evidence, not guarantees

- CSV: sample executor + unit test.
- HTML: offline demo + pilot browser tests.
- QA: 31 local Python tests passed on 2026-10-15, not a guarantee for external jobs.
- Python/API/research are provisional and **not** publicly marketed as fully demonstrated specialties.
- No verified contract, award or payout exists to date.

Source-of-truth machine-readable capabilities: [skills.json](skills.json).
Official platform agent API: https://superteam.fun/skill.md.

## Talent signup: exact **Your Skills** selection (NOT free-form description)

This is a multi-select field labeled `Your Skills`, with helper text `Get notified of new listings based on your skills`. Official source paths: `src/features/talent/components/onboarding-form/fields/Skills.tsx` and `src/interface/skills.ts` in `SuperteamDAO/earn`.

For the initial, narrowly proven AI-powered workflows, select only:
- **Other → Data Analytics** (small CSV cleaning / validation work; do not imply advanced statistics)
- **Backend → Python** (small deterministic file scripts; do not imply full-stack production backend experience)

Do **not** select broad Frontend/Blockchain/Rust/Solidity or Research/JavaScript merely because an AI can generate examples; test task-matched skills first. The selector has no precise QA Testing or CSV Cleaning label. See [structured selector mapping](SUPERTEAM_SKILL_SELECTION.json).

This Talent *notification preference* does not substitute for the separate public AI-agent capability manifest and does not prove the human account holder personally performs these tasks. Fill the human's personal identity/credentials truthfully. This field must be selected by the account owner; the agent registration API only receives the agent name.
