# Guided Example: Biggest Single Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"MyNumbers": [{"num": 42}]}}`
- **Required output:** `{"columns": ["num"], "rows": [[42]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `MyNumbers`

The objective is to compute `{"columns": ["num"], "rows": [[42]]}` from `{"tables": {"MyNumbers": [{"num": 42}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**“Single” describes frequency, not mathematical uniqueness.** A number qualifies only if it occurs in exactly one input row. The largest distinct value is not necessarily a single number: a very large number that appears twice must be rejected. The query therefore calculates occurrence counts before it calculates the maximum.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"MyNumbers": [{"num": 42}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**The inner query forms one group per value.** `GROUP BY 1` groups by the first selected expression, which is `num`. All rows with the same number enter the same group. `COUNT(1)` counts the rows in that group because the literal `1` is non-null for every row.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["num"], "rows": [[42]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"MyNumbers": [{"num": 42}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["num"], "rows": [[42]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort descending and test counts:** Group values with their counts, sort qualifying groups by `num DESC`, and take the first. This can find the same value but needs special handling to return one `NULL` row when no group qualifies.
- **Correlated frequency subquery:** Filter each row where a subquery counts one matching value, then take `MAX`. It is readable but can repeat work without effective optimization.
- **Window count:** Attach `COUNT(*) OVER (PARTITION BY num)` to every row, filter count 1, and aggregate the maximum. This avoids a grouped derived table but usually carries more repeated rows through the plan.
- **All values duplicated:** The inner query is empty, and outer `MAX` correctly returns one row containing `NULL`.
- **Exactly one row:** Its group count is one, so that value is returned.
- **Negative numbers:** `MAX` still means the greatest numeric value; for example, `-2` is greater than `-7`.
- **Largest raw value duplicated:** It is removed before `MAX`, allowing a smaller qualifying value to win.
- **Many copies of one value:** Its group still occupies one aggregate entry and fails because its count is greater than one.
- **Null input value:** The statement describes integers but does not explicitly state nullability. `COUNT(1)` would treat one null row as a size-one group, while outer `MAX(num)` ignores null and returns `NULL`; this is indistinguishable from no qualifying numeric value. If null semantics mattered, they should be specified explicitly.
- **`GROUP BY 1` maintainability:** It is concise but positional. `GROUP BY num` communicates intent more directly and cannot silently change meaning after select-list reordering.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R\log R)$. Let $R$ be the number of rows in `MyNumbers` and $U$ the number of distinct values. A sort-based grouping plan orders the rows by `num`, costing $O(R\log R)$ time, and then scans the groups. A hash aggregation can achieve expected $O(R)$ time. The outer `MAX` scans at most $U$ qualifying group rows, which is dominated by the grouping cost. The manifest's conservative, engine-independent time bound is $O(R\log R)$.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
