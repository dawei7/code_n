# Guided Example: Rolling Average Steps

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Steps": [{"user_id": 1, "steps_count": 687, "steps_date": "2021-09-02"}, {"user_id": 1, "steps_count": 395, "steps_date": "2021-09-04"}, {"user_id": 1, "steps_count": 499, "steps_date": "2021-09-05"}, {"user_id": 1, "steps_count": 712, "steps_date": "2021-09-06"}, {"user_id": 1, "steps_count": 576, "steps_date": "2021-09-07"}, {"user_id": 2, "steps_count": 153, "steps_date": "2021-09-06"}, {"user_id": 2, "steps_count": 171, "steps_date": "2021-09-07"}, {"user_id": 2, "steps_count": 530, "steps_date": "2021-09-08"}, {"user_id": 3, "steps_count": 945, "steps_date": "2021-09-04"}, {"user_id": 3, "steps_count": 120, "steps_date": "2021-09-07"}, {"user_id": 3, "steps_count": 557, "steps_date": "2021-09-08"}, {"user_id": 3, "steps_count": 840, "steps_date": "2021-09-09"}, {"user_id": 3, "steps_count": 627, "steps_date": "2021-09-10"}, {"user_id": 5, "steps_count": 382, "steps_date": "2021-09-05"}, {"user_id": 6, "steps_count": 480, "steps_date": "2021-09-01"}, {"user_id": 6, "steps_count": 191, "steps_date": "2021-09-02"}, {"user_id": 6, "steps_count": 303, "steps_date": "2021-09-05"}]}}`
- **Required output:** `{"columns": ["user_id", "steps_date", "rolling_average"], "rows": [[1, "2021-09-06", 535.33], [1, "2021-09-07", 595.67], [2, "2021-09-08", 284.67], [3, "2021-09-09", 505.67], [3, "2021-09-10", 674.67]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Steps`

The objective is to compute `{"columns": ["user_id", "steps_date", "rolling_average"], "rows": [[1, "2021-09-06", 535.33], [1, "2021-09-07", 595.67], [2, "2021-09-08", 284.67], [3, "2021-09-09", 505.67], [3, "2021-09-10", 674.67]]}` from `{"tables": {"Steps": [{"user_id": 1, "steps_count": 687, "steps_date": "2021-09-02"}, {"user_id": 1, "steps_count": 395, "steps_date": "2021-09-04"}, {"user_id": 1, "steps_count": 499, "steps_date": "2021-09-05"}, {"user_id": 1, "steps_count": 712, "steps_date": "2021-09-06"}, {"user_id": 1, "steps_count": 576, "steps_date": "2021-09-07"}, {"user_id": 2, "steps_count": 153, "steps_date": "2021-09-06"}, {"user_id": 2, "steps_count": 171, "steps_date": "2021-09-07"}, {"user_id": 2, "steps_count": 530, "steps_date": "2021-09-08"}, {"user_id": 3, "steps_count": 945, "steps_date": "2021-09-04"}, {"user_id": 3, "steps_count": 120, "steps_date": "2021-09-07"}, {"user_id": 3, "steps_count": 557, "steps_date": "2021-09-08"}, {"user_id": 3, "steps_count": 840, "steps_date": "2021-09-09"}, {"user_id": 3, "steps_count": 627, "steps_date": "2021-09-10"}, {"user_id": 5, "steps_count": 382, "steps_date": "2021-09-05"}, {"user_id": 6, "steps_count": 480, "steps_date": "2021-09-01"}, {"user_id": 6, "steps_count": 191, "steps_date": "2021-09-02"}, {"user_id": 6, "steps_count": 303, "steps_date": "2021-09-05"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Calculate by user and date order.** A rolling average must never mix users. Both window expressions use `PARTITION BY user_id`, creating an independent chronological sequence for each user.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Steps": [{"user_id": 1, "steps_count": 687, "steps_date": "2021-09-02"}, {"user_id": 1, "steps_count": 395, "steps_date": "2021-09-04"}, {"user_id": 1, "steps_count": 499, "steps_date": "2021-09-05"}, {"user_id": 1, "steps_count": 712, "steps_date": "2021-09-06"}, {"user_id": 1, "steps_count": 576, "steps_date": "2021-09-07"}, {"user_id": 2, "steps_count": 153, "steps_date": "2021-09-06"}, {"user_id": 2, "steps_count": 171, "steps_date": "2021-09-07"}, {"user_id": 2, "steps_count": 530, "steps_date": "2021-09-08"}, {"user_id": 3, "steps_count": 945, "steps_date": "2021-09-04"}, {"user_id": 3, "steps_count": 120, "steps_date": "2021-09-07"}, {"user_id": 3, "steps_count": 557, "steps_date": "2021-09-08"}, {"user_id": 3, "steps_count": 840, "steps_date": "2021-09-09"}, {"user_id": 3, "steps_count": 627, "steps_date": "2021-09-10"}, {"user_id": 5, "steps_count": 382, "steps_date": "2021-09-05"}, {"user_id": 6, "steps_count": 480, "steps_date": "2021-09-01"}, {"user_id": 6, "steps_count": 191, "steps_date": "2021-09-02"}, {"user_id": 6, "steps_count": 303, "steps_date": "2021-09-05"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`ORDER BY steps_date` places that user's recorded days in ascending calendar order. The primary key `(user_id, steps_date)` guarantees at most one row per user per date, so there are no same-day ordering ties.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Average the current and two preceding rows.** The expression

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id", "steps_date", "rolling_average"], "rows": [[1, "2021-09-06", 535.33], [1, "2021-09-07", 595.67], [2, "2021-09-08", 284.67], [3, "2021-09-09", 505.67], [3, "2021-09-10", 674.67]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Steps": [{"user_id": 1, "steps_count": 687, "steps_date": "2021-09-02"}, {"user_id": 1, "steps_count": 395, "steps_date": "2021-09-04"}, {"user_id": 1, "steps_count": 499, "steps_date": "2021-09-05"}, {"user_id": 1, "steps_count": 712, "steps_date": "2021-09-06"}, {"user_id": 1, "steps_count": 576, "steps_date": "2021-09-07"}, {"user_id": 2, "steps_count": 153, "steps_date": "2021-09-06"}, {"user_id": 2, "steps_count": 171, "steps_date": "2021-09-07"}, {"user_id": 2, "steps_count": 530, "steps_date": "2021-09-08"}, {"user_id": 3, "steps_count": 945, "steps_date": "2021-09-04"}, {"user_id": 3, "steps_count": 120, "steps_date": "2021-09-07"}, {"user_id": 3, "steps_count": 557, "steps_date": "2021-09-08"}, {"user_id": 3, "steps_count": 840, "steps_date": "2021-09-09"}, {"user_id": 3, "steps_count": 627, "steps_date": "2021-09-10"}, {"user_id": 5, "steps_count": 382, "steps_date": "2021-09-05"}, {"user_id": 6, "steps_count": 480, "steps_date": "2021-09-01"}, {"user_id": 6, "steps_count": 191, "steps_date": "2021-09-02"}, {"user_id": 6, "steps_count": 303, "steps_date": "2021-09-05"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id", "steps_date", "rolling_average"], "rows": [[1, "2021-09-06", 535.33], [1, "2021-09-07", 595.67], [2, "2021-09-08", 284.67], [3, "2021-09-09", 505.67], [3, "2021-09-10", 674.67]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Three-way self-join by exact dates:** Join each row to records one and two days earlier for the same user, then average their counts. It directly enforces calendar adjacency but performs more joins.
- **Calendar range frame:** A date-based range can express time span, but it must also ensure exactly all three daily rows exist; the LAG check is explicit and reliable here.
- **Fewer than three user records:** `LAG(..., 2)` is null, so no output row is produced.
- **Three recorded rows with a gap:** Their date difference exceeds two and the row is filtered out even though the row frame has size three.
- **Exactly three consecutive dates:** The current third date produces the first rolling average.
- **Long consecutive run:** Every date from the third onward receives an overlapping three-day average.
- **Separate users:** Partitioning resets both averaging and lag state.
- **One row per user-date:** The primary key is essential to infer the middle date from the two-day span.
- **Rounding:** `ROUND` occurs after AVG, not on individual step counts.
- **Partial internal averages:** They exist in the CTE but are removed by `st = 1`.
- **Required order:** Ordinal ordering refers to user ID and step date in the outer select list.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S log S)$. Let $S$ be the number of `Steps` rows. Window functions generally require ordering rows within user partitions. Without a suitable index supplying that order, sorting costs $O(S\log S)$ in the worst case.
- **Auxiliary Space Complexity:** $O(S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
