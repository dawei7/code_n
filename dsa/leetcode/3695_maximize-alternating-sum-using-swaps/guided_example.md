# Guided Example: Maximize Alternating Sum Using Swaps

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3], "swaps": [[0, 2], [1, 2]]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `4` from `{"nums": [1, 2, 3], "swaps": [[0, 2], [1, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why connected indices allow arbitrary permutations

A listed edge lets the values at its two endpoints be transposed. Because swaps may be repeated and reversed, a value can be moved along a path through the component.

More strongly, edge transpositions of a connected graph can generate any permutation of values over its vertices. One way to see this is to use a spanning tree: a desired value can travel along tree edges to its target position, and repeated such moves can arrange every position. Intermediate disruptions can be repaired because every swap is reversible.

Thus direct adjacency is not required. If index zero can swap with two and index two can swap with one, values can ultimately move among all three indices. This transitive freedom is why connected components, rather than individual swap pairs, are the correct units of optimization.

No operation connects two different components, so their sets of values remain independent. The total alternating sum is the sum of each component's contribution, allowing every component to be optimized separately.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3], "swaps": [[0, 2], [1, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Building components with disjoint-set union

Initially, every index is its own root:

`parent = list(range(len(nums)))`

and every component has size one.

The local `find` function follows parent pointers until it reaches a root. During this walk, it applies path halving:

`parent[node] = parent[parent[node]]`

which moves the current node two levels upward. Repeated searches make the trees increasingly flat and future root queries faster.

For each allowed pair `left, right`, the source finds both roots. If they already match, the edge lies inside one known component and no merge is needed.

Otherwise, union by size attaches the smaller root below the larger root. The `size` entry of the surviving root is increased accordingly. Combining union by size with path compression gives almost constant amortized work per operation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Initially, every index is its own root:

`parent = list(rang... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Collecting exactly the information each component needs

After all unions, the source scans the original positions. For index `index` with `value`, it finds the final root and performs two updates:

- append `value` to `values_by_root[root]`;
- if `index` is even, increment `even_positions_by_root[root]`.

For a component, it is unnecessary to remember which particular even position receives which selected large value. Every even position has coefficient $+1$, and every odd position has coefficient $-1$. Only the number of positive slots matters.

Suppose a component contains $c$ positions and $E$ of them are even. It necessarily has $c-E$ odd positions. Its values may be assigned to these sign slots in any order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3], "swaps": [[0, 2], [1, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Apply beneficial listed swaps greedily:** A lo:** - **Apply beneficial listed swaps greedily:** A locally improving direct swap can prevent recognizing a better sequence of swaps, and values can travel through intermediate vertices. Component-level permutation freedom is the correct abstraction.
- **Build graph components with DFS or BFS:** An adjacency list plus traversal also finds components in $O(n+m)$ time and space. Disjoint-set union avoids storing every edge after processing it.
- **Sort all values globally:** Values cannot cross disconnected components, so a global rearrangement may be unreachable and overestimate the answer.
- **Use a heap per component:** Selecting the largest $E$ values with a heap is possible, but sorting also identifies the remaining negative values and remains within $O(n\log n)$.
- **No allowed swaps:** Every index is a one-value component. Even positions contribute positively and odd positions negatively, reproducing the original alternating sum.
- **Component containing only one parity:** Rearrangement inside it cannot change the contribution because all its positions have the same sign.
- **Equal values:** Their relative assignment is irrelevant; sorting and the exchange argument allow equality without requiring a strict order.
- **Repeated or cyclic connectivity:** An edge whose endpoints already share a root is skipped. Extra paths do not enlarge the component twice.
- **Indirect swaps:** Two indices need not appear in one listed pair. Any path between them places them in the same permutation component.
- **Input order:** The source sorts copied component lists, not `nums` itself, so the original input array is not reordered.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((n + m) log n)$. Let $n$ be the number of values and $m$ be `len(swaps)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
