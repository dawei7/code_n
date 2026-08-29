# Guided Example: Minimum Height Trees

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "edges": [[1, 0], [1, 2], [1, 3]]}`
- **Required output:** `[1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A tree is an undirected graph in which any two vertices are connected by *exactly* one path. In other words, any connected graph without simple cycles is a tree.

The objective is to compute `[1]` from `{"n": 4, "edges": [[1, 0], [1, 2], [1, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why leaves cannot be the best roots in a nontrivial tree

A leaf has only one neighbor. If the tree has more than two nodes, moving the root from that leaf to its neighbor decreases the distance to every node reached through that neighbor—which is every other node in the tree—by one. The maximum distance cannot improve by staying at the outer leaf.

More generally, the nodes farthest from the center lie on the tree's periphery. Removing all peripheral leaves exposes the next inward layer without changing where the middle of the tree lies.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "edges": [[1, 0], [1, 2], [1, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Connection to a longest path

A diameter is a longest simple path in the tree. If its length is $D$ edges, rooting at a node $r$ cannot make both diameter endpoints closer than the larger of their distances from $r$. Along the unique path between those endpoints, that larger distance is minimized at the middle.

- If $D$ is even, the diameter has one middle node.
- If $D$ is odd, it has two adjacent middle nodes.

Those middle nodes minimize the greatest distance to all nodes and are precisely the minimum-height roots.

When all current leaves are removed simultaneously, both ends of every longest surviving path move inward by one edge. The middle node or middle pair does not change. Repeating this symmetric trimming eventually leaves the diameter's middle as the final layer.

This explains both why leaf peeling works and why there can be no more than two answers.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Building adjacency and degrees

The source builds an adjacency list `g`. For every undirected edge `[a, b]`, it appends `b` to `g[a]` and `a` to `g[b]`.

The parallel array `degree` initially stores the number of neighbors of every node. In a tree with at least two nodes, a current leaf is exactly a node with degree one. The initial queue contains all such nodes.

The graph is guaranteed to be a tree, so it is connected and has $n-1$ edges. For $n\ge2$, at least two leaves exist, ensuring that the initial queue is nonempty.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "edges": [[1, 0], [1, 2], [1, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Run BFS or DFS from every possible root:** Measuring every root's farthest distance is direct but costs $O(n^2)$ time on a tree, which is too slow for $n=2\cdot10^4$.
- **Find a diameter, then take its middle:** Run BFS or DFS from any node to find a farthest endpoint, run again from that endpoint while recording parents, and return the middle one or two nodes of the resulting diameter. This is also $O(n)$ time and $O(n)$ space.
- **Stop when at most two nodes remain:** Track a remaining-node count and halt before peeling the center layer. This is the common variant. The exact source instead processes all layers and preserves the last one in `ans`.
- **Process newly enqueued leaves immediately:** That would mix distance layers and could erase the intended final-layer distinction. Snapshotting `len(q)` keeps rounds simultaneous.
- **Use directed indegrees:** The input edges are undirected. Both adjacency directions and ordinary neighbor counts are required.
- **One node:** Its degree is zero, not one, so the normal queue would be empty. The explicit `n == 1` case correctly returns `[0]`.
- **Two nodes:** Both are leaves and both are valid minimum-height roots with height one.
- **Path with an odd number of nodes:** Repeated endpoint peeling leaves one middle node.
- **Path with an even number of nodes:** Peeling leaves two adjacent middle nodes.
- **Star:** All outer nodes are removed in the first round, leaving the central node as the sole answer.
- **Balanced tree:** Entire depth layers are peeled together until the central root or central edge remains.
- **Arbitrary labels:** Labels are exactly 0 through $n-1$, so they index `g` and `degree` directly.
- **Answer order:** The queue's discovery order determines output order, but any order is accepted.
- **Tree guarantee:** Connectivity and acyclicity are essential. A general graph may have no degree-one node or may leave a cyclic core, so this leaf-peeling proof would not apply.
- **No repeated edges:** Degree counts match actual distinct neighbors, and no duplicate adjacency entry can cause premature decrements.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The tree has $n$ nodes and $n-1$ edges. Building the two-sided adjacency list processes every edge once and stores two neighbor entries, costing $O(n)$ time and space. Computing initial leaves scans the $n$ degrees once.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
