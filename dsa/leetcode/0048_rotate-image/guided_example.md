# Guided Example: Rotate Image

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}`
- **Required output:** `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90** degrees (clockwise).

The objective is to compute `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]` from `{"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Start from the coordinate rule for a clockwise rotation

In an $n \times n$ matrix, an element originally at row $r$ and column $c$ must end at row $c$ and column $n - 1 - r$ after a $90^\circ$ clockwise rotation:

$$
(r,c) \longmapsto (c,n-1-r).
$$

Moving every element directly to its destination would overwrite values that have not yet moved unless four-cell cycles are handled carefully. The selected solution instead decomposes the coordinate rule into two familiar in-place reflections: reverse the order of the rows, then transpose across the main diagonal.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: First transformation: flip top and bottom

The first nested loop swaps row `i` with row `n - i - 1`, one column at a time. Only `n >> 1`, which equals integer floor division by two for nonnegative `n`, top rows are processed. This prevents swapping each pair twice.

After this vertical or horizontal-axis mirror, an original coordinate `(r, c)` has moved to `(n - 1 - r, c)`. For a three-by-three matrix,

`[[1,2,3],[4,5,6],[7,8,9]]`

becomes

`[[7,8,9],[4,5,6],[1,2,3]]`.

When $n$ is odd, the middle row is not swapped, which is correct because it mirrors to itself. Every element in paired rows is exchanged using Python's simultaneous assignment, so neither value is lost.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Second transformation: transpose the main diagonal

Transposition maps coordinate `(a, b)` to `(b, a)`. The source loops over each row `i` and only columns `j < i`, which is the strict lower triangle. It swaps `matrix[i][j]` with `matrix[j][i]`, the corresponding position in the strict upper triangle.

The main diagonal is omitted because `(i, i)` maps to itself. Processing only one triangle is essential: if both `(i, j)` and `(j, i)` were visited as starting cells, the second swap would undo the first.

Applied to the row-reversed example, transposition produces `[[7,4,1],[8,5,2],[9,6,3]]`, the required clockwise rotation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Transpose first, then reverse each row:** Main-diagonal transposition followed by a left-to-right reversal also maps `(r,c)` to `(c,n-1-r)`. It is the most common equivalent decomposition.
- **Four-cell cyclic swaps:** Process one quadrant and rotate top, left, bottom, and right values in groups of four. It performs one direct rotation pass but has more intricate index formulas.
- **Allocate a new matrix:** Write each original value directly to `out[c][n-1-r]`. This is very easy to verify but violates the in-place requirement and uses $O(n^2)$ extra space.
- **Anti-diagonal reflection plus top/bottom flip:** This is another valid composition. Its reflection coordinates differ, so mixing formulas between decompositions would rotate or reflect incorrectly.
- **One-by-one matrix:** Both loops perform no swaps, leaving the sole value unchanged, which is the correct rotation.
- **Odd dimension:** The middle row is unchanged by the first flip, and diagonal cells are unchanged by transposition; off-axis cells still move normally.
- **Even dimension:** Every row participates in exactly one first-phase pair, with no special center.
- **Negative or repeated values:** Rotation depends only on positions, so value magnitude and equality have no effect.
- **Calling the method twice:** Two clockwise rotations produce a $180^\circ$ rotation; each call is an independent in-place coordinate transformation.
- **Return behavior:** The absence of `return` is intentional. Callers inspect the same matrix object after the method completes.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. The row-reversal phase swaps approximately $n^2/2$ element pairs: `floor(n/2)` row pairs times $n$ columns. The transpose phase swaps $n(n-1)/2$ off-diagonal pairs. Their sum is proportional to $n^2$, so time is $O(n^2)$. This is optimal up to constants because a rotation must place all $n^2$ matrix entries.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
