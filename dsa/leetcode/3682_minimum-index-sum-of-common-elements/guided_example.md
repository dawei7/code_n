# Guided Example: Minimum Index Sum of Common Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [3, 2, 1], "nums2": [1, 3, 1]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integer arrays `nums1` and `nums2` of equal length `n`.

The objective is to compute `1` from `{"nums1": [3, 2, 1], "nums2": [1, 3, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why one index per value is sufficient

Let

$$
i_x = \min\{i \mid \texttt{nums1}[i]=x\}
$$

and

$$
j_x = \min\{j \mid \texttt{nums2}[j]=x\}.
$$

For any good pair containing value $x$, its indices satisfy $i \ge i_x$ and $j \ge j_x$. Therefore,

$$
i+j \ge i_x+j_x.
$$

So the best pair for value $x$ is completely characterized by those two earliest positions. All later duplicates of $x$ are irrelevant to the minimum.

The source chooses to store earliest positions from `nums2`:

`d[x] = i`

but only when `x not in d`. Since `nums2` is scanned from left to right, the first time a value appears is its smallest index. Refusing to overwrite that entry preserves the useful index. Although the manifest summary describes recording positions from `nums1` and scanning `nums2`, the exact source does the symmetric reverse; the result and complexity are identical, and this explanation follows the actual code.

For example, if `nums2 = [7, 3, 7, 3]`, the dictionary stores `d[7] = 0` and `d[3] = 1`. The occurrences at indices $2$ and $3$ cannot improve a sum for their values, so they are intentionally ignored.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [3, 2, 1], "nums2": [1, 3, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Scanning the other array

The variable `ans` begins as positive infinity:

`ans = inf`

This sentinel means that no good pair has been found yet. The source then enumerates `nums1`. At position `i` with value `x`:

- if `x` is absent from `d`, there is no occurrence of `x` anywhere in `nums2`, so index `i` cannot form a good pair;
- if `x` is present, `d[x]` is the earliest matching index in `nums2`, and `i + d[x]` is the smallest sum possible using this particular occurrence of `nums1[i]`.

The candidate updates

`ans = min(ans, i + d[x])`.

The scan does not explicitly skip later duplicates in `nums1`. That is harmless: for the same value `x`, a later index `i` produces a sum at least as large as the one produced by its earliest occurrence. The `min` operation simply leaves the better earlier candidate unchanged. Storing an earliest-index dictionary for both arrays would save a few redundant checks but would use another data structure without improving the asymptotic bound.

Consider `nums1 = [3, 2, 1]` and `nums2 = [1, 3, 1]`. The dictionary is `{1: 0, 3: 1}`. At `nums1[0] = 3`, the candidate sum is $0+1=1$. The value $2$ has no match. At `nums1[2] = 1`, the candidate is $2+0=2$. The minimum remains $1$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the final minimum covers every good pair

Take any good pair $(i,j)$ with shared value $x$. When the algorithm scans `nums1[i]`, the dictionary contains the earliest occurrence `d[x] = j_x` of $x$ in `nums2`. Since $j_x \le j$,

$$
i + j_x \le i + j.
$$

Thus, for every possible good pair, the algorithm evaluates another good pair with the same `nums1` index and an index sum no larger. The minimum over the evaluated candidates can therefore be no greater than the true optimum.

In the other direction, every evaluated candidate uses an index `i` where `nums1[i] = x` and a stored index `d[x]` where `nums2[d[x]] = x`. Every candidate is a genuine good pair, so the algorithm cannot produce a value smaller than the true optimum by using an invalid combination.

Together, these two directions show that the smallest evaluated sum is exactly the minimum index sum among all good pairs.

If no common value exists, no candidate ever replaces `inf`. The final expression

`return -1 if ans == inf else ans`

then returns the required sentinel $-1$. If at least one match exists, every index sum is a finite nonnegative integer, so `ans` differs from infinity and the stored minimum is returned.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [3, 2, 1], "nums2": [1, 3, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Check every pair of indices:** Comparing every `nums1[i]` with every `nums2[j]` directly takes $O(n^2)$ time and repeats work for equal values.
- **Store all positions per value:** Lists of every occurrence are unnecessary because only the earliest index can minimize a sum. One integer per distinct value is enough.
- **Build two earliest-index maps:** This also leads to an $O(n)$ solution by intersecting their keys, but the second dictionary is optional. The exact source scans `nums1` directly.
- **Sort value-index pairs:** Sorting can group common values while retaining original indices, but it increases the running time to $O(n \log n)$.
- **Overwrite dictionary entries:** Assigning every occurrence from `nums2` would leave the latest index rather than the earliest one and could produce a nonminimum result. The `if x not in d` guard is essential.
- **No common value:** `ans` remains `inf` and the method returns $-1$, rather than leaking the sentinel.
- **A common value at index zero in both arrays:** The minimum possible sum is zero. The dictionary stores zero normally, and membership is tested with `x in d` rather than truthiness of the stored index.
- **Duplicate values in either array:** Only the earliest `nums2` index is stored. Later `nums1` occurrences may be checked, but cannot improve on an earlier occurrence of the same value.
- **Negative and zero element values:** Values are dictionary keys, not indices. Their sign has no effect on matching or on the nonnegative index sum.
- **Equal-length guarantee:** The method does not rely on synchronized positions; a good pair may use any `i` and `j`. Equal lengths affect only the shared symbol $n$ used in the complexity bound.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the common length of the two arrays, and let $u$ be the number of distinct values in `nums2`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
