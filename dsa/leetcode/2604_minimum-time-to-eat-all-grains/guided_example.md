# Guided Example: Minimum Time to Eat All Grains

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"hens": [3, 6, 7], "grains": [2, 4, 7, 9]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` hens and `m` grains on a line. You are given the initial positions of the hens and the grains in two integer arrays `hens` and `grains` of size `n` and `m` respectively.

The objective is to compute `2` from `{"hens": [3, 6, 7], "grains": [2, 4, 7, 9]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Binary-search a shared completion time

All hens move simultaneously, so a proposed time $t$ is feasible when the grains can be divided among hens such that each hen can eat its assigned grains within $t$ seconds.

If time $t$ works, every larger time works by following the same routes and optionally waiting. Feasibility is monotone, so the minimum time is the first true value of a binary search.

The helper `check(t)` greedily tests one time limit after both position arrays are sorted.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"hens": [3, 6, 7], "grains": [2, 4, 7, 9]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Assign consecutive grains from left to right

Pointer `j` identifies the leftmost grain not yet assigned. Hens are processed from left to right.

An optimal assignment can give each hen a consecutive block of remaining sorted grains. Crossing assignments are unnecessary: if a left hen goes past a grain assigned to a right hen while that right hen travels back for an earlier grain, exchanging their responsibilities cannot increase the maximum travel distance.

Thus each hen should consume the longest feasible prefix beginning at `grains[j]`. This leaves later hens with only later grains and is maximally helpful.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Case one: the leftmost grain is left of the hen

Let hen position be $x$, leftmost remaining grain be $y\le x$, and

$$
d=x-y.
$$

The hen must at least travel distance $d$ to reach $y$. If $d>t$, this hen cannot eat the grain. No later hen can either, because later hens stand at positions at least $x$ and are even farther right. The check returns false immediately.

If $d\le t$, every unassigned grain between $y$ and $x$ is eaten along a trip through that interval. The first `while` advances past all grains `<= x`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"hens": [3, 6, 7], "grains": [2, 4, 7, 9]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit assignment search:** Distributing grains among hens combinatorially is unnecessary because sorted noncrossing greedy assignment is optimal.
- **Simulate movement per second:** Time coordinates can be huge; route formulas evaluate reach directly.
- **All grains on one side:** Each hen uses a one-direction distance check with no reversal.
- **Hen on a grain:** Eating costs no time, and the grain is consumed by the `<= x` loop.
- **Unreachable leftmost grain:** If the current hen is too far right, every later hen is worse, justifying immediate false.
- **Multiple hens at one position:** They are processed independently and can split consecutive grain blocks.
- **Duplicate grain positions:** Pointer advancement consumes every occurrence at that coordinate.
- **Input mutation:** Both position arrays are sorted.
- **Exclusive search endpoint:** Adding one ensures the constructive all-grains route is present in `range(r)`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let $n$ be the number of hens, $m$ the number of grains, and $C$ the searched time bound. Sorting costs $O(n\log n+m\log m)$. In one check, each hen is visited once and pointer `j` advances at most $m$ times, so cost is $O(n+m)$.
- **Auxiliary Space Complexity:** $O(n + m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
