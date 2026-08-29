# Guided Example: Next Greater Element IV

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 4, 0, 9, 6]}`
- **Required output:** `[9, 6, 6, -1, -1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array of non-negative integers `nums`. For each integer in `nums`, you must find its respective **second greater** integer.

The objective is to compute `[9, 6, 6, -1, -1]` from `{"nums": [2, 4, 0, 9, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Rephrase “second greater” as an ordered-index query

For index `i`, consider all indices to its right whose values are strictly greater than `nums[i]`. Sort those qualifying indices by their natural array order. The first is the first greater element; the second, if it exists, is exactly the requested second greater element.

The exact solution processes elements from larger value to smaller value while maintaining a sorted set of indices already processed. When handling `i`, that set represents positions with values strictly greater than `nums[i]`. It can then select the second stored index greater than `i`.

This differs from the manifest summary's two-monotonic-stack $O(n)$ method. The protected source uses sorting plus a `SortedList` and therefore takes $O(n\log n)$ time.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 4, 0, 9, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sort values in descending order

`arr = [(x,i) for i,x in enumerate(nums)]` creates value-index pairs. Sorting with `key=lambda x: -x[0]` processes larger values first.

Python's sort is stable. Equal values retain their original increasing-index order from `enumerate`. This stability is important because equal values are not strictly greater and should not act as candidates for one another.

When an equal-valued earlier index has already been added to `sl`, it lies to the left of the current index. The later equal-valued indices, which would lie to its right, have not yet been processed. Thus positions in `sl` to the right of current `i` all have strictly greater values.

Without stable tie ordering or explicit equal-value batching, inserting one equal value before another could incorrectly treat it as greater if its index were to the right.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Locate the first two greater positions

`sl` stores processed indices in ascending order. For current index `i`,

`j = sl.bisect_right(i)`

returns the list position of the first stored index strictly greater than `i`. If it exists, `sl[j]` is the first greater element to the right. The requested answer is the next qualifying index, `sl[j+1]`.

The condition `j + 1 < len(sl)` checks that this second index exists. If so, `ans[i] = nums[sl[j+1]]` stores its value. Otherwise the initial -1 remains.

After answering the current index, `sl.add(i)` makes it available as a greater-value position for later-processed smaller values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[9, 6, 6, -1, -1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 4, 0, 9, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[9, 6, 6, -1, -1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two monotonic stacks:** Move indices from a stack awaiting their first greater value to one awaiting their second, resolving the second stack as new values arrive. This matches the manifest and achieves $O(n)$ time.
- **Batch equal values:** Process all indices of one value by querying first and adding the entire group afterward. This removes reliance on stable tie order and is often clearer for strict comparisons.
- **Balanced tree of indices:** Any ordered set supporting successor queries and insertion can replace `SortedList` with the same $O(n\log n)$ structure.
- **Duplicate values:** Equal values do not count as greater. Stable ascending-index tie processing prevents later equals from appearing in the queried right-side set.
- **Fewer than two greater elements:** The answer remains the initialized -1.
- **Greater values before `i`:** They are stored but ignored by `bisect_right(i)` because only positions to the right matter.
- **Second qualifying index:** Its numeric value can be smaller than the first greater value; only both must exceed `nums[i]`.
- **Strict comparison:** Values equal to `nums[i]` must never count, which is the subtle reason tie handling matters.
- **Single element:** The sorted set is initially empty, so the sole answer is -1.
- **Metadata mismatch:** The exact implementation is sorting plus ordered-index queries in $O(n\log n)$, not the documented two-stack linear scan.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the array length. Building pairs takes $O(n)$ time and space. Sorting them takes $O(n\log n)$ time. Each of the $n$ iterations performs one `bisect_right` and one `SortedList.add`, each $O(\log n)$ for the balanced sorted-container implementation. Total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
