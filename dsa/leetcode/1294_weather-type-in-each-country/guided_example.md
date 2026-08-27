# Guided Example: Weather Type in Each Country

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Countries": [{"country_id": 2, "country_name": "USA"}, {"country_id": 3, "country_name": "Australia"}, {"country_id": 7, "country_name": "Peru"}, {"country_id": 5, "country_name": "China"}, {"country_id": 8, "country_name": "Morocco"}, {"country_id": 9, "country_name": "Spain"}], "Weather": [{"country_id": 2, "weather_state": 15, "day": "2019-11-01"}, {"country_id": 2, "weather_state": 12, "day": "2019-10-28"}, {"country_id": 2, "weather_state": 12, "day": "2019-10-27"}, {"country_id": 3, "weather_state": -2, "day": "2019-11-10"}, {"country_id": 3, "weather_state": 0, "day": "2019-11-11"}, {"country_id": 3, "weather_state": 3, "day": "2019-11-12"}, {"country_id": 5, "weather_state": 16, "day": "2019-11-07"}, {"country_id": 5, "weather_state": 18, "day": "2019-11-09"}, {"country_id": 5, "weather_state": 21, "day": "2019-11-23"}, {"country_id": 7, "weather_state": 25, "day": "2019-11-28"}, {"country_id": 7, "weather_state": 22, "day": "2019-12-01"}, {"country_id": 7, "weather_state": 20, "day": "2019-12-02"}, {"country_id": 8, "weather_state": 25, "day": "2019-11-05"}, {"country_id": 8, "weather_state": 27, "day": "2019-11-15"}, {"country_id": 8, "weather_state": 31, "day": "2019-11-25"}, {"country_id": 9, "weather_state": 7, "day": "2019-10-23"}, {"country_id": 9, "weather_state": 3, "day": "2019-12-23"}]}}`
- **Required output:** `{"columns": ["country_name", "weather_type"], "rows": [["USA", "Cold"], ["Australia", "Cold"], ["Peru", "Hot"], ["Morocco", "Hot"], ["China", "Warm"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Countries`

The objective is to compute `{"columns": ["country_name", "weather_type"], "rows": [["USA", "Cold"], ["Australia", "Cold"], ["Peru", "Hot"], ["Morocco", "Hot"], ["China", "Warm"]]}` from `{"tables": {"Countries": [{"country_id": 2, "country_name": "USA"}, {"country_id": 3, "country_name": "Australia"}, {"country_id": 7, "country_name": "Peru"}, {"country_id": 5, "country_name": "China"}, {"country_id": 8, "country_name": "Morocco"}, {"country_id": 9, "country_name": "Spain"}], "Weather": [{"country_id": 2, "weather_state": 15, "day": "2019-11-01"}, {"country_id": 2, "weather_state": 12, "day": "2019-10-28"}, {"country_id": 2, "weather_state": 12, "day": "2019-10-27"}, {"country_id": 3, "weather_state": -2, "day": "2019-11-10"}, {"country_id": 3, "weather_state": 0, "day": "2019-11-11"}, {"country_id": 3, "weather_state": 3, "day": "2019-11-12"}, {"country_id": 5, "weather_state": 16, "day": "2019-11-07"}, {"country_id": 5, "weather_state": 18, "day": "2019-11-09"}, {"country_id": 5, "weather_state": 21, "day": "2019-11-23"}, {"country_id": 7, "weather_state": 25, "day": "2019-11-28"}, {"country_id": 7, "weather_state": 22, "day": "2019-12-01"}, {"country_id": 7, "weather_state": 20, "day": "2019-12-02"}, {"country_id": 8, "weather_state": 25, "day": "2019-11-05"}, {"country_id": 8, "weather_state": 27, "day": "2019-11-15"}, {"country_id": 8, "weather_state": 31, "day": "2019-11-25"}, {"country_id": 9, "weather_state": 7, "day": "2019-10-23"}, {"country_id": 9, "weather_state": 3, "day": "2019-12-23"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Joining observations to country names

`Weather` contains `country_id`, `weather_state`, and `day`, while `Countries` supplies `country_name` for each `country_id`. The clause

`Weather AS w JOIN Countries USING (country_id)`

is an inner join. `USING (country_id)` is shorthand for matching rows whose `country_id` values are equal, and it exposes the shared join column once rather than as two separately qualified columns. The alias `w` names `Weather`, although the rest of this short query does not need to use that alias explicitly.

The inner join is semantically important. A country with no weather rows cannot form an average and should not appear. After the later month filter, a country with weather in other months but no weather in November 2019 also has no surviving row and therefore produces no output group. This matches the required behavior of reporting countries that have observations in the target month.

The `Weather` composite primary key `(country_id, day)` guarantees at most one observation for a given country on a given date. `Countries.country_id` is its primary key, so every matching weather observation obtains one country name rather than multiplying into duplicate country records.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Countries": [{"country_id": 2, "country_name": "USA"}, {"country_id": 3, "country_name": "Australia"}, {"country_id": 7, "country_name": "Peru"}, {"country_id": 5, "country_name": "China"}, {"country_id": 8, "country_name": "Morocco"}, {"country_id": 9, "country_name": "Spain"}], "Weather": [{"country_id": 2, "weather_state": 15, "day": "2019-11-01"}, {"country_id": 2, "weather_state": 12, "day": "2019-10-28"}, {"country_id": 2, "weather_state": 12, "day": "2019-10-27"}, {"country_id": 3, "weather_state": -2, "day": "2019-11-10"}, {"country_id": 3, "weather_state": 0, "day": "2019-11-11"}, {"country_id": 3, "weather_state": 3, "day": "2019-11-12"}, {"country_id": 5, "weather_state": 16, "day": "2019-11-07"}, {"country_id": 5, "weather_state": 18, "day": "2019-11-09"}, {"country_id": 5, "weather_state": 21, "day": "2019-11-23"}, {"country_id": 7, "weather_state": 25, "day": "2019-11-28"}, {"country_id": 7, "weather_state": 22, "day": "2019-12-01"}, {"country_id": 7, "weather_state": 20, "day": "2019-12-02"}, {"country_id": 8, "weather_state": 25, "day": "2019-11-05"}, {"country_id": 8, "weather_state": 27, "day": "2019-11-15"}, {"country_id": 8, "weather_state": 31, "day": "2019-11-25"}, {"country_id": 9, "weather_state": 7, "day": "2019-10-23"}, {"country_id": 9, "weather_state": 3, "day": "2019-12-23"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Filtering exactly November 2019

The `WHERE` clause is

`DATE_FORMAT(day, '%Y-%m') = '2019-11'`.

For each date, `DATE_FORMAT` produces a year-and-month string such as `2019-11`. Equality keeps dates whose year is 2019 and month is November, regardless of the day number. A row from November 2018 fails because its year differs; a row from December 2019 fails because its month differs.

Conceptually, SQL filters rows before it groups them. This order is crucial: the average must be based only on November observations, not on a country's entire history followed by a later attempt to label the result. The `WHERE` predicate ensures that rows from every other month are absent when `AVG` runs.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The `WHERE` clause is

`DATE_FORMAT(day, '%Y-%m') = '2019-11... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Forming one group and average

`GROUP BY 1` uses an ordinal reference: `1` means the first selected expression, which is `country_name`. All surviving joined rows with the same country name are placed in one group. `AVG(weather_state)` then adds that group's weather values and divides by the number of non-null values.

For example, suppose one country's surviving November values are $10$, $20$, and $30$. Their average is

$$
\frac{10+20+30}{3}=20,
$$

so the country is classified as warm. Negative weather values pose no special problem; they participate in the arithmetic average normally.

The exact source groups only by `country_name`. The local schema guarantees uniqueness for `country_id` but does not explicitly say that `country_name` is unique. If two different identifiers were allowed to share the same name, `GROUP BY 1` would merge their observations. The accepted query relies on country names acting as unique labels in the data. A schema-defensive version would group by both identifier and name while selecting only the name.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["country_name", "weather_type"], "rows": [["USA", "Cold"], ["Australia", "Cold"], ["Peru", "Hot"], ["Morocco", "Hot"], ["China", "Warm"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Countries": [{"country_id": 2, "country_name": "USA"}, {"country_id": 3, "country_name": "Australia"}, {"country_id": 7, "country_name": "Peru"}, {"country_id": 5, "country_name": "China"}, {"country_id": 8, "country_name": "Morocco"}, {"country_id": 9, "country_name": "Spain"}], "Weather": [{"country_id": 2, "weather_state": 15, "day": "2019-11-01"}, {"country_id": 2, "weather_state": 12, "day": "2019-10-28"}, {"country_id": 2, "weather_state": 12, "day": "2019-10-27"}, {"country_id": 3, "weather_state": -2, "day": "2019-11-10"}, {"country_id": 3, "weather_state": 0, "day": "2019-11-11"}, {"country_id": 3, "weather_state": 3, "day": "2019-11-12"}, {"country_id": 5, "weather_state": 16, "day": "2019-11-07"}, {"country_id": 5, "weather_state": 18, "day": "2019-11-09"}, {"country_id": 5, "weather_state": 21, "day": "2019-11-23"}, {"country_id": 7, "weather_state": 25, "day": "2019-11-28"}, {"country_id": 7, "weather_state": 22, "day": "2019-12-01"}, {"country_id": 7, "weather_state": 20, "day": "2019-12-02"}, {"country_id": 8, "weather_state": 25, "day": "2019-11-05"}, {"country_id": 8, "weather_state": 27, "day": "2019-11-15"}, {"country_id": 8, "weather_state": 31, "day": "2019-11-25"}, {"country_id": 9, "weather_state": 7, "day": "2019-10-23"}, {"country_id": 9, "weather_state": 3, "day": "2019-12-23"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["country_name", "weather_type"], "rows": [["USA", "Cold"], ["Australia", "Cold"], ["Peru", "Hot"], ["Morocco", "Hot"], ["China", "Warm"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sargable half-open date range:** Replacing the:** - **Sargable half-open date range:** Replacing the formatting predicate with `day >= '2019-11-01' AND day < '2019-12-01'` expresses the same month and can let an index on `day` support a range scan. The half-open upper bound avoids guessing the month's final time value.
- **Defensive grouping by identity:** `GROUP BY country_id, country_name` keeps different countries separate even if they share a name. This is safer under only the locally stated key guarantees, although the exact accepted source uses `GROUP BY 1`.
- **Conditional aggregation:** One could group a broader joined dataset and average a `CASE` expression that returns weather only for November. That is more complicated and needs extra logic to exclude countries whose target-month average is null; filtering first is clearer here.
- **Correlated subquery:** Computing a separate average subquery per country can be correct, but without strong indexing it may repeatedly scan `Weather` and perform much more work than one join-and-group pass.
- **Average exactly 15:** The first inclusive condition assigns `Cold`. It must not fall through to `Warm`.
- **Average exactly 25:** The second inclusive condition assigns `Hot`. It must not fall through to `Warm`.
- **Negative weather states:** `AVG` handles them normally, and sufficiently low averages remain `Cold`.
- **No November observation:** An inner join followed by the `WHERE` filter leaves no row for that country, so it is absent rather than reported with a null or invented type.
- **Rows in November of another year:** Formatting includes both `%Y` and `%m`, so November 2018 does not accidentally enter the November 2019 average.
- **Composite weather key:** At most one row exists per country and day. If duplicates were possible outside the contract, each duplicate would receive equal weight and could distort the intended daily average.
- **Null values outside the contract:** SQL `AVG` ignores null inputs. If `weather_state` could be null, the average would use fewer observations and an all-null group would make every `WHEN` comparison unknown, falling to `Warm`. Such behavior would need an explicit policy, but the given schema supplies integer states.
- **Output order:** No `ORDER BY` is required, so consumers must not rely on an incidental country ordering produced by one execution plan.
- **Ordinal grouping readability:** `GROUP BY 1` is concise but becomes fragile if the select-list order changes. `GROUP BY country_name` communicates the grouping key directly while preserving the same result under the accepted data assumption.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(W)$. Let $C$ be the number of rows in `Countries` and $W$ the number of rows in `Weather`. Under the standard relational-algorithm model, a hash join can index the country table in $O(C)$ time and then scan the weather rows in $O(W)$ time. Filtering, accumulating a sum, and maintaining a count for each surviving group are constant expected work per processed row. This gives expected $O(C+W)$ time.
- **Auxiliary Space Complexity:** $O(C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
