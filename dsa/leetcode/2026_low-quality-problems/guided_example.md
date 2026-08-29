# Guided Example: Low-Quality Problems

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Problems": [{"problem_id": 1, "likes": 3, "dislikes": 2}]}}`
- **Required output:** `{"columns": ["problem_id"], "rows": []}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Problems`

The objective is to compute `{"columns": ["problem_id"], "rows": []}` from `{"tables": {"Problems": [{"problem_id": 1, "likes": 3, "dislikes": 2}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate the percentage definition directly

For one problem row, the total number of votes is

`likes + dislikes`.

Its like proportion is therefore

`likes / (likes + dislikes)`.

The definition says that a problem is low-quality only when this proportion is strictly below sixty percent. The query places the exact comparison

`likes / (likes + dislikes) < 0.6`

in the `WHERE` clause. Every row satisfying it is retained, and every row whose proportion is at least `0.6` is discarded.

The distinction between “strictly less than” and “at most” matters. A row with exactly 60 percent likes must not be returned, and the `<` operator implements that boundary correctly.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Problems": [{"problem_id": 1, "likes": 3, "dislikes": 2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand the query as three logical stages

The `FROM Problems` clause begins with every problem row. Because `problem_id` is the primary key, each problem occurs at most once and no grouping or duplicate removal is necessary.

The `WHERE` clause evaluates the ratio independently for each row. This is a row-local calculation: the likes of one problem are never combined with those of another problem.

The `SELECT problem_id` clause projects away the vote counts and retains only the requested identifier. Finally, `ORDER BY problem_id` sorts those identifiers in ascending order so the result satisfies the required presentation order.

This sequence is important conceptually. Sorting is performed on the filtered result, not used to decide which rows qualify. Likewise, selecting only `problem_id` does not prevent the filtering phase from reading `likes` and `dislikes`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Walk through the threshold calculation

Problem 7 in the example has 8,569 likes and 6,086 dislikes. Its total is 14,655, and its like ratio is about 0.5847. Because 0.5847 is below 0.6, its identifier survives the filter.

Problem 1 has 4,446 likes and 2,760 dislikes. Its ratio is about 0.6170, which is greater than 0.6, so its identifier is removed.

After all rows are evaluated this way, the remaining identifiers are sorted numerically. The input table need not already be in identifier order; the explicit `ORDER BY` produces 7, 10, 11, and 13 in the example.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["problem_id"], "rows": []}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Problems": [{"problem_id": 1, "likes": 3, "dislikes": 2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["problem_id"], "rows": []}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Cross multiplication:** Use `2 * likes < 3 * dislikes` to avoid decimal division when the vote total is positive; choose numeric types wide enough to prevent multiplication overflow.
- **Percentage multiplication:** Writing `100 * likes / (likes + dislikes) < 60` is equivalent for a positive denominator but introduces an unnecessary multiplication.
- **Integer division:** Using an operator or cast that truncates the quotient would be incorrect because fractional percentages carry the decision.
- **Exactly 60 percent:** The row is excluded because the condition is strict `< 0.6`.
- **Just below 60 percent:** The row is included even if the difference is very small.
- **All likes and no dislikes:** The ratio is one, so the row is excluded.
- **No likes and positive dislikes:** The ratio is zero, so the row is included.
- **Zero total votes:** The exact division yields no true predicate and the row is excluded; the description supplies no alternative convention.
- **Null vote value:** If data outside the stated model contained `NULL`, the arithmetic would become `NULL` and the row would not pass.
- **Duplicate identifiers:** The primary-key guarantee prevents them, so neither grouping nor `DISTINCT` is needed.
- **Unsorted input storage:** `ORDER BY problem_id` still guarantees ascending output.
- **Empty qualifying set:** The query correctly returns an empty result table.
- **Database execution plan:** Indexes may improve physical performance, but they do not change the logical filter or ordering.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P\log P)$. Let $P$ be the number of rows in `Problems` and let $Q$ be the number that satisfy the ratio predicate. Evaluating the arithmetic condition during a table scan takes $O(P)$ time. Sorting the retained identifiers takes $O(Q\log Q)$ time in a comparison-based plan, so the general worst-case bound is $O(P\log P)$ when $Q$ can equal $P$.
- **Auxiliary Space Complexity:** $O(P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
