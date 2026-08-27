# Guided Example: Find the Value of the Partition

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 2, 4]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **positive** integer array `nums`.

The objective is to compute `1` from `{"nums": [1, 3, 2, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The partition value is a distance between two input values

For any valid partition, let:

- $a=\max(\texttt{nums1})$;
- $b=\min(\texttt{nums2})$.

Both $a$ and $b$ are elements taken from the original array, and the partition value is $\lvert a-b\rvert$.

Therefore no partition can achieve a value smaller than the smallest absolute difference between any two array elements. The remaining question is whether that global closest-pair gap can always be realized by a partition. It can.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 2, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sorting reveals the closest pair

After sorting:

$$
v_0\le v_1\le\cdots\le v_{n-1},
$$

the minimum absolute difference between any two values occurs between adjacent elements.

If a nonadjacent pair $v_i,v_j$ with $i<j$ is chosen, its gap is the sum of adjacent nonnegative gaps from $i$ to $j$. null of those component gaps can exceed the whole sum, so at least one adjacent pair is no farther apart.

The expression `min(b - a for a, b in pairwise(nums))` computes the smallest adjacent gap. Since the list is sorted, `b-a` is already nonnegative and no absolute-value call is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | After sorting:

$$
v_0\le v_1\le\cdots\le v_{n-1},
$$

the m... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the adjacent gap is attainable as a partition value

Let adjacent sorted values `a` and `b` achieve the minimum gap.

Place all values at or below `a` into `nums1` and all values at or above `b` into `nums2`. Because `a` and `b` are adjacent in sorted order, there is no value strictly between them that creates an assignment problem.

Then `max(nums1)=a` and `min(nums2)=b`, so the partition value is `b-a`. Both arrays are nonempty because they contain the selected occurrences.

If duplicate values make `a=b`, place one occurrence in each partition. Distribute lower values to the first side and higher values to the second. Both extrema equal the duplicated value, producing value zero.

Thus the smallest adjacent gap is not merely a lower bound; a legal partition achieves it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 2, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Check every pair:** Finds the closest values i:** - **Check every pair:** Finds the closest values in $O(n^2)$ time but ignores the adjacent-after-sorting property.
- **Balanced tree insertion:** Can track predecessor and successor gaps in $O(n\log n)$ time without a full final sort, but is more complex.
- **Counting array:** Useful only when the numeric range is small; values here reach $10^9$.
- **Two elements:** They must be separated, and their absolute difference is the only adjacent gap.
- **Duplicate values:** Adjacent gap zero is attainable by placing different occurrences on opposite sides.
- **Already sorted input:** Timsort may run faster, while the asymptotic bound remains $O(n\log n)$.
- **Original order:** Irrelevant to partition membership, but the exact source destroys it through in-place sorting.
- **Unequal partition sizes:** Fully allowed; only nonemptiness matters.
- **Positive values:** The proof would also work for negative values because it depends only on sorted differences.
- **No partition construction:** The function correctly returns only the optimal value requested.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the array length. In-place sorting costs $O(n\log n)$ time. `pairwise(nums)` lazily produces $n-1$ adjacent pairs, and `min` scans them in $O(n)$ time. Sorting dominates, so total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
