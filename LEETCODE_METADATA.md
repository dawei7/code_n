# LeetCode Metadata Maintenance

This document owns the provenance and historical workflows for LeetCode
attributes and the final canonical problem import. A new agent session should
follow the freeze policy below instead of hand-editing package metadata.

## Final metadata freeze

The application metadata was frozen on **2026-07-29**, together with the final
4,005-problem corpus. The authenticated capture contains the official
difficulty, acceptance rate, and Premium Frequency visible at that time. Any
bundled company/list membership or relevance signal is likewise a historical
snapshot of what the source exposed by the freeze date; it must not be
presented as current or predictive company interview activity.

The final Elo refresh used ZeroTrac revision
`a99138e145f303597b85290519aaf3d219b3a3e7`, whose upstream data was last
updated at `2026-07-24T10:15:30Z`. ZeroTrac supplied 2,545 real ratings. The
remaining 1,460 problems retain explicitly labelled estimates; in particular,
frontend ID 4005 had no ZeroTrac rating at the freeze and therefore keeps an
estimated Elo.

Do not refresh LeetCode metadata, company relevance, ZeroTrac ratings, or Elo
estimates after the freeze. The commands below remain documented only to make
the final capture reproducible and auditable. A future refresh requires an
explicit user decision to replace this freeze policy.

## Stored snapshot fields

Every `dsa/leetcode/<frontend_id>_<slug>/metadata.json` and matching
`dsa/leetcode/index.json` record contains:

- `frequency`: LeetCode's mutable `0`-`100` Frequency attribute, or `null`
  until an authenticated Premium refresh succeeds.
- `elo_rating`: the real ZeroTrac contest rating, or `null` when ZeroTrac has
  no rating for the problem.
- `estimated_elo_rating`: cOde(n)'s explicit fallback for a problem without a
  real ZeroTrac rating. It is `null` whenever a real rating exists.
- `contest_source`: the readable ZeroTrac contest label, such as
  `Biweekly Contest 143`, or `null` when `ratings.txt` has no entry.
- `contest_slug`: the source-native contest slug, such as
  `biweekly-contest-143`, or `null`.
- `contest_problem_index`: the source-native position such as `Q4`, or `null`.

Frequency and Elo are independent. Frequency is a relative LeetCode prominence
signal; it is not acceptance rate, problem difficulty, or a probability that a
specific company will ask the problem.

The licensed sparse source snapshot remains in
`dsa/leetcode/_meta/zerotrac-ratings.json`; `elo_rating` is its package-local
mirror. Exactly one of `elo_rating` and `estimated_elo_rating` is populated.
The Elo problem set is real-only: estimated values never make a problem
eligible for that set.

Contest provenance comes from `ratings.txt` at the same frozen ZeroTrac
revision as the Elo snapshot. It is available for all 2,545 real-rated
problems: 1,797 Weekly Contest entries and 748 Biweekly Contest entries. The
snapshot stores the sparse `contest_sources` mapping and its revision-pinned
source URL; every package and index record mirrors the three optional fields.
The human-readable label is derived only from the validated source slug, while
the original slug and problem index are retained unchanged.

To reproduce or verify this provenance without changing any frozen rating,
estimate, Frequency value, or other LeetCode metadata, run:

```powershell
.\.venv\Scripts\python.exe tools\sync_zerotrac_ratings.py --contest-provenance-only
.\.venv\Scripts\python.exe tools\sync_zerotrac_ratings.py --verify-contest-provenance
```

## Final Frequency and Elo capture procedure

The final complete refresh was run from the repository root with:

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

## Maintain the frozen 4,005-problem corpus

The application corpus ends permanently at frontend ID 4005. Run the importer
to add any missing eligible IDs through that boundary or to audit the freeze:

```powershell
.\.venv\Scripts\python.exe tools\import_new_leetcode_problems.py
```

It fetches the current official LeetCode problem list and compares numeric
frontend IDs through 4005 against `dsa/leetcode/index.json`. For each genuinely
new eligible ID it:

- creates the canonical zero-padded package directory;
- writes source metadata with explicit mutable-metric fields;
- creates `doc.md` from `dsa/leetcode/_template.md`;
- updates the canonical index and generated base subsets;
- computes an initial estimated Elo from local data.

Existing package metadata, documents, cases, benchmarks, solutions, and
submission evidence are not rewritten by this mode. Identity conflicts stop
the import. IDs above 4005 are reported and intentionally ignored. Once the
canonical index contains all 4,005 packages, the importer must always report
zero additions and must never grow the corpus, even as LeetCode publishes
later problems.

Before the final freeze, an import was followed by an authenticated metrics
refresh so new packages received current Frequency values:

```powershell
.\.venv\Scripts\python.exe tools\update_leetcode_metrics.py --refresh-zerotrac
```

This command is historical and must not be rerun after the metadata freeze.
New packages are scaffolds, not completed migrations. They still need the
normal documentation, correctness cases, complexity evidence, app-local
solution, native submission artifact, and remote verification workflow.

## Estimated Elo Specification & Exact Recomputation Guide (`difficulty-acceptance-v2`)

For non-contest LeetCode problems (problems without real ZeroTrac contest Elo), `estimated_elo_rating` is computed using a 100% reproducible statistical model fitted on the 2,549 real ZeroTrac contest ratings.

### 1. Mathematical Formula

For any problem $i$:

$$\text{Estimated Elo} = \text{clamp}\left(\alpha_D + \beta_D \cdot (z_i - \bar{z}_D) + \Delta_{T_i} + \delta_{\text{calib}, D}, \; \text{Min}_D, \; \text{Max}_D\right)$$

Where:
1. **Acceptance Rate Transformation (Log-Odds of Failure):**
   $$p_i = \max(0.01, \min(0.99, \text{acceptanceRate} / 100))$$
   $$z_i = \ln\left(\frac{1 - p_i}{p_i}\right)$$
   *Higher failure rate $\implies$ higher $z_i \implies$ higher estimated Elo.*

2. **Difficulty Tier Parameters:**
   - **Easy ($D = \text{Easy}$):**
     - Base $\alpha = 1253.5005$
     - Slope $\beta = 52.6991$
     - Median $z$ ($\bar{z}$) $= -1.0082$
     - Calibration offset $\delta_{\text{calib}} = -73.3795$
     - Clamping Bounds: $[1151.5867, 1440.1785]$
   - **Medium ($D = \text{Medium}$):**
     - Base $\alpha = 1646.8565$
     - Slope $\beta = 174.7010$
     - Median $z$ ($\bar{z}$) $= -0.2261$
     - Calibration offset $\delta_{\text{calib}} = -60.9093$
     - Clamping Bounds: $[1460.1785, 1944.5430]$
   - **Hard ($D = \text{Hard}$):**
     - Base $\alpha = 2262.2295$
     - Slope $\beta = 186.7697$
     - Median $z$ ($\bar{z}$) $= 0.1824$
     - Calibration offset $\delta_{\text{calib}} = -48.5512$
     - Clamping Bounds: $[1964.5430, 2765.0564]$

3. **Topic Adjustment ($\Delta_T$):**
   For problem topics $T$, $\Delta_T = \text{clamp}\left(\frac{\sum_{t \in T} w_t \cdot \delta_t}{\sqrt{\max(1, |T|)}}, -120.0, +120.0\right)$ where $\delta_t$ is the empirical residual and $w_t = \frac{N_t}{N_t + 20}$ is the shrinkage regularizer (e.g. $+127.9$ for Topological Sort, $+92.5$ for Bitmasking, $+71.2$ for Segment Trees, $+55.3$ for Dynamic Programming, $-37.5$ for Simulation).

4. **Machine-Readable Metadata:**
   The exact fitted parameters are saved in `dsa/leetcode/_meta/elo-estimation-model.json`.

### 2. Standalone Python Recomputation Function

Anyone can compute or verify the exact estimated Elo for any LeetCode problem using the standalone script below:

```python
import math

def compute_estimated_elo(difficulty: str, acceptance_rate: float, topic_adjustment: float = 0.0) -> float:
    params = {
        "Easy":   {"base": 1253.5005, "slope": 52.6991,  "median_z": -1.0082, "offset": -73.3795, "min": 1151.5867, "max": 1440.1785},
        "Medium": {"base": 1646.8565, "slope": 174.7010, "median_z": -0.2261, "offset": -60.9093, "min": 1460.1785, "max": 1944.5430},
        "Hard":   {"base": 2262.2295, "slope": 186.7697, "median_z":  0.1824, "offset": -48.5512, "min": 1964.5430, "max": 2765.0564},
    }[difficulty]
    
    p = max(0.01, min(0.99, acceptance_rate / 100.0))
    z = math.log((1.0 - p) / p)
    raw = params["base"] + params["slope"] * (z - params["median_z"]) + topic_adjustment + params["offset"]
    return max(params["min"], min(params["max"], raw))

# Example: LC 1 (Two Sum): Easy, 57.9% acceptance
print("LC 1 Estimated Elo:", round(compute_estimated_elo("Easy", 57.9), 2)) # -> 1245.52
```

## Verification

After either workflow, run:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_leetcode_metadata_tools.py server\tests\test_challenges_route.py -q
npm.cmd run build --prefix web
git diff --check
```

