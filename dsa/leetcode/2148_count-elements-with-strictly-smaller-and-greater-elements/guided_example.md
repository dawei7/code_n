# Guided Example: Count Elements With Strictly Smaller and Greater Elements 

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [11, 7, 2, 15]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, return *the number of elements that have **both** a strictly smaller and a strictly greater element appear in *`nums`.

The objective is to compute `2` from `{"nums": [11, 7, 2, 15]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the global minimum as the smaller witness

Let `mi = min(nums)`. If `x > mi`, then an occurrence of `mi` appears somewhere in the array and is strictly smaller than `x`. This proves the first requirement.

If `x == mi`, no array value can be strictly smaller by the definition of a minimum. Therefore no occurrence equal to `mi` can count.

There is no possibility that `x < mi` because `x` itself is an array element.

Thus “a strictly smaller element exists” is exactly equivalent to `mi < x`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [11, 7, 2, 15]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use the global maximum as the greater witness

Let `mx = max(nums)`. If `x < mx`, an occurrence of `mx` supplies a strictly greater element. If `x == mx`, no greater value exists. Therefore the second requirement is exactly `x < mx`.

Combining the two independent requirements gives one complete condition:

`mi < x < mx`.

An element counts if and only if its value lies strictly inside the open interval between the array’s global minimum and maximum.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count occurrences, not distinct values

The generator `(mi < x < mx for x in nums)` visits every array occurrence. Python’s chained comparison checks both inequalities for that occurrence and returns a boolean.

The outer `sum(...)` uses the fact that `true` behaves like integer one and `false` like zero. Every qualifying occurrence adds one.

This correctly handles duplicates. In `[-3,3,3,90]`, both occurrences of three satisfy `-3 < 3 < 90`, so both count. The task asks for the number of elements, meaning positions or occurrences, not the number of distinct qualifying values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [11, 7, 2, 15]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort the array:** After sorting, count elements strictly between the first and last values. This costs $O(n\log n)$ time and may mutate the input, offering no benefit over extrema.
- **Compare every pair:** For each element, search the array for smaller and greater witnesses. This can cost $O(n^2)$ even though the global extrema answer every witness query.
- **Frequency map:** Counts of the minimum and maximum can be subtracted from $n$. This is correct but uses $O(n)$ space unless a second extrema-based pass is still used.
- **Formula using counts:** After finding `mi` and `mx`, one may return `n - count(mi) - count(mx)` when `mi != mx`. The exact generator is clearer and naturally handles all cases.
- **One element:** Minimum and maximum are equal, so the strict chained comparison is false and the result is zero.
- **All values equal:** No value has either strict witness; every comparison fails.
- **Exactly two distinct values:** Every element equals one of the extrema, so the answer is zero.
- **Repeated interior value:** Every occurrence counts separately, as in the two threes from Example 2.
- **Repeated minimum:** null of those occurrences count because equality is not strict.
- **Repeated maximum:** null count for the symmetric reason.
- **Negative values:** Ordering works identically; no sign-specific handling is needed.
- **Minimum and maximum each occur once:** They serve as witnesses for every interior occurrence but do not count themselves.
- **Boolean summation:** In Python, `sum` counts true generator results without an explicit integer conversion.
- **Input preservation:** Unlike sorting, the three scans leave `nums` in its original order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. `min(nums)` scans all $n$ elements, and `max(nums)` performs another $n$-element scan. The generator used by `sum` performs one final scan. Three linear passes are still $O(n)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
