# Guided Example: Palindromic Subarray Sum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [10, 10]}`
- **Required output:** `20`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `20` from `{"nums": [10, 10]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why only the longest palindrome at each center matters

Every shorter palindrome with a fixed center is nested inside the longest palindrome for that center. Extending an odd or even palindrome by one radius adds two array values.

All `nums[i]` are positive, so adding those outer values strictly increases the sum. Therefore, among palindromes sharing a center, the longest one always has the greatest sum.

This positivity fact is essential. With negative values, a shorter inner palindrome could have a larger sum, and scoring only the maximum radius would be insufficient.

Every palindromic subarray has either an odd center at an element or an even center between two elements. Evaluating the longest palindrome for every center therefore includes a palindrome whose sum is at least that of every possible candidate.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [10, 10]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Prefix sums for constant-time range totals

The source builds:



For a half-open range `[a,b)`, its sum is:

$$
\texttt{prefix}[b]-\texttt{prefix}[a].
$$

This avoids walking across a palindrome after its boundaries have been found.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source builds:



For a half-open range `[a,b)`, its sum... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Odd-radius definition

For an odd palindrome centered at index `c`, define radius `R` so the palindrome covers:

$$
[c-R+1,\ c+R-1].
$$

Radius one is the single element `nums[c]`. A radius-two palindrome contains three elements, and so on.

The array `odd[c]` stores the maximum such radius.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `20` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [10, 10]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `20` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all subarrays:** There are `O(n^2)` :** - **Enumerate all subarrays:** There are `O(n^2)` candidates before palindrome checking. This is too slow for `n=10^5`.
- **- **Expand independently around every center:** Th:** - **Expand independently around every center:** This is simple and correct but can take `O(n^2)` time on an array whose values are all equal. Manacher reuses symmetry.
- **- **String conversion:** Joining integer values in:** - **String conversion:** Joining integer values into text can confuse multi-digit value boundaries and is unnecessary. Manacher operates directly on array equality.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the array length.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
