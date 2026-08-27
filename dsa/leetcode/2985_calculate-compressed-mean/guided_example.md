# Guided Example: Calculate Compressed Mean

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Orders": [{"order_id": 10, "item_count": 1, "order_occurrences": 500}, {"order_id": 11, "item_count": 2, "order_occurrences": 1000}, {"order_id": 12, "item_count": 3, "order_occurrences": 800}, {"order_id": 13, "item_count": 4, "order_occurrences": 1000}]}}`
- **Required output:** `{"columns": ["average_items_per_order"], "rows": [[2.7]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Orders`

The objective is to compute `{"columns": ["average_items_per_order"], "rows": [[2.7]]}` from `{"tables": {"Orders": [{"order_id": 10, "item_count": 1, "order_occurrences": 500}, {"order_id": 11, "item_count": 2, "order_occurrences": 1000}, {"order_id": 12, "item_count": 3, "order_occurrences": 800}, {"order_id": 13, "item_count": 4, "order_occurrences": 1000}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Understand the compressed representation

One row does not necessarily represent one order. `item_count` says how many items an order has, while `order_occurrences` says how many such orders exist. A row with `item_count = 3` and `order_occurrences = 800` represents 800 separate orders, each containing three items.

The ordinary average over the expanded orders must therefore be weighted. Treating every compressed row equally with `AVG(item_count)` would give a row average, not an order average. A rare row and a row representing thousands of orders would receive the same weight, which is incorrect.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Orders": [{"order_id": 10, "item_count": 1, "order_occurrences": 500}, {"order_id": 11, "item_count": 2, "order_occurrences": 1000}, {"order_id": 12, "item_count": 3, "order_occurrences": 800}, {"order_id": 13, "item_count": 4, "order_occurrences": 1000}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build the numerator

For one compressed row, the total number of items represented is:

`item_count * order_occurrences`.

Summing this product over all rows yields the item count that would appear across the fully expanded order data:

`SUM(item_count * order_occurrences)`.

In the sample, the products are 500, 2,000, 2,400, and 4,000, totaling 8,900 items.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For one compressed row, the total number of items represente... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build the denominator

The number of represented orders in one row is `order_occurrences`. Therefore:

`SUM(order_occurrences)`

is the total expanded order count. The sample denominator is $500+1000+800+1000=3300$.

Dividing the two sums gives the weighted mean:

$$
\frac{\sum(\texttt{item_count}\cdot\texttt{order_occurrences})}
{\sum\texttt{order_occurrences}}.
$$

For the sample this is $8900/3300\approx2.696969\ldots$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["average_items_per_order"], "rows": [[2.7]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Orders": [{"order_id": 10, "item_count": 1, "order_occurrences": 500}, {"order_id": 11, "item_count": 2, "order_occurrences": 1000}, {"order_id": 12, "item_count": 3, "order_occurrences": 800}, {"order_id": 13, "item_count": 4, "order_occurrences": 1000}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["average_items_per_order"], "rows": [[2.7]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`AVG(item_count)`:** This averages compressed :** - **`AVG(item_count)`:** This averages compressed rows equally and is wrong whenever occurrence weights differ.
- **Expand every represented order:** It produces the same statistic but can require enormous time and storage; weighted sums are the algebraic compression.
- **Average row products:** `AVG(item_count * order_occurrences)` divides by compressed-row count rather than represented-order count and is incorrect.
- **Round intermediate values:** Only the final quotient should be rounded to avoid accumulated rounding error.
- **One compressed row:** The answer is exactly its `item_count`, regardless of how many occurrences it represents.
- **Equal occurrence counts:** In that special case the weighted and unweighted row means coincide, but the weighted formula remains correct.
- **Large weights:** Aggregate multiplication and sums should use the database’s promoted numeric types; the query avoids materializing repeated rows.
- **Empty input:** The exact SQL returns a row containing `NULL` because both global sums are null; no alternative behavior is specified in the source.
- **Output order:** A single-row result needs no `ORDER BY`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R)$. Let $R$ be the number of compressed rows. MySQL can update both sums during one sequential scan, so logical running time is $O(R)$. No sorting, grouping by keys, join, or window operation is required.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
