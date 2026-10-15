# FreelancerAGT — Superteam Activation Status

Updated: 2026-10-15.

## Talent owner
- `talent_signup_status`: **USER_REPORTED_COMPLETED**.
- Login method: **Google SSO** (reported by owner).
- Profile completion: **USER_REPORTED_COMPLETED**.
- Selected notification skills: **Not independently inspected on the Superteam website**; previously recommended narrow matching options were `Other → Data Analytics` and `Backend → Python`.
- `talent_profile_url`: **UNKNOWN**, public profile not independently checked.
- Connected Gmail: **AVAILABLE_IN_CHATGPT**. A targeted Gmail search for Superteam messages on 2026-10-15 returned no matches. This neither proves nor disproves completion.
- **Gmail connection does not grant Superteam website Google OAuth/SSO authentication**. Browser login requires an authenticated human-managed browser session (for example ChatGPT Work cloud browser).
- Store no owner's OAuth tokens, email address, personal ID or payout details in this **public** repository.

## AI Agent separate registration
- `agent_registration_status`: **NOT_VERIFIED**.
- `agentId`, `agent_api_key`, `claimCode`: **NONE_PRESENT_IN_PROJECT**.
- `GET /api/agents/listings/live` with valid key: **NOT_TESTED_LIVE**.
- `agent_claim_status`: **NOT_VERIFIED**.
- `verified_payout`: **0 USD**.

## Next required steps
1. Verify public Talent profile if the owner shares its **public URL**; do not request SSO credentials.
2. Run existing `register_superteam.py` from the full pilot ZIP on a trusted machine with connectivity. Register only once, and save `apiKey` and `claimCode` in a restricted local secret store (never chat/GitHub). If an Agent was already registered, recover that identity instead of registering a duplicate.
3. Use the CLI's read-only verification to authenticate, then discover `AGENT_ALLOWED`/`AGENT_ONLY` opportunities. The existence of a working Talent login does not prove Agent API authentication.
4. Review sponsor conditions, eligibility, payout network/wallet, fee schedule, and task acceptance criteria. Human owner performs claim when appropriate; no AI signing or KYC.
5. Record net income only after independently verified settled payment.

Primary source: https://superteam.fun/earn/agents
