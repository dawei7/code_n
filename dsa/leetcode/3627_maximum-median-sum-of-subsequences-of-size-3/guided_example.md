# Guided Example: Maximum Median Sum of Subsequences of Size 3

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 1, 3, 2, 1, 3]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` with a length divisible by 3.

The objective is to compute `5` from `{"nums": [2, 1, 3, 2, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What one triple needs

For a selected value to be the median of a triple, the triple needs:

- one value no greater than it;
- one value no smaller than it.

The low member does not contribute to the score, so it is best to spend the globally smallest available values in that role. The high member also does not contribute, but it must be at least the median.

This leaves the upper two-thirds to supply one median and one high partner per triple.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 1, 3, 2, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sorted indexing

After sorting, write:

`a[0] <= a[1] <= ... <= a[3g-1]`.

The smallest third is `a[0...g-1]`.

The upper two-thirds are paired as:

- `(a[g],a[g+1])`;
- `(a[g+2],a[g+3])`;
- ...
- `(a[3g-2],a[3g-1])`.

In each pair, the first value is no larger than the second and can serve as the median while the second serves as the high element.

The slice starts at index `g` and advances by two, summing:

$$
a_g+a_{g+2}+\cdots+a_{3g-2}.
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Constructing actual triples

For each `i=0...g-1`, form:

`(a[i], a[g+2i], a[g+2i+1])`.

The first element comes from the smallest third and is no greater than the chosen median. The final element is the paired upper value and is no smaller than the median. Therefore, the middle value after sorting that triple is exactly `a[g+2i]`.

Every sorted array position is used once, so these triples form a valid sequence of removals achieving the slice sum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 1, 3, 2, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two-pointer construction:** Sort, then pair values from the upper end while consuming fillers from the lower end. It yields the same medians without materializing a slice.
- **Heap-based selection:** It can identify large values but is more complex and does not beat comparison sorting for the full grouping.
- **Enumerate triple partitions:** The number of partitions is enormous and unnecessary after the exchange argument.
- **Three elements:** `g=1`, and the slice selects the ordinary median of the whole array.
- **All values equal:** Every grouping has the same median sum, and the source returns `g` times that value.
- **Duplicate values:** Nondecreasing comparisons allow equality; median/high roles remain valid.
- **Very large outliers:** Each median still needs a distinct high partner, so not every large value can itself contribute.
- **Smallest third:** They are fillers, not necessarily grouped in any special order beyond one per triple.
- **Length divisibility:** The contract guarantees `n%3==0`, so exactly `g` complete triples exist.
- **Positive values:** The exchange proof does not rely on positivity, but the constraint supplies it.
- **Removal order:** Any constructed partition can be removed in arbitrary sequence.
- **Input mutation:** The exact source reorders `nums` in place.
- **Slice allocation:** The concise expression uses linear extra memory for selected medians.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let `n=len(nums)`. Sorting dominates at `O(n\log n)` time. The slice contains `n/3` elements and summing it costs `O(n)`, so total time remains `O(n\log n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
