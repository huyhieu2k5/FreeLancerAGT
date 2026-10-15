# Superteam Earn — Activation (2026-10-15)

## Verified official contract
- Agent docs: https://superteam.fun/skill.md
- Agent console: https://superteam.fun/earn/agents
- Human talent account: https://superteam.fun/earn/new
- Payments FAQ: https://docs.superteam.fun/the-superteam-handbook/community/faqs/superteam-earn-faq

Use **https://superteam.fun**, not an unofficial API host.

## Truthful human owner / AI agent profiles

**Do not pretend that the human payout claimant personally has the AI agent's technical skills.** Superteam supports a separately registered AI agent identity. The human Talent account must contain truthful owner information; the AI agent profile, its skills and its work samples are separately described in [agent/PROFILE.md](agent/PROFILE.md) and [agent/skills.json](agent/skills.json). If a mandatory *personal skills* field does not offer an honest option for the human, contact Superteam rather than fabricate qualifications.

The initial **FreelancerAGT — AI Data & Automation Agent** capability shortlist is CSV cleanup, small HTML/JavaScript utilities and automated QA. All are bounded pilot-tested capabilities, not a blanket claim of professional expertise. [Sub-agent handoff instructions](agent/HANDOFF.md) preserve the distinction.

Registration's published `POST /api/agents` contract accepts a *name*, not a human resume or skill certifications. Avoid listing unverified skills.

## Human operator: required
1. Open the Talent link, sign in using your own verified identity, and complete the real Talent profile.
2. Check sponsor-specific payout requirements. Superteam/Solana-sponsored listings can require payment forms and KYC; external sponsors generally pay the linked wallet but may also require KYC/invoices.
3. Before any work, confirm payout currency and wallet **network**, KYC/residency eligibility, and net fees. Never publish seed phrases, private keys, OTPs or ID documents in GitHub.
4. Only the human operator confirms payouts and links a victorious agent with the secure **claim code** via `https://superteam.fun/earn/claim/<claim-code>`. Agent itself cannot KYC.

## Register ONE agent from a user-controlled machine
A local registration script is in the conversation's full pilot archive. Alternatively, following the official skill:
```bash
curl -fsS -X POST https://superteam.fun/api/agents \
  -H 'Content-Type: application/json' \
  -d '{"name":"freelancer-agent-lab"}'
```
**WARNING:** the response contains an API key and claim code; never run this in shared terminals or paste its output into chat/GitHub. The full pilot uses `register_superteam.py` to save this to a private restricted file. Do not register a second agent if one exists.

## Read-only API verification
Set `SUPERTEAM_API_KEY` in a private runtime, not GitHub:
```bash
python scripts/superteam_probe.py
```
This calls `GET /api/agents/listings/live?take=25` using a Bearer key, reads only listings marked `AGENT_ALLOWED` / `AGENT_ONLY`, and prints NO credential. `401` = invalid key; `429` = rate limit; network errors are separate. A 200 response **does not** establish cash-out readiness, award status or escrow.

## Submission and payout gates
No automated submissions, bidding, public comments, contract acceptance or wallet signing in this repository. Projects require the human operator's real Telegram URL in their submission payload. The agent must be selected, output accepted and the payment settled on the real wallet before any revenue is recorded.

## Test status
On 15 October 2026, the project local Superteam verifier passed **9 mocked tests** and the full suite passed **30 tests**. Actual live verification was **not possible** due to DNS failure, and no API key or claim code has been created in this environment. Revenue received: **$0**.

Historical caution: https://github.com/SuperteamDAO/earn/issues/1456 reports agent live discovery glitches. Independently verify deadline and winner-announcement status; do not treat an empty API result as proof of zero work.

## Talent signup `Your Skills` field — fixed choices, not free text

The real registration screen shows `Your Skills` and `Get notified of new listings based on your skills`. It uses Superteam's controlled multi-select taxonomy and must be completed in the Talent web UI; it is not an Agent bio field. For narrow initial work, select **Other → Data Analytics** and **Backend → Python**. These map imperfectly to pilot CSV cleanup and small Python file transformation, so the human must not claim personal professional credentials they do not have. Do not select backend Javascript or Research until appropriate independent skills are demonstrated. Refer to [selector mapping](agent/SUPERTEAM_SKILL_SELECTION.json).

The separate AI-agent registration `POST /api/agents` only takes the **agent name**. Do not send Talent skill selections as arbitrary extra fields to that endpoint.
