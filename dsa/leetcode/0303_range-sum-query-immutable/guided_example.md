# Guided Example: Range Sum Query - Immutable

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [-2, 0, 3, -5, 2, -1], "queries": [[0, 2], [2, 5], [0, 5]]}`
- **Required output:** `[1, -1, -3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, handle multiple queries of the following type:

The objective is to compute `[1, -1, -3]` from `{"nums": [-2, 0, 3, -5, 2, -1], "queries": [[0, 2], [2, 5], [0, 5]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why subtracting two prefixes isolates a range

For an inclusive query `[left, right]`, `s[right + 1]` contains all values from index 0 through `right`:

$$
\texttt{s}[right+1]
=
\texttt{nums}[0]+\cdots+\texttt{nums}[left-1]
+
\texttt{nums}[left]+\cdots+\texttt{nums}[right].
$$

Meanwhile, `s[left]` contains exactly the portion before the requested range:

$$
\texttt{s}[left]
=
\texttt{nums}[0]+\cdots+\texttt{nums}[left-1].
$$

Subtracting cancels every element before `left`, leaving only the inclusive query range:

$$
\texttt{s}[right+1]-\texttt{s}[left]
=
\sum_{i=left}^{right}\texttt{nums}[i].
$$

This cancellation is the whole reason a query no longer needs a loop. Two already-computed cumulative totals encode the desired sum.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [-2, 0, 3, -5, 2, -1], "queries": [[0, 2], [2, 5], [0, 5]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why `right + 1` is necessary

Prefix index `k` is a boundary, not the index of the last included element. It represents the half-open original range `[0, k)`. To include original element `nums[right]`, the ending boundary must be one position after it, namely `right + 1`.

Using `s[right]` would sum only through original index `right - 1`, incorrectly excluding the query's last element. This is the most common off-by-one error in this pattern.

The left side does not need `left - 1`. Because `s[left]` already represents all elements strictly before `left`, it is exactly the amount that should be removed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Prefix index `k` is a boundary, not the index of the last in... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the leading zero matters

Suppose a query starts at index 0. There are no elements before the range, so the amount to subtract should be zero. With the leading prefix, `s[0]` supplies that zero naturally:

`s[right + 1] - s[0]`.

Without the leading zero, one common definition stores the sum through each index. Queries beginning at zero then require a separate conditional branch because there is no prefix at index `-1` that conceptually means zero. The extra element makes every valid query use the same formula.

It also makes a one-element query uniform. For `[i, i]`, the result is

$$
\texttt{s}[i+1]-\texttt{s}[i]=\texttt{nums}[i].
$$

Adjacent prefix boundaries differ by exactly the original element between them.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, -1, -3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [-2, 0, 3, -5, 2, -1], "queries": [[0, 2], [2, 5], [0, 5]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, -1, -3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sum every query directly:** Loop from `left` t:** - **Sum every query directly:** Loop from `left` through `right`. It uses $O(1)$ extra space but costs $O(right-left+1)$ per query and can repeat the same additions up to $10^4$ times.
- **Precompute every possible range:** Store a sum for all pairs `(left, right)`. Queries become constant-time, but construction and storage both grow to $O(n^2)$, far more than the one-dimensional prefix array requires.
- **Fenwick tree:** It supports prefix sums and point updates in $O(\log n)$ time. Updates are absent here, so its logarithmic queries and more complex indexing are unnecessary compared with $O(1)$ prefix subtraction.
- **Segment tree:** It supports mutable range queries but needs more code and $O(\log n)$ query time. Immutability lets prefix sums do better.
- **Prefix sums without a leading zero:** This works with a special case for `left == 0`, but the exact source's leading zero gives one formula for every query.
- **Using `s[right] - s[left]`:** This excludes `nums[right]` because prefix indices represent half-open boundaries. The correct ending index is `right + 1`.
- **Using `s[right + 1] - s[left + 1]`:** This also removes `nums[left]`, turning an inclusive range into one that begins after `left`.
- **Single-element range:** `[i, i]` returns the difference of adjacent prefixes, exactly `nums[i]`.
- **Full-array range:** `[0, n - 1]` returns `s[n] - s[0]`, the complete sum.
- **One-element input:** The prefix list is `[0, nums[0]]`, and the only valid query returns their difference.
- **All zeros:** Every prefix is zero, and every range sum is zero.
- **Negative numbers:** Prefix values may fall as elements are added, but algebraic cancellation remains exact.
- **Mixed signs with a zero total:** Equal prefix totals at different boundaries correctly indicate that the intervening range sums to zero.
- **Repeated queries:** No cache lookup keyed by the query is needed; every query is already constant-time, whether repeated or new.
- **Mutation after construction:** If the original data could change, stored prefixes would become stale from the changed index onward. The immutable contract is what makes one-time preprocessing correct.
- **Bounds guarantee:** The method performs no explicit index validation because every query is guaranteed to satisfy `0 <= left <= right < n`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+q)$. Let $n$ be the array length and $q$ the number of `sumRange` calls.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
