# Guided Example: Reorder Routes to Make All Paths Lead to the City Zero

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 6, "connections": [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` cities numbered from `0` to $n - 1$ and $n - 1$ roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

The objective is to compute `3` from `{"n": 6, "connections": [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Root the underlying tree at the destination.** Ignoring road directions, the network is a tree. Root it at city zero. Every non-root city has exactly one parent: the next city on its unique undirected path toward zero.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 6, "connections": [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

For every city to reach zero, each edge must point from a child toward its parent. If an edge instead points from the parent out toward the child, it must be reversed. Because a tree has only one path to the root, there is no alternative route that could compensate for a wrongly directed parent-child edge.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For every city to reach zero, each edge must point from a ch... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The problem therefore becomes: traverse the tree outward from zero and count the edges whose original direction also points outward.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 6, "connections": [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Iterative DFS:** Store node, parent pairs on a:** - **Iterative DFS:** Store node, parent pairs on an explicit stack and add edge costs while visiting children. It avoids Python recursion-depth failure.
- **Breadth-first search:** A queue can traverse outward from zero with the same labeled adjacency entries and count rule.
- **Visited array:** It is valid but unnecessary for a tree when the parent is passed. It becomes necessary if cycles are allowed.
- **Traverse original edges only:** This can fail to reach children whose roads point toward the current node. Artificial reverse entries are required for undirected exploration.
- **All roads already point to zero:** Every outward traversal uses cost-zero entries, and the answer is zero.
- **All rooted edges point away from zero:** Every road contributes one, so `n - 1` reversals are necessary.
- **Single chain:** Each road's cost is evaluated once according to whether it faces toward its parent.
- **Star centered at zero:** Roads directed zero-to-leaf must reverse; leaf-to-zero roads do not.
- **Input endpoint order:** `[a,b]` is directional, not an unordered pair. The two labeled adjacency entries preserve that fact.
- **Leaf city:** Its DFS returns zero after its incoming edge cost has already been counted by the parent.
- **Unique-path guarantee:** It proves that every outward edge is unavoidable and makes the count minimal.
- **Parent sentinel:** `-1` cannot equal a valid city, so root processes all neighbors.
- **Deep tree:** Prefer iterative traversal in Python if runtime recursion limits are not adjusted.
- **No actual mutation:** The method counts required reversals; it does not need to rewrite the connection list.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The tree has `n - 1` roads. Building `g` inserts two entries per road, taking `O(n)` time and `O(n)` space.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
