# Guided Example: Find Peak Calling Hours for Each City

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Calls": [{"caller_id": 8, "recipient_id": 4, "call_time": "2021-08-24 22:46:07", "city": "Houston"}, {"caller_id": 4, "recipient_id": 8, "call_time": "2021-08-24 22:57:13", "city": "Houston"}, {"caller_id": 5, "recipient_id": 1, "call_time": "2021-08-11 21:28:44", "city": "Houston"}, {"caller_id": 8, "recipient_id": 3, "call_time": "2021-08-17 22:04:15", "city": "Houston"}, {"caller_id": 11, "recipient_id": 3, "call_time": "2021-08-17 13:07:00", "city": "New York"}, {"caller_id": 8, "recipient_id": 11, "call_time": "2021-08-17 14:22:22", "city": "New York"}]}}`
- **Required output:** `{"columns": ["city", "peak_calling_hour", "number_of_calls"], "rows": [["Houston", 22, 3], ["New York", 14, 1], ["New York", 13, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Calls`

The objective is to compute `{"columns": ["city", "peak_calling_hour", "number_of_calls"], "rows": [["Houston", 22, 3], ["New York", 14, 1], ["New York", 13, 1]]}` from `{"tables": {"Calls": [{"caller_id": 8, "recipient_id": 4, "call_time": "2021-08-24 22:46:07", "city": "Houston"}, {"caller_id": 4, "recipient_id": 8, "call_time": "2021-08-24 22:57:13", "city": "Houston"}, {"caller_id": 5, "recipient_id": 1, "call_time": "2021-08-11 21:28:44", "city": "Houston"}, {"caller_id": 8, "recipient_id": 3, "call_time": "2021-08-17 22:04:15", "city": "Houston"}, {"caller_id": 11, "recipient_id": 3, "call_time": "2021-08-17 13:07:00", "city": "New York"}, {"caller_id": 8, "recipient_id": 11, "call_time": "2021-08-17 14:22:22", "city": "New York"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: First define the exact unit being counted

Each row in `Calls` represents one call associated with one city and one timestamp. “Peak calling hour” means the hour-of-day value from zero through 23 that has the greatest number of rows for that city. Dates are not separate groups: calls at 22:10 on different days all contribute to hour 22 for their city.

The inner derived table computes this first aggregation:

`SELECT city, HOUR(call_time) AS h, COUNT(1) AS cnt FROM Calls GROUP BY 1, 2`.

`HOUR(call_time)` extracts only the hour component. Grouping by selected column positions one and two means grouping by `city` and `h`. `COUNT(1)` counts every call row in that city/hour bucket.

After this stage, there is at most one row for each pair `(city, hour)`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Calls": [{"caller_id": 8, "recipient_id": 4, "call_time": "2021-08-24 22:46:07", "city": "Houston"}, {"caller_id": 4, "recipient_id": 8, "call_time": "2021-08-24 22:57:13", "city": "Houston"}, {"caller_id": 5, "recipient_id": 1, "call_time": "2021-08-11 21:28:44", "city": "Houston"}, {"caller_id": 8, "recipient_id": 3, "call_time": "2021-08-17 22:04:15", "city": "Houston"}, {"caller_id": 11, "recipient_id": 3, "call_time": "2021-08-17 13:07:00", "city": "New York"}, {"caller_id": 8, "recipient_id": 11, "call_time": "2021-08-17 14:22:22", "city": "New York"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Rank hour buckets inside each city

The outer part of CTE `T` applies:

`RANK() OVER (PARTITION BY city ORDER BY cnt DESC) AS rk`.

`PARTITION BY city` restarts ranking independently for each city. Ordering `cnt` descending puts the largest count first. Every hour tied for that largest count receives rank one because `RANK` assigns the same rank to equal ordering values.

That tie behavior is essential. `ROW_NUMBER` would choose an arbitrary single hour among ties, violating the requirement to return all peak hours. `RANK` preserves every co-maximum.

The final `WHERE rk = 1` keeps precisely those peak buckets.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Rename columns to the requested schema

The output selects:

- `city` unchanged;
- `h AS peak_calling_hour`; and
- `cnt AS number_of_calls`.

These aliases are presentation details but part of the required result contract. The CTE’s short internal names do not leak into the final schema.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["city", "peak_calling_hour", "number_of_calls"], "rows": [["Houston", 22, 3], ["New York", 14, 1], ["New York", 13, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Calls": [{"caller_id": 8, "recipient_id": 4, "call_time": "2021-08-24 22:46:07", "city": "Houston"}, {"caller_id": 4, "recipient_id": 8, "call_time": "2021-08-24 22:57:13", "city": "Houston"}, {"caller_id": 5, "recipient_id": 1, "call_time": "2021-08-11 21:28:44", "city": "Houston"}, {"caller_id": 8, "recipient_id": 3, "call_time": "2021-08-17 22:04:15", "city": "Houston"}, {"caller_id": 11, "recipient_id": 3, "call_time": "2021-08-17 13:07:00", "city": "New York"}, {"caller_id": 8, "recipient_id": 11, "call_time": "2021-08-17 14:22:22", "city": "New York"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["city", "peak_calling_hour", "number_of_calls"], "rows": [["Houston", 22, 3], ["New York", 14, 1], ["New York", 13, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Use `ROW_NUMBER`:** This incorrectly drops tied peak hours because it forces unique row numbers.
- **Use `DENSE_RANK`:** Filtering rank one would also work; differences between later ranks do not matter.
- **Correlated maximum subquery:** Each grouped row can be compared with its city’s maximum, but the window rank expresses tie preservation more directly.
- **Group by full timestamp:** That would count individual moments, not hour-of-day buckets across dates.
- **Group by date and hour:** That would find daily peaks rather than one peak-hour profile per city.
- **One hour for a city:** Its only group automatically receives rank one.
- **All hours tied:** Every observed hour for that city is returned.
- **No call rows:** The grouped relation and output are empty; no synthetic hours are required.
- **Ordinal ordering:** `ORDER BY 2 DESC, 1 DESC` depends on select-column positions and implements hour first, then city.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R log R)$. Let $R$ be the number of call rows and $G$ the number of distinct city/hour groups. Reading and grouping the input is $O(R)$ expected with hash aggregation or $O(R\log R)$ with sort-based grouping. Ranking may sort the $G$ grouped rows by city and count, costing $O(G\log G)$ in a general model. Final sorting of at most $G$ peak rows is also $O(G\log G)$.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
