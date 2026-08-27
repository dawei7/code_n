# Guided Example: Drop Type 1 Orders for Customers With Type 0 Orders

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Orders": [{"order_id": 1, "customer_id": 1, "order_type": 0}, {"order_id": 2, "customer_id": 1, "order_type": 0}, {"order_id": 11, "customer_id": 2, "order_type": 0}, {"order_id": 12, "customer_id": 2, "order_type": 1}, {"order_id": 21, "customer_id": 3, "order_type": 1}, {"order_id": 22, "customer_id": 3, "order_type": 0}, {"order_id": 31, "customer_id": 4, "order_type": 1}, {"order_id": 32, "customer_id": 4, "order_type": 1}]}}`
- **Required output:** `{"columns": ["order_id", "customer_id", "order_type"], "rows": [[1, 1, 0], [2, 1, 0], [11, 2, 0], [22, 3, 0], [31, 4, 1], [32, 4, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Orders`

The objective is to compute `{"columns": ["order_id", "customer_id", "order_type"], "rows": [[1, 1, 0], [2, 1, 0], [11, 2, 0], [22, 3, 0], [31, 4, 1], [32, 4, 1]]}` from `{"tables": {"Orders": [{"order_id": 1, "customer_id": 1, "order_type": 0}, {"order_id": 2, "customer_id": 1, "order_type": 0}, {"order_id": 11, "customer_id": 2, "order_type": 0}, {"order_id": 12, "customer_id": 2, "order_type": 1}, {"order_id": 21, "customer_id": 3, "order_type": 1}, {"order_id": 22, "customer_id": 3, "order_type": 0}, {"order_id": 31, "customer_id": 4, "order_type": 1}, {"order_id": 32, "customer_id": 4, "order_type": 1}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: First identify customers for whom type 1 must be suppressed

The rule is customer-wide: seeing even one type 0 order changes which rows should be reported for that customer's entire collection. A row cannot be decided by looking only at its own `order_type`.

The common table expression `T` computes the set of customers who have at least one type 0 order:

`SELECT DISTINCT customer_id FROM Orders WHERE order_type = 0`.

The `WHERE` clause selects type 0 rows, and `DISTINCT` collapses multiple such orders for the same customer into one identifier. The resulting derived table is conceptually a set of “customers with a preferred type 0 order.”

For the example:

- customers 1, 2, and 3 appear in `T` because each has at least one type 0 order;
- customer 4 does not appear because both of that customer's orders are type 1.

The main query then evaluates every original order against this set.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Orders": [{"order_id": 1, "customer_id": 1, "order_type": 0}, {"order_id": 2, "customer_id": 1, "order_type": 0}, {"order_id": 11, "customer_id": 2, "order_type": 0}, {"order_id": 12, "customer_id": 2, "order_type": 1}, {"order_id": 21, "customer_id": 3, "order_type": 1}, {"order_id": 22, "customer_id": 3, "order_type": 0}, {"order_id": 31, "customer_id": 4, "order_type": 1}, {"order_id": 32, "customer_id": 4, "order_type": 1}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Express the two ways an order may be kept

The main predicate is

`order_type = 0 OR NOT EXISTS (...)`.

An order is returned when either of these conditions holds:

1. The order itself has type 0. Such orders must always be reported, whether the customer has one or many.
2. No row in `T` has the same `customer_id`. This means the customer has no type 0 order at all, so all of that customer's orders must be reported.

The correlated subquery

`SELECT 1 FROM T AS t WHERE t.customer_id = o.customer_id`

asks only whether a matching customer exists. The selected literal 1 has no special value; `EXISTS` cares only whether the subquery produces at least one row. `NOT EXISTS` reverses that answer.

The outer alias `o` distinguishes the current `Orders` row from the CTE alias `t` and supplies the current customer's identifier to the correlated test.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The main predicate is

`order_type = 0 OR NOT EXISTS (...)`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Understand the predicate for each customer category

Suppose a customer has at least one type 0 order. That customer appears in `T`.

- Each of the customer's type 0 rows passes the left side of the `OR` and is returned.
- Each type 1 row fails `order_type = 0`. Its matching row in `T` makes `NOT EXISTS` false, so it is excluded.

Now suppose a customer has no type 0 order. Under the problem's two-type guarantee, all of their orders are type 1. The customer is absent from `T`, so `NOT EXISTS` is true for every one of those rows. All their orders are returned.

These are exactly the two rules in the statement.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["order_id", "customer_id", "order_type"], "rows": [[1, 1, 0], [2, 1, 0], [11, 2, 0], [22, 3, 0], [31, 4, 1], [32, 4, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Orders": [{"order_id": 1, "customer_id": 1, "order_type": 0}, {"order_id": 2, "customer_id": 1, "order_type": 0}, {"order_id": 11, "customer_id": 2, "order_type": 0}, {"order_id": 12, "customer_id": 2, "order_type": 1}, {"order_id": 21, "customer_id": 3, "order_type": 1}, {"order_id": 22, "customer_id": 3, "order_type": 0}, {"order_id": 31, "customer_id": 4, "order_type": 1}, {"order_id": 32, "customer_id": 4, "order_type": 1}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["order_id", "customer_id", "order_type"], "rows": [[1, 1, 0], [2, 1, 0], [11, 2, 0], [22, 3, 0], [31, 4, 1], [32, 4, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Correlated minimum order type:** Since types a:** - **Correlated minimum order type:** Since types are only 0 and 1, one could compare each row with the customer's minimum type. That requires grouping or a window computation; the explicit type 0 customer set states the rule more directly.
- **Window function:** Computing a per-customer flag such as whether any type 0 exists and filtering on it can be correct. It may retain repeated flag values on every row and is more machinery than the CTE existence test.
- **`NOT IN` subquery:** `customer_id NOT IN (...)` can express set exclusion, but null values can give surprising three-valued logic. `NOT EXISTS` is the safer existence formulation.
- **Joining `T` and testing null:** A left join followed by a null test can implement the same logic. The correlated `NOT EXISTS` avoids adding join columns and duplicate concerns to the outer rowset.
- **Omitting `DISTINCT`:** The result remains logically correct because `EXISTS` ignores multiplicity, but the CTE may carry redundant customer rows.
- **Customer with only type 0 orders:** Every row passes the first condition and is returned.
- **Customer with both types:** All type 0 rows are returned, and all type 1 rows are suppressed.
- **Customer with only type 1 orders:** The customer is absent from `T`, so all orders are returned.
- **Several type 0 orders:** They all remain in the output; the rule never asks to deduplicate orders.
- **Empty table:** The CTE and outer result are empty, which is the correct set of reported orders.
- **Any output order:** No ordering is guaranteed or required, so downstream comparison should treat rows as an unordered result set.
- **Exact two-type guarantee:** The proof uses the fact that every order is type 0 or 1. The query would also include a hypothetical other type for a customer absent from `T`, but such rows are outside the valid input domain.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N)$. Let $N$ be the number of rows in `Orders`.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
