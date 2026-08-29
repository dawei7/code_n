# Guided Example: Island Perimeter

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]}`
- **Required output:** `16`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given `row x col` `grid` representing a map where $\text{grid}[i][j] = 1$ represents land and $\text{grid}[i][j] = 0$ represents water.

The objective is to compute `16` from `{"grid": [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why one shared side removes two edges

Suppose two horizontal or vertical land squares touch. Adding four for each square initially counts the touching segment once as an edge of the first square and once as an edge of the second. The segment lies inside the combined shape, so both contributions are wrong. Subtracting two removes exactly those two copies.

No other perimeter contribution changes when the cells touch. Their remaining six unit edges stay exposed unless other neighbors cover them.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why checking only down and right is enough

Every orthogonally adjacent pair has one cell above the other or one cell left of the other. The upper cell sees the pair when checking downward; the lower cell must not count it again. Similarly, the left cell sees a horizontal pair when checking rightward.

Thus, checking down and right finds every shared side exactly once. Checking all four directions would find each shared side twice and would require subtracting one per neighbor rather than two. The exact formulation avoids redundant comparisons while keeping the simple `+4, -2` accounting.

Boundary checks prevent accessing outside the matrix:

- `i < m - 1` means a row below exists before reading `grid[i + 1][j]`.
- `j < n - 1` means a column to the right exists before reading `grid[i][j + 1]`.

An edge on the grid boundary has no neighboring cell and remains in the four-edge contribution, correctly counting the exterior water that conceptually surrounds the grid.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A compact formula

If $L$ is the number of land cells and $A$ is the number of orthogonally adjacent land-cell pairs, then the scan computes

$$
4L-2A.
$$

This equals the perimeter because the first term counts every edge of every land square, while the second removes both copies of every internal shared edge.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `16` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `16` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Check all four neighbors:** For every land cell, add one for each side adjacent to water or the exterior. It is equally $O(mn)$ and $O(1)$ but performs more neighbor checks.
- **Depth-first or breadth-first search:** Traverse the island and count exposed sides. This works, but needs a visited mechanism or input mutation and adds traversal machinery that whole-grid counting does not require.
- **Count land and adjacency separately:** First count all land cells and then all right/down land pairs; return `4 * land - 2 * pairs`. This is algebraically identical to the running update.
- **Single land cell:** No shared edges exist, so the result is four.
- **Land on a grid boundary:** Missing neighbors leave those unit edges counted as perimeter.
- **Diagonal land cells:** They do not share sides and therefore do not reduce one another's perimeter.
- **A thin line of cells:** Every consecutive pair removes two, leaving the perimeter of the resulting rectangle-like strip.
- **Water cells:** They add nothing; perimeter is attributed entirely through exposed land edges.
- **Multiple components outside the contract:** The formula would return their combined perimeter even though the source guarantees one island.
- **Input preservation:** The scan never changes any cell value.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let $m$ be the number of rows and $n$ the number of columns. The nested loops visit all $mn$ cells exactly once. Each cell triggers only a fixed number of comparisons and arithmetic operations, so time complexity is $O(mn)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
