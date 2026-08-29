# Guided Example: Maximum Good Subarray Sum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4, 5, 6], "k": 1}`
- **Required output:** `11`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `nums` of length `n` and a **positive** integer `k`.

The objective is to compute `11` from `{"nums": [1, 2, 3, 4, 5, 6], "k": 1}` while avoiding redundant calculations and unnecessary overhead.

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

**Rewrite a subarray sum using prefix sums.** A good subarray `nums[j..i]` must satisfy

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4, 5, 6], "k": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

$$
\lvert \texttt{nums}[j]-\texttt{nums}[i]\rvert=k.
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Equivalently, its first value must be either `nums[i] - k` or `nums[i] + k`. If `s` is the prefix sum through index $i$ and $P_j$ is the prefix sum strictly before index $j$, then

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `11` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4, 5, 6], "k": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `11` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate every subarray:** Checking both endpoints and summing directly costs up to $O(N^3)$; adding prefix sums reduces sums to $O(1)$ but still leaves $O(N^2)$ endpoint pairs.
- **Store every index per value:** This allows all legal starts to be revisited, but it can degrade to quadratic work. Only the minimum prefix-before-start value is relevant to maximizing a future sum.
- **Sliding window:** Negative values and a condition on endpoint values rather than window sum destroy the monotonicity a sliding window would need.
- **Kadane's algorithm alone:** Kadane finds an unconstrained maximum-sum subarray and does not enforce that the endpoint values differ by exactly $k$.
- **No good subarray:** Neither dictionary lookup ever succeeds for a legal endpoint pairing, `ans` remains negative infinity, and the method returns zero.
- **Best good sum is negative:** A valid negative candidate replaces the sentinel and is returned unchanged; zero is not used merely because it is numerically larger.
- **Repeated starting value:** The map retains the smallest preceding prefix, since every larger prefix is dominated for all future endpoints.
- **Both `x-k` and `x+k` exist:** They represent different possible start values and must both be tested. Either may produce the better sum.
- **Positive $k$:** The contract guarantees $k>0$, so the two searched values are distinct. The implementation would still perform two equivalent lookups if $k=0$, but that case is outside the stated input.
- **Length-two good subarray:** The first position was registered with prefix zero before iteration begins, so the earliest possible pair is considered correctly.
- **Input preservation:** The method only reads `nums` and never sorts or alters it.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the length of `nums` and $U$ its number of distinct values. The method performs one pass over the array. Each iteration uses a constant number of expected-$O(1)$ dictionary lookups or updates and constant arithmetic, so expected time is $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
