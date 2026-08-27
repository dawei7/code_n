# Guided Example: Find the Missing IDs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Customers": [{"customer_id": 1, "customer_name": "Customer1"}]}}`
- **Required output:** `{"columns": ["ids"], "rows": []}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Customers`

The objective is to compute `{"columns": ["ids"], "rows": []}` from `{"tables": {"Customers": [{"customer_id": 1, "customer_name": "Customer1"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Generate the bounded candidate domain

The largest customer ID is guaranteed not to exceed 100. The recursive common table expression `t` generates integers from one through 100:

- the anchor row is `SELECT 1 AS n`;
- the recursive member selects `n + 1` while `n < 100`.

When `n = 99`, it generates 100. When `n = 100`, the condition fails and recursion stops. The CTE therefore provides a complete fixed candidate domain without requiring a permanent numbers table.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Customers": [{"customer_id": 1, "customer_name": "Customer1"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Keep only values below the current maximum

The first outer predicate is:

`n < (SELECT MAX(customer_id) FROM Customers)`.

The requested range includes the maximum itself, but that maximum is necessarily present in `Customers` by definition. It can never be a missing ID. Excluding it with strict `<` rather than generating it for a later membership rejection does not change the missing-ID set.

Values greater than the maximum are excluded because they lie outside the requested interval.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first outer predicate is:

`n < (SELECT MAX(customer_id)... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Remove identifiers that exist

The second predicate is:

`n NOT IN (SELECT customer_id FROM Customers)`.

For every generated candidate below the maximum, this keeps it only when no customer row has that identifier. Since `customer_id` is the table’s unique identifier and is treated as a concrete key, each present ID is removed regardless of customer name.

The query selects `n AS ids` to give the single output column its required name.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["ids"], "rows": []}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Customers": [{"customer_id": 1, "customer_name": "Customer1"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["ids"], "rows": []}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recursive CTE stopping at the actual maximum:*:** - **Recursive CTE stopping at the actual maximum:** Seed one and recurse while `n < MAX(customer_id)` through a prepared bound, avoiding generation beyond the needed range.
- **Permanent numbers table:** It is efficient and reusable in production schemas but adds an external dependency.
- **`NOT EXISTS`:** A correlated anti-join avoids `NOT IN` null hazards and expresses absence directly.
- **Left anti-join:** Left-join candidates to customers and keep rows with a null matched key.
- **Window-gap expansion:** Use `LEAD` to identify gaps and a number generator to expand them; this is more complex for a maximum of only 100.
- **Maximum ID equals one:** The strict `n < max` predicate keeps no candidates, correctly returning an empty set.
- **No gaps:** Every candidate below the maximum is removed by membership, producing no rows.
- **Gap immediately before maximum:** It is below the maximum and absent, so it is returned.
- **ID 100 as maximum:** The CTE includes 100, though the strict predicate tests only one through 99; 100 is known present.
- **Maximum itself:** It never needs to be returned because being the maximum proves it exists.
- **Nullable IDs:** `NOT IN` would be unsafe; the key contract is required.
- **Empty customer table:** `MAX` would be null and no candidate would pass. The task’s notion of a present maximum implicitly assumes data exists.
- **Missing explicit ordering:** Add `ORDER BY ids ASC` for guaranteed compliance; generation order alone is not a SQL ordering contract.
- **Hard-coded domain bound:** It is valid only because the reference guarantees a maximum no larger than 100.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((m+c)\log(c+1))$. Let $C$ be the number of customer rows and $M=\max(\texttt{customer_id})$, with $M\le100$.
- **Auxiliary Space Complexity:** $O(m+c)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
