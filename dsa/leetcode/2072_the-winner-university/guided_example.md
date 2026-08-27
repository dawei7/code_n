# Guided Example: The Winner University

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"NewYork": [{"student_id": 1, "score": 90}, {"student_id": 2, "score": 87}], "California": [{"student_id": 2, "score": 89}, {"student_id": 3, "score": 88}]}}`
- **Required output:** `{"columns": ["winner"], "rows": [["New York University"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `NewYork`

The objective is to compute `{"columns": ["winner"], "rows": [["New York University"]]}` from `{"tables": {"NewYork": [{"student_id": 1, "score": 90}, {"student_id": 2, "score": 87}], "California": [{"student_id": 2, "score": 89}, {"student_id": 3, "score": 88}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn the scoring rule into two independent counts

The result depends on only one fact about each university: how many of its students have a score of at least 90. Individual student names, the order of the rows, and the exact values above 90 do not affect the winner. A student with score 90 qualifies because the boundary is inclusive, and a student with score 89 does not.

The query therefore reduces each input table to a single number:

- the `NewYork` subquery evaluates `COUNT(1)` over rows satisfying `score >= 90` and names that count `cnt`;
- the `California` subquery performs the same calculation for its own table.

This is the essential simplification. The outer query does not need to retain qualifying rows or match students across universities. It needs only the two totals.

Suppose New York has scores 88, 90, and 97, while California has scores 90, 91, 72, and 84. The New York count is 2 and the California count is also 2. The outer comparison consequently returns `'No Winner'`. Notice that 97 being higher than 91 is irrelevant: the problem compares the number of qualifying students, not the universities' maximum scores or average scores.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"NewYork": [{"student_id": 1, "score": 90}, {"student_id": 2, "score": 87}], "California": [{"student_id": 2, "score": 89}, {"student_id": 3, "score": 88}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why each aggregate subquery always produces one usable row

An aggregate query containing `COUNT` and no `GROUP BY` summarizes the entire filtered input as one group. It returns exactly one row even when no source rows satisfy the condition. In that empty case, `COUNT(1)` returns 0 rather than `NULL`.

That behavior matters to the structure of the solution. If the subqueries merely selected qualifying rows, one side could produce no rows and prevent the outer query from producing a result. Here, each side is guaranteed to produce its one scalar count. Even if both university tables are empty, the derived tables contain one row each, both counts are 0, and the answer is `'No Winner'`.

The aliases `n1` and `n2` name these two one-row derived tables. Their columns are accessed as `n1.cnt` and `n2.cnt`. The comma between the derived tables is a cross join. A cross join normally pairs every row on the left with every row on the right, but each side has exactly one row, so the result has exactly one pair. The outer `SELECT` therefore also returns exactly one row.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | An aggregate query containing `COUNT` and no `GROUP BY` summ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Choose the output with a complete three-way comparison

The `CASE` expression checks the possible relationships between the counts in a deliberate order:

1. If `n1.cnt > n2.cnt`, New York has more qualifying students, so the returned value is `'New York University'`.
2. If `n1.cnt < n2.cnt`, California has more qualifying students, so the returned value is `'California University'`.
3. Otherwise, neither strict inequality is true. For ordinary integer counts, that means the counts are equal, so the returned value is `'No Winner'`.

These cases are mutually exclusive and exhaustive. Two integer counts cannot simultaneously be greater and less than one another, and exactly one of greater than, less than, or equal must hold. As a result, the `CASE` cannot select an incorrect university and cannot omit the tie case.

The expression is aliased as `winner` because that is the required output column name. The exact result strings are part of the contract. Returning a shortened name such as `'New York'` or changing capitalization would produce the wrong output even if the comparison itself were correct.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["winner"], "rows": [["New York University"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"NewYork": [{"student_id": 1, "score": 90}, {"student_id": 2, "score": 87}], "California": [{"student_id": 2, "score": 89}, {"student_id": 3, "score": 88}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["winner"], "rows": [["New York University"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Conditional aggregation after combining the ta:** - **Conditional aggregation after combining the tables:** One could label and combine both universities' rows and then compute conditional counts in one larger aggregate. That introduces unnecessary union and labeling work when two small scalar subqueries express the two independent totals directly.
- **Joining students by an identifier:** A regular join would be conceptually wrong because the task does not compare corresponding students. It compares two population counts, and there may be no meaningful cross-university key relationship.
- **Sorting qualifying scores:** Sorting cannot help decide which university has more qualifying rows. Counting alone is sufficient, so sorting would add avoidable $O(N\log N)$ work in a typical comparison-based implementation.
- **Using an average or maximum score:** The winner is based solely on how many scores meet the threshold. A university can have the highest individual score or the higher average and still lose by having fewer qualifying students.
- **Inclusive score boundary:** The predicate must be `score >= 90`. Replacing it with `score > 90` incorrectly excludes every student whose score is exactly 90.
- **Both counts equal:** Equality must return `'No Winner'` whether the shared count is large or zero. The `ELSE` branch covers every tie without needing another arithmetic test.
- **No qualifying rows:** `COUNT(1)` returns 0 rather than `NULL`. Thus one university with no qualifying students can still be compared normally, and two zero counts correctly form a tie.
- **Empty input tables:** Each ungrouped aggregate still returns one row containing 0, so the cross join and outer `SELECT` continue to return exactly one answer row.
- **Exact output literals:** The three strings and the `winner` column alias must be preserved exactly because SQL result schemas and string values are judged as part of the answer.
- **Database execution details:** An optimizer may rewrite the cross join of scalar aggregates internally. That does not change the reasoning: each table contributes one exact count, and one three-way comparison selects the result.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N_Y$ be the number of rows in `NewYork`, let $N_C$ be the number of rows in `California`, and define $N=N_Y+N_C$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
