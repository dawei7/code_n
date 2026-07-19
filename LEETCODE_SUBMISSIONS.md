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

Every package owns its submission artifacts inside the mandatory Optimal
branch:

```text
dsa/leetcode/<frontend_id:04d>_<slug>/
  solution_variants.json
  variants/
    optimal/
      submission.json
      solutions/
        leetcode_python3.py
```

The source must use LeetCode's native declaration exactly—for example
`class Solution` and `twoSum(...)`, not the app-local `solve(...)` adapter.

Each additional published branch owns the same two artifacts under
`variants/<variant>/`. Its `submission.json` source path is relative to that
branch. The root/default one-click action always resolves the Optimal branch;
an additional branch is publishable only after its own exact native source is
Accepted.

`submission.json` records provider, status, internal question id, frontend id,
title slug, access class, LeetCode language slug, source path, and remote
verification evidence. Valid statuses are:

- `candidate`: reviewed locally but never proven Accepted by LeetCode; blocked
  in the user UI.
- `verified`: promoted only after the exact packaged source receives an
  Accepted result; eligible for one-click submission.

Never label a candidate verified based only on local tests or code inspection.

## Migration authoring order

For corpus migration and maintainer-authored package work, obtain remote
Accepted evidence early enough that the platform-verified native source anchors
the remaining artifacts. This is distinct from the end-user **Send to
LeetCode** gate above, which still requires the complete local judge to pass.

Use this order for every package when remote submission is available:

1. Confirm the public contract, LeetCode identity, access class, supported
   language, and exact native declaration or query interface.
2. Create the platform-native source and perform minimal, contract-focused
   sanity checks. Also create the candidate manifest needed to submit that
   exact file.
3. Submit the exact native source to LeetCode early. Do not begin full case or
   benchmark authoring until it is Accepted, unless remote verification is
   unavailable and an exact blocker has been recorded.
4. Treat the Accepted source as the semantic and algorithmic anchor for the
   separate app-local implementation. Preserve both artifacts; never replace
   the native declaration with the app adapter.
5. Author comprehensive visible and hidden correctness cases from the problem
   contract, including semantic traps exposed while obtaining acceptance.
6. Author and calibrate exactly three legal scaling tiers, or the reviewed
   strict certificate when scaling is inapplicable. Verify the accepted-class
   implementation and an independent same-class implementation pass, while a
   correct principal slower class returns every expected output and fails only
   the complexity verdict.
7. Rerun all correctness, calibration, audit, dataset, and regression checks
   after any later source change.

A rejection caused only by an implementation defect normally changes the
native and app-local sources, not contract-derived expected results. A
rejection that reveals misunderstood semantics requires a coordinated repair:
update the document, cases, expected outputs, both solution forms, and any
benchmark workload or complexity claim affected by that misunderstanding.
Never patch only the submitted source and leave contradictory local evidence.

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
promotes `variants/optimal/submission.json` atomically only after Accepted.
Clear the environment variables after verification.

For development-owner verification, the candidate can instead use credentials
already saved by the running Electron app. This bridge decrypts the values only
inside Electron and passes them to the verifier through the child-process
environment; it never prints or persists plaintext credentials:

```powershell
npx.cmd --prefix electron electron electron/scripts/verify-leetcode-candidate.cjs lc_44
```

To verify a non-default branch, append its manifest id after a colon. This
promotes only that branch's manifest:

```powershell
npx.cmd --prefix electron electron electron/scripts/verify-leetcode-candidate.cjs lc_1502:simplified
```

Premium statement authoring should use the separate read-only authenticated
bridge. It verifies the live identity against canonical metadata and prints
transient statement/snippet evidence without writing LeetCode text into the
dataset or exposing credentials. If Cloudflare rejects the direct API request,
the same bridge retries through a temporary headless Chrome profile:

```powershell
npx.cmd --prefix electron electron electron/scripts/fetch-leetcode-question.cjs lc_1902
```

Use this authenticated evidence instead of a third-party statement mirror
whenever the stored account can access the Premium problem.

Multiple candidates may be supplied in numeric order. The bridge waits ten
seconds between real posts and clears a migration blocker only after Accepted:

```powershell
npx.cmd --prefix electron electron electron/scripts/verify-leetcode-candidate.cjs lc_44 lc_45 lc_46
```

For every future package, verify problem identity, language declaration,
free/Premium access metadata, exact source, Accepted evidence, blocked states,
progress persistence, and the second-checkmark UI before calling the migration
complete.
