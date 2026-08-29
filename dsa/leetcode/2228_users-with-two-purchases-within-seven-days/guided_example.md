# Guided Example: Users With Two Purchases Within Seven Days

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Purchases": [{"purchase_id": 4, "user_id": 2, "purchase_date": "2022-03-13"}, {"purchase_id": 1, "user_id": 5, "purchase_date": "2022-02-11"}, {"purchase_id": 3, "user_id": 7, "purchase_date": "2022-06-19"}, {"purchase_id": 6, "user_id": 2, "purchase_date": "2022-03-20"}, {"purchase_id": 5, "user_id": 7, "purchase_date": "2022-06-19"}, {"purchase_id": 2, "user_id": 2, "purchase_date": "2022-06-08"}]}}`
- **Required output:** `{"columns": ["user_id"], "rows": [[2], [7]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Purchases`

The objective is to compute `{"columns": ["user_id"], "rows": [[2], [7]]}` from `{"tables": {"Purchases": [{"purchase_id": 4, "user_id": 2, "purchase_date": "2022-03-13"}, {"purchase_id": 1, "user_id": 5, "purchase_date": "2022-02-11"}, {"purchase_id": 3, "user_id": 7, "purchase_date": "2022-06-19"}, {"purchase_id": 6, "user_id": 2, "purchase_date": "2022-03-20"}, {"purchase_id": 5, "user_id": 7, "purchase_date": "2022-06-19"}, {"purchase_id": 2, "user_id": 2, "purchase_date": "2022-06-08"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce all possible pairs to neighboring dates

For one user, imagine sorting all purchase rows by `purchase_date`. The requirement asks whether any two dates differ by at most seven days. It may seem necessary to compare every pair, but sorted order makes only neighboring dates necessary.

Suppose two non-neighboring dates `a` and `b` are at most seven days apart. Every date between them lies inside the same seven-day interval. In particular, an adjacent pair somewhere from `a` through `b` has a gap no larger than `b - a`, and therefore no larger than seven days. Thus, the existence of any qualifying pair guarantees a qualifying adjacent pair.

The reverse is immediate: an adjacent pair is still a pair of purchases. If its gap is at most seven, the user qualifies. Checking consecutive sorted dates is therefore both sufficient and necessary.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Purchases": [{"purchase_id": 4, "user_id": 2, "purchase_date": "2022-03-13"}, {"purchase_id": 1, "user_id": 5, "purchase_date": "2022-02-11"}, {"purchase_id": 3, "user_id": 7, "purchase_date": "2022-06-19"}, {"purchase_id": 6, "user_id": 2, "purchase_date": "2022-03-20"}, {"purchase_id": 5, "user_id": 7, "purchase_date": "2022-06-19"}, {"purchase_id": 2, "user_id": 2, "purchase_date": "2022-06-08"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use a window function to find each previous purchase

The common table expression `t` selects every `user_id` and computes

`LAG(purchase_date, 1) OVER (PARTITION BY user_id ORDER BY purchase_date)`.

`PARTITION BY user_id` creates a separate ordered sequence for each user. Purchases from different users never become neighbors. `ORDER BY purchase_date` puts that user's rows in chronological order, and `LAG(..., 1)` returns the date from the immediately preceding row.

For a user's earliest purchase, no preceding row exists, so `LAG` returns `NULL`. That row cannot establish a pair and should not qualify anyone by itself.

When several purchases occur on the same date, their tie order is immaterial. At least one tied row follows another tied row, producing a zero-day gap. The unique `purchase_id` is not needed as a secondary order key because every order among equal dates yields the same date difference.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Turn neighboring dates into day gaps

The expression `DATEDIFF(purchase_date, previous_date)` subtracts the previous date from the current date and returns the number of calendar days. Because the rows are sorted ascending, this value is nonnegative.

The CTE names the result `d`. A same-day pair has `d = 0`, purchases exactly one week apart have `d = 7`, and both satisfy the “at most seven days” wording.

For the first row in each partition, the previous date is `NULL`, so `DATEDIFF` also yields `NULL`. In SQL's three-valued logic, `NULL <= 7` is not true, and the later `WHERE` clause discards it automatically.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["user_id"], "rows": [[2], [7]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Purchases": [{"purchase_id": 4, "user_id": 2, "purchase_date": "2022-03-13"}, {"purchase_id": 1, "user_id": 5, "purchase_date": "2022-02-11"}, {"purchase_id": 3, "user_id": 7, "purchase_date": "2022-06-19"}, {"purchase_id": 6, "user_id": 2, "purchase_date": "2022-03-20"}, {"purchase_id": 5, "user_id": 7, "purchase_date": "2022-06-19"}, {"purchase_id": 2, "user_id": 2, "purchase_date": "2022-06-08"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["user_id"], "rows": [[2], [7]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Self-join every user's purchases:** Join two rows on equal `user_id` and a date gap at most seven. It is straightforward but can generate quadratically many row pairs for a user with many purchases.
- **Correlated existence subquery:** Test each row for another qualifying row. An optimizer and suitable index may execute it well, but the window formulation directly exploits sorted adjacency.
- **Compare only minimum and maximum dates:** A user can have a close pair amid a much wider overall span, so the extremes alone are insufficient.
- **Same-day purchases:** `DATEDIFF` is zero, and zero is correctly within seven days.
- **Exactly seven days:** The inclusive comparison `<= 7` admits the boundary.
- **Eight days:** It fails the condition.
- **Only one purchase:** `LAG` is null and the user is absent.
- **Many qualifying pairs:** `DISTINCT` ensures one output row per user.
- **Equal-date tie ordering:** Any order among tied rows creates a zero gap between neighboring tied purchases, so no secondary key is required for correctness.
- **Partition boundary:** `PARTITION BY user_id` prevents one user's last purchase from becoming another user's previous date.
- **First row null:** SQL does not treat null as zero; `WHERE d <= 7` discards it.
- **Required ordering:** `DISTINCT` alone does not guarantee order. The final `ORDER BY user_id` is necessary.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r log r)$. Let `r` be the number of rows in `Purchases`. Computing `LAG` requires rows to be ordered by `user_id` partitions and `purchase_date`. Without a supporting index or already useful physical order, sorting dominates at `O(r \log r)` time. Window evaluation, filtering, and scanning are linear after ordering.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
