# Guided Example: The Number of Rich Customers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Store": [{"bill_id": 6, "customer_id": 1, "amount": 549}, {"bill_id": 8, "customer_id": 1, "amount": 834}, {"bill_id": 4, "customer_id": 2, "amount": 394}, {"bill_id": 11, "customer_id": 3, "amount": 657}, {"bill_id": 13, "customer_id": 3, "amount": 257}]}}`
- **Required output:** `{"columns": ["rich_count"], "rows": [[2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Store`

The objective is to compute `{"columns": ["rich_count"], "rows": [[2]]}` from `{"tables": {"Store": [{"bill_id": 6, "customer_id": 1, "amount": 549}, {"bill_id": 8, "customer_id": 1, "amount": 834}, {"bill_id": 4, "customer_id": 2, "amount": 394}, {"bill_id": 11, "customer_id": 3, "amount": 657}, {"bill_id": 13, "customer_id": 3, "amount": 257}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Filter qualifying bills before counting customers

A customer is considered rich if at least one of their bills has an amount strictly greater than 500. The result must count customers, not bills. A customer with several qualifying bills still contributes only one to the answer.

The SQL query handles these two ideas in the natural order:

1. `WHERE amount > 500` keeps only bills that satisfy the strict threshold.
2. `COUNT(DISTINCT customer_id)` counts the different customers represented by those remaining bills.

The filter is applied logically before the aggregation. Bills of amount 500 do not qualify because “strictly greater” requires `>` rather than `>=`. Bills below the threshold are also removed. Once a row is filtered out, its customer does not influence the distinct count through that row.

For the example, the qualifying bills belong to customer 1 twice and customer 3 once. The sequence of qualifying customer identifiers is conceptually `[1, 1, 3]`. Applying `DISTINCT` reduces those identifiers to `[1, 3]`, and `COUNT` returns 2.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Store": [{"bill_id": 6, "customer_id": 1, "amount": 549}, {"bill_id": 8, "customer_id": 1, "amount": 834}, {"bill_id": 4, "customer_id": 2, "amount": 394}, {"bill_id": 11, "customer_id": 3, "amount": 657}, {"bill_id": 13, "customer_id": 3, "amount": 257}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why `DISTINCT` is essential

The table's primary key is `bill_id`, which means every bill row is unique. It does not mean `customer_id` is unique. The same customer can have many different bills, each with its own `bill_id`.

A plain `COUNT(customer_id)` after the filter would count qualifying bills. In the example, it would return 3 because customer 1 has two qualifying rows. That is not the requested number of customers.

`COUNT(DISTINCT customer_id)` first treats repeated occurrences of the same customer identifier as one distinct value, then counts those values. It precisely expresses “had at least one” because after the first qualifying bill establishes a customer's membership, further qualifying bills do not increase the count.

There is no need to group by customer and return one row per customer. The required result is a single total, and the distinct aggregate calculates it directly.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The table's primary key is `bill_id`, which means every bill... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Produce the required one-row schema

The expression is aliased with

`AS rich_count`.

This alias is part of the result contract. It names the sole output column `rich_count` rather than exposing a database-generated aggregate label.

Because the query contains an aggregate and no `GROUP BY`, it returns one summary row for the entire filtered table. If there are no bills above 500, the distinct count is 0, and the result is still one row containing zero. This is preferable to a grouped query that might return no rows when nobody qualifies.

No `ORDER BY` is needed because the result contains only one row.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["rich_count"], "rows": [[2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Store": [{"bill_id": 6, "customer_id": 1, "amount": 549}, {"bill_id": 8, "customer_id": 1, "amount": 834}, {"bill_id": 4, "customer_id": 2, "amount": 394}, {"bill_id": 11, "customer_id": 3, "amount": 657}, {"bill_id": 13, "customer_id": 3, "amount": 257}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["rich_count"], "rows": [[2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Plain `COUNT(customer_id)`:** This counts qual:** - **Plain `COUNT(customer_id)`:** This counts qualifying bill rows, so customers with multiple bills are overcounted. `DISTINCT` is necessary.
- **`GROUP BY customer_id` alone:** This yields one row per rich customer rather than the required single total. An outer count could repair it, but the direct distinct aggregate is simpler.
- **Nested grouped subquery:** Selecting qualifying customer IDs with `GROUP BY` and then counting those rows is correct, but it introduces an unnecessary query layer compared with `COUNT(DISTINCT ...)`.
- **`EXISTS` against a customer table:** If a separate complete customer table existed, an existence test could mark qualifying customers. No such table is needed here because qualifying identifiers can be obtained directly from `Store`.
- **Threshold exactly 500:** Such a bill does not qualify. Replacing `> 500` with `>= 500` changes the problem's strict boundary.
- **Several qualifying bills for one customer:** They contribute one distinct identifier and therefore one to the result.
- **Qualifying and nonqualifying bills for one customer:** The qualifying row is sufficient. Filtering individual bills before deduplication retains that customer once.
- **Only nonqualifying bills:** The filtered input is empty, but the aggregate still returns one row with `rich_count = 0`.
- **Empty table:** The same ungrouped aggregate behavior returns zero rather than no rows.
- **Unique bill identifiers:** `bill_id` prevents duplicate bill records by key, but customers may repeat. Counting bill IDs would answer a different question.
- **Null customer identifiers:** Standard `COUNT(DISTINCT ...)` ignores null. The intended data identifies customers, so no special null substitute is required.
- **Exact output alias:** The aggregate must be named `rich_count` to match the expected result schema.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B\log B)$. Let $B$ be the number of bill rows in `Store`, and let $C$ be the number of distinct customers among bills whose amount exceeds 500.
- **Auxiliary Space Complexity:** $O(C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
