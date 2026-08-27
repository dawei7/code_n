# Guided Example: Count the Number of Fair Pairs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 1, 7, 4, 4, 5], "lower": 3, "upper": 6}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **0-indexed** integer array `nums` of size `n` and two integers `lower` and `upper`, return *the number of fair pairs*.

The objective is to compute `6` from `{"nums": [0, 1, 7, 4, 4, 5], "lower": 3, "upper": 6}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sorting turns valid partners into one contiguous interval

For a fixed first value $x$, a partner value $y$ is valid exactly when

$$
\texttt{lower}-x\le y\le\texttt{upper}-x.
$$

In an unsorted array, qualifying partners can appear anywhere. After sorting, every value in this numeric interval appears in one contiguous block, whose boundaries can be found with binary search.

Sorting changes element positions, but the answer asks for the number of unordered pairs of distinct original indices, not for the indices themselves. Sorting preserves every occurrence as a separate element and preserves every pair sum. It only gives the values a useful order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 1, 7, 4, 4, 5], "lower": 3, "upper": 6}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Fix the left member of each sorted pair

The loop visits sorted index $i$ with value `x`. It searches only the suffix beginning at `i + 1`. This restriction serves two purposes:

- an element can never pair with itself;
- every pair is counted once, when its smaller sorted index is the fixed index.

Even when values are equal, their array occurrences have different sorted positions. One occurrence at $i$ can pair with equal occurrences after it, and those are distinct original-index pairs.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The loop visits sorted index $i$ with value `x`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find the first partner meeting the lower bound

The expression

`j = bisect_left(nums, lower - x, lo=i + 1)`

returns the first suffix position whose value is at least `lower - x`. Every suffix element before $j$ is too small: adding it to $x$ produces a sum below `lower`. Every element from $j$ onward satisfies the lower inequality until values perhaps become too large for the upper inequality.

Passing `lo=i + 1` is essential. Without it, the binary search could return the fixed element or an earlier element, causing self-pairs or double counting.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 1, 7, 4, 4, 5], "lower": 3, "upper": 6}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two threshold sweeps:** Count pairs with sum b:** - **Two threshold sweeps:** Count pairs with sum below `upper + 1` using two pointers, subtract the count below `lower`, and obtain the same answer after sorting in $O(n)$ scan time.
- **Check every pair:** Two nested loops take $O(n^2)$ time, which is too slow for $10^5$ values.
- **Frequency map:** Counting by value can help when the number of distinct values is small, but duplicate multiplicities and range queries make the sorted method simpler and reliably $O(n\log n)$.
- **Exact single sum:** When `lower == upper`, the two boundaries isolate partners producing exactly that sum.
- **Negative values:** Binary search works on sorted numeric order without assuming positivity.
- **Duplicate values:** Occurrences remain separate list entries, so all distinct-index combinations are counted.
- **One-element array:** Every suffix is empty, both bisections return the same position, and the answer is zero.
- **No valid partner:** The lower and upper insertion points coincide, contributing zero.
- **All pairs valid:** Each fixed index contributes the size of its suffix, and the total becomes $n(n-1)/2$.
- **Input mutation:** `nums.sort()` changes the original order; sort a copy if the caller requires preservation.
- **Inclusive bounds:** The lower search uses “at least,” while `upper - x + 1` converts the inclusive upper condition into an exclusive lower-bound search.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log n)$. Let $n$ be the number of values. Python sorting takes $O(n\log n)$ time. The loop runs $n$ times and performs two $O(\log n)$ binary searches, adding another $O(n\log n)$ time. The combined bound remains $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
