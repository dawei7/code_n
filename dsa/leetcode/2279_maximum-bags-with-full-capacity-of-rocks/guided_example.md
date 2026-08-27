# Guided Example: Maximum Bags With Full Capacity of Rocks

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"capacity": [2, 3, 4, 5], "rocks": [1, 2, 4, 4], "additionalRocks": 2}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have `n` bags numbered from `0` to $n - 1$. You are given two **0-indexed** integer arrays `capacity` and `rocks`. The $$i^{\text{th}}$$ bag can hold a maximum of $\text{capacity}[i]$ rocks and currently contains $\text{rocks}[i]$ rocks. You are also given an integer `additionalRocks`, the number of additional rocks you can place in **any** of the bags.

The objective is to compute `3` from `{"capacity": [2, 3, 4, 5], "rocks": [1, 2, 4, 4], "additionalRocks": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Replace each bag by its filling cost

For bag `i`, the only relevant quantity is how many additional rocks it needs:

$$
d_i = \texttt{capacity}[i] - \texttt{rocks}[i].
$$

Two bags with the same deficit cost the same to complete, regardless of their absolute capacities or current rock counts. Completing a bag is an all-or-nothing benefit of one: partially filling it does not increase the number of full bags.

The first loop computes every deficit in place with `capacity[i] -= x`, where `x` is the corresponding value from `rocks`. After that loop, `capacity` no longer contains capacities; it contains filling costs.

The constraints ensure `rocks[i] \le capacity[i]` before mutation, so every deficit is nonnegative.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"capacity": [2, 3, 4, 5], "rocks": [1, 2, 4, 4], "additionalRocks": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Choose the cheapest bags first

`capacity.sort()` orders the deficits from smallest to largest. If the goal is to buy as many unit-value items as possible with a fixed budget, choosing cheaper items before expensive ones is optimal.

An exchange argument proves this. Suppose a plan fills a bag with deficit `y` but omits another bag with deficit `x \le y`. Replacing `y` by `x` does not use more rocks and keeps the same number of full bags. Repeating such exchanges transforms any size-`k` feasible plan into the `k` smallest deficits without increasing cost.

Therefore, for every possible count `k`, the minimum number of additional rocks needed to fill any `k` bags is the sum of the first `k` sorted deficits. The largest affordable prefix length is the global optimum.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `capacity.sort()` orders the deficits from smallest to large... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Spend the budget along the sorted prefix

The second loop visits each sorted deficit `x` and performs `additionalRocks -= x`. If the result remains nonnegative, the current bag can be completed in addition to all earlier bags.

If the subtraction makes the budget negative at index `i`, exactly `i` earlier deficits were affordable. The current deficit is the smallest remaining one, so every later deficit is at least as large. No alternative choice among the unfilled bags can add another full bag to the already optimal cheapest prefix. Returning `i` is therefore correct.

The code checks after subtraction rather than before. On failure, the local budget temporarily becomes negative, but the method returns immediately, so that temporary value has no later effect.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"capacity": [2, 3, 4, 5], "rocks": [1, 2, 4, 4], "additionalRocks": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Separate deficit list:** It preserves `capacit:** - **Separate deficit list:** It preserves `capacity` while using explicit `O(n)` additional storage and the same time bound.
- **Min-heap:** Heapifying deficits and repeatedly extracting the cheapest can also find the answer, but sorting is simpler and has the same worst-case order here.
- **Counting sort:** Capacities reach `10^9`, so a frequency array over all possible deficits is impractical.
- **Fill bags in original order:** It can spend rocks on a costly bag while several cheaper bags could yield a larger count.
- **Partial filling:** It provides no benefit unless the bag reaches capacity, so the greedy algorithm commits whole deficits.
- **Already-full bag:** Its zero deficit is counted without consuming budget.
- **All bags already full:** Every deficit is zero and the method returns `n`.
- **Budget fills every deficit:** The loop completes and returns the full list length, even if rocks remain unused.
- **Budget fails on the first positive deficit:** The returned index counts any preceding zero deficits and no unaffordable bag.
- **Equal deficits:** Their order is irrelevant because they cost the same and give the same unit reward.
- **Very large capacity values:** Only differences and a running budget are stored; Python integer arithmetic is safe.
- **Post-subtraction check:** A negative local budget is harmless because the function returns immediately.
- **Array-length correspondence:** The source guarantee lets `enumerate(rocks)` safely index the matching capacity entry.
- **Capacity mutation:** Values are replaced by deficits and then reordered; callers must not expect the original list afterward.
- **Rocks preservation:** The `rocks` list is never changed.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \log n)$. Let `n` be the number of bags. Computing deficits in place takes `O(n)` time. Sorting dominates at `O(n \log n)`, and the budget loop takes at most `O(n)`. Total time is `O(n \log n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
