# Guided Example: Maximum Sum of M Non-Overlapping Subarrays II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 1, -5, 2], "m": 2, "l": 1, "r": 3}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n`, and three integers `m`, `l`, and `r`.

The objective is to compute `7` from `{"nums": [4, 1, -5, 2], "m": 2, "l": 1, "r": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Prefix sums and the best mandatory single subarray

The prefix array gives:

$$
\operatorname{sum}(start,end)=P[end]-P[start].
$$

Before penalty search, the source computes `best_single`, the maximum sum of any one subarray whose length is between `l` and `r`.

For each `end`, valid starts lie in `[end-r,end-l]`. Maximizing $P[end]-P[start]$ means minimizing $P[start]$. `minimum_prefixes` is a monotonic deque of prefix indices with increasing prefix values and the same sliding length window.

This value guarantees a correct nonempty fallback when a penalized DP prefers selecting nothing.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 1, -5, 2], "m": 2, "l": 1, "r": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Penalized DP state

For a fixed $\lambda=$ `penalty`:

- `values[end]` is the greatest penalized total achievable within the first `end` elements;
- `counts[end]` is the number of selected subarrays in that solution.

The source compares states lexicographically as:

`(value, -count)`.

It first maximizes value and, on an exact tie, prefers fewer selected subarrays. This deterministic tie rule makes the chosen count nonincreasing as the penalty rises and fixes which side of a penalty boundary binary search observes.

The empty selection initializes `values[0] = 0` and `counts[0] = 0`. Other entries are filled left to right.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Transition for an interval ending at `end`

If the new interval starts at `start`, its penalized combined value is:

$$
\texttt{values[start]}
+P[end]-P[start]
-\lambda.
$$

For fixed `end`, maximize:

`values[start] - prefix[start]`

over the valid length window. When those numeric keys tie, prefer the candidate whose `counts[start]` is smaller, because both transitions add one interval.

The candidate deque therefore orders the pair:

`(values[start] - prefix[start], -counts[start])`

from best to worst. A newer candidate removes older candidates whose key is no greater, because it is equally or more valuable and expires later.

Starts smaller than `end - r` are removed from the front. The remaining front gives the best legal interval transition in constant amortized time.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 1, -5, 2], "m": 2, "l": 1, "r": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Reuse problem I's exact-count layers:** That costs $O(mn)$ and is too slow when both values reach $10^5$.
- **Binary search without a consistent tie rule:** Counts at equal penalized values could fluctuate at the boundary. Comparing `(value, -count)` deliberately prefers fewer intervals.
- **Return the penalty-zero empty solution:** At least one subarray is mandatory; `best_single` supplies the correct negative or zero fallback.
- **Omit `best_single`:** When all valid intervals have negative sums, penalized DP selects nothing and cannot by itself satisfy the contract.
- **Use an insufficient high penalty:** The search needs a guaranteed count-zero endpoint. `positive_sum + 1` exceeds every possible nonempty original gain.
- **Add `penalty * selected_count` instead of `penalty * m`:** Boundary recovery targets the count limit $m$, including a jump across it; using only the returned count does not perform the interpolation.
- **Forget length-window expiration:** Old starts would create intervals longer than `r`.
- **Forget the minimum-length delay:** A start enters only at `end - l`, preventing intervals shorter than `l`.
- **Equal candidate keys:** The newer start dominates because it expires later; its key includes the fewer-count tie preference.
- **All values negative:** Penalty zero selects zero intervals, and `best_single` returns the least negative legal subarray.
- **Unrestricted optimum already uses at most `m`:** It is globally optimal and is returned without binary search.
- **`l = r`:** Candidate windows reduce to one fixed-length start per end; penalty logic is unchanged.
- **At most rather than exactly `m`:** The early unrestricted branch can return fewer. When the unconstrained optimum exceeds `m`, the positive-gain boundary is recovered at $m$.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log S)$. Let
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
