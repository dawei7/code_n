# Guided Example: Reformat Department Table

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Department": [{"id": 1, "revenue": 8000, "month": "Jan"}, {"id": 2, "revenue": 9000, "month": "Jan"}, {"id": 3, "revenue": 10000, "month": "Feb"}, {"id": 1, "revenue": 7000, "month": "Feb"}, {"id": 1, "revenue": 6000, "month": "Mar"}]}}`
- **Required output:** `{"columns": ["id", "Jan_Revenue", "Feb_Revenue", "Mar_Revenue", "Apr_Revenue", "May_Revenue", "Jun_Revenue", "Jul_Revenue", "Aug_Revenue", "Sep_Revenue", "Oct_Revenue", "Nov_Revenue", "Dec_Revenue"], "rows": [[1, 8000, 7000, 6000, null, null, null, null, null, null, null, null, null], [2, 9000, null, null, null, null, null, null, null, null, null, null, null], [3, null, 10000, null, null, null, null, null, null, null, null, null, null]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Department`

The objective is to compute `{"columns": ["id", "Jan_Revenue", "Feb_Revenue", "Mar_Revenue", "Apr_Revenue", "May_Revenue", "Jun_Revenue", "Jul_Revenue", "Aug_Revenue", "Sep_Revenue", "Oct_Revenue", "Nov_Revenue", "Dec_Revenue"], "rows": [[1, 8000, 7000, 6000, null, null, null, null, null, null, null, null, null], [2, 9000, null, null, null, null, null, null, null, null, null, null, null], [3, null, 10000, null, null, null, null, null, null, null, null, null, null]]}` from `{"tables": {"Department": [{"id": 1, "revenue": 8000, "month": "Jan"}, {"id": 2, "revenue": 9000, "month": "Jan"}, {"id": 3, "revenue": 10000, "month": "Feb"}, {"id": 1, "revenue": 7000, "month": "Feb"}, {"id": 1, "revenue": 6000, "month": "Mar"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: First group all rows belonging to one department

The query ends with `GROUP BY 1`. In MySQL, the ordinal `1` refers to the first expression in the `SELECT` list, which is `id`. Thus all input rows with the same department ID form one group, and the query produces one output row for each distinct department.

Grouping alone is not enough. A department group can contain several revenue values belonging to different months, and SQL needs an unambiguous expression for every output column. The solution therefore uses conditional aggregation: each monthly expression hides rows from the other eleven months and exposes only the revenue for its own month.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Department": [{"id": 1, "revenue": 8000, "month": "Jan"}, {"id": 2, "revenue": 9000, "month": "Jan"}, {"id": 3, "revenue": 10000, "month": "Feb"}, {"id": 1, "revenue": 7000, "month": "Feb"}, {"id": 1, "revenue": 6000, "month": "Mar"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How one monthly column is formed

January’s expression is structurally:

`SUM(CASE month WHEN 'Jan' THEN revenue END) AS Jan_Revenue`.

The simple `CASE` compares the current row’s `month` value with `'Jan'`. On a January row, it returns that row’s `revenue`. There is no explicit `ELSE`, so every non-January row produces `NULL` for this expression.

The surrounding `SUM` reduces all those per-row results to one value for the department group. SQL aggregate functions such as `SUM` ignore `NULL` inputs. Because the primary key permits at most one January row for a department, there are only two meaningful outcomes:

- If a January row exists, `SUM` sees its one revenue value and returns that value.
- If no January row exists, every result supplied to `SUM` is `NULL`, and MySQL returns `NULL` for the all-`NULL` aggregate.

That is precisely the required behavior. The query repeats this same pattern for every month, changing the month literal and alias. The aliases are part of the result contract: `Jan_Revenue`, `Feb_Revenue`, and the remaining ten names label the pivoted columns.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | January’s expression is structurally:

`SUM(CASE month WHEN ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Following a department through the pivot

Suppose department one has rows `(1, 8000, 'Jan')`, `(1, 7000, 'Feb')`, and `(1, 6000, 'Mar')`. The grouping step puts all three rows together. For the January expression, the first row contributes 8000 and the other two contribute `NULL`, so the aggregate returns 8000. The February expression exposes only 7000, and the March expression exposes only 6000. Every expression from April through December sees only `NULL` and returns `NULL`. The result is one row with all thirteen requested columns: the ID plus twelve monthly revenue cells.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["id", "Jan_Revenue", "Feb_Revenue", "Mar_Revenue", "Apr_Revenue", "May_Revenue", "Jun_Revenue", "Jul_Revenue", "Aug_Revenue", "Sep_Revenue", "Oct_Revenue", "Nov_Revenue", "Dec_Revenue"], "rows": [[1, 8000, 7000, 6000, null, null, null, null, null, null, null, null, null], [2, 9000, null, null, null, null, null, null, null, null, null, null, null], [3, null, 10000, null, null, null, null, null, null, null, null, null, null]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Department": [{"id": 1, "revenue": 8000, "month": "Jan"}, {"id": 2, "revenue": 9000, "month": "Jan"}, {"id": 3, "revenue": 10000, "month": "Feb"}, {"id": 1, "revenue": 7000, "month": "Feb"}, {"id": 1, "revenue": 6000, "month": "Mar"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["id", "Jan_Revenue", "Feb_Revenue", "Mar_Revenue", "Apr_Revenue", "May_Revenue", "Jun_Revenue", "Jul_Revenue", "Aug_Revenue", "Sep_Revenue", "Oct_Revenue", "Nov_Revenue", "Dec_Revenue"], "rows": [[1, 8000, 7000, 6000, null, null, null, null, null, null, null, null, null], [2, 9000, null, null, null, null, null, null, null, null, null, null, null], [3, null, 10000, null, null, null, null, null, null, null, null, null, null]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Twelve left joins:** Start from distinct depar:** - **Twelve left joins:** Start from distinct department IDs and left-join one filtered table alias for every month. This preserves missing months as `NULL` but is substantially more verbose and may require repeated table access.
- **Native `PIVOT` syntax:** Some database systems provide a pivot operator, which can express the intent directly. The submitted solution targets MySQL, where portable conditional aggregation is the appropriate technique.
- **`MAX` or `MIN` instead of `SUM`:** Because `(id, month)` is unique, any aggregate that ignores `NULL` and returns the lone non-`NULL` value works. `SUM` is correct here because there cannot be multiple monthly rows to combine.
- **Department with only one recorded month:** The group still produces one complete result row. That month contains its revenue and all other monthly aggregates return `NULL`.
- **Missing month:** Omitting `ELSE` from `CASE` deliberately produces `NULL`. Replacing it with zero would incorrectly report zero revenue instead of absent data.
- **Revenue equal to zero:** A stored zero is not `NULL`. The matching monthly aggregate returns zero, correctly distinguishing a recorded zero from a missing row.
- **Several departments:** `GROUP BY 1` keeps their rows in separate groups, so revenues from different IDs can never be combined.
- **Primary-key dependence:** If duplicate rows for the same `(id, month)` were illegally present, `SUM` would add their revenues. The stated primary key rules out that situation and is essential to the extractor interpretation.
- **Ordinal grouping:** `GROUP BY 1` means group by the first selected expression, `id`. Writing `GROUP BY id` would be more explicit but would produce the same result for this query.
- **Output order:** No `ORDER BY` is needed because the problem accepts any row order. Applications that require deterministic display order should add an explicit ordering clause, but that is outside this contract.
- **Case-sensitive month literals:** The query uses exactly the documented abbreviations from `'Jan'` through `'Dec'`. Misspelling an abbreviation or alias would leave a column empty or violate the required output schema.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(d)$. Let $n$ be the number of rows in `Department` and $d$ be the number of distinct department IDs. There are exactly twelve monthly expressions, which is a fixed constant.
- **Auxiliary Space Complexity:** $O(d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
