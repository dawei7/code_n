# Guided Example: Pacific Atlantic Water Flow

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"heights": [[1]]}`
- **Required output:** `[[0, 0]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is an `m x n` rectangular island that borders both the **Pacific Ocean** and **Atlantic Ocean**. The **Pacific Ocean** touches the island's left and top edges, and the **Atlantic Ocean** touches the island's right and bottom edges.

The objective is to compute `[[0, 0]]` from `{"heights": [[1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reverse the direction of the search

Water flows from a cell to an orthogonally adjacent cell of equal or lower height. Starting a separate search from every cell would repeatedly explore many of the same paths. Instead, the solution starts from each ocean's boundary and traverses the flow relation backward.

If water can flow forward from a cell `A` to a neighbor `B`, then `height[A] >= height[B]`. A reverse search standing at `B` may therefore move to `A` when `height[A] >= height[B]`. Every cell reached by that reverse search has a valid forward downhill-or-level path to the ocean.

The algorithm performs this reverse breadth-first search twice: once from all Pacific boundary cells and once from all Atlantic boundary cells. A cell belongs in the answer exactly when both searches reach it.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"heights": [[1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Seed each ocean with every directly touching cell

The Pacific touches the left and top edges. For every row `i`, `(i, 0)` is placed in `q1` and marked in `vis1`; for every column `j`, `(0, j)` is also seeded.

The Atlantic touches the right and bottom edges. The corresponding seeds are `(i, n - 1)` and `(m - 1, j)` in `q2` and `vis2`.

Marking a cell when it is enqueued is important. Later traversal edges will not enqueue that cell again, preventing cycles on equal-height plateaus. The two corners shared by an ocean's two boundary loops can be inserted twice before BFS begins, but this is only a constant amount of harmless duplicate processing. Their visited flags are already true, so they do not cause their neighbors to be repeatedly enqueued.

For a one-cell grid, the sole coordinate belongs to all four conceptual edges. Both visited matrices mark it, and it correctly appears once in the final row-major scan.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Traverse four orthogonal directions

The tuple `dirs = (-1, 0, 1, 0, -1)` is a compact direction encoding. `pairwise(dirs)` yields

`(-1,0)`, `(0,1)`, `(1,0)`, and `(0,-1)`,

representing up, right, down, and left. Diagonal movement is never generated.

For a dequeued cell `(x, y)`, the candidate neighbor is `(nx, ny) = (x + dx, y + dy)`. It is enqueued only when all of the following are true:

- its row lies in `[0, m)`;
- its column lies in `[0, n)`;
- this ocean's visited matrix has not marked it; and
- `heights[nx][ny] >= heights[x][y]`.

The last comparison is the reversed flow rule. It may feel counterintuitive because the search climbs uphill, but the path is being discovered from ocean to source. Reversing the discovered path makes every step go from high or equal elevation to low or equal elevation, which is exactly how water travels.

Once accepted, the neighbor is marked before being appended to the queue. Each cell is therefore enqueued at most once per ocean during normal traversal.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[0, 0]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"heights": [[1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[0, 0]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Run DFS or BFS from every cell:** This directly tests whether each source reaches both oceans but can revisit the grid for every source, reaching $O((rc)^2)$ time in a worst case.
- **Reverse depth-first search:** The same multi-source and reversed-height reasoning works with DFS and still takes $O(rc)$ time. Recursive DFS risks a call stack as deep as the number of cells; the deque avoids that risk.
- **One traversal carrying ocean bit flags:** Reachability information can be combined in other graph formulations, but two independent searches make the proof and state separation simple.
- **Use the forward inequality during reverse search:** Checking `neighbor <= current` from the ocean is wrong; it finds cells the ocean could flow downhill into, not cells whose rain can flow to the ocean. Reverse traversal must accept equal-or-higher neighbors.
- **Equal-height plateaus:** The `>=` comparison permits movement across equal cells in either direction, as required. Visited marking prevents endless cycles.
- **Single row:** Every cell touches both the top Pacific edge and bottom Atlantic edge, so every coordinate is returned.
- **Single column:** Every cell similarly touches both left and right ocean edges and is returned.
- **One cell:** It touches both oceans and appears in the intersection.
- **Strictly rising terrain:** Reverse traversal climbs from each ocean until blocked according to the opposing boundary; the intersection still follows from the same reachability proof.
- **Boundary duplication:** Corner cells may be seeded twice in one queue, but they are never duplicated in the result because the final scan tests Boolean matrices once per coordinate.
- **No diagonal flow:** `pairwise(dirs)` creates exactly four orthogonal moves and cannot cross a corner diagonally.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(rc)$. Let $r=m$ be the number of rows and $c=n$ the number of columns. For each ocean, every cell is marked and enqueued at most once through traversal, and each dequeue checks four neighbors. Boundary corner duplication adds only constant extra work. Two BFS runs therefore take $O(rc)$ time. The final intersection scan also takes $O(rc)$ time, leaving total time $O(rc)$.
- **Auxiliary Space Complexity:** $O(rc)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
