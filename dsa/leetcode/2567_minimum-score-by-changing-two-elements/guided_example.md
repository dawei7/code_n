# Guided Example: Minimum Score by Changing Two Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 4, 7, 8, 5]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `3` from `{"nums": [1, 4, 7, 8, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The low score can always be made zero

The low score is the minimum absolute difference between any pair. After changing two elements, set at least one changed value equal to another value in the final array. Then two elements are equal and their absolute difference is zero. Since absolute differences cannot be negative, the low score is exactly zero.

With $n\ge3$, there is always an unchanged value available. The two changed elements can both be assigned a value already present among the survivors, creating duplicates without enlarging the remaining range.

Therefore, the optimization reduces to minimizing the high score, which is the maximum absolute difference. For any set of numbers, that maximum is simply

$$
\max(\texttt{nums})-\min(\texttt{nums}).
$$

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 4, 7, 8, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Only extreme values can control the high score

Changing an element strictly inside the current minimum and maximum cannot shrink the range: both old extremes would remain. To reduce the high score, the two permitted changes must neutralize two occurrences among the low and high extremes.

After sorting, write the values as

$$
a_0\le a_1\le\cdots\le a_{n-1}.
$$

There are only three ways to distribute two changes between the ends:

- change the two smallest values;
- change one smallest and one largest value;
- change the two largest values.

Changing any less-extreme combination cannot produce a smaller surviving interval, because an unchanged value farther outside would still determine the range.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Changing an element strictly inside the current minimum and ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Case one: neutralize the two smallest

If `nums[0]` and `nums[1]` are changed into values inside the interval of the remaining elements, the smallest unchanged value becomes `nums[2]` and the largest remains `nums[-1]`. The smallest possible high score for this case is

`nums[-1] - nums[2]`.

The changed values can, for example, both be assigned `nums[2]`. This keeps them inside the new range and also makes the low score zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 4, 7, 8, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Track six extremes:** Maintain the three small:** - **Track six extremes:** Maintain the three smallest and three largest values in one pass, then evaluate the same formulas in $O(n)$ time and $O(1)$ space.
- **Try all changed pairs:** Choosing two indices gives $O(n^2)$ possibilities and is unnecessary because only extreme removals can shrink the range.
- **Change interior elements:** Unless an extreme is also changed, the old minimum or maximum survives and prevents the high score from shrinking.
- **Exactly three elements:** Two can be changed to the third, so the answer is always zero.
- **All values equal:** Both low and high scores are already zero; changing values to themselves or the same value preserves zero.
- **Duplicate extremes:** The sorted formulas correctly account for remaining copies of a minimum or maximum.
- **Low score:** It need not be optimized separately once a changed element is assigned equal to a surviving value; zero is the absolute lower bound.
- **Large values:** Only subtraction is used, and Python integers avoid overflow.
- **Input mutation:** `nums.sort()` changes the original order. Sorting a copy would preserve caller state at $O(n)$ explicit storage.
- **Manifest distinction:** The three-case method is optimal in insight, but this exact implementation uses full sorting rather than constant-space extrema selection.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let $n$ be the array length. Sorting `nums` takes $O(n\log n)$ time. Evaluating three differences and their minimum takes $O(1)$ time. The exact implementation is therefore $O(n\log n)$, not the manifest's stated $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
