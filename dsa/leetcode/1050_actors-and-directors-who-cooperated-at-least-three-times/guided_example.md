# Guided Example: Actors and Directors Who Cooperated At Least Three Times

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"ActorDirector": [{"actor_id": 1, "director_id": 1, "timestamp": 0}, {"actor_id": 1, "director_id": 1, "timestamp": 1}, {"actor_id": 1, "director_id": 1, "timestamp": 2}, {"actor_id": 1, "director_id": 2, "timestamp": 3}, {"actor_id": 1, "director_id": 2, "timestamp": 4}, {"actor_id": 2, "director_id": 1, "timestamp": 5}, {"actor_id": 2, "director_id": 1, "timestamp": 6}]}}`
- **Required output:** `{"columns": ["actor_id", "director_id"], "rows": [[1, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `ActorDirector`

The objective is to compute `{"columns": ["actor_id", "director_id"], "rows": [[1, 1]]}` from `{"tables": {"ActorDirector": [{"actor_id": 1, "director_id": 1, "timestamp": 0}, {"actor_id": 1, "director_id": 1, "timestamp": 1}, {"actor_id": 1, "director_id": 1, "timestamp": 2}, {"actor_id": 1, "director_id": 2, "timestamp": 3}, {"actor_id": 1, "director_id": 2, "timestamp": 4}, {"actor_id": 2, "director_id": 1, "timestamp": 5}, {"actor_id": 2, "director_id": 1, "timestamp": 6}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: One row represents one cooperation event

Each `ActorDirector` row names an actor, a director, and a unique `timestamp`. The timestamp primary key ensures no two table rows describe the same keyed event.

The question asks for pairs, not individual actors or directors. Rows must therefore be grouped by the combination `(actor_id, director_id)`. The number of rows in one such group is the number of recorded collaborations for that exact pair.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"ActorDirector": [{"actor_id": 1, "director_id": 1, "timestamp": 0}, {"actor_id": 1, "director_id": 1, "timestamp": 1}, {"actor_id": 1, "director_id": 1, "timestamp": 2}, {"actor_id": 1, "director_id": 2, "timestamp": 3}, {"actor_id": 1, "director_id": 2, "timestamp": 4}, {"actor_id": 2, "director_id": 1, "timestamp": 5}, {"actor_id": 2, "director_id": 1, "timestamp": 6}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Group by both selected columns

The query selects `actor_id` first and `director_id` second, then writes `GROUP BY 1, 2`.

In MySQL, positional grouping references select-list positions:

- `1` means `actor_id`.
- `2` means `director_id`.

Writing `GROUP BY actor_id, director_id` would be equivalent and more explicit.

Grouping by only actor would combine work with different directors. Grouping by only director would combine different actors. Both identifiers are required to preserve pair identity.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The query selects `actor_id` first and `director_id` second,... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count rows in each pair

`COUNT(1)` counts one non-null constant for every row in the group. It is therefore the group row count.

The query could use `COUNT(*)` with the same meaning. It does not need `COUNT(DISTINCT timestamp)` because `timestamp` is already a primary key and hence unique across the entire table.

Every row contributes exactly one collaboration to exactly one actor-director group.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["actor_id", "director_id"], "rows": [[1, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"ActorDirector": [{"actor_id": 1, "director_id": 1, "timestamp": 0}, {"actor_id": 1, "director_id": 1, "timestamp": 1}, {"actor_id": 1, "director_id": 1, "timestamp": 2}, {"actor_id": 1, "director_id": 2, "timestamp": 3}, {"actor_id": 1, "director_id": 2, "timestamp": 4}, {"actor_id": 2, "director_id": 1, "timestamp": 5}, {"actor_id": 2, "director_id": 1, "timestamp": 6}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["actor_id", "director_id"], "rows": [[1, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit column names in `GROUP BY`:** `GROUP :** - **Explicit column names in `GROUP BY`:** `GROUP BY actor_id, director_id` is clearer and more portable than positional references while producing the same result.
- **`COUNT(*)`:** It is semantically equivalent to `COUNT(1)` for counting group rows.
- **`COUNT(timestamp)`:** Because the primary key cannot be null, it also counts every row. The constant count avoids depending on that column detail.
- **`COUNT(DISTINCT timestamp)`:** It is correct but redundant because timestamp is globally unique and may add unnecessary distinct-processing work.
- **Window function:** Compute `COUNT(*) OVER (PARTITION BY actor_id, director_id)`, filter counts, and select distinct pairs. It works but needs an extra deduplication step.
- **Self-joining three copies:** Require three different timestamps for one pair. This is much more complex and can create large intermediate combinations.
- **Correlated subquery:** Count matching rows for every outer pair, then deduplicate. Repeated counting is typically less efficient than one aggregation.
- **Exactly three rows:** The group passes because the comparison is inclusive.
- **More than three rows:** The group also passes, as required by “at least.”
- **Two rows:** The group fails.
- **Same actor with several directors:** Each director forms a separate group and frequency.
- **Same director with several actors:** Each actor likewise remains separate.
- **Unique timestamp:** Every physical row is a distinct keyed cooperation event, so plain row counting is appropriate.
- **Result order:** No `ORDER BY` is required or implied by the problem.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R log R)$. Let `R` be the number of rows in `ActorDirector`.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
