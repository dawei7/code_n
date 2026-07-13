# Verified LeetCode Submissions

cOde(n) can submit a reviewed, package-authored solution to leetcode.com after
the user has passed the complete local judge. The editor contents are never
sent by this feature.

## User contract

- The action is one button: **Send to LeetCode**.
- It is enabled only after local acceptance, a valid connected session, account
  access to the problem, and a remotely verified package submission.
- Missing or candidate-only package artifacts produce a transparent blocked
  explanation.
- Premium-only problems disclose the restriction and require a connected
  Premium account.
- An Accepted response is stored in the active local profile and rendered as a
  second checkmark using the cOde(n) accent color.

LeetCode credentials are configured in Settings. Electron encrypts
`LEETCODE_SESSION`, `csrftoken`, and optional `cf_clearance` using the operating
system credential facility. The encrypted file lives in Electron user data,
outside `progress.json`. Stored values are never returned to the renderer or
written to logs. Session status is checked live so expired, rejected, and
Cloudflare-blocked sessions can be distinguished.

This integration uses LeetCode's website endpoints, not a stable public API.
Failures must remain explicit, conservative, and non-destructive.

## Package contract

A submission-enabled package contains both artifacts:

```text
dsa/leetcode/<frontend_id>_<slug>/
  submission.json
  solutions/
    leetcode_python3.py
```

The source must use LeetCode's native declaration exactly—for example
`class Solution` and `twoSum(...)`, not the app-local `solve(...)` adapter.

`submission.json` records provider, status, internal question id, frontend id,
title slug, access class, LeetCode language slug, source path, and remote
verification evidence. Valid statuses are:

- `candidate`: reviewed locally but never proven Accepted by LeetCode; blocked
  in the user UI.
- `verified`: promoted only after the exact packaged source receives an
  Accepted result; eligible for one-click submission.

Never label a candidate verified based only on local tests or code inspection.

## Maintainer verification

Credentials are read from environment variables so secrets do not appear in
arguments or source files:

```powershell
$env:LEETCODE_SESSION = '<value>'
$env:LEETCODE_CSRFTOKEN = '<value>'
$env:LEETCODE_CFCLEARANCE = '<optional value>'
.\.venv\Scripts\python.exe tools\verify_leetcode_submission.py lc_1 --confirm-submit
```

The verifier checks the authenticated account and live problem metadata,
submits the exact candidate source, polls the returned submission id, and
promotes `submission.json` atomically only after Accepted. Clear the environment
variables after verification.

For development-owner verification, the candidate can instead use credentials
already saved by the running Electron app. This bridge decrypts the values only
inside Electron and passes them to the verifier through the child-process
environment; it never prints or persists plaintext credentials:

```powershell
npx.cmd --prefix electron electron electron/scripts/verify-leetcode-candidate.cjs lc_44
```

Multiple candidates may be supplied in numeric order. The bridge waits ten
seconds between real posts and clears a migration blocker only after Accepted:

```powershell
npx.cmd --prefix electron electron electron/scripts/verify-leetcode-candidate.cjs lc_44 lc_45 lc_46
```

For every future package, verify problem identity, language declaration,
free/Premium access metadata, exact source, Accepted evidence, blocked states,
progress persistence, and the second-checkmark UI before calling the migration
complete.
