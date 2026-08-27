# Guided Example: Customers Who Bought Products A and B but Not C

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Customers": [{"customer_id": 1, "customer_name": "Daniel"}, {"customer_id": 2, "customer_name": "Diana"}, {"customer_id": 3, "customer_name": "Elizabeth"}, {"customer_id": 4, "customer_name": "Jhon"}], "Orders": [{"order_id": 10, "customer_id": 1, "product_name": "A"}, {"order_id": 20, "customer_id": 1, "product_name": "B"}, {"order_id": 30, "customer_id": 1, "product_name": "D"}, {"order_id": 40, "customer_id": 1, "product_name": "C"}, {"order_id": 50, "customer_id": 2, "product_name": "A"}, {"order_id": 60, "customer_id": 3, "product_name": "A"}, {"order_id": 70, "customer_id": 3, "product_name": "B"}, {"order_id": 80, "customer_id": 3, "product_name": "D"}, {"order_id": 90, "customer_id": 4, "product_name": "C"}]}}`
- **Required output:** `{"columns": ["customer_id", "customer_name"], "rows": [[3, "Elizabeth"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Customers`

The objective is to compute `{"columns": ["customer_id", "customer_name"], "rows": [[3, "Elizabeth"]]}` from `{"tables": {"Customers": [{"customer_id": 1, "customer_name": "Daniel"}, {"customer_id": 2, "customer_name": "Diana"}, {"customer_id": 3, "customer_name": "Elizabeth"}, {"customer_id": 4, "customer_name": "Jhon"}], "Orders": [{"order_id": 10, "customer_id": 1, "product_name": "A"}, {"order_id": 20, "customer_id": 1, "product_name": "B"}, {"order_id": 30, "customer_id": 1, "product_name": "D"}, {"order_id": 40, "customer_id": 1, "product_name": "C"}, {"order_id": 50, "customer_id": 2, "product_name": "A"}, {"order_id": 60, "customer_id": 3, "product_name": "A"}, {"order_id": 70, "customer_id": 3, "product_name": "B"}, {"order_id": 80, "customer_id": 3, "product_name": "D"}, {"order_id": 90, "customer_id": 4, "product_name": "C"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Create one group per customer

The output needs customer identity and name, while qualification depends on all orders belonging to that customer. The query starts from `Customers` and left-joins `Orders` by their shared `customer_id`. This expands each customer into zero or more joined order rows.

`GROUP BY 1` groups by the first selected expression, `customer_id`. Since customer ID is unique in `Customers`, `customer_name` is functionally determined by the group and can be selected alongside it.

The group is the right unit of reasoning: the query must answer whether products A, B, and C occur anywhere in the complete purchase history, not whether one individual order row qualifies.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Customers": [{"customer_id": 1, "customer_name": "Daniel"}, {"customer_id": 2, "customer_name": "Diana"}, {"customer_id": 3, "customer_name": "Elizabeth"}, {"customer_id": 4, "customer_name": "Jhon"}], "Orders": [{"order_id": 10, "customer_id": 1, "product_name": "A"}, {"order_id": 20, "customer_id": 1, "product_name": "B"}, {"order_id": 30, "customer_id": 1, "product_name": "D"}, {"order_id": 40, "customer_id": 1, "product_name": "C"}, {"order_id": 50, "customer_id": 2, "product_name": "A"}, {"order_id": 60, "customer_id": 3, "product_name": "A"}, {"order_id": 70, "customer_id": 3, "product_name": "B"}, {"order_id": 80, "customer_id": 3, "product_name": "D"}, {"order_id": 90, "customer_id": 4, "product_name": "C"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Turn Boolean conditions into counts

In MySQL, a comparison such as `product_name = 'A'` evaluates to one when true and zero when false. Summing it across a customer group therefore counts that customer's orders for A.

The three `HAVING` conditions express the contract directly:

- `SUM(product_name = 'A') > 0` means at least one A purchase exists.
- `SUM(product_name = 'B') > 0` means at least one B purchase exists.
- `SUM(product_name = 'C') = 0` means no C purchase exists.

Repeated A or B orders merely make a positive sum larger; the greater-than-zero test still represents presence. Other products contribute zero to all three sums and do not affect eligibility.

Using `COUNT(product_name = 'A')` would be wrong. `COUNT` counts non-null expression results, and both true and false Boolean results are non-null. It would count almost every order rather than only A orders.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | In MySQL, a comparison such as `product_name = 'A'` evaluate... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why filtering belongs in `HAVING`

`WHERE` filters individual rows before grouping. If C rows were removed there, a customer who did buy C could appear to have no C purchase and qualify incorrectly. `HAVING` runs after aggregation and can inspect the complete group's three conditional counts.

Similarly, requiring A and B in a row-level `WHERE` cannot work because one order row has only one `product_name`. The conditions describe the set of rows together.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["customer_id", "customer_name"], "rows": [[3, "Elizabeth"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Customers": [{"customer_id": 1, "customer_name": "Daniel"}, {"customer_id": 2, "customer_name": "Diana"}, {"customer_id": 3, "customer_name": "Elizabeth"}, {"customer_id": 4, "customer_name": "Jhon"}], "Orders": [{"order_id": 10, "customer_id": 1, "product_name": "A"}, {"order_id": 20, "customer_id": 1, "product_name": "B"}, {"order_id": 30, "customer_id": 1, "product_name": "D"}, {"order_id": 40, "customer_id": 1, "product_name": "C"}, {"order_id": 50, "customer_id": 2, "product_name": "A"}, {"order_id": 60, "customer_id": 3, "product_name": "A"}, {"order_id": 70, "customer_id": 3, "product_name": "B"}, {"order_id": 80, "customer_id": 3, "product_name": "D"}, {"order_id": 90, "customer_id": 4, "product_name": "C"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["customer_id", "customer_name"], "rows": [[3, "Elizabeth"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Three `EXISTS` predicates:** Require an A orde:** - **Three `EXISTS` predicates:** Require an A order, require a B order, and reject an existing C order. With indexes this is clear and can short-circuit, though it repeats correlated lookups.
- **Set intersection and difference:** Build customer-ID sets for A, B, and C, then compute $A\cap B\setminus C$. It expresses the set logic directly but needs joins to recover names.
- **Inner join:** It is sufficient for the final answer because qualification requires orders, but the left join makes customer preservation explicit.
- **Filter C in `WHERE`:** This is incorrect because it erases evidence that should disqualify a customer.
- **Repeated A or B purchases:** Positive-sum conditions remain true and output still has one grouped row.
- **Repeated C purchases:** Any positive C count disqualifies the customer.
- **Other products:** Their comparisons are all false and they do not change the three conditions.
- **No orders:** Null aggregate comparisons do not pass, so the customer is excluded.
- **Only A or only B:** One required positive sum fails.
- **A, B, and C:** The C-zero condition fails even though both required products exist.
- **Unique customer ID:** It makes the selected name functionally dependent on `GROUP BY customer_id`.
- **Positional clauses:** `GROUP BY 1` and `ORDER BY 1` refer to `customer_id`; explicit column names are safer during future edits.
- **Required order:** The final sort is necessary because grouping alone does not promise customer-ID order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C + O + R)$. Let $C$ be the customer count, $O$ the order count, and $R$ the result size. Under a standard hash-join and hash-aggregation plan, scanning both inputs and updating customer aggregates takes expected $O(C+O)$ time. Producing results costs $O(R)$. This matches the manifest's $O(C+O+R)$ logical work.
- **Auxiliary Space Complexity:** $O(C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
