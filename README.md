# FreeLancerAGT — bootstrap

Freelancer Autonomous Agent research/pilot (15 Oct 2026).

## Current status
- GitHub application connected and this repository initialized for the project.
- The **locally unit-tested full source** (Python CLI, seven-tool local MCP server, 31 unit tests, research scanner, sample executor, CI/workflow templates) is available as a downloadable ZIP in the project's ChatGPT conversation.
- **The full source archive has NOT yet been synced to this GitHub repository.** Do not assume a workflow or autonomous income process is deployed merely because this README exists.
- No paid work, automatic external applications or verified payout have occurred.

## Safe operating model
Official public API discovery → evidence-based scoring → human-approved application → deterministic executor & QA → authorized delivery → verified payout/ledger.

Never commit credentials, wallet private keys, customer files, bank/KYC documents, or receipts to this **public** repository.

## Sync local pilot code
Extract `freelancer_agent_mcp_v0.3.zip` from the ChatGPT conversation. From the extracted project folder, after reviewing files and secrets:

```bash
git init
git remote add origin https://github.com/huyhieu2k5/FreeLancerAGT.git
git fetch origin main
git checkout -b main origin/main
git add .gitignore .env.example *.py *.md mcp.config.example.json .github/workflows tests data/demo_jobs.json data/sample_products.csv
git commit -m "Import reviewed freelancer pilot source"
git push -u origin main
```

This GitHub push requires the repository owner's authentication. If your extracted files are not in the project root, adjust paths accordingly.

## Income blockers
- Human verified marketplace worker identity and approved external submissions
- Payout account / eligible bank or wallet, KYC where required
- Verified escrow, actual completion and acceptance, actual settled funds
- Proper handling of provider ToS, private data, platform fees, and compliance

Official MCP SDK: https://py.sdk.modelcontextprotocol.io/

## Superteam Earn setup

- [Human payout, one-time agent registration and read-only API verification](SUPERTEAM_SETUP.md)
- [Standalone safe GET connectivity probe](scripts/superteam_probe.py)

The bundled full v0.4 pilot (including local MCP, tests, integration fixes) is attached to the ChatGPT Freelancer project conversation and **not yet fully mirrored** into this public repository. As of 2026-10-15, live Superteam authentication and payout eligibility have not been verified because the local environment has no agent key and no external DNS. Do not commit credentials or customer materials.

## Truthful AI operator profile & future skill transfer

- [AI-agent skills allowlist, evidence status and selection policy](agent/skills.json)
- [AI-agent profile copy and guidance for the *human payout owner*](agent/PROFILE.md)
- [Future sub-agent handoff and capability gates](agent/HANDOFF.md)

**Do not claim that the human account holder has the AI executor's skills.** Superteam registers an agent with its own identity. A human owner completes their personal Talent profile truthfully and handles payout claiming. The skills listed above have only passed bounded local pilot tests. No agent registration, live API key verification, customer award, or payout has yet been confirmed.

## Activation checkpoint (15 October 2026)

The account owner reports that their **human Talent** registration via Google sign-in and Talent profile creation have been completed. This is **not independently confirmed** by an authenticated Superteam browser session. A connected Gmail app does **not** give the CLI or ChatGPT a website SSO token. See [Superteam Activation Status](SUPERTEAM_ACTIVATION_STATUS.md) for the remaining separated AI Agent registration and payout verification gates.
