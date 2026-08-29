# Guided Example: Number of Subarrays That Match a Pattern II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4, 5, 6], "pattern": [1, 1]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums` of size `n`, and a **0-indexed** integer array `pattern` of size `m` consisting of integers `-1`, `0`, and `1`.

The objective is to compute `4` from `{"nums": [1, 2, 3, 4, 5, 6], "pattern": [1, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

**Transform numbers into the language of the pattern.** The pattern describes relationships between adjacent values, not the values themselves. The source first builds an array `s` of length $N-1$. For every adjacent pair:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4, 5, 6], "pattern": [1, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- append 1 when the new value is larger;
- append 0 when the values are equal;
- append $-1$ when the new value is smaller.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

A subarray `nums[i..i+M]` matches the length-$M$ pattern exactly when

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4, 5, 6], "pattern": [1, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Naive comparison at every start:** It takes $O((N-M)M)$ worst-case time and is too slow for $N$ up to one million.
- **Z-function:** Concatenating pattern, a separator, and the relation array also finds matches in linear time, but still normally stores a linear auxiliary array.
- **Rolling hash:** It can compare windows quickly but introduces collision risk unless equality is independently verified.
- **Streaming KMP count:** Relations can be fed directly into the KMP state and a scalar count incremented on matches. It would preserve linear time and use $O(M)$ space, unlike the exact source's materialized arrays.
- **Pattern length one:** Every adjacent relationship matching that one symbol is counted.
- **Overlapping matches:** The `pi[g - 1]` fallback after a full match preserves them.
- **Equal adjacent values:** They map to zero, distinct from both increasing and decreasing relationships.
- **Large values:** Only comparisons are performed; magnitudes up to $10^9$ do not affect matching.
- **Input preservation:** Neither `nums` nor `pattern` is mutated.
- **Manifest mismatch:** Its $O(M)$ space claim describes a streaming KMP design, while the protected source uses $O(N+M)$ storage.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N+M)$. Let $N$ be `len(nums)` and $M$ be `len(pattern)`. Creating `s` costs $O(N)$ time. Prefix-function construction costs $O(M)$, and matching costs $O(N+M)$ amortized. Total time is $O(N+M)$.
- **Auxiliary Space Complexity:** $O(N+M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
