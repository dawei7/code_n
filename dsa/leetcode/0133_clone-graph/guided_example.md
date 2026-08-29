# Guided Example: Clone Graph

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"adj_list": [[2, 4], [1, 3], [2, 4], [1, 3]]}`
- **Required output:** `[[2, 4], [1, 3], [2, 4], [1, 3]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a reference of a node in a **<a href="https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph" target="_blank">connected</a>** undirected graph.

The objective is to compute `[[2, 4], [1, 3], [2, 4], [1, 3]]` from `{"adj_list": [[2, 4], [1, 3], [2, 4], [1, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A deep copy must preserve relationships, not identities

Returning the original starting node would reproduce the visible graph but would not be a clone. A deep copy requires one new object for every reachable original node. Each cloned node must have the same value, and its neighbor list must point only to cloned nodes in the same order as the original neighbor list.

Graphs make this harder than copying a tree. A node can have several incoming edges, and an undirected edge appears in both endpoints’ neighbor lists. Cycles are therefore normal. Recursing from `A` to `B` and then following `B` back to `A` would never terminate unless the algorithm remembers that `A` already has a clone.

The dictionary `g` is the central structure. It maps each original node object to the unique new node representing it:

`original node -> cloned node`

This mapping simultaneously prevents infinite traversal, preserves shared references, and guarantees that two edges pointing to the same original also point to the same clone.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"adj_list": [[2, 4], [1, 3], [2, 4], [1, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create the clone before following edges

The nested function `dfs(node)` first handles `null`, which represents the empty graph. It then checks whether the original node is already in `g`. If so, the function immediately returns the existing clone.

For a newly seen node, the function performs these steps in a crucial order:

1. create a new `Node` containing the same `val`;
2. store that clone in `g`;
3. recursively clone each neighbor;
4. append each returned neighbor clone to the new node’s neighbor list.

The dictionary insertion must happen before recursion. Consider two connected nodes `A` and `B`. While cloning `A`, recursion begins cloning `B`. When `B` follows its edge back to `A`, `A` is already in `g`, so that call returns the partially constructed clone of `A` instead of creating another object or recursing forever.

It is safe to return a clone before all its neighbors have been filled. Graph nodes are mutable reference objects. The returned reference points to the same clone that the original call continues populating, so later appends become visible through every edge already connected to it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What one DFS result guarantees

Whenever `dfs(x)` returns, its return value is the one clone assigned to original node `x`. It has the same value. For each neighbor entry in `x.neighbors`, the clone’s list receives the result of cloning that exact original neighbor.

If a neighbor was unseen, recursion constructs it. If it was already seen, the dictionary supplies the previously created object. This distinction preserves graph topology:

- a cycle closes back to an existing clone;
- two originals sharing one neighbor also share one neighbor clone;
- parallel references would remain parallel references, although the stated graph has no repeated edges;
- the order of neighbor entries is preserved because the loop appends results in original order.

The mapping gives uniqueness. Only the branch for a node absent from `g` calls `Node(node.val)`, and that branch immediately inserts the result. Every later request for the same original returns that object. Thus there is exactly one clone per reachable original.

It also gives independence. Every mapped value was produced by a `Node` constructor, and neighbor lists contain those new values rather than original keys. Mutating a cloned node or its neighbor list therefore does not mutate the original graph.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[2, 4], [1, 3], [2, 4], [1, 3]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"adj_list": [[2, 4], [1, 3], [2, 4], [1, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[2, 4], [1, 3], [2, 4], [1, 3]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Breadth-first cloning:** Create the starting clone, then use a queue to discover originals and connect their clones. It avoids recursion depth while using the same original-to-clone map.
- **Iterative depth-first cloning:** A manual stack follows depth-first order without relying on Python’s call stack. Its asymptotic bounds are unchanged.
- **Two-pass traversal:** First discover every vertex and create every clone, then traverse edges to fill neighbor lists. It can make the phases explicit but requires revisiting adjacency lists.
- **Map by node value:** Unique values make this possible under the stated contract, but mapping by original object is more robust and directly preserves identity even if value uniqueness changes.
- **Empty graph:** `null` returns `null`; no clone or dictionary entry is created.
- **Single isolated node:** Exactly one new node is returned with an empty neighbor list.
- **Cycles:** Storing a clone before descending is essential; moving `g[node] = cloned` after the neighbor loop would recurse forever.
- **Self-loops and repeated edges:** The contract excludes them, but the mapping-based algorithm would still clone them faithfully, including repeated neighbor-list entries.
- **Hashability:** Original nodes are dictionary keys. Ordinary Python objects are identity-hashable unless their class overrides equality without a compatible hash.
- **Runtime dependency:** The selected file imports `Optional` but calls `defaultdict` without importing it. A standalone execution needs `from collections import defaultdict`; a plain `{}` would also provide every operation this code uses.
- **Platform-provided type:** `Node` appears only inside a triple-quoted template block because the platform supplies it. The user solution should not recreate it in the native LeetCode environment.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V+E)$. Let $V$ be the number of reachable vertices and $E$ the number of undirected edges.
- **Auxiliary Space Complexity:** $O(V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
