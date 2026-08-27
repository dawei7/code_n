# Guided Example: Calculate Orders Within Each Interval

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Orders": [{"minute": 1, "order_count": 0}, {"minute": 2, "order_count": 2}, {"minute": 3, "order_count": 4}, {"minute": 4, "order_count": 6}, {"minute": 5, "order_count": 1}, {"minute": 6, "order_count": 4}, {"minute": 7, "order_count": 1}, {"minute": 8, "order_count": 2}, {"minute": 9, "order_count": 4}, {"minute": 10, "order_count": 1}, {"minute": 11, "order_count": 4}, {"minute": 12, "order_count": 6}]}}`
- **Required output:** `{"columns": ["interval_no", "total_orders"], "rows": [[1, 17], [2, 18]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Orders`

The objective is to compute `{"columns": ["interval_no", "total_orders"], "rows": [[1, 17], [2, 18]]}` from `{"tables": {"Orders": [{"minute": 1, "order_count": 0}, {"minute": 2, "order_count": 2}, {"minute": 3, "order_count": 4}, {"minute": 4, "order_count": 6}, {"minute": 5, "order_count": 1}, {"minute": 6, "order_count": 4}, {"minute": 7, "order_count": 1}, {"minute": 8, "order_count": 2}, {"minute": 9, "order_count": 4}, {"minute": 10, "order_count": 1}, {"minute": 11, "order_count": 4}, {"minute": 12, "order_count": 6}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Understand the exact query as a rolling-window calculation.** The source first builds common table expression `T`. For every order row, it computes:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Orders": [{"minute": 1, "order_count": 0}, {"minute": 2, "order_count": 2}, {"minute": 3, "order_count": 4}, {"minute": 4, "order_count": 6}, {"minute": 5, "order_count": 1}, {"minute": 6, "order_count": 4}, {"minute": 7, "order_count": 1}, {"minute": 8, "order_count": 2}, {"minute": 9, "order_count": 4}, {"minute": 10, "order_count": 1}, {"minute": 11, "order_count": 4}, {"minute": 12, "order_count": 6}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`SUM(order_count) OVER (ORDER BY minute ROWS 5 PRECEDING)`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `SUM(order_count) OVER (ORDER BY minute ROWS 5 PRECEDING)`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

`ORDER BY minute` places rows into chronological minute order for the window calculation. `ROWS 5 PRECEDING` means the frame contains the current row plus at most five preceding rows: six rows in total once enough history exists. `total_orders` is therefore a rolling six-row sum attached to every minute row.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["interval_no", "total_orders"], "rows": [[1, 17], [2, 18]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Orders": [{"minute": 1, "order_count": 0}, {"minute": 2, "order_count": 2}, {"minute": 3, "order_count": 4}, {"minute": 4, "order_count": 6}, {"minute": 5, "order_count": 1}, {"minute": 6, "order_count": 4}, {"minute": 7, "order_count": 1}, {"minute": 8, "order_count": 2}, {"minute": 9, "order_count": 4}, {"minute": 10, "order_count": 1}, {"minute": 11, "order_count": 4}, {"minute": 12, "order_count": 6}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["interval_no", "total_orders"], "rows": [[1, 17], [2, 18]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Direct bucket grouping:** Group by `(minute - :** - **Direct bucket grouping:** Group by `(minute - 1) DIV 6 + 1`, sum counts, and `ORDER BY interval_no`. This is robust to missing minute rows and matches the manifest.
- **Consecutive minutes:** Only under this unstated guarantee does six preceding rows equal the current six-minute interval.
- **Missing boundary minute:** The exact query omits that interval entirely.
- **Sparse rows:** `ROWS` counts records, not minute distance, so totals can cross interval boundaries.
- **First five rows:** Their rolling frames have fewer than six rows, but they are filtered out when conventional boundaries begin at minute six.
- **Final ordering:** Add outer `ORDER BY interval_no`; window ordering alone does not guarantee result order.
- **Division:** Boundary minutes are divisible by six, so `minute / 6` has an integer value even if MySQL represents it as a decimal type.
- **Primary key:** It guarantees unique minute labels, not consecutiveness.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M\log M)$. Let $M$ be the number of order rows and $I$ the number of emitted boundary rows. The window needs rows in minute order. If the primary-key index can provide that order and the engine streams the frame, processing can be $O(M)$ with a constant six-row rolling state. If an explicit sort is required, time can be $O(M\log M)$ and sort or materialization space can be $O(M)$.
- **Auxiliary Space Complexity:** $O(M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
