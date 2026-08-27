# Guided Example: Kth Largest Element in an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 2, 1, 5, 6, 4], "k": 2}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` and an integer `k`, return *the* $$k^{\text{th}}$$ *largest element in the array*.

The objective is to compute `5` from `{"nums": [3, 2, 1, 5, 6, 4], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert the requested rank into one array index

The problem gives `k` as a one-based rank counted from the largest value. The
partition routine in the exact source arranges values in ascending relation to
a pivot and reasons with ordinary zero-based indices. For an array of length
$n$, the $k$th largest value occupies ascending sorted index $n-k$.

For example, in an array of six elements, the second largest is at ascending
index `6 - 2 = 4`: four elements occupy indices 0 through 3 before it. The
source therefore executes `k = n - k` before selection. From that point onward,
the local variable `k` means a fixed zero-based target index, not the original
one-based rank. Duplicates remain separate positions; no distinct-value set is
created, exactly as the contract requires.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 2, 1, 5, 6, 4], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Selection needs only the side containing the target

Sorting establishes the order of every element, but the method needs only the
value at one position. Quickselect partitions the active interval so that a
boundary separates values on the low side from values on the high side. Once
the target index is known to lie on one side, the other side can be discarded
without being internally sorted.

The nested function is named `quick_sort`, but it is a selection routine: after
each partition it recurses into only one subinterval. That one-branch behavior
is the difference between Quickselect and Quicksort.

The active range uses inclusive boundaries `l` and `r`. If `l == r`, only one
candidate remains, so `nums[l]` is returned. Otherwise the pivot value `x` is
read from the middle position `nums[(l + r) >> 1]`. The bit shift by one is
integer division by two for these nonnegative indices.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Sorting establishes the order of every element, but the meth... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Hoare partition uses two inward scans

The exact source applies Hoare's two-pointer partition scheme. Pointer `i`
starts one position before the interval at `l - 1`, and `j` starts one position
after it at `r + 1`. Each pass does the following:

- Increment `i` at least once, then continue moving it right while values are
  strictly less than the pivot. It stops at a value `nums[i] >= x`, which is
  potentially misplaced on the low side.
- Decrement `j` at least once, then continue moving it left while values are
  strictly greater than the pivot. It stops at a value `nums[j] <= x`, which
  is potentially misplaced on the high side.
- If `i < j`, swap those two stopped values. The smaller-or-equal value moves
  left, and the greater-or-equal value moves right.
- When `i >= j`, the scans have crossed, and `j` is returned implicitly as the
  partition boundary used by the following recursion decision.

The pivot is a value from inside the active range. Therefore the left scan must
encounter at least that pivot value, which is not less than itself, and the
right scan must encounter one, which is not greater than itself. These built-in
stopping points keep both scans inside the interval without explicit boundary
checks in the inner loops.

After crossing, every position from `l` through `j` contains a value no greater
than every value that has been forced to the right partition in the needed
partition sense, and every position from `j + 1` through `r` lies on the high
side. Neither side is fully sorted. Equal-to-pivot values may appear on both
sides, which is permitted and important for making progress when duplicates
are common.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 2, 1, 5, 6, 4], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Randomized in-place Quickselect:** Choose a un:** - **Randomized in-place Quickselect:** Choose a uniformly random pivot before the same one-sided recursion. It retains $O(n^2)$ theoretical worst-case time but gives expected $O(n)$ time independent of a fixed adversarial input pattern.
- **Three-way partitioning:** Separate values less than, equal to, and greater than the pivot. If the target falls in the equal block, return immediately; this is especially effective with many duplicates and matches part of the manifest description, but it is not the exact source.
- **Median of medians:** A carefully selected deterministic pivot guarantees $O(n)$ worst-case selection, but its implementation and constant factors are substantially more involved.
- **Min-heap of size `k`:** Keep the largest `k` values seen, with the heap root as the answer. It offers deterministic $O(n\log k)$ time and $O(k)$ space without mutating the input.
- **Counting frequencies:** The narrow guaranteed value range from $-10^4$ through $10^4$ allows $O(n+R)$ time and $O(R)$ space for range width $R$. It is deterministic and attractive here, though it depends on the numeric-domain constraint.
- **Full sorting:** Sorting and indexing is concise and deterministic but takes $O(n\log n)$ time and does more ordering work than selection requires.
- **`k = 1`:** The converted target is `n - 1`, the last ascending position, so selection returns the maximum.
- **`k = n`:** The converted target is 0, so selection returns the minimum.
- **All values equal:** Inner scans stop on equal values from both sides, swap or cross, and shrink the interval. The answer is that repeated value for every legal rank.
- **Negative values:** Partition comparisons work directly on signed integers; no offset or special case is needed.
- **One element:** The converted target is 0, the initial call satisfies `l == r`, and that element is returned without partitioning.
- **Mutation of `nums`:** Swaps change the caller-provided list's order. This is acceptable to the platform contract, but callers that require preservation must pass a copy, adding $O(n)$ time and space.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the number of elements. One partition of an active interval of size
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
