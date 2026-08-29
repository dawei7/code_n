# Guided Example: Smallest String With Swaps

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "dcab", "pairs": [[0, 3], [1, 2]]}`
- **Required output:** `"bacd"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s`, and an array of pairs of indices in the string `pairs` where $\text{pairs}[i] = [a, b]$ indicates 2 indices(0-indexed) of the string.

The objective is to compute `"bacd"` from `{"s": "dcab", "pairs": [[0, 3], [1, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build connectivity with parent links

The parent list `p` begins as `[0, 1, ..., n - 1]`, so every index starts in its own component.

`find(x)` follows parent pointers to a root whose parent is itself. During the recursive return, `p[x] = find(p[x])` performs path compression, redirecting visited vertices straight to the root.

For every allowed pair `[a, b]`, the code executes `p[find(a)] = find(b)`. This connects the root of `a`’s component to the root of `b`’s component. Once all pairs are processed, two indices have the same representative exactly when a path of allowed swaps connects them.

The union step does not use rank or component size. Path compression still shortens traversed paths, but the exact data structure should not be credited with the strongest inverse-Ackermann bound that requires a balancing heuristic as well.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "dcab", "pairs": [[0, 3], [1, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why a connected component permits any permutation

Along one graph edge, the two endpoint characters can swap directly. Along a path, a character can be moved step by step to another vertex. More generally, swaps along edges of a connected graph generate every permutation of the component’s positions. One constructive view is to use a spanning tree and move desired characters along tree paths.

Therefore, only the multiset of characters in each component matters; their original positions inside that component do not restrict the final arrangement.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Collect and reverse-sort component characters

The loop over `enumerate(s)` finds each index’s root and appends its character to `d[root]`. Afterward, every dictionary list contains exactly the characters movable among that component’s indices.

Each list is sorted with `reverse=true`, putting its largest character first and smallest character last. This direction is chosen because Python list `pop()` removes the last element in $O(1)$ amortized time. The code can therefore retrieve the smallest remaining character efficiently.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"bacd"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "dcab", "pairs": [[0, 3], [1, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"bacd"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Balanced DSU:** Track rank or size and attach the smaller tree beneath the larger. Together with path compression, this provides the inverse-Ackermann amortized bound.
- **DFS or BFS components:** Build an adjacency list, traverse each component, sort its indices and characters, and assign them together. This uses $O(n+p)$ graph storage.
- **No swap pairs:** Every index is a singleton component. Each list contains one character, so the original string is returned.
- **One fully connected component:** All characters can be permuted, and the result is the globally sorted string.
- **Duplicate characters:** Component lists preserve multiplicity; equal values are popped into consecutive eligible positions as needed.
- **Indirect swaps:** A path is enough. The DSU merges transitive connectivity even when an endpoint pair is not listed directly.
- **Reverse sort plus `pop`:** Sorting ascending and popping from the end would assign largest characters first and be wrong. Reverse sorting makes the end hold the smallest.
- **Input string immutability:** The method constructs a new string and does not attempt to modify `s` in place.
- **Representative stability:** Character grouping occurs only after all unions, so later path compression cannot move a component to a different root.
- **Recursive `find` depth:** Arbitrary unbalanced linking can create deep parent chains before compression. A balanced union or iterative find can reduce operational recursion risk.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((n+p)\alpha(n)+n\log n)$. Let $n$ be the string length and $p$ be the number of swap pairs.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
