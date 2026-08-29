# Guided Example: Form a Chemical Bond

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Elements": [{"symbol": "He", "type": "Noble", "electrons": 0}, {"symbol": "Na", "type": "Metal", "electrons": 1}, {"symbol": "Ca", "type": "Metal", "electrons": 2}, {"symbol": "La", "type": "Metal", "electrons": 3}, {"symbol": "Cl", "type": "Nonmetal", "electrons": 1}, {"symbol": "O", "type": "Nonmetal", "electrons": 2}, {"symbol": "N", "type": "Nonmetal", "electrons": 3}]}}`
- **Required output:** `{"columns": ["metal", "nonmetal"], "rows": [["Na", "Cl"], ["Na", "N"], ["Na", "O"], ["Ca", "Cl"], ["Ca", "N"], ["Ca", "O"], ["La", "Cl"], ["La", "N"], ["La", "O"]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Elements`

The objective is to compute `{"columns": ["metal", "nonmetal"], "rows": [["Na", "Cl"], ["Na", "N"], ["Na", "O"], ["Ca", "Cl"], ["Ca", "N"], ["Ca", "O"], ["La", "Cl"], ["La", "N"], ["La", "O"]]}` from `{"tables": {"Elements": [{"symbol": "He", "type": "Noble", "electrons": 0}, {"symbol": "Na", "type": "Metal", "electrons": 1}, {"symbol": "Ca", "type": "Metal", "electrons": 2}, {"symbol": "La", "type": "Metal", "electrons": 3}, {"symbol": "Cl", "type": "Nonmetal", "electrons": 1}, {"symbol": "O", "type": "Nonmetal", "electrons": 2}, {"symbol": "N", "type": "Nonmetal", "electrons": 3}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A valid result is a Cartesian product of two filtered sets

The bond rule has only two roles: one element must be a metal and the other a nonmetal. Electron counts do not restrict pairing, and noble elements never participate.

The SQL reads `Elements` twice using aliases `a` and `b`. Alias `a` supplies the metal side; alias `b` supplies the nonmetal side.

The comma-separated tables in

`FROM Elements AS a, Elements AS b`

form a cross join. Before filtering, every row from `a` is paired with every row from `b`.

The `WHERE` clause retains only pairs satisfying

`a.type='Metal' AND b.type='Nonmetal'`.

The selected symbols are renamed `metal` and `nonmetal` to match the required output columns.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Elements": [{"symbol": "He", "type": "Noble", "electrons": 0}, {"symbol": "Na", "type": "Metal", "electrons": 1}, {"symbol": "Ca", "type": "Metal", "electrons": 2}, {"symbol": "La", "type": "Metal", "electrons": 3}, {"symbol": "Cl", "type": "Nonmetal", "electrons": 1}, {"symbol": "O", "type": "Nonmetal", "electrons": 2}, {"symbol": "N", "type": "Nonmetal", "electrons": 3}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why every valid pair appears

Take any metal row $M$ and nonmetal row $N$. A cross join includes ordered pair $(M,N)$. The type predicates are both true, so it survives and the query emits their symbols.

Conversely, every emitted row passed both predicates, so its first symbol belongs to a metal and its second to a nonmetal. It is therefore a valid bond pair.

These two directions prove the result is exactly

$$
\{\text{metals}\}\times\{\text{nonmetals}\}.
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why aliases are required

Both roles come from the same table. Without aliases, column references such as `symbol` and `type` would be ambiguous after joining the table to itself. `a.symbol` and `b.symbol` identify which logical copy supplies each field.

The aliases do not duplicate stored data permanently; they are query-level names that let the optimizer plan a self-join.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["metal", "nonmetal"], "rows": [["Na", "Cl"], ["Na", "N"], ["Na", "O"], ["Ca", "Cl"], ["Ca", "N"], ["Ca", "O"], ["La", "Cl"], ["La", "N"], ["La", "O"]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Elements": [{"symbol": "He", "type": "Noble", "electrons": 0}, {"symbol": "Na", "type": "Metal", "electrons": 1}, {"symbol": "Ca", "type": "Metal", "electrons": 2}, {"symbol": "La", "type": "Metal", "electrons": 3}, {"symbol": "Cl", "type": "Nonmetal", "electrons": 1}, {"symbol": "O", "type": "Nonmetal", "electrons": 2}, {"symbol": "N", "type": "Nonmetal", "electrons": 3}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["metal", "nonmetal"], "rows": [["Na", "Cl"], ["Na", "N"], ["Na", "O"], ["Ca", "Cl"], ["Ca", "N"], ["Ca", "O"], ["La", "Cl"], ["La", "N"], ["La", "O"]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit `CROSS JOIN`:** Write two filtered aliases with clear cross-join syntax. It is semantically identical and may be easier to read.
- **Conditional self-join with `ON`:** Use `JOIN Elements b ON a.type='Metal' AND b.type='Nonmetal'`. It works but uses an unconditional relationship in the join condition.
- **Filter subqueries first:** Cross join `SELECT symbol FROM Elements WHERE type='Metal'` with the equivalent nonmetal subquery. This makes predicate pushdown explicit.
- **No metals:** The filtered left set is empty, so no bonds are returned.
- **No nonmetals:** The filtered right set is empty, also producing no rows.
- **Noble-only table:** Both role sets are empty.
- **One metal and several nonmetals:** One row is emitted for each nonmetal.
- **Electron mismatch:** It does not matter because type alone defines a bond in this task.
- **Primary-key symbols:** They prevent duplicate logical element rows and remove any need for `DISTINCT`.
- **Any result order:** Omitting `ORDER BY` is correct.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(b)$. Let $r$ be the number of element rows, $M$ the number of metals, $N$ the number of nonmetals, and $b=M\cdot N$ the output size.
- **Auxiliary Space Complexity:** $O(b)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
