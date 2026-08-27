# Guided Example: Average Selling Price

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Prices": [{"product_id": 1, "start_date": "2019-02-17", "end_date": "2019-02-28", "price": 5}, {"product_id": 1, "start_date": "2019-03-01", "end_date": "2019-03-22", "price": 20}, {"product_id": 2, "start_date": "2019-02-01", "end_date": "2019-02-20", "price": 15}, {"product_id": 2, "start_date": "2019-02-21", "end_date": "2019-03-31", "price": 30}], "UnitsSold": [{"product_id": 1, "purchase_date": "2019-02-25", "units": 100}, {"product_id": 1, "purchase_date": "2019-03-01", "units": 15}, {"product_id": 2, "purchase_date": "2019-02-10", "units": 200}, {"product_id": 2, "purchase_date": "2019-03-22", "units": 30}]}}`
- **Required output:** `{"columns": ["product_id", "average_price"], "rows": [[1, 6.96], [2, 16.96]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Prices`

The objective is to compute `{"columns": ["product_id", "average_price"], "rows": [[1, 6.96], [2, 16.96]]}` from `{"tables": {"Prices": [{"product_id": 1, "start_date": "2019-02-17", "end_date": "2019-02-28", "price": 5}, {"product_id": 1, "start_date": "2019-03-01", "end_date": "2019-03-22", "price": 20}, {"product_id": 2, "start_date": "2019-02-01", "end_date": "2019-02-20", "price": 15}, {"product_id": 2, "start_date": "2019-02-21", "end_date": "2019-03-31", "price": 30}], "UnitsSold": [{"product_id": 1, "purchase_date": "2019-02-25", "units": 100}, {"product_id": 1, "purchase_date": "2019-03-01", "units": 15}, {"product_id": 2, "purchase_date": "2019-02-10", "units": 200}, {"product_id": 2, "purchase_date": "2019-03-22", "units": 30}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A simple average of price periods would be wrong

Each price applies during a date interval, and different numbers of units may be sold under different prices. The required average is weighted by units:

\[
\text{average price}
=
\frac{\sum(\text{price}\cdot\text{units})}
{\sum\text{units}}.
\]

A period with 100 units sold must contribute more weight than one with 15 units. The query joins every sale to the price interval active on its purchase date, then computes this weighted fraction per product.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Prices": [{"product_id": 1, "start_date": "2019-02-17", "end_date": "2019-02-28", "price": 5}, {"product_id": 1, "start_date": "2019-03-01", "end_date": "2019-03-22", "price": 20}, {"product_id": 2, "start_date": "2019-02-01", "end_date": "2019-02-20", "price": 15}, {"product_id": 2, "start_date": "2019-02-21", "end_date": "2019-03-31", "price": 30}], "UnitsSold": [{"product_id": 1, "purchase_date": "2019-02-25", "units": 100}, {"product_id": 1, "purchase_date": "2019-03-01", "units": 15}, {"product_id": 2, "purchase_date": "2019-02-10", "units": 200}, {"product_id": 2, "purchase_date": "2019-03-22", "units": 30}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Match sales by product and inclusive date range

The join condition has two parts:

- `p.product_id = u.product_id` ensures the price and sale belong to the same product.
- `purchase_date BETWEEN start_date AND end_date` ensures the sale date lies inside that price period, including both endpoints.

Price periods for one product do not overlap. Therefore, one sale matches at most one price row. This prevents the same sale from being multiplied by two prices.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The join condition has two parts:

- `p.product_id = u.produ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the query starts from `Prices` with a left join

The output must include a product even if it has no sold units. A `LEFT JOIN` preserves every price-side product row when no sale matches, filling sale columns with null.

If a product has several price periods and no sales, several null-extended rows may exist before grouping, but they all belong to the same `product_id` and produce one output group.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product_id", "average_price"], "rows": [[1, 6.96], [2, 16.96]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Prices": [{"product_id": 1, "start_date": "2019-02-17", "end_date": "2019-02-28", "price": 5}, {"product_id": 1, "start_date": "2019-03-01", "end_date": "2019-03-22", "price": 20}, {"product_id": 2, "start_date": "2019-02-01", "end_date": "2019-02-20", "price": 15}, {"product_id": 2, "start_date": "2019-02-21", "end_date": "2019-03-31", "price": 30}], "UnitsSold": [{"product_id": 1, "purchase_date": "2019-02-25", "units": 100}, {"product_id": 1, "purchase_date": "2019-03-01", "units": 15}, {"product_id": 2, "purchase_date": "2019-02-10", "units": 200}, {"product_id": 2, "purchase_date": "2019-03-22", "units": 30}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product_id", "average_price"], "rows": [[1, 6.96], [2, 16.96]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Correlated price lookup per sale:** Find the m:** - **Correlated price lookup per sale:** Find the matching price row for every sale, then aggregate. It can be clear but may execute repeated searches without good indexes.
- **Pre-aggregate sales by product, date, and units:** Useful when many identical sale rows exist operationally, but duplicates represent additional units and must be summed, not discarded.
- **Use `AVG(price)`:** Incorrect because it weights price periods rather than units sold.
- **Average row revenue:** Also incorrect; the denominator must be total units.
- **No sold units:** Left join plus `COALESCE` returns zero.
- **Sale on a boundary date:** `BETWEEN` is inclusive, so the appropriate period matches.
- **Nonoverlapping periods:** This guarantee prevents one sale from joining to multiple prices.
- **Duplicate sales rows:** Their units and revenue are both counted, preserving the weighted unit price.
- **Dialect-specific division:** Engines with integer division require a decimal cast before division.
- **Rounding stage:** Round the final quotient, not individual contributions.
- **Any output order:** No explicit sort is necessary.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r)$. Let \(r\) be the combined number of price and sales rows. With useful indexes on product and dates and an efficient join/group plan, the logical processing can be near \(O(r)\), matching the manifest’s abstraction.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
