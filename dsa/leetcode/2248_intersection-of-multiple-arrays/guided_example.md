# Guided Example: Intersection of Multiple Arrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]}`
- **Required output:** `[3, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a 2D integer array `nums` where $\text{nums}[i]$ is a non-empty array of **distinct** positive integers, return *the list of integers that are present in **each array** of* `nums`* sorted in **ascending order***.

The objective is to compute `[3, 4]` from `{"nums": [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count in how many rows each value appears

An integer belongs to the intersection exactly when it appears in every row of `nums`. The constraints provide a crucial guarantee: values inside each individual row are distinct.

Because of that guarantee, every occurrence of value `x` comes from a different row. If its total occurrence count equals `len(nums)`, then it appeared once in every row. If the count is smaller, at least one row omitted it.

The solution uses `cnt = [0] * 1001` because every value lies from one through one thousand. Array index `x` directly stores the number of rows containing `x`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Process every input value once

The nested loops visit every row and every integer in that row:

`cnt[x] += 1`.

No per-row set is needed because duplicates within a row are forbidden. That condition prevents one row from contributing two or more to the same value's count.

Let `q = len(nums)`. After all rows:

- if `cnt[x] == q`, `x` occurs in all `q` rows;
- if `cnt[x] < q`, it is absent from at least one;
- `cnt[x] > q` cannot occur under the distinct-within-row guarantee.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build sorted output without a separate sort

The return comprehension enumerates `cnt` from index zero through one thousand:

`[x for x, v in enumerate(cnt) if v == len(nums)]`.

Enumeration visits numeric indices in increasing order, so selected values are automatically ascending. No output sort is required.

Index zero is outside the allowed input value range. Its count stays zero, and since `nums` has at least one row, it cannot satisfy the equality. Keeping slot zero simplifies direct indexing without affecting output.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Repeated set intersection:** Convert rows to sets and intersect them. It is general and matches the manifest summary but uses hash structures instead of the bounded domain.
- **Sort every row and use pointers:** This avoids hashing but costs sorting time and requires more complicated multi-row coordination.
- **Count raw occurrences when duplicates are allowed:** That would be incorrect without first deduplicating each row; this solution relies on the stated uniqueness guarantee.
- **Single row:** All its values are returned in ascending order.
- **No common value:** No count reaches the row total, producing `[]`.
- **All rows identical:** Every row value reaches the required count.
- **Value one or one thousand:** Both map to valid counter endpoints.
- **Unused index zero:** It remains unselected because row count is positive.
- **Input rows unsorted:** Counting ignores their order; final index enumeration supplies sorting.
- **Different row lengths:** Only presence in every row matters, not row size.
- **Output distinctness:** Each numeric index is considered once, so no duplicate can appear.
- **Input preservation:** No row is sorted or mutated.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(U)$. Let
- **Auxiliary Space Complexity:** $O(T)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
