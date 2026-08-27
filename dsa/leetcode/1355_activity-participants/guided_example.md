# Guided Example: Activity Participants

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Friends": [{"id": 1, "name": "Jonathan D.", "activity": "Eating"}, {"id": 2, "name": "Jade W.", "activity": "Singing"}, {"id": 3, "name": "Victor J.", "activity": "Singing"}, {"id": 4, "name": "Elvis Q.", "activity": "Eating"}, {"id": 5, "name": "Daniel A.", "activity": "Eating"}, {"id": 6, "name": "Bob B.", "activity": "Horse Riding"}], "Activities": [{"id": 1, "name": "Eating"}, {"id": 2, "name": "Singing"}, {"id": 3, "name": "Horse Riding"}]}}`
- **Required output:** `{"columns": ["activity"], "rows": [["Singing"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Friends`

The objective is to compute `{"columns": ["activity"], "rows": [["Singing"]]}` from `{"tables": {"Friends": [{"id": 1, "name": "Jonathan D.", "activity": "Eating"}, {"id": 2, "name": "Jade W.", "activity": "Singing"}, {"id": 3, "name": "Victor J.", "activity": "Singing"}, {"id": 4, "name": "Elvis Q.", "activity": "Eating"}, {"id": 5, "name": "Daniel A.", "activity": "Eating"}, {"id": 6, "name": "Bob B.", "activity": "Horse Riding"}], "Activities": [{"id": 1, "name": "Eating"}, {"id": 2, "name": "Singing"}, {"id": 3, "name": "Horse Riding"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count participants per activity once

The common table expression `t` groups `Friends` by `activity` and computes `COUNT(1) AS cnt`. Each friend row represents one participant and has a primary-key `id`, so counting rows gives the number of participants in that activity. `COUNT(DISTINCT id)` would produce the same result but is unnecessary.

The CTE yields one row such as `(activity, cnt)` for every activity appearing in `Friends`.

The query does not read `Activities`. This is correct because the contract guarantees every catalog activity is performed by at least one friend. Consequently, every activity that must participate in the minimum and maximum comparison already appears as a group in `Friends`. If zero-participant catalog activities were allowed, ignoring `Activities` would incorrectly omit them and could change the minimum.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Friends": [{"id": 1, "name": "Jonathan D.", "activity": "Eating"}, {"id": 2, "name": "Jade W.", "activity": "Singing"}, {"id": 3, "name": "Victor J.", "activity": "Singing"}, {"id": 4, "name": "Elvis Q.", "activity": "Eating"}, {"id": 5, "name": "Daniel A.", "activity": "Eating"}, {"id": 6, "name": "Bob B.", "activity": "Horse Riding"}], "Activities": [{"id": 1, "name": "Eating"}, {"id": 2, "name": "Singing"}, {"id": 3, "name": "Horse Riding"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compute the global extremes from grouped counts

`SELECT MIN(cnt) FROM t` returns the smallest participant count among all activity groups. `SELECT MAX(cnt) FROM t` returns the largest.

The outer predicate requires both:

- `cnt > minimum`, excluding every activity tied for the minimum.
- `cnt < maximum`, excluding every activity tied for the maximum.

Strict comparisons are important. The task does not ask to remove only one minimum activity and one maximum activity; all activities whose count equals either extreme must be excluded.

In the example, counts are three for Eating, two for Singing, and one for Horse Riding. Only two is strictly greater than one and strictly less than three, so Singing is returned.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `SELECT MIN(cnt) FROM t` returns the smallest participant co... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the filter is exact

Every catalog activity has one count row in `t`. If its count lies strictly between the extrema, both comparisons are true and the activity is selected. If its count equals the minimum or maximum, at least one comparison is false and it is excluded. No other reason can include or exclude a row.

If all activities have the same number of participants, the minimum equals the maximum. No count can be both greater than and less than that value, so the correct result is empty. With only two distinct count levels, both levels are extremes and the result is also empty.

The result may appear in any order, so no `ORDER BY` is necessary. The selected column is named `activity` directly from the grouped friend data.

Depending on the MySQL optimizer, the CTE may be materialized once and reused by both scalar subqueries, or its logic may be transformed into an equivalent plan. Logically, both extrema must be computed over the same complete set of grouped counts.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["activity"], "rows": [["Singing"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Friends": [{"id": 1, "name": "Jonathan D.", "activity": "Eating"}, {"id": 2, "name": "Jade W.", "activity": "Singing"}, {"id": 3, "name": "Victor J.", "activity": "Singing"}, {"id": 4, "name": "Elvis Q.", "activity": "Eating"}, {"id": 5, "name": "Daniel A.", "activity": "Eating"}, {"id": 6, "name": "Bob B.", "activity": "Horse Riding"}], "Activities": [{"id": 1, "name": "Eating"}, {"id": 2, "name": "Singing"}, {"id": 3, "name": "Horse Riding"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["activity"], "rows": [["Singing"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Window functions:** Compute each count togethe:** - **Window functions:** Compute each count together with `MIN(count) OVER ()` and `MAX(count) OVER ()`, then filter in an outer query. This makes the single grouped pass explicit.
- **Ranking both directions:** Assign ascending and descending ranks to counts and keep rows whose two ranks are not one. Ties are handled naturally.
- **Anti-join against extreme counts:** Build a two-row set containing minimum and maximum, then keep grouped activities that do not join it.
- **Using `Activities` with a left join:** Required if catalog activities could have zero participants. The current guarantee makes that extra work unnecessary.
- **Tied minimum:** Every activity with that count fails the strict lower comparison.
- **Tied maximum:** Every activity with that count fails the strict upper comparison.
- **All counts equal:** Minimum and maximum coincide, so no activity qualifies.
- **Only two count levels:** Both levels are extremes, leaving an empty answer.
- **Several middle levels:** Every activity on any strictly intermediate level is returned.
- **No output order:** The query intentionally omits sorting because any order is accepted.
- **Friend names:** They do not affect participant totals; each row counts once regardless of name text.
- **Catalog guarantee:** Omitting `Activities` is safe only while every catalog activity has at least one matching friend.
- **Activity name identity:** Grouping uses the activity text stored in `Friends`. The data contract must keep that text aligned with the unique catalog activity names; inconsistent spellings would form separate groups.
- **Null activity outside the intended model:** A null activity would form its own SQL group and influence the extrema. The problem describes every friend as taking part in a named catalog activity, so the intended data excludes that ambiguity.
- **Repeated scalar subqueries:** Both extrema read `t`. A materialized CTE avoids regrouping `Friends`, while an optimizer may produce another equivalent plan; the logical answer is unchanged.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(F)$. Let $F$ be the number of friend rows and $A$ the number of activities.
- **Auxiliary Space Complexity:** $O(A)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
