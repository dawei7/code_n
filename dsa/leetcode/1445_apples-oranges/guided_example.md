# Guided Example: Apples & Oranges

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Sales": {"columns": ["sale_date", "fruit", "sold_num"], "rows": []}}}`
- **Required output:** `{"columns": ["sale_date", "diff"], "rows": []}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Sales`

The objective is to compute `{"columns": ["sale_date", "diff"], "rows": []}` from `{"tables": {"Sales": {"columns": ["sale_date", "fruit", "sold_num"], "rows": []}}}` while avoiding redundant calculations and unnecessary overhead.

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

**Turn subtraction into signed addition.** The required value for each date is apples sold minus oranges sold. SQL aggregation works especially naturally with addition, so the query changes the sign of each orange quantity before summing:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Sales": {"columns": ["sale_date", "fruit", "sold_num"], "rows": []}}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- An apples row contributes `sold_num`.
- An oranges row contributes `-sold_num`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | - An apples row contributes `sold_num`.
- An oranges row con... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

For one date, adding those signed contributions produces exactly `apples - oranges`. This is sometimes called conditional aggregation: a condition decides how each row contributes to an aggregate for its group.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["sale_date", "diff"], "rows": []}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Sales": {"columns": ["sale_date", "fruit", "sold_num"], "rows": []}}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["sale_date", "diff"], "rows": []}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **SUM with CASE WHEN:** `SUM(CASE WHEN fruit = ':** - **SUM with CASE WHEN:** `SUM(CASE WHEN fruit = 'apples' THEN sold_num ELSE -sold_num END)` expresses the same signed aggregation in standard SQL style. The stored query uses MySQL's shorter `IF` function.
- **Explicit orange test:** A defensive version can return `-sold_num` only for oranges and zero for any other fruit. That is useful in a broader schema, but the problem guarantees exactly the relevant categories.
- **Self-join by date:** Join an apples alias to an oranges alias and subtract their quantities. It is intuitive, but it references the table twice and can lose dates if one category is missing unless outer joins and null handling are added.
- **Separate filtered subqueries:** Build one apple relation and one orange relation, then join on `sale_date`. This makes the two values visually explicit but is more machinery than conditional aggregation needs.
- **Pivot-style aggregation:** Compute separate conditional sums for apples and oranges and subtract them afterward. It generalizes well when both category totals must also be displayed, but the requested output needs only their difference.
- **Equal daily sales:** Positive and negative contributions cancel, yielding zero rather than a missing row.
- **More oranges than apples:** The result is negative. Applying `ABS` would be wrong because the requested difference is directional.
- **Zero sold quantity:** A zero contributes nothing but its date still belongs to a group and must appear in the result.
- **Only an apples row on a date:** The query returns the apple quantity, effectively subtracting zero. This is sensible even if the dataset does not require missing categories.
- **Only an oranges row on a date:** Its signed contribution produces a negative difference, again behaving as if missing apple sales were zero.
- **Unexpected fruit outside the contract:** The false branch would subtract it. The solution intentionally relies on the schema guarantee that rows describe apples or oranges only.
- **Duplicate category rows outside the contract:** `SUM` would total them correctly by category sign, although their presence would violate the declared composite primary key.
- **Chronological ordering:** Sorting the `date` value directly gives chronological order. Sorting a custom display string could produce a different order and is unnecessary.
- **Ordinal references:** `GROUP BY 1` and `ORDER BY 1` both mean `sale_date` only because it is the first selected expression. Reordering the `SELECT` list would require updating those ordinals.
- **Exact output name:** `AS diff` supplies the required result-column name. Omitting or changing the alias could make an otherwise correct calculation fail the expected schema.
- **No recorded rows:** The aggregate query produces no date groups and therefore an empty result. It does not invent calendar dates absent from `Sales`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(D)$. Let `R` be the number of rows in `Sales` and `D` the number of distinct sale dates. A standard aggregate plan scans the `R` rows once and maintains a group accumulator for each date, taking expected `O(R)` time with hash aggregation and `O(D)` grouping memory.
- **Auxiliary Space Complexity:** $O(D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
