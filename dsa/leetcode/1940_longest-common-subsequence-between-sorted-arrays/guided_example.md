# Guided Example: Longest Common Subsequence Between Sorted Arrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arrays": [[1, 3, 4], [1, 4, 7, 9]]}`
- **Required output:** `[1, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integer arrays `arrays` where each $\text{arrays}[i]$ is sorted in **strictly increasing** order, return *an integer array representing the **longest common subsequence** among **all** the arrays*.

The objective is to compute `[1, 4]` from `{"arrays": [[1, 3, 4], [1, 4, 7, 9]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sorted, strictly increasing arrays turn LCS into intersection

In a general longest-common-subsequence problem, two shared values may appear in conflicting orders, so dynamic programming must decide which matches can coexist. Here every input array is strictly increasing. Any value that appears in several arrays has the same relative order in all of them: smaller common values always precede larger common values.

Each array also contains a value at most once. Therefore the longest common subsequence consists of exactly the values present in every array, listed in increasing order. No further ordering decision is needed.

The exact solution counts occurrences across all arrays. The constraints restrict values to $1$ through $100$, so `cnt = [0] * 101` supplies one counter for every possible value. For each `x` in each row, `cnt[x] += 1` records that this array contains `x`.

Because a row is strictly increasing, it cannot contribute twice to the same counter. Thus `cnt[x]` is not merely the total number of occurrences; it is exactly the number of different input arrays containing $x$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arrays": [[1, 3, 4], [1, 4, 7, 9]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Select values found in every array

There are `len(arrays)` input arrays. A value is common to all of them exactly when its counter equals that number. The result comprehension enumerates counters in numeric index order:

`[x for x, v in enumerate(cnt) if v == len(arrays)]`.

Enumeration automatically returns qualifying values from zero through 100 in increasing order. Index zero never qualifies because input values start at one and there are at least two arrays, but including its unused counter simplifies direct indexing.

For arrays `[2, 3, 6, 8]`, `[1, 2, 3, 5, 6, 7, 10]`, and `[2, 3, 4, 6, 9]`, the counters for two, three, and six become three. All other encountered values have smaller counts. The comprehension returns `[2, 3, 6]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why all common values can be included together

Suppose $a<b$ are both present in every array. Strict increasing order forces $a$ to occur before $b$ in each array. Thus including $a$ never prevents including $b$. Applying this to every pair of common values shows that the complete sorted intersection is a subsequence of every array.

Any common subsequence can contain only values present in every array, so it cannot be longer than that intersection. Since the algorithm returns the entire intersection as a valid common subsequence, it is longest.

This also explains why no duplicate should appear in the result. Strictly increasing rows contain no duplicates, and the returned subsequence is itself strictly increasing.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arrays": [[1, 3, 4], [1, 4, 7, 9]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Set intersection:** Convert the first row to a set and repeatedly intersect it with later rows, then sort the result. This is correct but uses hashing and a final sort despite the small bounded value domain.
- **Repeated two-pointer intersection:** Merge the current common list with each sorted row. It takes linear time in the scanned data and does not rely on the value upper bound.
- **General LCS dynamic programming:** It would solve a much broader problem but waste time and memory because strict sorting eliminates order conflicts.
- **No common value:** No counter reaches the number of arrays, so the comprehension returns an empty list.
- **One shared value:** It is returned as a length-one subsequence.
- **Different row lengths:** Counts depend on membership, not row length, so no special handling is needed.
- **Value 100:** The counter has index 100 because its length is 101, so the upper bound is safely included.
- **Unused index zero:** It remains zero and cannot qualify because at least two arrays exist.
- **Strict-increase dependency:** Duplicate values in one row could falsely inflate a count; the exact method relies on the stated contract.
- **Sorted-order dependency:** In unsorted arrays, all common values need not form a common subsequence in sorted numeric order.
- **Result ordering:** Enumerating the counter array returns the required increasing sequence without a separate sort.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(T+V)$. Let $T$ be the total number of elements across all arrays and let $V=101$ be the counter-array length.
- **Auxiliary Space Complexity:** $O(V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
