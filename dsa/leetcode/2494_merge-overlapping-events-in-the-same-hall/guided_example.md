# Guided Example: Merge Overlapping Events in the Same Hall

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"HallEvents": [{"hall_id": 1, "start_day": "2023-01-13", "end_day": "2023-01-14"}, {"hall_id": 1, "start_day": "2023-01-14", "end_day": "2023-01-17"}, {"hall_id": 1, "start_day": "2023-01-18", "end_day": "2023-01-25"}, {"hall_id": 2, "start_day": "2022-12-09", "end_day": "2022-12-23"}, {"hall_id": 2, "start_day": "2022-12-13", "end_day": "2022-12-17"}, {"hall_id": 3, "start_day": "2022-12-01", "end_day": "2023-01-30"}]}}`
- **Required output:** `{"columns": ["hall_id", "start_day", "end_day"], "rows": [[1, "2023-01-13", "2023-01-17"], [1, "2023-01-18", "2023-01-25"], [2, "2022-12-09", "2022-12-23"], [3, "2022-12-01", "2023-01-30"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `HallEvents`

The objective is to compute `{"columns": ["hall_id", "start_day", "end_day"], "rows": [[1, "2023-01-13", "2023-01-17"], [1, "2023-01-18", "2023-01-25"], [2, "2022-12-09", "2022-12-23"], [3, "2022-12-01", "2023-01-30"]]}` from `{"tables": {"HallEvents": [{"hall_id": 1, "start_day": "2023-01-13", "end_day": "2023-01-14"}, {"hall_id": 1, "start_day": "2023-01-14", "end_day": "2023-01-17"}, {"hall_id": 1, "start_day": "2023-01-18", "end_day": "2023-01-25"}, {"hall_id": 2, "start_day": "2022-12-09", "end_day": "2022-12-23"}, {"hall_id": 2, "start_day": "2022-12-13", "end_day": "2022-12-17"}, {"hall_id": 3, "start_day": "2022-12-01", "end_day": "2023-01-30"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Intervals must be merged independently per hall

Two events interact only when their `hall_id` values match. Within one hall, events are ordered by `start_day`. Once ordered, overlapping events form consecutive islands: a new island begins only when the next start lies after every end date seen in the current island.

Comparing a row only with the immediately previous row's `end_day` is insufficient. For intervals `[1,10]`, `[2,3]`, and `[9,12]`, the third interval overlaps the first even though it does not overlap the second. The solution therefore carries the maximum end date reached so far.

The query implements the standard gaps-and-islands pattern with three common table expressions.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"HallEvents": [{"hall_id": 1, "start_day": "2023-01-13", "end_day": "2023-01-14"}, {"hall_id": 1, "start_day": "2023-01-14", "end_day": "2023-01-17"}, {"hall_id": 1, "start_day": "2023-01-18", "end_day": "2023-01-25"}, {"hall_id": 2, "start_day": "2022-12-09", "end_day": "2022-12-23"}, {"hall_id": 2, "start_day": "2022-12-13", "end_day": "2022-12-17"}, {"hall_id": 3, "start_day": "2022-12-01", "end_day": "2023-01-30"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: CTE `S` computes the running reach

For every event, `cur_max_end_day` is calculated with

`MAX(end_day) OVER (PARTITION BY hall_id ORDER BY start_day)`.

Partitioning restarts the calculation for each hall. Ordering by `start_day` processes that hall's events chronologically. The running maximum represents the farthest end date covered by the current or any earlier interval in the ordered partition.

This running reach captures chained overlap. Even if an intermediate short interval ends early, an earlier long interval keeps `cur_max_end_day` extended far enough for later overlapping intervals to remain in the same island.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For every event, `cur_max_end_day` is calculated with

`MAX(... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: CTE `T` marks where islands begin

`LAG(cur_max_end_day)` obtains the running reach associated with the preceding ordered row in the same hall. The current interval overlaps the existing island when

`start_day <= previous_cur_max_end_day`.

Equality is included because events sharing at least one day overlap. For example, an event ending January 14 and another starting January 14 must merge.

The `IF` expression emits zero for an overlap and one for a gap. On the first row of a hall, `LAG` is `NULL`. The comparison with `NULL` is not true, so MySQL's `IF` takes the final branch and marks that row with one, correctly starting the hall's first island.

It is important that `LAG` is applied to the running maximum, not directly to the preceding event's raw end date. That is what preserves transitive overlap.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["hall_id", "start_day", "end_day"], "rows": [[1, "2023-01-13", "2023-01-17"], [1, "2023-01-18", "2023-01-25"], [2, "2022-12-09", "2022-12-23"], [3, "2022-12-01", "2023-01-30"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"HallEvents": [{"hall_id": 1, "start_day": "2023-01-13", "end_day": "2023-01-14"}, {"hall_id": 1, "start_day": "2023-01-14", "end_day": "2023-01-17"}, {"hall_id": 1, "start_day": "2023-01-18", "end_day": "2023-01-25"}, {"hall_id": 2, "start_day": "2022-12-09", "end_day": "2022-12-23"}, {"hall_id": 2, "start_day": "2022-12-13", "end_day": "2022-12-17"}, {"hall_id": 3, "start_day": "2022-12-01", "end_day": "2023-01-30"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["hall_id", "start_day", "end_day"], "rows": [[1, "2023-01-13", "2023-01-17"], [1, "2023-01-18", "2023-01-25"], [2, "2022-12-09", "2022-12-23"], [3, "2022-12-01", "2023-01-30"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Immediate previous end only:** This fails when:** - **Immediate previous end only:** This fails when a long earlier interval bridges over a short nested interval; use the previous running maximum.
- **Recursive interval expansion:** It can merge chains but is more complicated and less natural than window-based gaps and islands.
- **Touching dates:** `start_day == prior maximum end` is overlap because the shared date counts.
- **One-day event:** Its start equals its end and it merges with any same-hall interval containing that date.
- **Different halls:** They never merge even when date ranges are identical.
- **Nested intervals:** The running maximum remains the outer interval's end.
- **Duplicate rows:** Aggregation collapses them without requiring `DISTINCT`.
- **First row per hall:** A `NULL` lag causes the start marker to be one.
- **Transitive overlap:** A chain of pairwise overlaps belongs to one island.
- **Output order:** No ordering clause is required.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r log r)$. Let $r$ be the number of event rows. Window functions generally require ordering each hall's rows by `start_day`. Across all partitions, sorting dominates at $O(r\log r)$ worst-case time. The window passes and final aggregation are linear after ordering.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
