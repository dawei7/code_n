# Guided Example: Distribute Elements Into Two Arrays II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 1, 3, 3]}`
- **Required output:** `[2, 3, 1, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **1-indexed** array of integers `nums` of length `n`.

The objective is to compute `[2, 3, 1, 3]` from `{"nums": [2, 1, 3, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

**The challenge is answering greater-count queries quickly.** For each new value $x$, we need the number of existing elements strictly greater than $x$ in each destination array. Scanning both arrays every time would take quadratic time.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 1, 3, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The exact source uses coordinate compression and one Binary Indexed Tree, also called a Fenwick tree, per destination.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Compress large values into ordered ranks.** `st = sorted(set(nums))` contains every distinct input value in increasing order. `bisect_left(st, x) + 1` maps $x$ to a one-based rank `i`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 3, 1, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 1, 3, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 3, 1, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Scan both arrays per insertion:** It directly computes greater counts but costs $O(N^2)$ worst-case time.
- **Two sorted multisets:** They support rank queries, but Python has no standard logarithmic ordered multiset; Fenwick trees are explicit and predictable.
- **Segment tree:** It provides the same asymptotic operations with more code and memory constants.
- **Equal values:** Prefix query includes them, so they are not mistakenly counted as strictly greater.
- **Greater-count tie:** Array length decides; equal lengths choose `arr1` through `<=`.
- **All values equal:** Every greater count is zero, so assignments balance lengths with the first-array final tie.
- **One destination has more greater elements:** Count comparison takes priority over length.
- **Coordinate compression:** It handles values up to $10^9$ without allocating a billion-sized frequency array.
- **Tree/list synchronization:** Each append must be followed by exactly one matching update.
- **Input slice:** `nums[2:]` creates a real linear temporary but does not change the $O(N)$ bound.
- **Why subtract from array length:** A Fenwick prefix gives the complement of the desired strict-greater set. Every stored element is either at most $x$ or greater than $x$, so length minus prefix count is exact.
- **Duplicate frequency:** Updating by one for every occurrence means trees store multiplicities, not merely presence. This is required because `greaterCount` counts elements.
- **Final list order:** Fenwick ranks determine destinations only; values are appended to `arr1` and `arr2` in arrival order, which the final concatenation preserves.
- **Binary search always succeeds:** Every processed value came from `nums` and therefore appears in compressed set `st`, so `bisect_left` returns its exact rank.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N)$. Building the set and sorting $M\le N$ distinct values costs $O(N+M\log M)$. Every later element performs binary search, two Fenwick queries, and one update, each $O(\log M)$. Total time is $O(N\log N)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
