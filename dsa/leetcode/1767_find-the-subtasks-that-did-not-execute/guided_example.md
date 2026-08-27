# Guided Example: Find the Subtasks That Did Not Execute

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Tasks": [{"task_id": 1, "subtasks_count": 3}, {"task_id": 2, "subtasks_count": 2}, {"task_id": 3, "subtasks_count": 4}], "Executed": [{"task_id": 1, "subtask_id": 2}, {"task_id": 3, "subtask_id": 1}, {"task_id": 3, "subtask_id": 2}, {"task_id": 3, "subtask_id": 3}, {"task_id": 3, "subtask_id": 4}]}}`
- **Required output:** `{"columns": ["task_id", "subtask_id"], "rows": [[1, 1], [1, 3], [2, 1], [2, 2]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Tasks`

The objective is to compute `{"columns": ["task_id", "subtask_id"], "rows": [[1, 1], [1, 3], [2, 1], [2, 2]]}` from `{"tables": {"Tasks": [{"task_id": 1, "subtasks_count": 3}, {"task_id": 2, "subtasks_count": 2}, {"task_id": 3, "subtasks_count": 4}], "Executed": [{"task_id": 1, "subtask_id": 2}, {"task_id": 3, "subtask_id": 1}, {"task_id": 3, "subtask_id": 2}, {"task_id": 3, "subtask_id": 3}, {"task_id": 3, "subtask_id": 4}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Generate the complete expected subtask relation

`Tasks` stores only a count, not one row per valid subtask. Before missing rows can be found, the query must expand each task into identifiers one through `subtasks_count`.

The recursive common table expression `T(task_id, subtask_id)` performs that expansion. Its anchor member selects:

`task_id, subtasks_count`

from every task. This creates the highest valid subtask identifier for each task.

The recursive member then selects the same `task_id` with `subtask_id - 1` while `subtask_id > 1`. Repeated recursion therefore generates the descending sequence from the count down to one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Tasks": [{"task_id": 1, "subtasks_count": 3}, {"task_id": 2, "subtasks_count": 2}, {"task_id": 3, "subtasks_count": 4}], "Executed": [{"task_id": 1, "subtask_id": 2}, {"task_id": 3, "subtask_id": 1}, {"task_id": 3, "subtask_id": 2}, {"task_id": 3, "subtask_id": 3}, {"task_id": 3, "subtask_id": 4}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why every valid pair appears exactly once

For a task with count $c$, the anchor emits `(task_id, c)`. The recursion emits `c-1`, then `c-2`, continuing until the row with identifier one. The condition prevents a zero row.

`task_id` is unique in `Tasks`, and each descending numeric step is unique for that task. `UNION ALL` is therefore safe: it preserves all generated rows without paying for unnecessary duplicate elimination.

The constraint `subtasks_count >= 2` is not required for the recursion's correctness; even a count of one would produce its one anchor row and no recursive child.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For a task with count $c$, the anchor emits `(task_id, c)`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Compare expected pairs with executed pairs

After expansion, `T` contains the universe of valid task-subtask pairs. The query left-joins `Executed` using both `task_id` and `subtask_id`.

A matching execution row is attached when that exact pair executed successfully. When no match exists, columns from `Executed` are null because a left join preserves every row from `T`.

The filter:

`WHERE Executed.subtask_id IS NULL`

keeps only unmatched expected rows. Since valid `Executed.subtask_id` values are real integer identifiers and the key pair is unique, null here is an unambiguous no-match signal.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["task_id", "subtask_id"], "rows": [[1, 1], [1, 3], [2, 1], [2, 2]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Tasks": [{"task_id": 1, "subtasks_count": 3}, {"task_id": 2, "subtasks_count": 2}, {"task_id": 3, "subtasks_count": 4}], "Executed": [{"task_id": 1, "subtask_id": 2}, {"task_id": 3, "subtask_id": 1}, {"task_id": 3, "subtask_id": 2}, {"task_id": 3, "subtask_id": 3}, {"task_id": 3, "subtask_id": 4}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["task_id", "subtask_id"], "rows": [[1, 1], [1, 3], [2, 1], [2, 2]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Numbers helper table:** Join each task to pree:** - **Numbers helper table:** Join each task to preexisting integers from one through `subtasks_count`. It avoids recursion when such a table is available.
- **Recursive sequence upward:** Anchor at one and increment while below the task count. It is equally correct and naturally describes ascending identifiers.
- **NOT EXISTS:** Generate candidates, then retain those for which no matching execution row exists. It expresses the anti-join directly.
- **NOT IN:** Null semantics can be troublesome in general; a composite `NOT EXISTS` or left anti-join is safer.
- **No executions for a task:** Every generated subtask survives.
- **All executions present:** No row for that task survives.
- **Some executions present:** Only exact unmatched composite pairs are returned.
- **Different tasks share subtask numbers:** Composite joining keeps them separate.
- **Maximum count twenty:** Recursion depth per task is small.
- **UNION ALL:** Generated pairs are inherently unique, so duplicate removal is unnecessary.
- **Stop at one:** `WHERE subtask_id > 1` prevents invalid identifier zero.
- **Executed uniqueness:** A successful pair cannot duplicate the result through multiple matches.
- **Any-order main contract:** The exact query satisfies membership but promises no ordering.
- **Ascending-order stricter contract:** Add an explicit `ORDER BY` if that local requirement must be enforced.
- **Empty missing set:** The query naturally returns no rows when everything executed.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(T)$. Let $T=\sum \texttt{subtasks_count}$ be the total number of valid task-subtask pairs. The recursive CTE generates exactly $T$ rows, taking $O(T)$ logical work and $O(T)$ CTE storage.
- **Auxiliary Space Complexity:** $O(T)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
