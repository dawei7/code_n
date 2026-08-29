# Guided Example: Range Sum Query - Mutable

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [4], "n": 1, "queries": [["sum", 0, 0], ["update", 0, 7], ["sum", 0, 0]], "q": 3}`
- **Required output:** `[4, 7]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, handle multiple queries of the following types:

The objective is to compute `[4, 7]` from `{"arr": [4], "n": 1, "queries": [["sum", 0, 0], ["update", 0, 7], ["sum", 0, 0]], "q": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What a Fenwick entry stores

For a positive position $x$, define

$$
\operatorname{lowbit}(x)=x\mathbin{\&}(-x).
$$

The expression isolates the least significant 1 bit of $x$. In a Fenwick tree, `c[x]` stores the sum of a block ending at $x$ whose length is `lowbit(x)`. Its inclusive one-based interval is

$$
[x-\operatorname{lowbit}(x)+1,\ x].
$$

Examples make the pattern concrete:

| `x` | Binary form | `lowbit(x)` | Block summarized by `c[x]` |
| --- | --- | --- | --- |
| 1 | `001` | 1 | `[1, 1]` |
| 2 | `010` | 2 | `[1, 2]` |
| 3 | `011` | 1 | `[3, 3]` |
| 4 | `100` | 4 | `[1, 4]` |
| 6 | `110` | 2 | `[5, 6]` |

Larger powers of two summarize larger aligned ranges. These carefully overlapping blocks let the structure move between a position and the next relevant containing block with simple bit arithmetic.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [4], "n": 1, "queries": [["sum", 0, 0], ["update", 0, 7], ["sum", 0, 0]], "q": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Adding a delta at one position

`BinaryIndexedTree.update(x, delta)` means “increase the logical value at one-based position `x` by `delta`.” It is an additive operation, not an assignment.

The value belongs to `c[x]` and also to every larger Fenwick block whose interval contains position `x`. After updating one tree entry, the source moves to

`x += x & -x`.

This jumps to the next ancestor block that contains the original position. Repeating until `x > n` updates every stored partial sum affected by the point change and no unrelated block.

For example, in a tree of sufficient size, changing position 3 visits positions 3, 4, 8, and so on. Entry 3 covers `[3, 3]`, entry 4 covers `[1, 4]`, and entry 8 covers `[1, 8]`; all contain logical position 3.

Because `lowbit(x)` is at least one for positive `x`, each update step strictly increases `x`. The loop always terminates after moving through at most one relevant node per binary scale.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Reading a prefix sum

`query(x)` returns the sum of one-based positions 1 through `x`, which equals the first `x` original elements.

It begins with `s = 0`, adds `c[x]`, and then moves to

`x -= x & -x`.

The block stored at `c[x]` covers the trailing portion of the still-unaccounted prefix. Subtracting its length moves immediately before that block. The next entry covers the next trailing block, and the process repeats until `x` reaches zero.

These blocks are disjoint and together cover the full prefix. For example, `query(7)` uses a block ending at 7 of length 1, then a block ending at 6 of length 2, then a block ending at 4 of length 4. They cover `[7,7]`, `[5,6]`, and `[1,4]`, exactly positions 1 through 7 without overlap.

Each subtraction clears the least significant set bit, so the number of iterations is at most the number of bits needed to represent $n$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[4, 7]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [4], "n": 1, "queries": [["sum", 0, 0], ["update", 0, 7], ["sum", 0, 0]], "q": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[4, 7]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Iterative segment tree:** Store values in leaves and range sums in parent nodes. It also supports $O(\log n)$ assignments and queries with $O(n)$ space, but usually requires about twice as many array slots and more boundary logic.
- **Linear-time Fenwick construction:** Copy values into the tree and propagate each node once to its parent, building in $O(n)$. The exact source uses the simpler repeated-update build, so its constructor is $O(n\log n)$.
- **Keep a separate current-value array:** Then assignment can read `prev` in $O(1)$ rather than issuing a point query. This uses another $O(n)$ array and keeps update asymptotically $O(\log n)$.
- **Static prefix sums:** They answer queries in $O(1)$ but require $O(n)$ repair after an assignment, making them unsuitable for mixed mutable operations.
- **Direct array storage:** Assignment is $O(1)$ and a range sum is $O(n)$ in the worst case. It favors updates too strongly when both operation types can be frequent.
- **Square-root decomposition:** Block sums give approximately $O(\sqrt n)$ range queries and $O(1)$ updates, a valid middle ground but asymptotically slower for queries than Fenwick.
- **Passing an assignment value directly as the delta:** This would add `val` to the old value rather than replace it. The source must subtract `prev` first.
- **Zero-based Fenwick calls:** Position zero has `lowbit(0) = 0`, so an update loop would never advance. Original indices must be shifted by one.
- **Inclusive right boundary:** `query(right + 1)` is required to include `nums[right]`; using `query(right)` would exclude it.
- **Range starts at zero:** `query(left)` becomes `query(0)`, whose loop performs no iterations and returns zero naturally.
- **Single-element query:** The difference of neighboring prefixes recovers exactly the current value, which is also how public updates find `prev`.
- **Assigning the existing value:** `delta` is zero. The Fenwick traversal adds zero to its ancestors, preserving all sums.
- **Negative values and deltas:** Fenwick sums use ordinary addition, so negative entries and downward assignments work without any ordering assumption.
- **One-element array:** The tree has entries 0 and 1. Every update and query touches at most position 1 and remains valid.
- **Maximum operation count:** Each operation visits only logarithmically many tree nodes, avoiding a full-array scan under the stated $3\cdot10^4$ calls.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(q\log n)$. Let $n$ be the array length and $q$ the total number of update and range-sum operations.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
