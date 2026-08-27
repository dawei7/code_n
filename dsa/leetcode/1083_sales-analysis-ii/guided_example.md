# Guided Example: Sales Analysis II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Product": [{"product_id": 1, "product_name": "S8", "unit_price": 1000}, {"product_id": 2, "product_name": "G4", "unit_price": 800}, {"product_id": 3, "product_name": "iPhone", "unit_price": 1400}], "Sales": [{"seller_id": 1, "product_id": 1, "buyer_id": 1, "sale_date": "2019-01-21", "quantity": 2, "price": 2000}, {"seller_id": 1, "product_id": 2, "buyer_id": 2, "sale_date": "2019-02-17", "quantity": 1, "price": 800}, {"seller_id": 2, "product_id": 1, "buyer_id": 3, "sale_date": "2019-06-02", "quantity": 1, "price": 800}, {"seller_id": 3, "product_id": 3, "buyer_id": 3, "sale_date": "2019-05-13", "quantity": 2, "price": 2800}]}}`
- **Required output:** `{"columns": ["buyer_id"], "rows": [[1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Product`

The objective is to compute `{"columns": ["buyer_id"], "rows": [[1]]}` from `{"tables": {"Product": [{"product_id": 1, "product_name": "S8", "unit_price": 1000}, {"product_id": 2, "product_name": "G4", "unit_price": 800}, {"product_id": 3, "product_name": "iPhone", "unit_price": 1400}], "Sales": [{"seller_id": 1, "product_id": 1, "buyer_id": 1, "sale_date": "2019-01-21", "quantity": 2, "price": 2000}, {"seller_id": 1, "product_id": 2, "buyer_id": 2, "sale_date": "2019-02-17", "quantity": 1, "price": 800}, {"seller_id": 2, "product_id": 1, "buyer_id": 3, "sale_date": "2019-06-02", "quantity": 1, "price": 800}, {"seller_id": 3, "product_id": 3, "buyer_id": 3, "sale_date": "2019-05-13", "quantity": 2, "price": 2800}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Resolve product identifiers to names

`Sales` records what each buyer purchased using `product_id`, while the conditions are stated using names `S8` and `iPhone`.

The query joins:



`Sales.product_id` is a foreign key and `Product.product_id` is a primary key. Every sale matches exactly one product row, so the join attaches one trustworthy `product_name` without losing or multiplying sales.

Other product attributes, such as unit price, do not affect eligibility.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Product": [{"product_id": 1, "product_name": "S8", "unit_price": 1000}, {"product_id": 2, "product_name": "G4", "unit_price": 800}, {"product_id": 3, "product_name": "iPhone", "unit_price": 1400}], "Sales": [{"seller_id": 1, "product_id": 1, "buyer_id": 1, "sale_date": "2019-01-21", "quantity": 2, "price": 2000}, {"seller_id": 1, "product_id": 2, "buyer_id": 2, "sale_date": "2019-02-17", "quantity": 1, "price": 800}, {"seller_id": 2, "product_id": 1, "buyer_id": 3, "sale_date": "2019-06-02", "quantity": 1, "price": 800}, {"seller_id": 3, "product_id": 3, "buyer_id": 3, "sale_date": "2019-05-13", "quantity": 2, "price": 2800}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Group complete purchase history by buyer

The query selects `buyer_id` and uses:



One refers to the first select-list expression, so this is equivalent to `GROUP BY buyer_id`.

Every joined purchase row for one buyer enters the same group. This is the right grain because eligibility depends on whether anything in the buyer's entire history matches either product name.

Repeated sales remain inside the group but cannot create repeated result rows. Grouping returns at most one row per buyer.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The query selects `buyer_id` and uses:



One refers to the ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Turn name comparisons into numeric indicators

In MySQL, a Boolean equality expression used numerically evaluates to one when true and zero when false.

Therefore:



is one for an S8 purchase and zero for every other product.

Summing it:



counts how many S8 sale rows the buyer has. The exact count is not required, but whether it is positive establishes existence.

The same technique counts iPhone rows:



Purchases of G4 or any other product contribute zero to both sums and do not affect the decision.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["buyer_id"], "rows": [[1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Product": [{"product_id": 1, "product_name": "S8", "unit_price": 1000}, {"product_id": 2, "product_name": "G4", "unit_price": 800}, {"product_id": 3, "product_name": "iPhone", "unit_price": 1400}], "Sales": [{"seller_id": 1, "product_id": 1, "buyer_id": 1, "sale_date": "2019-01-21", "quantity": 2, "price": 2000}, {"seller_id": 1, "product_id": 2, "buyer_id": 2, "sale_date": "2019-02-17", "quantity": 1, "price": 800}, {"seller_id": 2, "product_id": 1, "buyer_id": 3, "sale_date": "2019-06-02", "quantity": 1, "price": 800}, {"seller_id": 3, "product_id": 3, "buyer_id": 3, "sale_date": "2019-05-13", "quantity": 2, "price": 2800}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["buyer_id"], "rows": [[1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **NOT EXISTS:** Select distinct S8 buyers and re:** - **NOT EXISTS:** Select distinct S8 buyers and reject any for whom an iPhone purchase exists. This often expresses the English condition directly.
- **NOT IN:** It works because `buyer_id` is guaranteed non-null, but `NOT EXISTS` is generally safer when nulls are possible.
- **Set difference:** Build the set of S8 buyers and subtract the set of iPhone buyers.
- **Conditional CASE aggregates:** `SUM(CASE WHEN ... THEN 1 ELSE 0 END)` is more portable across SQL dialects than MySQL Boolean arithmetic.
- **WHERE only S8:** It is incorrect because it hides iPhone evidence before grouping.
- **Buyer with several S8 purchases:** The first sum is greater than one and still passes.
- **Buyer with S8 and iPhone:** The iPhone sum is positive, so the buyer is rejected.
- **Buyer with only unrelated products:** The S8 sum is zero, so the buyer is rejected.
- **Repeated Sales rows:** Counts increase but group output remains one buyer row.
- **Product names:** Matching is exact and case-sensitive according to the database collation rules in use.
- **Non-null buyer identifier:** Every grouped row has a real buyer key.
- **Any output order:** No `ORDER BY` is required.
- **GROUP BY 1:** It refers to selected `buyer_id`; naming the column explicitly would be equivalent.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let `P` be the number of product rows and `R` the number of sales rows.
- **Auxiliary Space Complexity:** $O(P+R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
