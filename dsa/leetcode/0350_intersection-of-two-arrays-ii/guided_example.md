# Guided Example: Intersection of Two Arrays II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [1, 2, 2, 1], "nums2": [2, 2]}`
- **Required output:** `[2, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must appear as many times as it shows in both arrays and you may return the result in **any order**.

The objective is to compute `[2, 2]` from `{"nums1": [1, 2, 2, 1], "nums2": [2, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why a set is no longer enough.

A set can answer whether a value occurs, but it cannot distinguish one occurrence from ten. For `nums1 = [2, 2]` and `nums2 = [2, 2]`, a set intersection would contain only one `2`, which is too few. The counter preserves the exact quantity available from one side, allowing the scan of the other side to match occurrences one by one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [1, 2, 2, 1], "nums2": [2, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Building the available supply.

`Counter(nums1)` visits all values in `nums1`. For every distinct integer `x`, `cnt[x]` becomes the number of times `x` occurs in that array. The answer begins empty because no occurrences from `nums2` have yet been matched.

The implementation always counts `nums1`. It does not compare the array lengths or swap the inputs. This detail differs from the variant manifest's summary, which says that the shorter array is counted. Counting the shorter input is a useful optimization, but it is not present in the checked-in source and must not be silently attributed to it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Consuming matches while scanning the second array.

For each `x` in `nums2`, the condition `if cnt[x]` asks whether at least one unmatched copy of `x` remains from `nums1`. A `Counter` returns zero for a missing key, so values that never occurred in `nums1` fail the condition. Counts begin nonnegative, and the solution decrements only after a successful match, so a false condition means exactly that no available copy remains.

When the condition is true, `ans.append(x)` records one common occurrence. The following `cnt[x] -= 1` is essential: that specific copy from `nums1` has now been paired with the current copy from `nums2` and cannot be reused. Without the decrement, every later duplicate in `nums2` would also pass whenever `nums1` contained the value at least once, potentially producing too many copies.

For example, take `nums1 = [1, 2, 2, 1]` and `nums2 = [2, 2]`. The counter begins with two available `1`s and two available `2`s. The first scanned `2` is appended and reduces the remaining `2` count to one. The second is also appended and reduces it to zero. The returned answer is `[2, 2]`.

Now change `nums2` to `[2, 2, 2, 2]`. The first two copies consume the two available copies from `nums1`. For the third and fourth copies, `cnt[2]` is zero, so neither is appended. This gives exactly the minimum of the two input frequencies.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [1, 2, 2, 1], "nums2": [2, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Count the shorter array:** Swap the inputs when `nums1` is longer, then run the same counter-and-consumption procedure. Time remains expected $O(n+m)$ while counter storage becomes $O(\min(n,m))$. This matches the manifest summary but is absent from the exact solution.
- **Two pointers on sorted arrays:** When both arrays are already sorted, compare their current values. Advance the smaller side, and append then advance both sides when equal. This takes $O(n+m)$ time and $O(1)$ auxiliary space excluding output, directly answering the first follow-up.
- **Sort unsorted inputs first:** Sorting and then using two pointers costs $O(n\log n+m\log m)$ time. It can reduce hash storage, but in-place sorting mutates inputs and sorting implementations may use additional memory.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let $n$ be `len(nums1)`, let $m$ be `len(nums2)`, let $u_1$ be the number of distinct values in `nums1`, and let $r$ be the total length of the returned multiset intersection.
- **Auxiliary Space Complexity:** $O(\min(n, m))$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
