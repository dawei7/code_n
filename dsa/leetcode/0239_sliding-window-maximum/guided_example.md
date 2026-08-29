# Guided Example: Sliding Window Maximum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, -1, -3, 5, 3, 6, 7], "k": 3}`
- **Required output:** `[3, 3, 5, 5, 6, 7]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

The objective is to compute `[3, 3, 5, 5, 6, 7]` from `{"nums": [1, 3, -1, -3, 5, 3, 6, 7], "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The window boundaries

When the loop is processing index `i`, that index is the right endpoint of the current window. A window of length `k` ending at `i` begins at

$$
i-k+1.
$$

Therefore, a heap entry at index `j` is current exactly when

$$
j \ge i-k+1,
$$

or equivalently when $j>i-k$. Any entry satisfying $j\le i-k$ is stale.

The code uses precisely this test in `while q[0][1] <= i - k`. Notice the non-strict comparison. At the moment the right endpoint advances to `i`, the old index `i - k` is one position before the new window's left boundary, so it must no longer influence the answer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, -1, -3, 5, 3, 6, 7], "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build just before the first complete window

The initial comprehension inserts indices `0` through `k - 2`, the first `k - 1` elements. `heapify(q)` converts those pairs into a heap in linear time with respect to the number inserted. The main loop then begins at `i = k - 1`. It pushes the last element needed for the first full window before reading a maximum.

This division of work means every answer is produced by the same loop body:

1. Add the new rightmost element.
2. Remove stale entries from the top until the top belongs to the current window.
3. Convert the top's negated value back to its original sign and append it.

For `k = 1`, the initial slice `nums[:0]` is empty, so heapifying it is valid. Each main-loop iteration pushes the one visible element, removes any older top entries if necessary, and returns that element. Thus the same structure handles the smallest window without a separate branch.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why stale entries can be removed lazily

The heap may contain indices that have left the window. The solution does not search through the heap to delete every such entry because a binary heap supports efficient removal at the root, not efficient arbitrary removal by index. Instead, it performs lazy deletion: an expired entry is tolerated until it reaches the root.

This is safe because only the root is ever used as the answer. If a stale entry is buried below another entry, it cannot affect the reported maximum at that moment. When it eventually becomes the root, the `while` loop checks its index and discards it before any answer is appended. Several expired entries can surface consecutively, which is why the code uses `while` rather than `if`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 3, 5, 5, 6, 7]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, -1, -3, 5, 3, 6, 7], "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 3, 5, 5, 6, 7]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Monotonic decreasing deque:** Store useful indices in increasing index order and decreasing value order. Remove expired indices from the front and values dominated by the newcomer from the back. Each index enters and leaves once, giving $O(n)$ time and $O(k)$ auxiliary space; this is the stronger asymptotic solution described by the local editorial and manifest, but it is not what the exact optimal source implements.
- **Balanced multiset:** Insert the entering value, erase the leaving occurrence, and query the greatest value. This gives $O(n\log k)$ time and $O(k)$ space in languages with an ordered multiset, provided duplicates are represented correctly.
- **Direct scan of every window:** It uses only constant auxiliary space but costs $O(nk)$ in the worst case because it rediscovers nearly the same maximum repeatedly.
- **Lazy heap expiration:** Arbitrary expired entries do not need immediate deletion. Only an expired root can corrupt the answer, so root cleanup is sufficient for correctness, though it permits $O(n)$ memory growth.
- **Several stale roots:** The cleanup must be a `while` loop. Removing just one stale root may expose another stale entry before any current entry reaches the top.
- **Duplicate maximum values:** Pairing each value with its index distinguishes occurrences. Expiration is decided per occurrence, while either current occurrence yields the same maximum value.
- **`k = 1`:** The initial heap is empty, and every element becomes the maximum of its one-element window.
- **`k = n`:** Initialization loads the first $n-1$ values, the loop adds the last, and exactly one maximum is returned.
- **Negative values:** Negation still reverses priority correctly. For example, original `-3` is stored as `3`, while original `-1` is stored as `1`, so `-1` is recovered as the larger value.
- **Expired non-root entries:** Their presence is harmless for correctness but important for complexity analysis. Claiming the heap always contains only the current window would be inaccurate for this implementation.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the length of `nums`. Constructing and heapifying the first $k-1$ entries costs $O(k)$. Every one of the $n-k+1$ main iterations performs one heap insertion. A heap can contain as many as $O(n)$ entries, so an insertion costs $O(\log n)$ in the worst case.
- **Auxiliary Space Complexity:** $O(k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
