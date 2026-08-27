# Guided Example: Rank Transform of an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [40, 10, 20, 30]}`
- **Required output:** `[4, 1, 2, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `arr`, replace each element with its rank.

The objective is to compute `[4, 1, 2, 3]` from `{"arr": [40, 10, 20, 30]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Removing duplicates first

`set(arr)` retains one copy of every distinct value. This ensures that duplicates do not occupy multiple rank positions.

For `[100,100,100]`, the set contains only `100`. Sorting gives `[100]`, so every original occurrence receives rank one.

If duplicates remained in the sorted list, the next larger value could receive a rank with an unnecessary gap, violating the “as small as possible” rule.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [40, 10, 20, 30]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sorting establishes rank order

After sorting, `t` has strictly increasing values:

$$
t[0] < t[1] < \cdots < t[u-1],
$$

where $u$ is the number of distinct values.

The value at index zero must have rank one, the value at index one rank two, and generally `t[k]` rank `k + 1`.

Negative numbers and large magnitudes cause no special problem because only comparisons determine order.

This also explains why numerical gaps do not create rank gaps. If the only distinct values are `-100` and `5000`, their positions in `t` are zero and one, so their ranks are one and two. Rank measures how many distinct input values are no larger, not the arithmetic distance between values.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | After sorting, `t` has strictly increasing values:

$$
t[0] ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why `bisect_right` returns the rank

`bisect_right(t, x)` returns the insertion position after all entries less than or equal to `x`.

Every `x` being queried came from `arr` and therefore appears exactly once in `t`. If it is at zero-based index `k`, there are `k + 1` distinct values at most `x`. The right insertion position is consequently `k + 1`, exactly its required one-based rank.

For `t = [10,20,30,40]`:

- `bisect_right(t, 10)` is one;
- `bisect_right(t, 20)` is two;
- `bisect_right(t, 40)` is four.

`bisect_left(t, x) + 1` would be an equivalent expression. The exact source uses the right boundary so no explicit addition is needed.

Using `bisect_right` on a list that still contained duplicates would not work this way: it would return the position after every equal copy and inflate the rank. Deduplicating before binary search is therefore part of the correctness argument, not merely a memory optimization.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[4, 1, 2, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [40, 10, 20, 30]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[4, 1, 2, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Rank dictionary:** Enumerate the sorted unique:** - **Rank dictionary:** Enumerate the sorted unique values and map each to index plus one, then perform expected constant-time lookups.
- **Sort the full array:** It can still derive ranks by skipping duplicates, but stores and processes repeated values unnecessarily.
- **`bisect_left + 1`:** It is equivalent because every queried value exists exactly once in `t`.
- **All values equal:** The unique list has length one, and every rank is one.
- **Strictly increasing input:** Output is `[1,2,\ldots,n]`.
- **Strictly decreasing input:** Ranks appear in decreasing order while preserving input positions.
- **Negative values:** Sorting and binary search handle them normally.
- **Empty array:** Both the lookup and result lists are empty.
- **Duplicate values:** Deduplication ensures equal ranks and no gaps.
- **Original array unchanged:** The method returns a new rank list rather than overwriting `arr`.
- **Binary-search cost:** Although sorting dominates broadly, exact lookup is $O(\log u)$ per element rather than hash-map constant expected time.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(u)$. Let $n$ be the array length and $u$ the number of distinct values.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
