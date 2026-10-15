#!/usr/bin/env python3
"""Superteam Earn read-only connectivity probe. No key is printed or persisted."""
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request

def main():
    key = os.getenv("SUPERTEAM_API_KEY", "").strip()
    if not key:
        print(json.dumps({"api_status": "MISSING_KEY", "live_jobs": None}))
        return 2
    req = urllib.request.Request(
        "https://superteam.fun/api/agents/listings/live?take=25",
        headers={"Authorization": "Bearer " + key, "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            data = json.load(response)
        if isinstance(data, dict):
            data = data.get("result", data.get("listings", data.get("data")))
        if isinstance(data, dict):
            data = data.get("listings", data.get("items"))
        if not isinstance(data, list):
            print(json.dumps({"api_status": "SCHEMA_MISMATCH"}))
            return 2
        jobs = []
        now = dt.datetime.now(dt.timezone.utc)
        for job in data:
            if not isinstance(job, dict):
                continue
            if job.get("agentAccess") not in ("AGENT_ONLY", "AGENT_ALLOWED"):
                continue
            if str(job.get("status") or "OPEN").upper() not in ("OPEN", "LIVE"):
                continue
            if job.get("isWinnersAnnounced") is True:
                continue
            deadline = job.get("deadline")
            if deadline:
                try:
                    when = dt.datetime.fromisoformat(str(deadline).replace("Z", "+00:00"))
                    if when.tzinfo is None:
                        when = when.replace(tzinfo=dt.timezone.utc)
                    if when < now:
                        continue
                except ValueError:
                    pass
            jobs.append({"title": job.get("title"),
                         "slug": job.get("slug"),
                         "agentAccess": job.get("agentAccess"),
                         "token": job.get("token"),
                         "deadline": job.get("deadline")})
        print(json.dumps({"api_status": "AUTHENTICATED",
                          "eligible_live_count": len(jobs),
                          "listings": jobs[:10],
                          "human_claim_verified": False,
                          "payout_verified": False}, ensure_ascii=False, indent=2))
        return 0
    except urllib.error.HTTPError as exc:
        status = {401:"AUTH_FAILED", 403:"FORBIDDEN", 429:"RATE_LIMITED"}.get(exc.code, "HTTP_ERROR")
        print(json.dumps({"api_status": status, "http_status": exc.code}))
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        print(json.dumps({"api_status": "NETWORK_UNAVAILABLE", "error_type": type(exc).__name__}))
    return 2

if __name__ == "__main__":
    sys.exit(main())
