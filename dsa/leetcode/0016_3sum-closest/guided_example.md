# Guided Example: 3Sum Closest

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [-1, 2, 1, -4], "target": 1}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` of length `n` and an integer `target`, find three integers at **distinct indices** in `nums` such that the sum is closest to `target`.

The objective is to compute `2` from `{"nums": [-1, 2, 1, -4], "target": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sort so changing one pointer changes the sum predictably

Fix one value `v = nums[i]`. The remaining task is to choose two distinct later indices whose pair sum comes as close as possible to `target - v`. After sorting, pointer `j` starts at `i + 1` and `k` at the final index.

The current triplet sum is

$$
t = v + \texttt{nums[j]} + \texttt{nums[k]}.
$$

Increasing `j` keeps or raises `t`; decreasing `k` keeps or lowers it. This monotonic behavior lets the search discard many pairs without measuring each one.

Sorting mutates `nums`, but only values and the returned sum matter. Original indices are not part of the output, and `i < j < k` still guarantees three distinct positions.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [-1, 2, 1, -4], "target": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initialize the best sum with infinity

`ans = inf` means no real triplet has been considered. The comparison



must succeed for the first candidate because its finite distance is less than infinity. From then on, `ans` is always the closest evaluated triplet sum.

The contract guarantees at least three elements, so at least one inner-loop iteration occurs and infinity cannot be returned.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: An exact match is immediately optimal

If `t == target`, the absolute difference is zero. No other sum can be closer than zero, so the method returns `t` without continuing. The unique-solution guarantee is not even needed for this early return; exact equality is an absolute lower bound on distance.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [-1, 2, 1, -4], "target": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Binary search for the third value:** Fix two indices and binary-search the remaining suffix near the desired complement. It costs $O(n^2\log n)$, slower than two pointers.
- **Brute-force triples:** Examines $O(n^3)$ combinations and ignores sorted monotonic elimination.
- **Skip duplicate pivots:** This can reduce repeated work, but is not required for correctness or the $O(n^2)$ bound; the exact source processes them.
- **Exact target exists:** Return immediately with distance zero.
- **All values equal:** Repeated searches compute the same sum; the first candidate initializes `ans` correctly.
- **Target outside all attainable sums:** Pointer movement reaches the extreme attainable triplet closest to that target.
- **Negative target and values:** Only numerical order and differences matter; sign requires no special branch.
- **Distinct indices:** `j = i + 1` and `j < k` maintain `i < j < k`.
- **Input mutation:** In-place sorting changes the caller's list order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the array length.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
