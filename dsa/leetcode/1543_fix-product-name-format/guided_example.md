# Guided Example: Fix Product Name Format

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Sales": [{"sale_id": 1, "product_name": "LCPHONE", "sale_date": "2000-01-16"}, {"sale_id": 2, "product_name": "LCPhone", "sale_date": "2000-01-17"}, {"sale_id": 3, "product_name": "LcPhOnE", "sale_date": "2000-02-18"}, {"sale_id": 4, "product_name": "LCKeyCHAiN", "sale_date": "2000-02-19"}, {"sale_id": 5, "product_name": "LCKeyChain", "sale_date": "2000-02-28"}, {"sale_id": 6, "product_name": "Matryoshka", "sale_date": "2000-03-31"}]}}`
- **Required output:** `{"columns": ["product_name", "sale_date", "total"], "rows": [["lckeychain", "2000-02", 2], ["lcphone", "2000-01", 2], ["lcphone", "2000-02", 1], ["matryoshka", "2000-03", 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Sales`

The objective is to compute `{"columns": ["product_name", "sale_date", "total"], "rows": [["lckeychain", "2000-02", 2], ["lcphone", "2000-01", 2], ["lcphone", "2000-02", 1], ["matryoshka", "2000-03", 1]]}` from `{"tables": {"Sales": [{"sale_id": 1, "product_name": "LCPHONE", "sale_date": "2000-01-16"}, {"sale_id": 2, "product_name": "LCPhone", "sale_date": "2000-01-17"}, {"sale_id": 3, "product_name": "LcPhOnE", "sale_date": "2000-02-18"}, {"sale_id": 4, "product_name": "LCKeyCHAiN", "sale_date": "2000-02-19"}, {"sale_id": 5, "product_name": "LCKeyChain", "sale_date": "2000-02-28"}, {"sale_id": 6, "product_name": "Matryoshka", "sale_date": "2000-03-31"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Normalize before grouping

Rows that spell the same product with different letter case or extra outer spaces must belong to one group. Grouping the raw `product_name` would incorrectly separate `"LCPHONE"`, `"LCPhone"`, and a version padded with spaces.

The common table expression `t` transforms every sale row first:

- `TRIM(product_name)` removes leading and trailing space characters.
- `LOWER(...)` converts the trimmed result to lowercase.
- `DATE_FORMAT(sale_date, '%Y-%m')` converts the full date to its four-digit year and two-digit month string.

These computed values are aliased back to `product_name` and `sale_date`. The outer query therefore operates on canonical product-month keys.

The transformation does not change the source table; it produces a logical intermediate relation containing one normalized row for each sale.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Sales": [{"sale_id": 1, "product_name": "LCPHONE", "sale_date": "2000-01-16"}, {"sale_id": 2, "product_name": "LCPhone", "sale_date": "2000-01-17"}, {"sale_id": 3, "product_name": "LcPhOnE", "sale_date": "2000-02-18"}, {"sale_id": 4, "product_name": "LCKeyCHAiN", "sale_date": "2000-02-19"}, {"sale_id": 5, "product_name": "LCKeyChain", "sale_date": "2000-02-28"}, {"sale_id": 6, "product_name": "Matryoshka", "sale_date": "2000-03-31"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why both name operations are necessary

Lowercasing alone leaves leading and trailing spaces, so visually identical names could still compare as different strings. Trimming alone leaves case variations.

Applying both operations maps every permitted formatting variation to the same representation. The order used here trims first and lowercases second. For ordinary space and lowercase-English normalization, reversing those two functions would produce the same characters, but the stored expression clearly communicates cleanup followed by case normalization.

`TRIM` does not remove spaces inside a product name. The requirement concerns leading and trailing whitespace, so internal characters remain part of the product's identity.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Lowercasing alone leaves leading and trailing spaces, so vis... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Convert dates to month buckets

Sales are counted by calendar month, not by exact day. Formatting a date as `%Y-%m` maps every day within the same month and year to one identical string.

Including the year is essential. January 2000 and January 2001 are different reporting periods even though their month numbers match.

The fixed-width format also sorts chronologically as text: earlier years compare first, and within a year `01` through `12` compare in month order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["product_name", "sale_date", "total"], "rows": [["lckeychain", "2000-02", 2], ["lcphone", "2000-01", 2], ["lcphone", "2000-02", 1], ["matryoshka", "2000-03", 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Sales": [{"sale_id": 1, "product_name": "LCPHONE", "sale_date": "2000-01-16"}, {"sale_id": 2, "product_name": "LCPhone", "sale_date": "2000-01-17"}, {"sale_id": 3, "product_name": "LcPhOnE", "sale_date": "2000-02-18"}, {"sale_id": 4, "product_name": "LCKeyCHAiN", "sale_date": "2000-02-19"}, {"sale_id": 5, "product_name": "LCKeyChain", "sale_date": "2000-02-28"}, {"sale_id": 6, "product_name": "Matryoshka", "sale_date": "2000-03-31"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["product_name", "sale_date", "total"], "rows": [["lckeychain", "2000-02", 2], ["lcphone", "2000-01", 2], ["lcphone", "2000-02", 1], ["matryoshka", "2000-03", 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Group raw names:** It is incorrect because cas:** - **Group raw names:** It is incorrect because case and outer spaces would split one product into multiple groups.
- **Normalize after grouping:** It can produce duplicate-looking result rows whose counts were calculated separately; normalization must precede grouping.
- **Group by month number only:** It incorrectly combines the same month across different years.
- **Use YEAR and MONTH separately:** It is valid but needs formatting afterward to produce the exact `YYYY-MM` output.
- **Count sale id:** `COUNT(sale_id)` is equivalent when the unique identifier is non-null; `COUNT(1)` directly counts rows.
- **Positional GROUP BY:** `GROUP BY 1, 2` is concise but depends on select-expression order.
- **Positional ORDER BY:** `ORDER BY 1, 2` likewise depends on projection order; explicit aliases can be easier to maintain.
- **Internal spaces:** They are preserved because only leading and trailing spaces are declared formatting noise.
- **Case variants:** `LOWER` merges them into one canonical key under the database's character rules.
- **Different months:** They remain separate even for the same normalized product.
- **Different products in one month:** They remain separate because both key columns participate in grouping.
- **Chronological text order:** Fixed four-digit year and two-digit month ensure ascending string order matches ascending month order.
- **CTE execution:** MySQL may inline or materialize `t`, but either physical choice has the same relational meaning.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r \log r)$. Let $R$ be the number of sales rows and $G$ the number of distinct normalized product-month groups.
- **Auxiliary Space Complexity:** $O(g)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
