# Guided Example: Find K Pairs with Smallest Sums

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [1, 7, 11], "nums2": [2, 4, 6], "k": 3}`
- **Required output:** `[[1, 2], [1, 4], [1, 6]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integer arrays `nums1` and `nums2` sorted in **non-decreasing order** and an integer `k`.

The objective is to compute `[[1, 2], [1, 4], [1, 6]]` from `{"nums1": [1, 7, 11], "nums2": [2, 4, 6], "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why a row corresponds to one first-array occurrence.

Pairs are formed from array occurrences, not just distinct values. If `nums1` contains the same value twice, its two indices define two separate rows and can produce duplicate value pairs. This is required by examples such as two different `1` occurrences paired with the same `1` from `nums2`.

The heap entry `[sum, i, j]` identifies the exact occurrence pair. The answer stores values `[nums1[i], nums2[j]]`, while indices remain internal bookkeeping.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [1, 7, 11], "nums2": [2, 4, 6], "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The sorted-row frontier.

Initially, the smallest element in row `i` is its pair with `nums2[0]`. If the heap contains that first element for every considered row, its minimum is the globally smallest unreturned pair sum.

After removing row `i`'s front at column `j`, the only newly exposed candidate in that row is column `j + 1`. All later columns have sums at least as large. Pushing that one successor restores the invariant that the heap contains each nonexhausted row's smallest unreturned pair.

This is the same principle used to merge sorted lists: never insert an entire row, only its current front.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Initially, the smallest element in row `i` is its pair with ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why only the first `min(k, len(nums1))` rows are seeded.

The source builds initial entries from `nums1[:k]`. If `nums1` has more than `k` values, consider any omitted row index `i >= k`. Its smallest pair is `(nums1[i], nums2[0])`.

There are already `k` seeded pairs

$$
(\texttt{nums1}[0],\texttt{nums2}[0]),\ldots,
(\texttt{nums1}[k-1],\texttt{nums2}[0])
$$

whose sums are no larger because `nums1` is sorted. Therefore no omitted row is required to supply a pair strictly before the first `k` candidates. If sums tie, choosing the seeded occurrences is still valid because the contract accepts any collection of `k` smallest-sum pairs among tied possibilities.

Seeding beyond `k` would only enlarge the heap without improving the result.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 2], [1, 4], [1, 6]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [1, 7, 11], "nums2": [2, 4, 6], "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 2], [1, 4], [1, 6]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Generate all Cartesian-product pairs:** Build :** - **Generate all Cartesian-product pairs:** Build $mn$ sums, sort them, and take `k`. This costs at least $O(mn)$ space and $O(mn\log(mn))$ time, ignoring the small requested output.
- **- **Grid best-first search with a visited set:** S:** - **Grid best-first search with a visited set:** Start from `(0,0)` and push right/down neighbors while deduplicating states. It is correct but carries a visited set and can grow more frontier states than the row-merge formulation.
- **- **Binary-search a sum threshold:** Count how man:** - **Binary-search a sum threshold:** Count how many pairs have sum at most a candidate value, find the kth threshold, then enumerate qualifying pairs. This can be useful for counts but is more complicated when actual occurrence pairs must be returned.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(h)$. Let $m=\lvert\texttt{nums1}\rvert$, $n=\lvert\texttt{nums2}\rvert$, and $h=\min(k,m)$.
- **Auxiliary Space Complexity:** $O(h)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
