# Guided Example: Count the Number of Complete Components

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 6, "edges": [[0, 1], [0, 2], [1, 2], [3, 4]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n`. There is an **undirected** graph with `n` vertices, numbered from `0` to $n - 1$. You are given a 2D integer array `edges` where $\text{edges}[i] = [a_{i}, b_{i}]$ denotes that there exists an **undirected** edge connecting vertices $a_{i}$ and $b_{i}$.

The objective is to compute `3` from `{"n": 6, "edges": [[0, 1], [0, 2], [1, 2], [3, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: First identify each connected component

Completeness is a property of an entire connected component. The solution builds an undirected adjacency list `g` by appending both directions for every edge `[a, b]`.

It then starts depth-first search from every still-unvisited vertex. One DFS reaches exactly the vertices in that start's component because it follows every adjacency and never crosses a nonexistent edge.

Array `vis` prevents revisiting vertices and ensures each component is processed once.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 6, "edges": [[0, 1], [0, 2], [1, 2], [3, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Collect two numbers during DFS

The helper returns a pair:

- `x`, the number of vertices in the explored component;
- `y`, the sum of the adjacency-list lengths of those vertices.

At one vertex `i`, the local values begin as `x = 1` and `y = len(g[i])`.

For each unvisited neighbor, recursion returns that neighbor subtree's pair, and the caller adds both totals. When the starting call finishes, its accumulated pair covers the full component.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The helper returns a pair:

- `x`, the number of vertices in... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why `y` counts every edge twice

An undirected edge between $u$ and $v$ appears once in `g[u]` and once in `g[v]`.

Adding all vertex degrees therefore counts that edge at both endpoints. If a component has $e$ undirected edges:

$$
y=2e.
$$

The solution intentionally uses this doubled count, avoiding division and keeping the comparison integral.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 6, "edges": [[0, 1], [0, 2], [1, 2], [3, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Check every pair inside each component:** Corr:** - **Check every pair inside each component:** Correct but can require $O(a^2)$ work per component.
- **Verify every vertex degree equals component size minus one:** Also linear after collecting component vertices and is equivalent for a simple connected graph.
- **Breadth-first search:** Can gather the same vertex and degree totals iteratively, avoiding recursion depth.
- **Disjoint-set union:** Can group vertices and then compare component sizes with edge counts, but requires more bookkeeping.
- **Isolated vertex:** Counts as a complete one-vertex component.
- **Two vertices with one edge:** Their degree sum is two, matching `2 * 1`, so the component is complete.
- **Two isolated vertices:** They are two separate complete components, not one two-vertex component.
- **Missing one edge:** The degree sum is two below the complete requirement and the component is rejected.
- **No repeated edges:** Essential for maximum edge count to imply every pair exists.
- **No self-loops:** Ensures degrees correspond only to distinct-vertex pairs.
- **Recursive depth:** Small repository constraints are safe; iterative traversal is more robust for a much larger graph.
- **Boolean arithmetic:** Python converts true to one and false to zero in `ans += condition`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+e)$. Building adjacency lists takes $O(e)$ time for $e$ edges. Across all DFS calls, each of $n$ vertices is visited once and each undirected edge is examined from both endpoints, so traversal takes $O(n+e)$. Total time is $O(n+e)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
