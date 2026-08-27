# Guided Example: Investments in 2016

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Insurance": [{"pid": 1, "tiv_2015": 10, "tiv_2016": 5, "lat": 1, "lon": 1}, {"pid": 2, "tiv_2015": 10, "tiv_2016": 7.5, "lat": 2, "lon": 2}, {"pid": 3, "tiv_2015": 20, "tiv_2016": 100, "lat": 3, "lon": 3}]}}`
- **Required output:** `{"columns": ["tiv_2016"], "rows": [[12.5]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Insurance`

The objective is to compute `{"columns": ["tiv_2016"], "rows": [[12.5]]}` from `{"tables": {"Insurance": [{"pid": 1, "tiv_2015": 10, "tiv_2016": 5, "lat": 1, "lon": 1}, {"pid": 2, "tiv_2015": 10, "tiv_2016": 7.5, "lat": 2, "lon": 2}, {"pid": 3, "tiv_2015": 20, "tiv_2016": 100, "lat": 3, "lon": 3}]}}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Annotating rather than collapsing

The common table expression `T` reads `Insurance` and returns `tiv_2016` plus two counts:



and



An ordinary `GROUP BY tiv_2015` would collapse all policies with the same investment value into one row. That is useful for discovering duplicate values, but the final sum needs each qualifying row’s own `tiv_2016`. A window aggregate instead writes the group count beside every member of that group.

For `cnt1`, `PARTITION BY tiv_2015` forms one logical partition per 2015 investment value. `COUNT(1)` counts every row in that partition because the literal 1 is never `NULL`. If `cnt1 > 1`, at least one other policy has the same `tiv_2015`.

For `cnt2`, partitioning by both `lat` and `lon` treats the two coordinates as one compound location. The count is one exactly when no other policy occupies the same coordinate pair. It would be incorrect to test latitude and longitude uniqueness separately: two policies could share a latitude while having different longitudes and therefore represent different locations.

Using the two columns directly is also safer than concatenating coordinate text. Concatenation can create ambiguous encodings—for example, components `(1, 23)` and `(12, 3)` can both become `"123"` without a robust delimiter and type representation. A multi-column SQL partition preserves tuple identity.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Insurance": [{"pid": 1, "tiv_2015": 10, "tiv_2016": 5, "lat": 1, "lon": 1}, {"pid": 2, "tiv_2015": 10, "tiv_2016": 7.5, "lat": 2, "lon": 2}, {"pid": 3, "tiv_2015": 20, "tiv_2016": 100, "lat": 3, "lon": 3}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Filtering requires both conditions

The outer query applies:



`AND` is essential. Sharing a `tiv_2015` value is not enough if the location is duplicated, and having a unique location is not enough if the investment value occurs only once.

In the sample, policies 1, 3, and 4 all have `tiv_2015 = 10`, so each gets `cnt1 = 3`. Policy 2 has `tiv_2015 = 20` and gets `cnt1 = 1`. Locations `(10,10)` and `(40,40)` occur once, while `(20,20)` occurs twice. Policies 1 and 4 are the only rows with counts respectively greater than one and equal to one. Their 2016 values, 5 and 40, sum to 45.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The outer query applies:



`AND` is essential.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Aggregating and rounding at the end

After filtering, `SUM(tiv_2016)` combines the 2016 investments from all qualifying policyholders. `ROUND(..., 2)` rounds the combined result to two decimal places:



Rounding after summation follows the requested operation. Rounding every individual value first and then adding can produce a different total when values contain more than two fractional digits. The alias gives the output its required column name.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["tiv_2016"], "rows": [[12.5]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Insurance": [{"pid": 1, "tiv_2015": 10, "tiv_2016": 5, "lat": 1, "lon": 1}, {"pid": 2, "tiv_2015": 10, "tiv_2016": 7.5, "lat": 2, "lon": 2}, {"pid": 3, "tiv_2015": 20, "tiv_2016": 100, "lat": 3, "lon": 3}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["tiv_2016"], "rows": [[12.5]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two grouped subqueries and joins:** One subque:** - **Two grouped subqueries and joins:** One subquery finds `tiv_2015` groups with count above one, another finds location groups with count one, and the base table joins both. This is correct but more verbose than annotating each row once with window counts.
- **Correlated `EXISTS` and `NOT EXISTS`:** Check for another row with equal `tiv_2015` and ensure none with the same location but a different `pid`. Clear logic, but without suitable indexes it may repeatedly scan the table.
- **Grouped counts joined back:** Precompute both count maps and join them to `Insurance`. This mirrors the window logic explicitly and can be portable where window functions are unavailable.
- **Concatenated location key:** Avoid it because formatting and delimiter collisions can merge different coordinate pairs. Partition by both columns.
- **Same latitude only:** Sharing one coordinate does not mean sharing a city; both `lat` and `lon` must match.
- **Location shared by two otherwise qualifying policies:** Both receive `cnt2 = 2` and both must be excluded.
- **A `tiv_2015` value occurring once:** Its row fails `cnt1 > 1` even if its location is unique.
- **More than two duplicate investments:** Every member qualifies for the first condition; “same as one or more” means count at least two, not exactly two.
- **No qualifying rows:** Standard SQL `SUM` over an empty set returns `NULL`, and `ROUND(NULL, 2)` remains `NULL`. The expected dataset generally supplies a result; `COALESCE` would be needed if the contract demanded numeric zero.
- **Rounding order:** Sum first, round once. Per-row rounding can alter the final answer.
- **Non-null coordinates:** The schema guarantee avoids special window grouping semantics for missing locations.
- **Exact float grouping:** SQL groups stored values according to their exact database equality semantics; visually similar floating-point inputs need not compare equal if stored differently.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \log n)$. Let $n$ be the number of `Insurance` rows. Computing the two window partitions usually requires hashing or sorting rows by `tiv_2015` and by `(lat, lon)`. A conventional sort-based plan takes $O(n\log n)$ time, matching the manifest. Hash-based partition counting may achieve expected $O(n)$ aggregation work, but SQL does not mandate that plan.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
