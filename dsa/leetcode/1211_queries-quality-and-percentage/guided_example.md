# Guided Example: Queries Quality and Percentage

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Queries": [{"query_name": "Dog", "result": "Golden Retriever", "position": 1, "rating": 5}, {"query_name": "Dog", "result": "German Shepherd", "position": 2, "rating": 5}, {"query_name": "Dog", "result": "Mule", "position": 200, "rating": 1}, {"query_name": "Cat", "result": "Shirazi", "position": 5, "rating": 2}, {"query_name": "Cat", "result": "Siamese", "position": 3, "rating": 3}, {"query_name": "Cat", "result": "Sphynx", "position": 7, "rating": 4}]}}`
- **Required output:** `{"columns": ["query_name", "quality", "poor_query_percentage"], "rows": [["Cat", 0.66, 33.33], ["Dog", 2.5, 33.33]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Queries`

The objective is to compute `{"columns": ["query_name", "quality", "poor_query_percentage"], "rows": [["Cat", 0.66, 33.33], ["Dog", 2.5, 33.33]]}` from `{"tables": {"Queries": [{"query_name": "Dog", "result": "Golden Retriever", "position": 1, "rating": 5}, {"query_name": "Dog", "result": "German Shepherd", "position": 2, "rating": 5}, {"query_name": "Dog", "result": "Mule", "position": 200, "rating": 1}, {"query_name": "Cat", "result": "Shirazi", "position": 5, "rating": 2}, {"query_name": "Cat", "result": "Siamese", "position": 3, "rating": 3}, {"query_name": "Cat", "result": "Sphynx", "position": 7, "rating": 4}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Exclude unnamed groups

`WHERE query_name IS NOT NULL` removes rows that cannot belong to a named result group. This matters if the table permits null query names. Ordinary duplicate rows are not removed; each row is an observation and contributes separately to both averages.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Queries": [{"query_name": "Dog", "result": "Golden Retriever", "position": 1, "rating": 5}, {"query_name": "Dog", "result": "German Shepherd", "position": 2, "rating": 5}, {"query_name": "Dog", "result": "Mule", "position": 200, "rating": 1}, {"query_name": "Cat", "result": "Shirazi", "position": 5, "rating": 2}, {"query_name": "Cat", "result": "Siamese", "position": 3, "rating": 3}, {"query_name": "Cat", "result": "Sphynx", "position": 7, "rating": 4}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compute quality as an average of row ratios

`rating / position` calculates the ratio for one row. MySQL’s division operator produces a non-integer numeric result, so values such as five divided by two contribute 2.5 rather than being truncated.

`AVG(rating / position)` then averages those per-row ratios within a query-name group. The order is important: average of ratios is not generally the same as total rating divided by total position.

`ROUND(..., 2)` rounds the final group average to two decimal places and aliases it as `quality`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Turn the poor condition into a percentage

In MySQL, `rating < 3` evaluates to one when the row is poor and zero otherwise. Averaging this indicator gives the fraction of group rows that are poor:

$$
\frac{\text{poor row count}}{\text{total row count}}.
$$

Multiplying by 100 converts the fraction to a percentage, and rounding to two decimals produces `poor_query_percentage`.

For three rows with one poor rating, the Boolean values are zero, zero, and one. Their average is one third; multiplying by 100 and rounding gives 33.33.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["query_name", "quality", "poor_query_percentage"], "rows": [["Cat", 0.66, 33.33], ["Dog", 2.5, 33.33]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Queries": [{"query_name": "Dog", "result": "Golden Retriever", "position": 1, "rating": 5}, {"query_name": "Dog", "result": "German Shepherd", "position": 2, "rating": 5}, {"query_name": "Dog", "result": "Mule", "position": 200, "rating": 1}, {"query_name": "Cat", "result": "Shirazi", "position": 5, "rating": 2}, {"query_name": "Cat", "result": "Siamese", "position": 3, "rating": 3}, {"query_name": "Cat", "result": "Sphynx", "position": 7, "rating": 4}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["query_name", "quality", "poor_query_percentage"], "rows": [["Cat", 0.66, 33.33], ["Dog", 2.5, 33.33]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit `CASE` for poor rows:** `AVG(CASE WHEN rating < 3 THEN 1 ELSE 0 END)` is more portable across SQL dialects.
- **Count-based percentage:** Compute `100 * SUM(rating < 3) / COUNT(*)`. It is algebraically equivalent when all ratings are non-null.
- **Round each ratio first:** This is incorrect because early rounding can change the average; round only the final aggregate.
- **Rating exactly three:** It is not poor because the condition is strictly less than three.
- **Duplicate rows:** They represent repeated observations and must each contribute; the query preserves them.
- **Null query name:** The `WHERE` clause deliberately excludes it rather than creating a null-named group.
- **One-row group:** Quality is that row’s ratio, and the poor percentage is either zero or 100.
- **Position is never zero:** The documented range starts at one, so division by zero cannot occur.
- **Any result order:** No presentation sort is required.
- **Ordinal grouping:** `GROUP BY 1` depends on `query_name` remaining the first selected expression.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(g)$. Let $n$ be the number of table rows and $g$ the number of non-null query-name groups.
- **Auxiliary Space Complexity:** $O(g)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
