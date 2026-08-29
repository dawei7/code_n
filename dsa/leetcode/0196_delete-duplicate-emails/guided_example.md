# Guided Example: Delete Duplicate Emails

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Person": [{"id": 1, "email": "a@x.com"}, {"id": 2, "email": "b@x.com"}, {"id": 3, "email": "a@x.com"}]}}`
- **Required output:** `{"columns": ["id", "email"], "rows": [[1, "a@x.com"], [2, "b@x.com"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Person`

The objective is to compute `{"columns": ["id", "email"], "rows": [[1, "a@x.com"], [2, "b@x.com"]]}` from `{"tables": {"Person": [{"id": 1, "email": "a@x.com"}, {"id": 2, "email": "b@x.com"}, {"id": 3, "email": "a@x.com"}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Identify one permanent keeper for every email

The task is destructive: it must delete rows, not merely display a deduplicated
result. Before deleting anything, the query defines which rows must survive.
For each email group, the primary key's minimum value is the unique required
keeper ID.

Because `id` is a primary key, no two rows share that value. Even if many rows
have the same email, `MIN(id)` therefore identifies exactly one original row in
that group.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Person": [{"id": 1, "email": "a@x.com"}, {"id": 2, "email": "b@x.com"}, {"id": 3, "email": "a@x.com"}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build the keeper-ID set with grouping

The innermost `SELECT * FROM Person` reads a snapshot-like derived relation
named `p`. The surrounding query groups those rows by `email` and computes
`MIN(id)` once for every group. Conceptually, its result is a one-column set of
IDs that are protected from deletion.

For the sample, the `john@example.com` group contains IDs 1 and 3, so its keeper
is 1. The `bob@example.com` group contains only ID 2, so its keeper is 2. The
subquery thus produces IDs 1 and 2.

Grouping by email text is the correct identity rule. The lowercase guarantee
means the application does not need to normalize letter case before grouping,
although actual SQL string comparison still follows the column's collation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why there is an extra derived-table layer

MySQL restricts some updates and deletes that read directly from the same target
table in a nested subquery, producing the familiar “can't specify target table”
error. Wrapping `SELECT * FROM Person` in another derived table gives the
aggregate query a named intermediate source and is a conventional workaround.

The layer is not part of the mathematical deduplication idea. Logically, it
still contains the same Person rows. Its purpose is to make the read-before-
delete structure acceptable to the target SQL engine.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["id", "email"], "rows": [[1, "a@x.com"], [2, "b@x.com"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Person": [{"id": 1, "email": "a@x.com"}, {"id": 2, "email": "b@x.com"}, {"id": 3, "email": "a@x.com"}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["id", "email"], "rows": [[1, "a@x.com"], [2, "b@x.com"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Self-join delete:** Delete a row whenever another row has the same email and smaller ID; concise MySQL syntax but can generate many matching pairs.
- **Window function:** Rank rows by `id` within each email and delete ranks above one through an engine-supported writable relation.
- **Pandas grouping:** The local editorial broadcasts each email's minimum ID and drops nonminimum DataFrame rows in place.
- **Single row per email:** Its ID is the group minimum and it remains.
- **Many duplicates:** Exactly the smallest-ID row survives, regardless of group size.
- **Primary-key non-nullness:** Guarantees the keeper subquery cannot poison `NOT IN` with null.
- **Nullable email:** The query treats all null emails as one group; confirm that semantic if the domain expands.
- **Duplicate letter case:** Input is lowercase, while database collation still defines equality.
- **Empty table:** The keeper set and deletion target are empty, so nothing changes.
- **Final ordering:** Not specified and not controlled by `DELETE`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of Person rows and $u$ the number of distinct emails. The
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
