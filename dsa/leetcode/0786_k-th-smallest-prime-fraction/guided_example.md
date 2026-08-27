# Guided Example: K-th Smallest Prime Fraction

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [1, 2, 3, 5], "k": 3}`
- **Required output:** `[2, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a sorted integer array `arr` containing `1` and **prime** numbers, where all the integers of `arr` are unique. You are also given an integer `k`.

The objective is to compute `[2, 5]` from `{"arr": [1, 2, 3, 5], "k": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Organize all fractions into sorted lists

Every valid pair satisfies `i < j` and represents fraction `arr[i] / arr[j]`. Instead of generating all $\frac{n(n-1)}{2}$ fractions, group them by their denominator index `j`.

For a fixed `j`, valid numerator indices are:

`0, 1, 2, ..., j - 1`.

Because `arr` is strictly increasing and the denominator stays fixed, these fractions are already sorted:

$$
\frac{arr[0]}{arr[j]}
<
\frac{arr[1]}{arr[j]}
<
\cdots
<
\frac{arr[j-1]}{arr[j]}.
$$

There are `n - 1` such lists, one for every denominator index from one through `n - 1`. The problem is now to find the `k`th item in the sorted merge of these lists.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [1, 2, 3, 5], "k": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Put the first item of every list in a min-heap

The smallest fraction for denominator `j` uses numerator index zero. Since `arr[0] = 1`, the initial heap entry is:

`(1 / arr[j], 0, j)`.

The list comprehension builds one entry for each denominator. Its actual code uses `enumerate(arr[1:])`, so the enumeration position `j` is shifted back to the array index with `j + 1`.

The heap therefore exposes the smallest not-yet-consumed fraction across all denominator lists. Calling `heapify` constructs this min-heap in linear time.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The smallest fraction for denominator `j` uses numerator ind... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Advance only the list whose front was removed

Suppose the heap removes entry `(value, i, j)`. This fraction is the globally smallest remaining front.

The next unseen item from that same denominator list uses numerator `i + 1`. It is valid only when `i + 1 < j`, preserving the required numerator-index-before-denominator-index rule.

If valid, the method pushes:

`(arr[i + 1] / arr[j], i + 1, j)`.

All other lists keep their current fronts in the heap. This is the standard multiway merge idea used to combine sorted sequences.

If `i + 1 == j`, that denominator list is exhausted. Pushing it would create the invalid fraction `arr[j] / arr[j] = 1`, so no replacement is added.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [1, 2, 3, 5], "k": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Value binary search with two-pointer counting::** - **Value binary search with two-pointer counting:** Count fractions below a candidate in $O(n)$ time and track the largest qualifying fraction. It can avoid dependence on `k` but needs careful termination and fraction recovery.
- **- **Generate and sort all pairs:** It is straightf:** - **Generate and sort all pairs:** It is straightforward but costs $O(n^2)$ space and $O(n^2\log n)$ sorting time.
- **- **Exact cross-multiplication heap comparator:** :** - **Exact cross-multiplication heap comparator:** It avoids floating-point priorities while retaining the same multiway-merge structure and asymptotic bounds.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + k\log n)$. Let $n$ be the array length. Creating the `n - 1` initial entries and heapifying them costs $O(n)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
