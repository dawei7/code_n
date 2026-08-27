# Guided Example: Count Pairs in Two Arrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [2, 1, 2, 1], "nums2": [1, 2, 1, 2]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two integer arrays `nums1` and `nums2` of length `n`, count the pairs of indices `(i, j)` such that `i < j` and $\text{nums1}[i] + \text{nums1}[j] > \text{nums2}[i] + \text{nums2}[j]$.

The objective is to compute `1` from `{"nums1": [2, 1, 2, 1], "nums2": [1, 2, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

**Move both sides of the inequality into one value per index.** The required condition is

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [2, 1, 2, 1], "nums2": [1, 2, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

$$
\texttt{nums1}[i]+\texttt{nums1}[j]
>
\texttt{nums2}[i]+\texttt{nums2}[j].
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | $$
\texttt{nums1}[i]+\texttt{nums1}[j]
>
\texttt{nums2}[i]+\... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

$$
(\texttt{nums1}[i]-\texttt{nums2}[i])
+
(\texttt{nums1}[j]-\texttt{nums2}[j])>0.
$$

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [2, 1, 2, 1], "nums2": [1, 2, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Binary search for each right endpoint:** After:** - **Binary search for each right endpoint:** After sorting, find the first value greater than `-nums[r]` with an upper-bound search. This is correct but takes another $O(n\log n)$ counting phase, while the monotone pointer makes it linear.
- **Brute-force all index pairs:** Directly testing every `i < j` takes $O(n^2)$ time and is too slow for $10^5$ elements.
- **Fenwick tree over differences:** Coordinate compression and frequency queries can count earlier values above a threshold online, but add data-structure complexity without improving the sorting-based asymptotic bound.
- **Strict inequality:** Difference sums equal to zero do not qualify. The inner loop must use `<= 0`, not `< 0`.
- **All differences nonpositive:** The left pointer eventually meets the right pointer without adding any positive count, and zero is returned.
- **All differences positive:** The inner loop never moves `l`, and each right endpoint contributes all earlier positions, totaling $n(n-1)/2$.
- **Duplicate differences:** They remain separate occurrences. Sorting and the `r - l` count include every distinct index pair even when values are equal.
- **A single element:** `l == r` initially, the loop does not execute, and no pair exists.
- **Equal input lengths:** The source relies on the contract. If lengths differed, `zip` would silently ignore extra elements, so validation would be needed in a generalized API.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the common array length. Constructing differences costs $O(n)$ time. Sorting them costs $O(n\log n)$. Pointer `r` moves left at most $n$ times, and `l` moves right at most $n$ times across all inner-loop executions, so the counting phase is $O(n)$. Total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
