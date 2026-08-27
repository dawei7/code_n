# Guided Example: Find Customers With Positive Revenue this Year

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Customers": [{"customer_id": 5, "year": 2021, "revenue": 0}]}}`
- **Required output:** `{"columns": ["customer_id"], "rows": []}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Customers`

The objective is to compute `{"columns": ["customer_id"], "rows": []}` from `{"tables": {"Customers": [{"customer_id": 5, "year": 2021, "revenue": 0}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The requested condition is entirely row-local

Each `Customers` row already contains the three facts needed:

- which customer it describes;
- which year it belongs to;
- that customer's revenue for the year.

The query needs no aggregation or join. It filters rows using both required predicates and projects only `customer_id`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Customers": [{"customer_id": 5, "year": 2021, "revenue": 0}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Filter to the requested year

The first condition is `year = '2021'`.

Column `year` has integer type, while the exact query writes 2021 as a quoted string literal. In MySQL, type coercion converts this numeric string for comparison, so it matches integer year 2021.

Writing `year = 2021` without quotes would express the schema type more directly and portably, but the protected source's comparison is correct in its MySQL environment.

Rows from every other year are rejected regardless of revenue. A customer with positive revenue in 2020 but no 2021 row must not be returned.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first condition is `year = '2021'`.

Column `year` has i... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Require strictly positive revenue

The second condition is `revenue > 0`.

Strict inequality matters:

- positive values qualify;
- zero does not;
- negative values do not.

The source explicitly notes that revenue may be negative, so testing only that revenue is nonzero would be incorrect.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["customer_id"], "rows": []}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Customers": [{"customer_id": 5, "year": 2021, "revenue": 0}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["customer_id"], "rows": []}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Unquoted numeric literal:** `year = 2021` avoi:** - **Unquoted numeric literal:** `year = 2021` avoids relying on MySQL string-to-integer coercion.
- **`BETWEEN 1 AND ...` for revenue:** It is unnecessary; `> 0` directly states strict positivity.
- **Aggregate by customer:** It could accidentally mix years and is unnecessary because each customer-year row is unique.
- **`DISTINCT customer_id`:** It is redundant after filtering one year under the composite primary key.
- **Positive revenue in another year:** It does not qualify without a positive 2021 row.
- **Negative 2021 revenue:** It is explicitly excluded.
- **Zero 2021 revenue:** It is not positive and is excluded.
- **Missing 2021 row:** The customer produces no result.
- **Multiple historical rows:** Only the 2021 row is tested.
- **Composite primary key:** It prevents duplicate output IDs for the same year.
- **Null revenue:** The schema does not describe nulls; if present, `revenue > 0` would evaluate unknown and exclude it.
- **Any result order:** No sorting is required.
- **Projection:** Only `customer_id` is returned, exactly matching the requested table.
- **Index dependence:** Performance may improve with a year-leading index without changing query semantics.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r)$. Let $r$ be the number of rows in `Customers` and $o$ the number of output rows.
- **Auxiliary Space Complexity:** $O(o)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
