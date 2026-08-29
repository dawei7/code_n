# Guided Example: Check if Matrix Is X-Matrix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A square matrix is said to be an **X-Matrix** if **both** of the following conditions hold:

The objective is to compute `true` from `{"grid": [[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Classify a cell by its coordinates

An X-Matrix has two diagonals:

- the main diagonal from the top-left corner to the bottom-right corner;
- the secondary diagonal from the top-right corner to the bottom-left corner.

For zero-based coordinates `(i, j)` in an `n x n` matrix, a cell lies on the main diagonal exactly when `i == j`. It lies on the secondary diagonal exactly when `i + j == n - 1`.

Every matrix position belongs to one of two required categories. If either diagonal condition holds, its value must be nonzero. If neither holds, its value must be zero. The solution checks this classification directly for every cell.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Visit every row and every value

The outer loop uses `enumerate(grid)` to obtain row index `i` and the row itself. The inner `enumerate(row)` obtains column index `j` and value `v`. This visits coordinates in ordinary row-major order, although correctness does not depend on that particular traversal order.

The diagonal branch is

`if i == j or i + j == len(grid) - 1`.

The logical OR is important because a position on either diagonal has the same nonzero requirement. In an odd-sized matrix, the central cell lies on both diagonals, but it is still one cell and is checked once by this combined condition.

If a diagonal value is zero, the method immediately returns `false`. One violation is enough to disqualify the matrix, so no remaining cells need examination.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Require zero everywhere else

The `elif v` branch runs only when neither diagonal condition held. In Python, an integer is truthy exactly when it is nonzero. Therefore `elif v` means “this off-diagonal value is nonzero.” Such a value violates the second X-Matrix condition, so the method returns `false`.

An off-diagonal zero is falsy, so no return occurs and scanning continues. The code could spell this as `elif v != 0`; the shorter truthiness test is equivalent under the integer-valued grid contract.

Only after every coordinate satisfies its category requirement does execution reach `return true`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Check the two diagonals first, then all other cells:** This can work, but avoiding double-checks of diagonal coordinates in the second pass requires the same coordinate classification. A single pass is simpler.
- **Build a set of diagonal coordinates:** Precompute all `(i, i)` and `(i, n-1-i)` pairs, then test membership for every cell. This uses `O(n)` extra space for formulas that are already constant-time.
- **Count nonzero cells:** An X-Matrix has `2n` nonzero diagonal positions when `n` is even and `2n-1` when odd, but the count alone cannot prove that the nonzeros are in the correct locations.
- **Sum diagonal values:** Nonzero values can cancel if negatives were allowed, and even with nonnegative values a sum does not verify off-diagonal zeros. Per-cell conditions are direct and reliable.
- **Use only `i == j`:** This checks the main diagonal but misses the secondary diagonal from top right to bottom left.
- **Use `i + j == n`:** Zero-based secondary-diagonal coordinates sum to `n - 1`, not `n`. The latter is an off-by-one error.
- **Logical AND between diagonal tests:** A cell needs to be on either diagonal, not both. AND would classify only the odd-sized center as diagonal.
- **Odd-sized center:** It belongs to both diagonals and must simply be nonzero; the OR condition handles it once.
- **Even-sized matrix:** There is no shared center cell, but both formulas still identify exactly `2n` diagonal positions.
- **Zero on a diagonal corner:** The first inspected corner may cause immediate failure. Corners `(0,0)` and `(0,n-1)` lie on the two diagonals.
- **Nonzero beside a diagonal:** Even if all diagonal entries are correct, any such off-diagonal value causes `false`.
- **All-zero matrix:** It satisfies the off-diagonal condition but fails at the first diagonal cell, so it is not an X-Matrix.
- **All-nonzero matrix:** It satisfies the diagonal condition but fails as soon as an off-diagonal cell is inspected.
- **Truthiness of negative values:** The source values are nonnegative, but Python would also treat a negative integer as nonzero, which is the correct requirement for either category test.
- **Square-shape guarantee:** The coordinate formulas use `len(grid)` for both dimensions. The contract guarantees every row has that length; a ragged or rectangular input is outside scope.
- **Input mutation:** Enumeration reads existing rows and values only, leaving `grid` unchanged.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let `n` be the side length. In the worst case, the nested loops inspect all `n^2` cells. Each inspection performs constant-time index comparisons and a value test, so worst-case running time is `O(n^2)`. An invalid matrix may return earlier—possibly after its first cell—but asymptotic worst-case analysis must include a valid matrix or a violation at the final inspected cell.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
