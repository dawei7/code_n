# Guided Example: Duplicate Emails

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Person": [{"id": 1, "email": "a@x"}, {"id": 2, "email": "b@x"}]}}`
- **Required output:** `{"columns": ["Email"], "rows": []}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Person`

The objective is to compute `{"columns": ["Email"], "rows": []}` from `{"tables": {"Person": [{"id": 1, "email": "a@x"}, {"id": 2, "email": "b@x"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn equal email rows into groups

The query begins by selecting `email` from `Person` and grouping by that same
expression. All rows with identical email text belong to one group.

The primary key `id` distinguishes people but is irrelevant to duplication:
two different IDs with the same email are exactly the condition being sought.
The query therefore neither selects nor groups by `id`.

The guarantee that email contains no uppercase letters means comparisons do not
need application-level case normalization. Actual SQL collation can still be
case-insensitive, but every supplied value is already lowercase.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Person": [{"id": 1, "email": "a@x"}, {"id": 2, "email": "b@x"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand positional `GROUP BY 1`

`GROUP BY 1` is MySQL shorthand for grouping by the first expression in the
`SELECT` list. Here that expression is `email`, so it is equivalent to:

`GROUP BY email`.

The positional form is concise, but it couples grouping to select-list order.
If another expression were inserted before `email`, the meaning could change.
Writing the column name explicitly is usually clearer for maintenance.

Under the exact current query, each output candidate row represents one unique
email group.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Filter groups with `HAVING`

`WHERE` filters individual input rows before grouping. The duplicate condition
depends on the number of rows in a completed group, so it belongs in `HAVING`.

`COUNT(1)` counts one non-null constant for every row in a group. Therefore it
equals the number of people sharing that email. The predicate:

`COUNT(1) > 1`

keeps groups containing at least two rows and rejects groups containing exactly
one.

`COUNT(*)` would have the same behavior. `COUNT(email)` is also equivalent
under the explicit non-null email guarantee, but would ignore null values if
they were allowed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["Email"], "rows": []}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Person": [{"id": 1, "email": "a@x"}, {"id": 2, "email": "b@x"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["Email"], "rows": []}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit named grouping:** `GROUP BY email` is clearer than positional `GROUP BY 1`.
- **Derived count table:** Group and count in a subquery, then filter `num > 1` outside; correct but more verbose than `HAVING`.
- **Self-join on equal email and different IDs:** Can find duplicates but may create many row pairs and then require `DISTINCT`.
- **Exactly two occurrences:** The group passes and emits one row.
- **Many occurrences:** Still emits one row because grouping collapses them.
- **All emails unique:** No group passes, returning an empty table.
- **Empty table:** Also returns no rows.
- **Non-null guarantee:** Makes `COUNT(1)`, `COUNT(*)`, and `COUNT(email)` equivalent here.
- **Output case:** Add `AS Email` if exact displayed capitalization is enforced.
- **Any order:** No sorting is required.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of people and $u$ the number of unique emails. A
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
