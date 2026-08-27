# Guided Example: Missing Ranges

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 1, 3, 50, 75], "lower": 0, "upper": 99}`
- **Required output:** `[[2, 2], [4, 49], [51, 74], [76, 99]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an inclusive range `[lower, upper]` and a **sorted unique** integer array `nums`, where all elements are within the inclusive range.

The objective is to compute `[[2, 2], [4, 49], [51, 74], [76, 99]]` from `{"nums": [0, 1, 3, 50, 75], "lower": 0, "upper": 99}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Missing values form maximal gaps

Because `nums` is sorted, unique, and entirely inside `[lower, upper]`, every
missing integer belongs to one of three locations:

- before the first array value;
- between two consecutive array values;
- after the last array value.

Within any such location, all consecutive integers are missing. Combining them
into one inclusive pair gives the shortest representation. Splitting one gap
would add unnecessary ranges, while merging across an existing number would
incorrectly include that number.

The selected method handles the empty array separately, then checks the leading
boundary, every internal neighboring pair, and the trailing boundary.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 1, 3, 50, 75], "lower": 0, "upper": 99}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Cover an empty array in one range

If `nums` has no elements, every integer from `lower` through `upper` is
missing. The shortest exact answer is therefore `[[lower, upper]]`.

This early return is also necessary for safe indexing: all later boundary
checks read `nums[0]` or `nums[-1]`.

Even when `lower == upper`, the pair `[lower, upper]` is the correct
single-number range. The output schema always uses two-element numeric lists;
it does not convert singleton gaps to a special string format.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If `nums` has no elements, every integer from `lower` throug... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Check the leading and trailing gaps

If `nums[0] > lower`, the integers from `lower` through `nums[0] - 1` do not
appear in the array. The source appends exactly
`[lower, nums[0] - 1]`.

If `nums[0] == lower`, there is no leading gap, so nothing is appended. Values
below `lower` are outside the requested interval and must never appear.

The symmetric trailing check compares `nums[-1]` with `upper`. If the last
present number is smaller, `[nums[-1] + 1, upper]` is missing. Equality means
the upper endpoint is already covered by `nums`.

These checks use strict inequalities, preventing invalid ranges whose start
would exceed their end.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[2, 2], [4, 49], [51, 74], [76, 99]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 1, 3, 50, 75], "lower": 0, "upper": 99}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[2, 2], [4, 49], [51, 74], [76, 99]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sentinel scan:** Treat `lower - 1` and `upper :** - **Sentinel scan:** Treat `lower - 1` and `upper + 1` as virtual present values, allowing one uniform loop over every gap.
- **Enumerate every integer:** Simple but can take time proportional to `upper - lower`, far larger than `n`.
- **Empty `nums`:** Return the complete inclusive interval as one range.
- **No missing values:** Boundary checks and consecutive pairs append nothing.
- **Singleton gap:** It remains `[x, x]` under the required numeric-pair schema.
- **Negative bounds:** Addition, subtraction, and ordering work unchanged.
- **Boundary presence:** Equality at either bound prevents an empty or reversed range.
- **Unique sorted guarantee:** It makes every adjacent difference positive and ranges naturally ordered.
- **Output space:** The result itself may be linear even though working storage is constant.
- **Missing imports:** `List` and `pairwise` must be supplied for standalone execution.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(nums)`. The pairwise scan examines $n-1$ adjacent pairs, and
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
