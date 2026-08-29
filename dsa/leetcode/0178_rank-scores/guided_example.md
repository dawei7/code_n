# Guided Example: Rank Scores

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Scores": [{"id": 1, "score": 8}]}}`
- **Required output:** `{"columns": ["score", "rank"], "rows": [[8, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Scores`

The objective is to compute `{"columns": ["score", "rank"], "rows": [[8, 1]]}` from `{"tables": {"Scores": [{"id": 1, "score": 8}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use dense rank because ties must not create gaps

The required sequence is a dense ranking:

- the highest distinct score receives rank one;
- equal scores receive the same rank;
- the next lower distinct score receives the next consecutive integer.

`DENSE_RANK()` implements exactly these rules. It differs from `ROW_NUMBER`,
which would give tied rows different numbers, and from `RANK`, which would skip
numbers after a tie.

The query applies the function as a window expression so that every input game
row remains in the output. A `GROUP BY score` would collapse ties into one row,
violating the requirement to retain every score row.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Scores": [{"id": 1, "score": 8}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Order the ranking window by score descending

The window clause is:

`OVER (ORDER BY score DESC)`.

This tells `DENSE_RANK` to process higher score values before lower ones. Rows
with equal `score` are peers and receive the same rank. Whenever the score
changes to a lower distinct value, the rank increases by one.

No `PARTITION BY` appears, so all rows belong to one global competition. Adding
a partition would restart ranking separately for each partition and answer a
different question.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Trace the sample ranks

The highest distinct value is 4.00. Both rows with that value are peers and
receive rank one.

The next lower value is 3.85, so it receives rank two. The two rows at 3.65
share rank three. Finally, 3.50 receives rank four.

The rank after the two 4.00 rows is two rather than three. That no-gap behavior
is precisely why dense rank is selected.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["score", "rank"], "rows": [[8, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Scores": [{"id": 1, "score": 8}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["score", "rank"], "rows": [[8, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Correlated distinct count:** Compute one plus the number of distinct greater scores for each row. It is clear mathematically but can be $O(n^2)$.
- **Self-join and grouping:** Join each row with scores greater than or equal to it, then count distinct joined values; also potentially quadratic.
- **`RANK()`:** Incorrect because ties create gaps in later ranks.
- **`ROW_NUMBER()`:** Incorrect because tied rows receive different numbers.
- **All scores equal:** Every row receives rank one.
- **Repeated ties:** Every peer is retained and shares one dense rank.
- **One row:** Receives rank one.
- **Required row order:** Add an outer `ORDER BY score DESC`; window ordering alone is insufficient.
- **MySQL version:** Window functions require MySQL 8.0 or newer.
- **Alias syntax:** `'rank'` works in MySQL's select alias context but an identifier quote is clearer.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the score-row count. A typical window plan sorts rows by score in
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
