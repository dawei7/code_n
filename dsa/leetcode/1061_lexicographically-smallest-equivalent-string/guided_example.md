# Guided Example: Lexicographically Smallest Equivalent String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s1": "parker", "s2": "morris", "baseStr": "parser"}`
- **Required output:** `"makkek"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings of the same length `s1` and `s2` and a string `baseStr`.

The objective is to compute `"makkek"` from `{"s1": "parker", "s2": "morris", "baseStr": "parser"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Equivalence pairs form connected components

Every aligned pair `s1[i]` and `s2[i]` says that two letters are equivalent. Symmetry makes that relation undirected, and transitivity means a chain of pairs joins every letter in the same equivalence group.

This can be viewed as a graph whose 26 lowercase letters are vertices. Each given pair is an edge. Every connected component is one equivalence class: any character in that component may replace any other.

To make `baseStr` lexicographically smallest, every character should become the smallest letter in its component. Choosing a larger equivalent letter at any position could only make the result larger, and choices at different positions do not constrain each other.

The solution maintains these components with a disjoint-set union structure, also called union-find.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s1": "parker", "s2": "morris", "baseStr": "parser"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Represent letters as small integer nodes

The parent array begins as:



Letter `"a"` maps to node zero, `"b"` to one, and so through `"z"` at node 25. Initially `p[x] == x` for every node, so each letter is the sole member and representative of its own component.

The representative is not arbitrary in this implementation. The union operation always chooses the smaller root. As a result, a component's representative is always its lexicographically smallest character.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find the current component root

The nested function is:



A root points to itself. If `p[x] == x`, the function returns `x` immediately.

Otherwise, `x` points toward another node in the same component. The recursive call follows parent links until it reaches the root. Then:



rewrites `x`'s parent to point directly at that root. This is path compression. Later searches from `x`, and often from nodes on related paths, become shorter.

The returned value is always the current representative of `x`'s complete equivalence class, not merely its immediate parent.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"makkek"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s1": "parker", "s2": "morris", "baseStr": "parser"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"makkek"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Graph plus depth-first search:** Build an undirected graph on the alphabet, find each connected component, record its smallest character, and map `baseStr`. This takes `O(P + B + A)` time with adjacency lists and is equally valid.
- **Adjacency matrix:** A 26 by 26 Boolean matrix plus DFS is simple because the alphabet is tiny, but it uses `O(A^2)` space rather than `O(A)` disjoint-set storage.
- **Repeated transitive closure:** Floyd–Warshall can compute equivalence reachability in `O(A^3)` time. It is acceptable for 26 letters but unnecessarily heavy.
- **Union by rank with minimum metadata:** For a growing alphabet, balance trees by rank and separately store the minimum node of each component. This preserves efficient general union-find behavior without requiring the root itself to be the minimum.
- **Same character paired with itself:** Both roots are equal, and the self-parent assignment changes nothing.
- **Repeated equivalence pair:** The second and later merges find the same root and are harmless.
- **Transitive chain:** Pairs such as `a = b` and `b = c` merge all three nodes, and `find(c)` returns `a`.
- **Equivalence pair order:** Components and their minima do not depend on the order in which edges are processed. The smaller-root invariant produces the same final representative.
- **Unmentioned base character:** It remains its own representative and is copied unchanged.
- **All letters equivalent:** Every component merge eventually has root zero, so every base character becomes `"a"`.
- **No useful change:** If each base character is already the smallest in its component, the returned string equals `baseStr`.
- **Duplicate base characters:** Each occurrence is mapped independently to the same root. The generator does not cache explicitly, but path compression makes repeated finds short.
- **Equal input lengths:** `zip` relies on the contract that `s1` and `s2` have equal length. With unequal strings it would silently ignore an unmatched suffix.
- **Input preservation:** Strings are immutable. Only the private parent array changes during unions and path compression.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P + B + A)$. Let `P` be the number of equivalence pairs, `B` the length of `baseStr`, and `A = 26` the lowercase alphabet size.
- **Auxiliary Space Complexity:** $O(A)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
