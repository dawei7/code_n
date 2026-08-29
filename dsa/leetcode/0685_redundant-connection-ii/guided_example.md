# Guided Example: Redundant Connection II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"edges": [[1, 2], [1, 3], [2, 3]]}`
- **Required output:** `[2, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

In this problem, a rooted tree is a **directed** graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The objective is to compute `[2, 3]` from `{"edges": [[1, 2], [1, 3], [2, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why there are only two incoming-edge candidates

The array `ind` counts incoming edges. For every directed edge `u -> v`, the code increments `ind[v - 1]`. Node labels are one-based, while list indices are zero-based.

The original rooted tree gave every non-root node one incoming edge and the root none. Adding one edge increases the indegree of exactly one destination. Therefore, if some node has indegree two, exactly two input edges point to that child. One is its original tree-parent edge and the other is the added edge, although the input does not reveal which is which.

The comprehension that builds `dup` records the indices of all edges whose destination has final indegree two. Under the source contract, `dup` is either empty or contains exactly two indices in increasing input order:

- `dup[0]` is the earlier incoming edge to that child;
- `dup[1]` is the later incoming edge to the same child.

This reduces the two-parent case to deciding which of those two edges is incompatible with a rooted tree.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"edges": [[1, 2], [1, 3], [2, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What union-find tests

The parent array `p` represents connected components of the edges currently being considered. The nested `find` follows parent pointers to a representative and performs path compression:

`p[x] = find(p[x])`.

Although the source edges are directed, union-find intentionally examines their underlying undirected connectivity. If endpoints `u` and `v` already share a representative, an undirected path between them already exists. Adding another edge between them closes a cycle. If their representatives differ, `p[pu] = pv` merges the two components.

The direction used for the union-find parent pointer is unrelated to the graph's parent-child direction. The array `p` is merely a connectivity data structure; it is not trying to reproduce the rooted tree's directed parent relation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Case 1: no node has two parents

If `dup` is empty, every node has indegree at most one. Because the graph has `n` nodes and `n` edges, the extra edge must have produced a cycle. The solution scans edges in their original order and unions their endpoints.

When an edge `[u, v]` has `find(u - 1) == find(v - 1)`, its endpoints were already connected by earlier edges. That edge is the one that closes the cycle in input order, so it is returned.

Returning the first cycle-closing edge also satisfies the “last answer in the input” rule. Among the edges belonging to the unique cycle, all earlier cycle edges must already be present before the final cycle edge can find an alternative path between its endpoints. Thus the first edge detected by forward union-find is the last-listed edge on that cycle.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"edges": [[1, 2], [1, 3], [2, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit validation of each candidate:** Identify the two incoming edges, remove candidates from later to earlier, and run a directed traversal to test whether all nodes form one rooted tree. This is easier to visualize but can require more graph construction and repeated work.
- **Directed parent-map and cycle traversal:** One can follow parent pointers to locate a directed cycle and combine that information with the indegree-two candidates. It can also be linear, but the case analysis is easier to implement incorrectly.
- **Union-find with rank or size:** A rank or component-size array makes the asymptotic guarantee match the standard `O(n\alpha(n))` claim while preserving all decisions in this solution.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \alpha(N))$. Let `n` be the number of nodes. The source guarantees `len(edges) == n`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
