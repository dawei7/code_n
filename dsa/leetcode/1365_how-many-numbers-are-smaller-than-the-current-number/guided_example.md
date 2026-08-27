# Guided Example: How Many Numbers Are Smaller Than the Current Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [8, 1, 2, 2, 3]}`
- **Required output:** `[4, 0, 1, 1, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given the array `nums`, for each $\text{nums}[i]$ find out how many numbers in the array are smaller than it. That is, for each $\text{nums}[i]$ you have to count the number of valid `j's` such that $j \neq i$ **and** $\text{nums}[j] < \text{nums}[i]$.

The objective is to compute `[4, 0, 1, 1, 3]` from `{"nums": [8, 1, 2, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn a counting question into a position question

For every original value `x`, the task asks how many array elements are strictly smaller than `x`. Comparing `x` with every other element would answer the question directly, but it repeats much of the same work. The exact solution instead creates `arr = sorted(nums)`. In this sorted copy, every value smaller than `x` must appear before the first occurrence of `x`.

That observation gives a direct equivalence:

$$
\text{number of elements smaller than }x
=
\text{index of the first }x\text{ in sorted order}.
$$

For example, sorting `[8, 1, 2, 2, 3]` produces `[1, 2, 2, 3, 8]`. The first `1` is at index zero, so nothing is smaller than one. The first `2` is at index one, so exactly one element is smaller. The first `3` is at index three, so three elements are smaller. The first `8` is at index four, so four elements are smaller.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [8, 1, 2, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why it must be the first occurrence

Duplicates are the reason an ordinary successful search is not enough. Both copies of `2` in the example need the answer one. If a search returned the second copy's index, it would incorrectly count the first `2` as smaller even though equal values do not satisfy the strict relation.

`bisect_left(arr, x)` finds the leftmost insertion position for `x`: the first index at which `x` could be inserted while keeping `arr` sorted. Every element before that position is strictly less than `x`. Every element from that position onward is greater than or equal to `x`. Thus its return value is exactly the desired count, including when `x` occurs many times.

It may help to separate an index from an element count. Python uses zero-based indices. If the first `x` is stored at index $k$, there are exactly $k$ slots before it, numbered from zero through $k-1$. Therefore the index itself is already the count; there is no need to add or subtract one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Duplicates are the reason an ordinary successful search is n... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Preserving the original order

Sorting rearranges values, but the result must align with the original `nums` positions. The solution therefore keeps `arr` only as a search structure and iterates through `nums` in its original order:

`[bisect_left(arr, x) for x in nums]`.

For each original `x`, it searches the same sorted copy and appends the count. This is why the answer for the sample is `[4, 0, 1, 1, 3]` rather than the counts in sorted-value order. Because `sorted(nums)` returns a new list, the caller's input list is not modified.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[4, 0, 1, 1, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [8, 1, 2, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[4, 0, 1, 1, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Frequency array and prefix counts:** Because e:** - **Frequency array and prefix counts:** Because every value lies between zero and one hundred, count each value and convert frequencies into counts of smaller values. This achieves the manifest's $O(n+U)$ time and $O(U)$ space, but it is tied to a small known universe.
- **Brute-force comparisons:** For every position, scan the whole array and count smaller values. It is easy to derive but costs $O(n^2)$ time.
- **First-rank dictionary:** Sort once and record the index only when a value is first encountered, then look up each original value. This has the same $O(n\log n)$ sorting cost and can avoid $n$ binary searches, at the price of a dictionary.
- **Duplicate values:** Every equal value receives the same answer because `bisect_left` always returns the shared first position, never an arbitrary duplicate position.
- **All values equal:** The first position of that value is zero, so every output entry is zero.
- **Smallest value:** Its left boundary is zero even if it appears several times, correctly showing that no value is strictly smaller.
- **Largest value:** Its first sorted index counts every smaller element but excludes all copies equal to it.
- **Original order:** Searching values from `nums` rather than iterating through `arr` is essential; otherwise the counts would be returned in sorted order.
- **Input mutation:** `sorted` creates a copy, so the method leaves `nums` unchanged. Using `nums.sort()` without retaining the original order would make constructing the correctly ordered result harder.
- **Import expectation:** The code calls `bisect_left` directly, so the execution environment must make that name available, commonly through `from bisect import bisect_left`.
- **Values outside the stated range:** The sort-and-binary-search method still works for arbitrary mutually comparable numbers; unlike the frequency-array alternative, it does not depend on the zero-to-one-hundred constraint.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the length of `nums`. Creating `arr` with comparison sorting takes $O(n\log n)$ time. Each call to `bisect_left` takes $O(\log n)$ time, and the comprehension makes $n$ calls, adding another $O(n\log n)$. The exact implementation therefore takes $O(n\log n)$ time overall.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
