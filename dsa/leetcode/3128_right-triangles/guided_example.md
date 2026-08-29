# Guided Example: Right Triangles

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": [[0, 1, 0], [0, 1, 1], [0, 1, 0]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D boolean matrix `grid`.

The objective is to compute `2` from `{"grid": [[0, 1, 0], [0, 1, 1], [0, 1, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Choose the right-angle vertex first

A valid triangle has three cells containing 1. One cell is special: it shares its row with one of the other cells and its column with the remaining cell. That special cell is the right-angle vertex.

Fix a 1-cell at coordinates `(i, j)`. To complete a triangle with this cell as the vertex, we independently choose:

1. another 1 somewhere else in row $i$;
2. another 1 somewhere else in column $j$.

If row $i$ contains `rows[i]` ones in total, there are `rows[i] - 1` possible horizontal partners because the vertex itself must be excluded. Similarly, there are `cols[j] - 1` possible vertical partners.

Every horizontal choice can be combined with every vertical choice, so the number of triangles whose right angle is at `(i, j)` is

$$
(\texttt{rows[i]} - 1)(\texttt{cols[j]} - 1).
$$

The other two cells cannot accidentally be the same cell: a horizontal partner differs from the vertex's column, while a vertical partner differs from its row. Their coordinates therefore differ in both roles. They also do not have to be adjacent to the vertex; the definition permits any distance in the same row or column.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": [[0, 1, 0], [0, 1, 1], [0, 1, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Precompute row and column counts

Computing the row and column totals separately for every possible vertex would repeatedly scan the same cells. The first nested loop avoids that repetition.

The array `rows` has one entry for each row, and `cols` has one entry for each column. When the loop sees `grid[i][j]`:

- it adds that 0 or 1 to `rows[i]`;
- it adds the same value to `cols[j]`.

After this full pass, every row and column count is available in constant time.

The second nested loop visits all cells again. A zero cell cannot be part of a requested triangle, much less serve as its vertex, so `if x` skips it. For each 1-cell, the code adds the product of the two partner counts to `ans`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why this counts every triangle exactly once

First, every contribution created by the formula is valid. The current cell contains 1, the chosen horizontal partner contains 1 in the same row, and the chosen vertical partner contains 1 in the same column. These are three distinct cells and meet the definition.

Second, every valid triangle is included. By definition, it has a cell that shares a row with one selected cell and a column with the third. When the second pass reaches that right-angle cell, its horizontal partner is among the `rows[i] - 1` choices and its vertical partner is among the `cols[j] - 1` choices. Their pair contributes exactly one to the product.

Third, the same geometric triangle is not counted from another vertex. Of its three cells, only the right-angle cell shares a row with one other selected cell and a column with the other. Each of the two endpoint cells shares only one required axis relation within that triple. Therefore, the triangle appears under one and only one vertex.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": [[0, 1, 0], [0, 1, 1], [0, 1, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recount for each vertex:** Scan the vertex's row and column whenever a 1 is found. This uses little extra storage but can take $O(mn(m+n))$ time on a dense grid.
- **Store coordinates of ones:** Group 1-cell coordinates by row and column, then apply the same product formula. This can be attractive for a sparse representation, but the given dense matrix still takes $O(mn)$ time to read and the groups can use $O(mn)$ space.
- **Count triples directly:** Enumerating every triple of 1-cells is far more expensive and then requires testing row/column relationships. Choosing the unique right-angle vertex exposes independent choices immediately.
- **Single row or single column:** One of `rows[i] - 1` or `cols[j] - 1` is always zero, so the answer is correctly zero.
- **Isolated 1-cell:** Both partner counts are zero and it contributes nothing.
- **Several collinear ones:** They still contribute nothing unless some cell also has a partner on the perpendicular axis.
- **All-zero grid:** The second pass never enters the contribution branch, leaving `ans` equal to zero.
- **All-one grid:** Every cell is a possible right-angle vertex and contributes $(n-1)(m-1)$; no triangle is duplicated because its right-angle vertex is unique.
- **Non-adjacent cells:** Distance is irrelevant. Row and column totals deliberately include partners anywhere on the corresponding axis.
- **Subtracting the vertex:** Both counts include the current 1, so subtracting one from each is mandatory. Omitting either subtraction would allow the vertex to be selected as its own partner.
- **Boolean matrix representation:** The code relies on entries being numeric 0 or 1 so that adding `x` directly counts ones.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. Let $m$ be the number of rows and $n$ be the number of columns.
- **Auxiliary Space Complexity:** $O(m+n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
