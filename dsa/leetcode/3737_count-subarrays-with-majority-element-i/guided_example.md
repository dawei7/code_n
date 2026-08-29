# Guided Example: Count Subarrays With Majority Element I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 2, 3], "target": 2}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and an integer `target`.

The objective is to compute `5` from `{"nums": [1, 2, 2, 3], "target": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate strict majority into one arithmetic test

For a candidate subarray of length `L`, let `f` be the number of positions equal to `target`. The target is a strict majority exactly when

$$
f>\frac{L}{2}.
$$

Multiplying by two avoids fractions:

$$
2f>L.
$$

The exact source maintains `f` as `cnt` and tests

`cnt * 2 > j - i + 1`.

The strict greater-than sign matters. Equality means the target occupies exactly half of an even-length subarray, which is not a majority.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 2, 3], "target": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Enumerate every subarray while reusing counts

The outer loop fixes each possible left endpoint `i`. For that new left boundary, `cnt` starts at zero. The inner loop advances `j` from `i` through the end, growing

`nums[i:j + 1]`

one element at a time.

When the appended value equals `target`, `int(nums[j] == target)` is one and increments `cnt`. Otherwise it is zero and leaves the target frequency unchanged.

The current length is `j-i+1`. After updating the frequency, the code applies the exact majority inequality and adds one to `ans` when it holds.

For `nums=[1,2,2,3]` and `target=2`, fixing `i=1` produces candidates `[2]`, `[2,2]`, and `[2,2,3]`. Their target frequencies are one, two, and two; all satisfy twice the frequency greater than lengths one, two, and three. Other left endpoints discover the remaining valid ranges.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why repeated work is limited to endpoint enumeration

Without reuse, counting target occurrences inside each selected subarray would cost another linear scan and produce $O(n^3)$ time. For a fixed `i`, extending `j` changes the frequency by at most one, so the source updates it in constant time.

Resetting `cnt` for the next left endpoint is necessary because the candidate family changes. The given limit `n<=1000` permits all endpoint pairs to be examined directly.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 2, 3], "target": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recount every candidate from scratch:** This is correct but costs $O(n^3)$. Incremental right-end extension removes the extra scan.
- **Transform target to `+1` and others to `-1`:** A subarray has target majority when its transformed sum is positive. Counting positive-sum subarrays with prefix sums and an order-statistics structure can improve scaling, but that is not the exact source.
- **Use a sliding window:** Majority is not monotonic under arbitrary expansion and shrinking, so a standard two-pointer rule cannot count all valid ranges safely.
- **Follow the manifest's claimed linear method:** Counting earlier smaller prefix balances generally requires a Fenwick tree or equivalent and is not constant time per position without structure. It must not be attributed to these nested loops.
- **Exactly half target values:** `2f=L` fails because majority is strict.
- **Odd-length boundary:** Integer multiplication avoids rounding questions; `2f>L` works uniformly.
- **Single target element:** A one-element matching subarray is valid.
- **Single non-target element:** Its frequency is zero and it is invalid.
- **Target absent:** The answer remains zero.
- **Every value is target:** Every subarray is valid, yielding `n(n+1)/2`.
- **Duplicate value sequences at different indices:** They are different subarrays and are each counted because the task is index-based.
- **Large numeric values:** Only equality with `target` matters; magnitude does not affect memory or running time.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. For left endpoint zero, the inner loop performs `n` iterations; for left endpoint one, `n-1`; and so on. The total is
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
