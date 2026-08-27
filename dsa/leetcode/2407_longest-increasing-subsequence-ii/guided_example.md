# Guided Example: Longest Increasing Subsequence II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 2, 1, 4, 3, 4, 5, 8, 15], "k": 3}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and an integer `k`.

The objective is to compute `5` from `{"nums": [4, 2, 1, 4, 3, 4, 5, 8, 15], "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Dynamic programming by ending value

When processing a value `v` from left to right, define its best subsequence length as one plus the best earlier subsequence whose final value `p` satisfies:

$$
v-k\le p\le v-1.
$$

The upper bound `v-1` enforces strict increase. The lower bound ensures the adjacent difference is at most `k`.

Only the best length for each possible ending value matters. A segment tree stores these lengths and can return the maximum across the allowed predecessor-value interval.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 2, 1, 4, 3, 4, 5, 8, 15], "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why processing order preserves subsequence order

The loop reads `nums` from left to right. Before value `v` is queried, the tree contains information only from earlier indices. Any predecessor chosen from it therefore respects original index order.

After computing the best length ending at the current index, the tree is updated at coordinate `v` for use by later elements.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The loop reads `nums` from left to right.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Segment-tree contents

The tree covers value coordinates `1` through `max(nums)`. A leaf at coordinate `x` stores the best ideal increasing-subsequence length seen so far that ends with value `x`.

Every internal node stores the maximum of its two children. Consequently, a range query can combine $O(\log M)$ covered nodes to find the best predecessor length, where $M=\max(\texttt{nums})$.

`build` explicitly records every node's left and right coordinate boundaries. `pushup` restores the maximum after a leaf modification.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 2, 1, 4, 3, 4, 5, 8, 15], "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Fenwick tree with transformed queries:** A sta:** - **Fenwick tree with transformed queries:** A standard Fenwick tree gives prefix maxima, not arbitrary interval maxima; additional techniques or a segment tree are needed for `[v-k,v-1]`.
- **Coordinate-compressed segment tree:** Compress occurring values and binary-search range endpoints. This reduces space when $M$ is much larger than the number of distinct values.
- **Quadratic DP:** Check every earlier index for each current value. It is simple but costs $O(n^2)$.
- **Repeated value:** It cannot precede itself under strict increase, but later best state for that value safely overwrites an earlier no-larger state.
- **`v = 1`:** No smaller positive predecessor exists, so the best length is one.
- **`k` larger than `v`:** The effective lower bound is the tree's minimum coordinate one.
- **No legal predecessor:** Zero query result produces a singleton.
- **Increasing gap too large:** The lower range bound excludes that predecessor.
- **Input order:** Tree updates occur only after querying the current item, preserving subsequence index order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M)$. Let $n$ be input length and $M=\max(\texttt{nums})$. Explicitly building the tree takes $O(M)$ time and allocates $O(M)$ nodes.
- **Auxiliary Space Complexity:** $O(M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
