# Guided Example: Maximum and Minimum Sums of at Most Size K Subarrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3], "k": 2}`
- **Required output:** `20`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and a **positive** integer `k`. Return the sum of the **maximum** and **minimum** elements of all subarrays with **at most** `k` elements.

The objective is to compute `20` from `{"nums": [1, 2, 3], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

**Group all eligible subarrays by their ending index.** When processing `end_idx`, the source needs the sum of maxima and the sum of minima over every subarray ending there with length at most $k$. If those two sums are known, adding them to the global answer counts every eligible subarray exactly once, at its unique right endpoint.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 4

Two monotonic deques compress extreme values for all such starting positions:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `20` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `20` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate all bounded subarrays:** There can be $O(nk)$ of them, and scanning each for extrema is even slower. Share groups aggregate their contributions.
- **One monotonic deque per single window:** Standard sliding-window extrema find only the maximum or minimum of a fixed-length window, not the sum of extrema over every suffix ending at a point. Shares are the extra ingredient.
- **Contribution boundaries per element:** Previous/next greater and smaller boundaries can also count bounded-length subarrays, but the at-most-$k$ cap makes the combinatorics more involved.
- **\(k=1\):** Only singleton subarrays remain. Each element contributes itself as both maximum and minimum, so the result is twice the array sum.
- **\(k=n\):** No start is evicted, and the method sums extremes over all subarrays.
- **Equal elements:** Non-strict pop comparisons merge equal groups. Every subarray still receives the correct equal extreme once.
- **Negative values:** Maximum and minimum sums may be negative. The arithmetic uses actual values and requires no nonnegative assumption.
- **Front share decrement:** Only one oldest start expires per new endpoint, so decrementing exactly one share is correct.
- **Back-pop amortization:** A single new extreme may pop many entries, but each entry can be popped only once over the entire traversal.
- **No modulo:** The task requests the exact integer sum. Python integers prevent overflow for the stated bounds.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Every index is appended once to each deque. An entry can be popped from the back once during extreme merging or from the front once when it expires. Share decrements occur once per endpoint after the window reaches length $k$. All deque-end operations and arithmetic are constant time, so total time is $O(n)$ despite the inner `while` loops.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
