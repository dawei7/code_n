# Guided Example: Find Occurrences of an Element in an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 1, 7], "queries": [1, 3, 2, 4], "x": 1}`
- **Required output:** `[0, -1, 2, -1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`, an integer array `queries`, and an integer `x`.

The objective is to compute `[0, -1, 2, -1]` from `{"nums": [1, 3, 1, 7], "queries": [1, 3, 2, 4], "x": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Precompute the ordered occurrence positions once

Every query asks about the same target value `x`. Scanning `nums` independently for each query would repeat identical work.

The list comprehension

`ids = [i for i, v in enumerate(nums) if v == x]`

collects exactly the zero-based indices where `x` occurs. Because `enumerate` visits the array from left to right, `ids` is already in increasing order.

Its entries have a direct meaning:

- `ids[0]` is the first occurrence's index;
- `ids[1]` is the second occurrence's index;
- in general, `ids[k - 1]` is the $k$th occurrence's index.

No sorting or frequency map is required.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 1, 7], "queries": [1, 3, 2, 4], "x": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Convert one-based query numbers to zero-based list positions

Query values are one-based ordinals. For query `i`, the desired list position is `i - 1`.

If `i - 1 < len(ids)`, that occurrence exists and the code returns `ids[i - 1]`. Otherwise, fewer than `i` copies of `x` exist, so it returns -1.

The constraints guarantee `i >= 1`, making `i - 1` nonnegative. Without that guarantee, query zero would incorrectly use Python's negative indexing when `ids` is nonempty.

The output list comprehension preserves query order. Queries do not need to be sorted, and repeated queries correctly produce repeated answers.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Query values are one-based ordinals.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Example

For `nums = [1,3,1,7]` and `x = 1`, preprocessing produces `ids = [0,2]`.

- Query 1 reads `ids[0] = 0`.
- Query 3 requests position 2, which is not less than list length 2, so it returns -1.
- Query 2 reads `ids[1] = 2`.
- Query 4 also returns -1.

This produces `[0,-1,2,-1]`.

If `x` never appears, `ids` is empty. Every positive query has `i - 1 >= 0 = len(ids)`, so all answers are -1 without any special branch.


During preprocessing, an index enters `ids` if and only if the value at that index equals `x`. Since indices are visited in increasing order, the list is exactly the occurrence sequence required by ordinal queries.

For a query $k$, if $k\le\lvert\texttt{ids}\rvert$, the element at zero-based position $k-1$ is by construction the $k$th occurrence. If $k$ exceeds the list length, no $k$th occurrence exists and -1 is required. The conditional implements these two exhaustive cases.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, -1, 2, -1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 1, 7], "queries": [1, 3, 2, 4], "x": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, -1, 2, -1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Scan for each query:** It uses no occurrence l:** - **Scan for each query:** It uses no occurrence list but can take $O(nq)$ time.
- **Map every value to positions:** Useful if queries named different target values, but wasteful when all ask about one fixed `x`.
- **Binary search cumulative counts:** A prefix count array plus binary search can locate occurrences, but direct stored indices answer faster and use comparable space.
- **Sort queries by ordinal:** Unnecessary because lookup is already constant time and output must preserve original order.
- **x absent:** `ids` is empty and every answer is -1.
- **x at every position:** `ids` contains `0,1,\ldots,n-1`, so query $k$ returns $k-1$ when in range.
- **First occurrence:** Query 1 maps to list index 0.
- **Too-large query:** The length comparison returns -1 without an out-of-range access.
- **Repeated queries:** Each independently reads the same stored index and returns the same result.
- **Unsorted queries:** Their order has no effect on correctness.
- **Positive-query guarantee:** It prevents accidental negative indexing for query zero.
- **Input preservation:** Only a new occurrence list and result list are created.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+q)$. Let $n=\lvert\texttt{nums}\rvert$, $q=\lvert\texttt{queries}\rvert$, and $r$ be the number of occurrences of `x`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
