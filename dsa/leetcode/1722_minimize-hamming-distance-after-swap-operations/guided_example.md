# Guided Example: Minimize Hamming Distance After Swap Operations

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"source": [1, 2, 3, 4], "target": [2, 1, 4, 5], "allowedSwaps": [[0, 1], [2, 3]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integer arrays, `source` and `target`, both of length `n`. You are also given an array `allowedSwaps` where each $\text{allowedSwaps}[i] = [a_{i}, b_{i}]$ indicates that you are allowed to swap the elements at index $a_{i}$ and index $b_{i}$ **(0-indexed)** of array `source`. Note that you can swap elements at a specific pair of indices **multiple** times and in **any** order.

The objective is to compute `1` from `{"source": [1, 2, 3, 4], "target": [2, 1, 4, 5], "allowedSwaps": [[0, 1], [2, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Allowed swaps create independent index components

Treat indices as vertices of an undirected graph and each allowed pair as an edge. If two indices lie in the same connected component, values can be moved between them through a sequence of allowed edge swaps.

In fact, swaps along the edges of a connected graph can realize any permutation of the values inside that component. A value can be routed along a path, and repeated transpositions generate arbitrary rearrangements. Values can never cross between different components because no allowed-swap path connects them.

Therefore exact positions inside one component are flexible; only the multiset of source values in that component matters.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"source": [1, 2, 3, 4], "target": [2, 1, 4, 5], "allowedSwaps": [[0, 1], [2, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build components with disjoint-set union

`p = list(range(n))` initially makes every index its own representative.

The nested `find(x)` follows parent pointers to a root. During recursive return, `p[x] = find(p[x])` rewrites the path directly to that root. This path compression speeds up later searches.

For each allowed pair `a,b`, the source performs

`p[find(a)] = find(b)`.

This makes the root of `a`'s component a child of `b`'s root, merging the components. If both roots are already the same, the assignment is harmless.

All unions finish before component value counts are built, so component membership never changes during the matching phase.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count source values within each component

`cnt = defaultdict(Counter)` maps a component representative to a frequency counter.

For each source position `i` with value `x`, the source obtains its compressed root `j = find(i)` and increments `cnt[j][x]`.

After this pass, `cnt[root][value]` is the number of copies of that value available anywhere in that component. The count deliberately forgets exact positions, because arbitrary within-component permutation makes those positions interchangeable.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"source": [1, 2, 3, 4], "target": [2, 1, 4, 5], "allowedSwaps": [[0, 1], [2, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Union by rank or size:** Add a balancing array while retaining path compression. This supports the manifest's inverse-Ackermann amortized bound and reduces recursion-depth risk.
- **Graph traversal components:** Build adjacency lists and label components with DFS or BFS in $O(n+m)$ time and space.
- **Simulate swaps:** Searching actual swap sequences is unnecessary and can be enormous; component permutations capture all reachability.
- **No allowed swaps:** Every index is its own component, so the result equals the ordinary Hamming distance.
- **One connected component:** Source values may be permuted globally, and the answer is the multiset shortage against all target values.
- **Duplicate values:** Counter multiplicities ensure each occurrence is used at most once.
- **Target value absent from a component:** Its counter becomes negative and adds a mismatch.
- **Same value in another component:** It cannot help because swaps cannot cross component boundaries.
- **Repeated or redundant edges:** Re-unioning an existing component changes nothing.
- **Already equal arrays:** Every target decrement consumes an available value and the answer stays zero.
- **Input preservation:** Source and target are not rearranged; only DSU and frequency structures change.
- **Deep DSU chain:** Recursive path compression eventually flattens it, but the first traversal may be deep because union by rank is absent.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((n+m)\alpha(n))$. Let $n$ be the array length and $m$ the number of allowed swaps. Hash-map and counter operations take expected constant time. There are $m$ unions and $O(n)$ additional `find` calls.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
