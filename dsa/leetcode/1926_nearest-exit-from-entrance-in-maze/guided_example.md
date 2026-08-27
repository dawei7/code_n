# Guided Example: Nearest Exit from Entrance in Maze

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"maze": [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], "entrance": [1, 0]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an `m x n` matrix `maze` (**0-indexed**) with empty cells (represented as `'.'`) and walls (represented as `'+'`). You are also given the `entrance` of the maze, where $entrance = [\text{entrance}_{row}, \text{entrance}_{col}]$ denotes the row and column of the cell you are initially standing at.

The objective is to compute `2` from `{"maze": [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], "entrance": [1, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Model the maze as an unweighted graph

Each empty cell is a graph vertex. Two empty cells share an edge when they are adjacent vertically or horizontally, because one legal move connects them. Every edge costs exactly one step. The task is therefore to find the shortest graph distance from the entrance to any border cell other than the entrance.

Breadth-first search is the natural shortest-path method for an unweighted graph. It visits all cells at distance $0$, then all cells at distance $1$, then distance $2$, and so on. Consequently, the first newly reached exit has the smallest possible distance.

The exact solution initializes `q = deque([(i, j)])` with the entrance and immediately changes `maze[i][j]` to `"+"`. Reusing the wall marker means “not available for another visit.” This serves two purposes: the entrance can never be enqueued again through a cycle, and an entrance already on the border is never mistaken for an exit.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"maze": [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], "entrance": [1, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Process one distance layer at a time

The variable `ans` starts at zero. At the start of each while-loop iteration, the queue contains exactly the cells at one common distance from the entrance. The code increments `ans`, records the current queue length, and removes exactly that many cells. Their unvisited neighbors are one step farther away, so those neighbors all have distance `ans`.

This ordering explains why the code returns `ans` when it discovers a border neighbor rather than storing a distance beside every queue entry. On the first loop iteration, it expands the distance-zero entrance after changing `ans` to one, so its neighbors are correctly labeled distance one. New cells appended during the loop are not processed in the same layer because `range(len(q))` evaluates the old queue size once. They wait for the next while iteration.

For each popped cell, the four direction pairs `[0, -1]`, `[0, 1]`, `[-1, 0]`, and `[1, 0]` produce left, right, up, and down neighbors. A neighbor is usable only if its row and column remain within the grid and `maze[x][y] == "."`. Walls and already visited cells both contain `"+"` and are skipped.

If a usable neighbor lies on row $0$, row $m-1$, column $0$, or column $n-1$, it is an exit. The method returns the current layer distance immediately. Otherwise it enqueues the neighbor and marks it as `"+"`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The variable `ans` starts at zero.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why marking happens when a cell is enqueued

A cell can be adjacent to several cells in the current BFS layer. If it remained `"."` until it was later removed from the queue, several parents could enqueue it, wasting work and breaking the simple one-visit bound. Marking immediately reserves the cell for the first path that reaches it. Because BFS reaches cells in nondecreasing distance, the first such path is already a shortest path, so ignoring later routes cannot lose a better answer.

The method modifies the supplied `maze` rather than allocating a separate visited matrix. After it returns, every cell discovered by BFS, including the entrance, has become `"+"`. That side effect is part of the exact implementation and should be understood by callers.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"maze": [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], "entrance": [1, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Depth-first search:** DFS can determine reacha:** - **Depth-first search:** DFS can determine reachability, but the first exit it encounters need not be the closest. Finding a shortest path would require exploring more routes and maintaining best distances.
- **Dijkstra's algorithm:** Dijkstra also finds shortest paths, but every move has unit cost, so its priority queue is unnecessary overhead. BFS is the specialized optimal method.
- **Separate visited set or matrix:** This avoids changing `maze` and still gives $O(RC)$ time and space. The exact solution chooses in-place marking to save that additional structure.
- **Entrance on the border:** It is explicitly not an exit. Marking it before the search and testing only newly discovered neighbors enforces this rule naturally.
- **Exit one move away:** The first layer increments `ans` to one and returns one as soon as it sees the adjacent border cell.
- **One-row or one-column maze:** Every cell is on a border, but the entrance is excluded. Any different reachable empty neighbor is an exit at its BFS distance; if none exists, the method returns `-1`.
- **Maze containing only the entrance:** The queue expands once, finds no valid neighbor, empties, and returns `-1`.
- **Several equally near exits:** BFS may return upon finding any one of them. Only the distance is requested, so direction order does not affect correctness.
- **Unreachable border cells:** A border opening behind walls is never enqueued and correctly does not influence the result.
- **Cycles in open corridors:** Immediate marking ensures each cell is visited once, preventing endless movement around a cycle.
- **Input mutation:** The exact method replaces visited `"."` cells with `"+"`. If the caller needs the original maze later, it must pass a copy or use a separate visited structure.
- **No exit:** Exhausting the deque proves that no reachable non-entrance border opening exists, so `-1` is the required sentinel.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(RC)$. Let $R$ be the number of rows and $C$ the number of columns.
- **Auxiliary Space Complexity:** $O(RC)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
