# Guided Example: Mean of Array After Removing Some Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]}`
- **Required output:** `2.0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `arr`, return *the mean of the remaining integers after removing the smallest `5%` and the largest `5%` of the elements.*

The objective is to compute `2.0` from `{"arr": [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sorting identifies the two trimmed tails

The task removes the smallest five percent and largest five percent by element count. After sorting `arr` in ascending order:

- the smallest values occupy the beginning;
- the largest values occupy the end;
- the values to average form one contiguous middle slice.

The source sorts the input list in place with `arr.sort()`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Calculate the slice boundaries

For length `n`, the source computes:

`start = int(n * 0.05)`

`end = int(n * 0.95)`.

The constraint says `n` is a multiple of 20. Therefore, five percent of `n` is an integer $n/20$, and 95 percent is $19n/20$.

The slice `arr[start:end]` excludes indices below `start` and excludes index `end` and everything after it. It removes exactly $n/20$ values from the front and:

$$
n-\frac{19n}{20}=\frac{n}{20}
$$

values from the back.

Using integer arithmetic `n // 20` and `n - n // 20` would avoid floating representation entirely, but the exact source uses decimal multiplications followed by `int`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For length `n`, the source computes:

`start = int(n * 0.05)... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why positional trimming handles duplicates

The instruction removes a percentage of elements, not every element equal to a threshold. If several equal values straddle a trim boundary, only the required number of occurrences is removed.

Sorting and slicing operate by position, so they remove exactly the correct count. Which identical occurrence is considered removed makes no numerical difference.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2.0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2.0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sum the sorted middle without slicing:** Use `:** - **Sum the sorted middle without slicing:** Use `sum(arr[start:end])` still creates a slice in Python; an index loop or iterator such as `islice` can avoid the $O(N)$ middle copy.
- **Selection algorithms:** Find the lower and upper order-statistic boundaries in linear expected time, but handling exact counts and duplicates is more complex.
- **Counting sort:** With values bounded by $10^5$, a frequency array can compute the trimmed sum in $O(N+V)$ time and $O(V)$ space.
- **Heap trimming:** Keeping tails in heaps can avoid full sorting but is unnecessary for $N\le1000$.
- **Length 20:** Exactly one value is removed from each end.
- **Length multiple of 20:** It guarantees both five-percent counts are integers and retained length is exactly 90 percent.
- **Duplicate boundary values:** Slicing removes the required number of occurrences; equal copies are interchangeable.
- **All values equal:** Trimming does not change the mean.
- **Zeros and large values:** Sorting and ordinary arithmetic handle the full allowed range.
- **Floating boundary calculation:** The exact code uses `int(n * 0.05)` and `int(n * 0.95)`; integer formulas `n // 20` and `n - n // 20` are more robust conceptually.
- **Five-place rounding:** It is within the accepted tolerance, though Python’s rounding semantics may use ties-to-even.
- **Input mutation:** The original order is lost because `arr.sort()` is in place.
- **Non-empty retained set:** Removing ten percent from a length of at least 20 always leaves elements for division.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N)$. Let $N$ be the array length.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
