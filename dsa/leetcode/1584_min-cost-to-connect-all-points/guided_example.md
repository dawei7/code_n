# Guided Example: Min Cost to Connect All Points

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"points": [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]}`
- **Required output:** `20`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where $\text{points}[i] = [x_{i}, y_{i}]$.

The objective is to compute `20` from `{"points": [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Recognizing a minimum spanning tree

Treat every point as a graph vertex. Any pair of points can be connected, so the graph is complete. The undirected edge between points `i` and `j` has weight equal to their Manhattan distance:

$$
\lvert x_i-x_j\rvert+\lvert y_i-y_j\rvert.
$$

The required connections must make all vertices reachable while leaving exactly one simple path between every pair. A connected undirected graph with exactly one simple path between each pair is a tree. Among all such spanning trees, the task asks for the one with minimum total edge weight: a minimum spanning tree, or MST.

The checked-in implementation uses Prim’s greedy algorithm. It grows one tree from vertex zero. At each step, it selects the unvisited vertex that can be attached to the current tree by the cheapest available edge.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"points": [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Materializing the complete weighted graph

The solution first creates `g` as an $N\times N$ matrix of zeros. For every pair with `i < j`, it computes the Manhattan distance `t` and assigns both:

`g[i][j] = g[j][i] = t`.

Writing both entries reflects that connections are undirected: the cost from `i` to `j` equals the cost from `j` to `i`. Restricting the computation to `j > i` prevents calculating every distance twice. The diagonal remains zero because connecting a point to itself is never a candidate MST edge.

This matrix makes all later edge-weight lookups constant time. It is important to describe this exact allocation because it differs from a matrix-free Prim implementation, which could calculate Manhattan distances during relaxation and use only linear auxiliary space.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The meaning of `dist` and `vis`

`vis[j]` records whether point `j` has already been added to the growing tree.

For an unvisited point `j`, `dist[j]` stores the cheapest edge found so far from any visited point to `j`. In other words, it is the least cost currently known for attaching `j` to the tree.

Initially, no actual point is in the tree, and every distance is infinity. The assignment `dist[0] = 0` creates an imaginary zero-cost connection to point zero. This lets the ordinary selection loop choose point zero first without a special-case insertion. Adding its zero distance to `ans` does not affect the final MST cost.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `20` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"points": [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `20` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Matrix-free optimized Prim:** Compute the Manhattan distance from the newly selected point to each unvisited point during relaxation. It keeps the same $O(N^2)$ time and reduces explicit auxiliary space to $O(N)$; this is the variant matching the manifest’s stated space bound.
- **Heap-based Prim:** A priority queue can select candidate edges, but a complete graph may place $O(N^2)$ edges in the heap and cost $O(N^2\log N)$ time and $O(N^2)$ space.
- **Kruskal’s algorithm:** Generate all $\binom{N}{2}$ edges, sort them, and use union-find to avoid cycles. It is correct but takes $O(N^2\log N)$ time and $O(N^2)$ edge storage.
- **Connecting each point to its nearest neighbor:** Independent nearest choices can form disconnected clusters or cycles. MST construction must reason about connectivity of the whole growing component.
- **One point:** `g` is a one-cell matrix, point zero is selected with distance zero, and the answer is zero because no real edge is needed.
- **Two points:** The second point’s `dist` becomes their Manhattan distance, so that sole required edge is returned.
- **Equal edge weights:** The selection scan keeps one tied minimum. Any lightest crossing edge is safe, and the minimum total cost is unchanged.
- **Negative coordinates:** Manhattan distance uses absolute coordinate differences, so negative coordinates require no special branch.
- **Distinct point guarantee:** Separate vertices never have identical coordinate pairs, although different edges may still have zero only on the diagonal. The algorithm would remain structurally valid with duplicates, but the source contract excludes them.
- **Complete-graph connectivity:** An index is always found after initialization because every point connects to every other point. On a general disconnected graph, the `i == -1` state would need explicit impossibility handling.
- **No parent array:** The source returns only total cost. It does not retain which particular edge produced `dist[i]`, so it cannot reconstruct the MST without an additional parent structure.
- **Input preservation:** The points list is read-only. The distance matrix, visited flags, and best distances are separate allocations.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$. Let $N$ be the number of points.
- **Auxiliary Space Complexity:** $O(N^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
