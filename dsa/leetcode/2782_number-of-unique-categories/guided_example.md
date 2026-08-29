# Guided Example: Number of Unique Categories

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 6, "categoryHandler": [1, 1, 2, 2, 3, 3]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n` and an object `categoryHandler` of class `CategoryHandler`.

The objective is to compute `3` from `{"n": 6, "categoryHandler": [1, 1, 2, 2, 3, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat category equality as graph connectivity

The handler does not reveal category names. It only answers whether two element indices belong to the same category. Category equality is an equivalence relation: members of one category are connected to one another, and different categories are disjoint.

The exact solution uses a disjoint-set union structure, also called union-find. Initially, each of the `n` elements is its own set. Every pair is queried. When the handler says two indices share a category, their sets are merged. The number of remaining set roots is the number of unique categories.

This is different from the Optimal manifest's claimed constant-space greedy scan. The real source allocates a parent list and performs union-find operations.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 6, "categoryHandler": [1, 1, 2, 2, 3, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Parent representation

`p = list(range(n))` creates `[0, 1, ..., n - 1]`. Entry `p[x]` is the current parent of element `x` in the union-find forest. A root points to itself.

Nested function `find(x)` follows parent pointers until it reaches a self-parent. On the way back, it assigns each visited node directly to the root:

`p[x] = find(p[x])`.

This is path compression. Future searches from those nodes become shorter because intermediate links have been removed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Query every unordered pair once

The loops choose `a` from zero through `n - 1` and `b` from `a + 1` through `n - 1`. Therefore:

- an element is never compared with itself;
- pair `(a, b)` is queried exactly once;
- reversed pair `(b, a)` is never repeated.

There are `n(n - 1) / 2` calls to `haveSameCategory` regardless of how many categories exist.

When a call returns true, the assignment

`p[find(a)] = find(b)`

finds the current roots and makes `a`'s root point to `b`'s root. If both already have the same root, the assignment simply writes that root to itself and changes nothing.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 6, "categoryHandler": [1, 1, 2, 2, 3, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Greedy representative scan:** Compare each new index with earlier representatives and count it only if none match. This can use constant extra space and matches the manifest summary.
- **Build an adjacency graph plus DFS:** It is correct but may store `O(n^2)` edges when all elements share one category.
- **Union by size or rank:** It provides stronger balancing guarantees alongside path compression. The exact source does not implement it.
- **All elements share one category:** Every positive union eventually leaves one root.
- **Every element has a unique category:** All queries return false and all `n` initial roots remain.
- **One element:** There are no pair queries, and its self-parent entry yields one category.
- **Repeated unions:** Attaching a root to itself is harmless.
- **Uncompressed non-root paths:** Root counting remains valid because only roots are self-parent.
- **Invalid handler indices:** The loops never generate them.
- **Handler-call cost:** If the interface call itself is expensive, the unavoidable quadratic number of calls is the main cost.
- **Recursive `find` depth:** Without rank balancing, an unfortunate forest may deepen; path compression shortens paths once searched.
- **Manifest mismatch:** Actual source uses `O(n)` parent storage and DSU rather than a constant-space earlier-match test.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. There are exactly `Theta(n^2)` handler calls, which dominate under the usual assumption that each call is `O(1)`. The union-find work occurs only for positive answers.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
