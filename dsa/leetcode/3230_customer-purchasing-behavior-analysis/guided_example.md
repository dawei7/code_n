# Guided Example: Customer Purchasing Behavior Analysis

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"transactions": [{"transaction_id": 1, "customer_id": 101, "product_id": 1, "transaction_date": "2023-01-01", "amount": 100}, {"transaction_id": 2, "customer_id": 101, "product_id": 2, "transaction_date": "2023-01-15", "amount": 150}, {"transaction_id": 3, "customer_id": 102, "product_id": 1, "transaction_date": "2023-01-01", "amount": 100}, {"transaction_id": 4, "customer_id": 102, "product_id": 3, "transaction_date": "2023-01-22", "amount": 200}, {"transaction_id": 5, "customer_id": 101, "product_id": 3, "transaction_date": "2023-02-10", "amount": 200}], "products": [{"product_id": 1, "category": "A", "price": 100}, {"product_id": 2, "category": "B", "price": 150}, {"product_id": 3, "category": "C", "price": 200}]}}`
- **Required output:** `{"columns": ["customer_id", "total_amount", "transaction_count", "unique_categories", "avg_transaction_amount", "top_category", "loyalty_score"], "rows": [[101, 450, 3, 3, 150, "C", 34.5], [102, 300, 2, 2, 150, "C", 23]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Transactions`

The objective is to compute `{"columns": ["customer_id", "total_amount", "transaction_count", "unique_categories", "avg_transaction_amount", "top_category", "loyalty_score"], "rows": [[101, 450, 3, 3, 150, "C", 34.5], [102, 300, 2, 2, 150, "C", 23]]}` from `{"tables": {"transactions": [{"transaction_id": 1, "customer_id": 101, "product_id": 1, "transaction_date": "2023-01-01", "amount": 100}, {"transaction_id": 2, "customer_id": 101, "product_id": 2, "transaction_date": "2023-01-15", "amount": 150}, {"transaction_id": 3, "customer_id": 102, "product_id": 1, "transaction_date": "2023-01-01", "amount": 100}, {"transaction_id": 4, "customer_id": 102, "product_id": 3, "transaction_date": "2023-01-22", "amount": 200}, {"transaction_id": 5, "customer_id": 101, "product_id": 3, "transaction_date": "2023-02-10", "amount": 200}], "products": [{"product_id": 1, "category": "A", "price": 100}, {"product_id": 2, "category": "B", "price": 150}, {"product_id": 3, "category": "C", "price": 200}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Enrich every transaction with its product category.** CTE `T` joins `Transactions` to `Products` by `product_id`. Each resulting row contains transaction facts—customer, date, amount—and the corresponding category. The product price is available through `SELECT *` but is not used; loyalty is based on actual transaction amount.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"transactions": [{"transaction_id": 1, "customer_id": 101, "product_id": 1, "transaction_date": "2023-01-01", "amount": 100}, {"transaction_id": 2, "customer_id": 101, "product_id": 2, "transaction_date": "2023-01-15", "amount": 150}, {"transaction_id": 3, "customer_id": 102, "product_id": 1, "transaction_date": "2023-01-01", "amount": 100}, {"transaction_id": 4, "customer_id": 102, "product_id": 3, "transaction_date": "2023-01-22", "amount": 200}, {"transaction_id": 5, "customer_id": 101, "product_id": 3, "transaction_date": "2023-02-10", "amount": 200}], "products": [{"product_id": 1, "category": "A", "price": 100}, {"product_id": 2, "category": "B", "price": 150}, {"product_id": 3, "category": "C", "price": 200}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The inner join relies on the product ID relationship being complete. A transaction whose product has no catalog row would disappear.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The inner join relies on the product ID relationship being c... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Find category statistics at customer-category grain.** CTE `P` groups `T` by `customer_id` and `category`. It computes:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["customer_id", "total_amount", "transaction_count", "unique_categories", "avg_transaction_amount", "top_category", "loyalty_score"], "rows": [[101, 450, 3, 3, 150, "C", 34.5], [102, 300, 2, 2, 150, "C", 23]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"transactions": [{"transaction_id": 1, "customer_id": 101, "product_id": 1, "transaction_date": "2023-01-01", "amount": 100}, {"transaction_id": 2, "customer_id": 101, "product_id": 2, "transaction_date": "2023-01-15", "amount": 150}, {"transaction_id": 3, "customer_id": 102, "product_id": 1, "transaction_date": "2023-01-01", "amount": 100}, {"transaction_id": 4, "customer_id": 102, "product_id": 3, "transaction_date": "2023-01-22", "amount": 200}, {"transaction_id": 5, "customer_id": 101, "product_id": 3, "transaction_date": "2023-02-10", "amount": 200}], "products": [{"product_id": 1, "category": "A", "price": 100}, {"product_id": 2, "category": "B", "price": 150}, {"product_id": 3, "category": "C", "price": 200}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["customer_id", "total_amount", "transaction_count", "unique_categories", "avg_transaction_amount", "top_category", "loyalty_score"], "rows": [[101, 450, 3, 3, 150, "C", 34.5], [102, 300, 2, 2, 150, "C", 23]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`ROW_NUMBER` with a deterministic final key:**:** - **`ROW_NUMBER` with a deterministic final key:** Order by count, latest date, then category (or another specified key) and keep row one. This prevents multiple top rows and aggregate multiplication.
- **Aggregate customer totals before joining the winner:** Build one CTE for customer metrics and another for exactly one top category, then join their one-row-per-customer results. This isolates totals from category-ranking multiplicity.
- **`DENSE_RANK`:** It has the same rank-one tie problem as `RANK` and does not fix the defect.
- **One transaction:** Its category is top, total equals average, and transaction count is one.
- **Frequency tie with different dates:** The latest category uniquely ranks first as intended.
- **Tie on count and latest date:** Multiple rank-one rows multiply final aggregates in the exact source.
- **Several products in one category:** They contribute to the same customer-category frequency.
- **Repeated product purchases:** Every transaction counts; the metric is purchase frequency, not distinct products.
- **Unique categories:** `COUNT(DISTINCT t.category)` avoids counting repeated purchases as new categories.
- **Catalog price:** It is correctly ignored because reported spending uses transaction `amount`.
- **Missing product row:** Inner join removes the transaction, relying on referential integrity.
- **Rounding:** Total, average, and loyalty are rounded independently after their underlying aggregates.
- **Output ties:** Equal loyalty scores are ordered by ascending customer ID.
- **Positional order references:** `7` and `1` depend on select-list layout and are less maintainable than explicit aliases.
- **Strict grouping mode:** Selecting top category outside `GROUP BY` may rely on permissive MySQL behavior or inferred functional dependence.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(t)$. Let $t$ be the transaction count and $g$ the number of customer-category groups. The product join is typically $O(t)$ expected with indexed product IDs. Grouping into `P` can be $O(t)$ by hashing or $O(t\log t)$ by sorting. Window ranking requires ordering $g$ rows within customer partitions, bounded by $O(g\log g)$. The final join/group and result ordering add linear-to-sort costs.
- **Auxiliary Space Complexity:** $O(t)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
