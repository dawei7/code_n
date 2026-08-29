# Guided Example: Symmetric Coordinates

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Coordinates": [{"X": 4, "Y": 4}]}}`
- **Required output:** `{"columns": ["x", "y"], "rows": []}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Coordinates`

The objective is to compute `{"columns": ["x", "y"], "rows": []}` from `{"tables": {"Coordinates": [{"X": 4, "Y": 4}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What symmetry means for ordinary and diagonal pairs

A row `(X,Y)` has a symmetric partner when another row `(Y,X)` exists. For unequal coordinates, one row in each direction is sufficient. The output keeps only the orientation satisfying `X <= Y`, so `(20,21)` is returned while `(21,20)` is not.

Diagonal coordinates require special care. A row `(20,20)` reverses to the same values, but the problem’s pair interpretation requires two coordinate rows. One physical row must not partner with itself. Therefore, `(x,x)` qualifies only when it occurs at least twice.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Coordinates": [{"X": 4, "Y": 4}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Give duplicate rows temporary identities

The CTE `P` selects every input row and assigns `ROW_NUMBER() OVER () AS id`. The order of these IDs is irrelevant. Their only purpose is to distinguish physical occurrences that have identical `x` and `y` values.

The query joins `P AS p1` to `P AS p2` under four effective conditions:

- `p1.x = p2.y`;
- `p1.y = p2.x`;
- `p1.x <= p1.y`; and
- `p1.id != p2.id`.

The first two conditions enforce reversal. The third keeps the canonical lower-or-equal orientation. The fourth requires two distinct source rows.

For an off-diagonal pair such as `(20,21)` and `(21,20)`, their IDs are naturally different. For two copies of `(20,20)`, each can join the other. For only one copy, the equal-ID candidate is rejected and no result is produced.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why `DISTINCT` is still required

The table may contain duplicates. If there are three copies of `(20,21)` and four copies of `(21,20)`, the self-join creates twelve matching row pairs. The requested output contains the unique coordinate only once. `SELECT DISTINCT p1.x, p1.y` collapses all those physical matches into one logical result.

Diagonal duplicates also create multiple ordered ID pairs, and `DISTINCT` similarly reduces them to one output row.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["x", "y"], "rows": []}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Coordinates": [{"X": 4, "Y": 4}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["x", "y"], "rows": []}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Aggregate by `x,y` first:** Store `COUNT(*)` for each coordinate, join one distinct row to its reverse, and require count at least two for diagonals. This avoids duplicate cross products and matches the manifest summary.
- **Use `EXISTS`:** A correlated existence test can stop after finding one partner, but it still needs a distinct output and an explicit different-row mechanism for diagonal values.
- **Omit row IDs:** Then a single `(x,x)` row can join itself and be incorrectly reported.
- **Omit `x <= y`:** Both `(x,y)` and `(y,x)` would appear for off-diagonal pairs.
- **Omit `DISTINCT`:** Duplicate input rows can generate many repeated output coordinates.
- **One diagonal row:** It is not enough; `id != id` rejects self-pairing.
- **Two or more diagonal rows:** At least one different-ID pairing exists, and the coordinate appears exactly once after `DISTINCT`.
- **Heavy duplicates:** The result remains correct, but the exact row-level join may have quadratic intermediate cardinality.
- **Unordered `ROW_NUMBER`:** Deterministic numbering is unnecessary because only ID inequality matters.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R^2)$. Let $R$ be the number of input rows and $D$ the number of distinct qualifying output coordinates. Assigning IDs and scanning rows is at least $O(R)$. The self-join can produce $\Theta(R^2)$ matches under heavy duplicate reversal, and duplicate elimination must process that logical result unless optimized away. Final ordering costs $O(D\log D)$.
- **Auxiliary Space Complexity:** $O(D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
