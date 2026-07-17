# LeetCode Metadata Maintenance

This document owns the repeatable workflows for mutable LeetCode attributes
and newly published problems. A new agent session should use these commands
instead of hand-editing package metadata.

## Stored mutable fields

Every `dsa/leetcode/<frontend_id>_<slug>/metadata.json` and matching
`dsa/leetcode/index.json` record contains:

- `frequency`: LeetCode's mutable `0`-`100` Frequency attribute, or `null`
  until an authenticated Premium refresh succeeds.
- `elo_rating`: the real ZeroTrac contest rating, or `null` when ZeroTrac has
  no rating for the problem.
- `estimated_elo_rating`: cOde(n)'s explicit fallback for a problem without a
  real ZeroTrac rating. It is `null` whenever a real rating exists.

Frequency and Elo are independent. Frequency is a relative LeetCode prominence
signal; it is not acceptance rate, problem difficulty, or a probability that a
specific company will ask the problem.

The licensed sparse source snapshot remains in
`dsa/leetcode/_meta/zerotrac-ratings.json`; `elo_rating` is its package-local
mirror. Exactly one of `elo_rating` and `estimated_elo_rating` is populated.
The Elo problem set is real-only: estimated values never make a problem
eligible for that set.

## Refresh Frequency and estimated Elo

Run the complete refresh from the repository root:

```powershell
.\.venv\Scripts\python.exe tools\update_leetcode_metrics.py --refresh-zerotrac
```

The tool:

1. optionally refreshes the sparse real-Elo snapshot from ZeroTrac;
2. verifies that LeetCode recognizes the configured session as signed-in and
   Premium;
3. queries `https://leetcode.com/graphql` for
   `problemsetQuestionList.questions[].frequency` together with current
   difficulty and acceptance rate—the same Frequency value that drives the
   problem-list bar;
4. rejects incomplete, identity-mismatched, invalid, or suspicious all-zero
   Frequency data before writing;
5. recalculates every estimated Elo from the complete problem-level corpus;
6. atomically updates every package metadata file, the canonical index, and
   `dsa/leetcode/_meta/leetcode-metrics.json`.

Authentication can come from `LEETCODE_COOKIE`, from
`LEETCODE_SESSION` plus `LEETCODE_CSRFTOKEN`, or from the ignored
`dsa/leetcode/_local/.leetcode_cookie` cookie-header file. Never commit these
credentials.

If the user asks to use their signed-in Chrome session, use the Chrome-control
workflow instead of copying browser cookies:

1. claim the user's already signed-in `https://leetcode.com/problemset/` tab
   and verify that the account has Premium access;
2. open `https://leetcode.com/api/problems/all/` in a temporary Chrome tab;
3. save that JSON response to a temporary file outside the repository;
4. verify that `num_total` equals the number of unique
   `stat_status_pairs[].stat.frontend_question_id` values;
5. apply it with the documented `--snapshot` mode and add
   `--refresh-zerotrac`;
6. delete the temporary file, close the temporary tab, and leave the user's
   original LeetCode tab open.

The REST endpoint's `frequency` is LeetCode's raw prominence score. Snapshot
loading normalizes it against the complete corpus maximum and rounds to one
decimal place, matching the `Frequency N.N%` tooltip in LeetCode's problem
list. The workflow stores neither cookies nor account credentials.

Useful controlled modes:

```powershell
# Validate the full authenticated refresh without writing.
.\.venv\Scripts\python.exe tools\update_leetcode_metrics.py --dry-run

# Recompute only estimated Elo from local data; preserve stored Frequency.
.\.venv\Scripts\python.exe tools\update_leetcode_metrics.py --offline

# Apply a reviewed API-shaped snapshot instead of making a live request.
.\.venv\Scripts\python.exe tools\update_leetcode_metrics.py --snapshot .\path\metrics.json
```

The estimate model uses real-Elo quantile bands within official Easy, Medium,
and Hard tiers. Acceptance percentile moves a problem within its tier, robust
percentile clamps limit outliers, legacy contest cohorts are calibrated to the
one-third point of their real tier, tier bands cannot overlap, and Hard
estimates stop at the real-rating 75th percentile to retain margin below the
hardest real contest problems. The exact model version and fitted bands are
recorded in `dsa/leetcode/_meta/leetcode-metrics.json`.

## Import newly published problems

Run the weekly importer:

```powershell
.\.venv\Scripts\python.exe tools\import_new_leetcode_problems.py
```

It fetches the current official LeetCode problem list and compares numeric
frontend IDs against `dsa/leetcode/index.json`. For each genuinely new ID it:

- creates the canonical zero-padded package directory;
- writes source metadata with explicit mutable-metric fields;
- creates `doc.md` from `dsa/leetcode/_template.md`;
- updates the canonical index and generated base subsets;
- computes an initial estimated Elo from local data.

Existing package metadata, documents, cases, benchmarks, solutions, and
submission evidence are not rewritten by this mode. Identity conflicts stop
the import. If no new frontend IDs exist, it reports zero additions.

After an import, refresh the authenticated metrics so new packages receive
current Frequency values:

```powershell
.\.venv\Scripts\python.exe tools\update_leetcode_metrics.py --refresh-zerotrac
```

New packages are scaffolds, not completed migrations. They still need the
normal documentation, correctness cases, complexity evidence, app-local
solution, native submission artifact, and remote verification workflow.

## Verification

After either workflow, run:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_leetcode_metadata_tools.py server\tests\test_challenges_route.py -q
npm.cmd run build --prefix web
git diff --check
```
