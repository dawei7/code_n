# Guided Example: The First Day of the Maximum Recorded Degree in Each City

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Weather": [{"city_id": 1, "day": "2022-01-07", "degree": -12}, {"city_id": 1, "day": "2022-03-07", "degree": 5}, {"city_id": 1, "day": "2022-07-07", "degree": 24}, {"city_id": 2, "day": "2022-08-07", "degree": 37}, {"city_id": 2, "day": "2022-08-17", "degree": 37}, {"city_id": 3, "day": "2022-02-07", "degree": -7}, {"city_id": 3, "day": "2022-12-07", "degree": -6}]}}`
- **Required output:** `{"columns": ["city_id", "day", "degree"], "rows": [[1, "2022-07-07", 24], [2, "2022-08-07", 37], [3, "2022-12-07", -6]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Weather`

The objective is to compute `{"columns": ["city_id", "day", "degree"], "rows": [[1, "2022-07-07", 24], [2, "2022-08-07", 37], [3, "2022-12-07", -6]]}` from `{"tables": {"Weather": [{"city_id": 1, "day": "2022-01-07", "degree": -12}, {"city_id": 1, "day": "2022-03-07", "degree": 5}, {"city_id": 1, "day": "2022-07-07", "degree": 24}, {"city_id": 2, "day": "2022-08-07", "degree": 37}, {"city_id": 2, "day": "2022-08-17", "degree": 37}, {"city_id": 3, "day": "2022-02-07", "degree": -7}, {"city_id": 3, "day": "2022-12-07", "degree": -6}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Define one complete priority order inside each city

For every city, the desired row is selected by two rules in sequence:

1. Prefer a larger `degree`.
2. If several rows have that same maximum degree, prefer the earlier `day`.

These rules can be encoded directly as an ordering. Descending degree puts the hottest records first, and ascending day puts the earliest record first among equal degrees. Once every city's rows have that order, the answer is simply its first row.

The common table expression `T` computes a window rank using

`PARTITION BY city_id ORDER BY degree DESC, day`.

Partitioning is essential. It restarts the ranking independently for each city, so a very hot measurement in one city has no effect on which row is selected for another city.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Weather": [{"city_id": 1, "day": "2022-01-07", "degree": -12}, {"city_id": 1, "day": "2022-03-07", "degree": 5}, {"city_id": 1, "day": "2022-07-07", "degree": 24}, {"city_id": 2, "day": "2022-08-07", "degree": 37}, {"city_id": 2, "day": "2022-08-17", "degree": 37}, {"city_id": 3, "day": "2022-02-07", "degree": -7}, {"city_id": 3, "day": "2022-12-07", "degree": -6}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the two order directions are different

`degree DESC` places a higher numerical degree before a lower one. This also works when all recorded values are negative. For example, `-6` is greater than `-7` and therefore appears first under descending numeric order.

The next key `day` uses SQL's default ascending direction. It matters only after degrees tie because it appears second in the ordering list. Earlier dates sort before later dates, implementing the required tie-break.

Changing either direction changes the problem. Ascending degree would choose the coldest record, while descending day would choose the latest occurrence of a city's maximum rather than the first.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why `RANK() = 1` leaves exactly one row per city

The window function assigns rank one to the first ordering key combination within each city. In general, `RANK` can assign the same rank to tied rows. Here a complete tie would require both the same `degree` and the same `day` within one city.

The table's primary key is `(city_id, day)`. A city cannot have two rows on the same day, so two rows in the same partition cannot tie on the `day` key. Even when several rows share the maximum degree, their dates are different and the earlier date orders first. Therefore exactly one row per city receives `rk = 1`.

The outer `WHERE rk = 1` keeps that unique winning row and removes every later record. Using `RANK` is safe because the order is total inside each valid city partition; `ROW_NUMBER` would produce the same winner.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["city_id", "day", "degree"], "rows": [[1, "2022-07-07", 24], [2, "2022-08-07", 37], [3, "2022-12-07", -6]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Weather": [{"city_id": 1, "day": "2022-01-07", "degree": -12}, {"city_id": 1, "day": "2022-03-07", "degree": 5}, {"city_id": 1, "day": "2022-07-07", "degree": 24}, {"city_id": 2, "day": "2022-08-07", "degree": 37}, {"city_id": 2, "day": "2022-08-17", "degree": 37}, {"city_id": 3, "day": "2022-02-07", "degree": -7}, {"city_id": 3, "day": "2022-12-07", "degree": -6}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["city_id", "day", "degree"], "rows": [[1, "2022-07-07", 24], [2, "2022-08-07", 37], [3, "2022-12-07", -6]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`ROW_NUMBER` with the same ordering:** This is equally correct and explicitly guarantees one row per partition. Under the unique `(city_id, day)` key, it selects the same row as `RANK`.
- **Aggregate maximum degree then join:** Compute `MAX(degree)` per city, join matching rows, and aggregate `MIN(day)` among the ties. This is valid but requires multiple logical stages and careful grouping to return the matching degree.
- **Correlated subqueries:** For each row, test whether a higher degree or an equal degree with an earlier day exists. This can be correct but is more verbose and may be less efficient without suitable indexes.
- **Use `MAX(day)` with `MAX(degree)` in one grouping:** Independent maxima may come from different source rows, producing a date that did not record the maximum degree. The tie-break must be applied only among maximum-degree rows.
- **Order by day before degree:** That would select the earliest weather record in the city, even when a later day is hotter. Degree has higher priority.
- **Order degree ascending:** This selects the minimum recorded degree and is incorrect, especially easy to overlook with negative values.
- **Order day descending:** This selects the latest occurrence of the maximum rather than the required earliest occurrence.
- **Several maximum-degree days:** The ascending date key makes exactly the earliest one rank first.
- **All degrees negative:** Numeric descending order still selects the greatest value, such as `-2` over `-10`. No special sign handling is needed.
- **One row for a city:** It is automatically rank one and is returned.
- **Many cities with the same maximum degree:** Partitions are independent, so cross-city ties never interact.
- **Duplicate day within a city:** The primary key forbids it. Without that guarantee, complete ordering ties could give more than one row `rk = 1`.
- **No final `ORDER BY`:** SQL does not promise partition or CTE output order. Correct row selection alone would not satisfy the requested ascending city presentation.
- **`ORDER BY 1` readability:** It correctly refers to `city_id` because that is the first projected column. Writing `ORDER BY city_id` would be more explicit but would not change the result.
- **Helper rank column:** It exists only inside `T` and is intentionally omitted from the final projection.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r log r)$. Let `r` be the number of rows in `Weather`. Evaluating the window order may require sorting rows by city and by the within-city keys, which takes `O(r \log r)` time with a general comparison sort. The final output ordering by `city_id` can also require sorting, but another `O(r \log r)` operation does not change the overall bound. A database optimizer may exploit an index or preserve a useful intermediate order, but the logical worst-case analysis remains `O(r \log r)`.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
