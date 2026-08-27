# Guided Example: Longest Alternating Subarray

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 3, 4, 3, 4]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums`. A subarray `s` of length `m` is called **alternating** if:

The objective is to compute `4` from `{"nums": [2, 3, 4, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Express the pattern as alternating adjacent differences

A valid subarray must have length at least two and look like

`a, a + 1, a, a + 1, ...`.

Its adjacent differences are therefore

$$
+1,\ -1,\ +1,\ -1,\ \ldots
$$

The exact solution uses this difference view directly. For every possible start index `i`, it sets `k = 1`, meaning the first required difference is positive one. It then advances `j` while

`nums[j + 1] - nums[j] == k`

and flips the next expectation with `k *= -1` after each successful step.

This avoids repeatedly comparing later values with the first value. The required current difference completely describes whether the next position continues the pattern.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 3, 4, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why every start is examined

An alternating subarray can begin anywhere, but it cannot begin with a decrease. Even if an index lies inside some other pattern, it might start a different valid pattern with its following value. The outer loop therefore tries each `i` independently.

For a fixed `i`, `j` begins equal to `i`. If the next difference is not positive one, the while loop performs no extension. If it does match, `j` advances and the expected difference becomes negative one. Each later success alternates that sign.

When the loop stops, one of two things is true: `j` is already the final array index, or the next adjacent difference does not match the required sign and magnitude. In either case, the interval `nums[i:j + 1]` is the longest alternating subarray beginning at this particular `i`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | An alternating subarray can begin anywhere, but it cannot be... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The magnitude matters, not only parity or sign

The condition is exact equality with `1` or `-1`. A change from 2 to 5 is positive, but it is not the required increase by one. A sequence such as `[2, 3, 2, 3]` succeeds because its differences are exactly `1, -1, 1`. A sequence `[2, 3, 1]` stops before 1 because the second difference is `-2`.

Likewise, merely alternating parity is not enough. Values 2 and 5 have opposite parity but differ by three. Tracking `k` captures the full numerical pattern stated in the contract.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 3, 4, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **One-pass dynamic tracking:** Carry the length :** - **One-pass dynamic tracking:** Carry the length of the valid alternating run ending at each position, continue it when the expected difference matches, and restart at length two on a new `+1` pair. That yields `O(n)` time and matches the manifest, but it is not the exact implementation.
- **Compare values to the start:** Checking whether each even offset equals `nums[i]` and each odd offset equals `nums[i] + 1` is correct, but adjacent differences plus a sign flip express the same rule more directly.
- **Parity-only test:** Alternating even and odd values is insufficient because the required numerical difference must be exactly one in magnitude.
- **No `+1` adjacent pair:** No start reaches length two, so the initial `-1` is returned.
- **Exactly one valid pair:** Its length two updates `ans` even if the pattern fails immediately afterward.
- **Consecutive increases:** A second `+1` is invalid because the expected difference after the first step is `-1`.
- **Difference with magnitude greater than one:** It fails even if its sign is the expected sign.
- **Pattern reaches the final element:** The bounds check `j + 1 < n` ends the loop safely, and the full length is recorded.
- **Overlapping valid subarrays:** Each start is considered independently. Overlap causes repeated work but does not cause duplicate answer counting because only the maximum length is stored.
- **Length-one candidate:** It is deliberately ignored due to the strict `> 1` definition.
- **Minimum input length two:** One comparison decides between answer two and `-1`.
- **Input mutation:** The method never changes the array, so later starts see the original values.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the array length. The outer loop has `n` iterations. A single inner scan can advance through nearly the rest of the array. In a long pattern such as `[a, a+1, a, a+1, ...]`, every other start has an initial positive-one difference and scans a long suffix. The total number of successful comparisons is an arithmetic series, producing `O(n^2)` worst-case time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
