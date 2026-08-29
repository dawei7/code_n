# Guided Example: Stamping the Grid

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[0, 0], [0, 0]], "stampHeight": 2, "stampWidth": 2}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` binary matrix `grid` where each cell is either `0` (empty) or `1` (occupied).

The objective is to compute `true` from `{"grid": [[0, 0], [0, 0]], "stampHeight": 2, "stampWidth": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build a prefix sum of occupied cells

The matrix `s` has dimensions $(m+1)$ by $(n+1)$. Its extra top row and left column remain zero. The code uses one-based coordinates for grid cells and fills

$$
s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+\texttt{grid}[i-1][j-1].
$$

Thus `s[i][j]` equals the number of occupied cells in the rectangle from the original top-left corner through one-based cell $(i,j)$.

For a proposed stamp whose top-left corner is $(i,j)$ and bottom-right corner is $(x,y)$, inclusion-exclusion gives its number of occupied cells:

$$
s[x][y]-s[x][j-1]-s[i-1][y]+s[i-1][j-1].
$$

The full prefix rectangle contributes first. The area above the stamp and the area left of it are subtracted, and their overlap was subtracted twice, so it is added back. A result of zero means every cell under that placement is empty. The query costs $O(1)$ regardless of the stamp’s area.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[0, 0], [0, 0]], "stampHeight": 2, "stampWidth": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Enumerate exactly the placements that stay inside

The top row `i` ranges from `1` through `m - stampHeight + 1`, expressed by `range(1, m - stampHeight + 2)`. Likewise, `j` ranges through `n - stampWidth + 1`. For each top-left corner, the code computes

`x = i + stampHeight - 1` and `y = j + stampWidth - 1`.

These formulas include exactly `stampHeight` rows and `stampWidth` columns. If a stamp dimension is larger than the grid’s corresponding dimension, the relevant range is empty, so no illegal out-of-bounds placement is considered.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Record a whole valid rectangle with four updates

When the occupied-cell sum is zero, every cell in the proposed rectangle is legally coverable. Marking all of those cells immediately would cost the stamp area per placement and could become far too slow. Instead, the solution uses a two-dimensional difference matrix `d`.

For an inclusive rectangle from $(i,j)$ through $(x,y)$, it performs:

- `d[i][j] += 1` to start a contribution;
- `d[i][y + 1] -= 1` to stop it after the right edge;
- `d[x + 1][j] -= 1` to stop it after the bottom edge;
- `d[x + 1][y + 1] += 1` to repair the corner that both negative updates affect.

The extra padding in the $(m+2)$ by $(n+2)$ matrix makes `x + 1` and `y + 1` safe even when a stamp touches the bottom or right border.

These four values are not coverage counts yet. They are boundaries whose two-dimensional prefix sum will later add one to exactly the cells inside the rectangle.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[0, 0], [0, 0]], "stampHeight": 2, "stampWidth": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Scan every stamp rectangle directly:** This is easy to describe but may cost $O(mn \cdot \textit{stampHeight}\cdot\textit{stampWidth})$. The occupied-cell prefix sum reduces each legality test to $O(1)$.
- **Paint every valid rectangle directly:** Even with constant-time legality checks, writing every covered cell for every stamp can be superlinear. The difference grid records each rectangle in four operations.
- **Greedy placement around uncovered cells:** Choosing a stamp locally is unnecessary and can be difficult near obstacles. Because overlap is allowed and stamps do not consume resources, the union of all legal placements is the complete feasibility test.
- **Stamp larger than the grid:** No placement loop iteration occurs. The result is true only when there are no empty cells requiring coverage; otherwise the final scan finds an uncovered zero.
- **Grid with no empty cells:** No stamp is required. The final condition checks only cells where `v == 0`, so it correctly returns true.
- **All-empty grid:** Every in-bounds stamp position is legal. The result depends solely on whether those rectangles cover every border and interior cell.
- **One-by-one stamp:** Every empty cell has its own legal placement, so all zeros become covered and occupied cells are skipped.
- **One-row or one-column grid:** The same rectangle formulas work because the padded prefix matrices eliminate special boundary branches.
- **Overlapping stamps:** Difference counts may exceed one, but the test needs only positive versus zero coverage. Overlap never invalidates a placement.
- **Occupied cells:** They may have zero coverage and are deliberately ignored in the final rejection condition.
- **Bottom and right borders:** The $(m+2)$ by $(n+2)$ padding safely receives the difference updates just outside a border-touching stamp.
- **Off-by-one coordinates:** `grid` is zero-based, while `s` and `d` are used with one-based cell coordinates. The enumerations with `enumerate(..., 1)` maintain this mapping consistently.
- **Early false return:** Once an uncovered empty cell is found after all valid placements have been accumulated, later cells cannot change its coverage, so stopping is conclusive.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let $m$ and $n$ be the grid dimensions. Building `s` visits all $mn$ cells once. There are at most $(m-\textit{stampHeight}+1)(n-\textit{stampWidth}+1)$ in-bounds placements, which is at most $mn$, and each uses one constant-time prefix query plus at most four difference updates. Reconstructing `d` and checking coverage visits all $mn$ cells once. Total time is $O(mn)$.
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
