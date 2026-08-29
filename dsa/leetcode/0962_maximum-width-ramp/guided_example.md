# Guided Example: Maximum Width Ramp

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [6, 0, 8, 2, 1, 5]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **ramp** in an integer array `nums` is a pair `(i, j)` for which `i < j` and $\text{nums}[i] \le \text{nums}[j]$. The **width** of such a ramp is $j - i$.

The objective is to compute `4` from `{"nums": [6, 0, 8, 2, 1, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A wide ramp wants an early small left endpoint

A ramp `(i, j)` needs `i < j` and `nums[i] <= nums[j]`. Its width grows when `i` is farther left and `j` farther right.

Not every index is useful as a left endpoint. If an earlier index has a value less than or equal to a later candidate, the earlier index dominates it: any right endpoint valid for the later candidate is also valid for the earlier one and gives at least as much width.

The first pass keeps only indices that establish a new strict prefix minimum.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [6, 0, 8, 2, 1, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Building the decreasing stack

The stack stores indices in increasing index order, while their values are strictly decreasing.

At index `i` with value `v`, the code appends when:

- the stack is empty; or
- `nums[stk[-1]] > v`.

If `v` is equal to or larger than the last stored minimum, some earlier stacked index has value at most `v` and dominates `i` as a left endpoint. Skipping `i` loses no maximum ramp.

For `[6, 0, 8, 2, 1, 5]`, the stack becomes indices `[0, 1]` with values `[6, 0]`. Every later value is at least zero, so none can be a better left candidate than index one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Scan right endpoints from farthest right

The second loop visits indices `i` from the end toward zero. For current right value `nums[i]`, it checks the most recently stored left candidate.

While:

`nums[stk[-1]] <= nums[i]`,

that left index and current right index form a valid ramp. The code updates width with `i - stk.pop()`.

The non-strict comparison is required because equal values are allowed in a ramp.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [6, 0, 8, 2, 1, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Check every pair:** It costs `O(N^2)` time.
- :** - **Check every pair:** It costs `O(N^2)` time.
- **Sort indices by value:** Processing indices in value order can track a minimum index in `O(N log N)` time.
- **Prefix minima and suffix maxima arrays:** A two-pointer scan gives linear time but uses two auxiliary arrays.
- **Strictly increasing array:** Only index zero is stacked, and it matches the last index for width `N - 1`.
- **Strictly decreasing array:** No positive-width ramp exists, so the answer stays zero.
- **Equal values:** Equality forms a valid ramp and must use `<=`.
- **Duplicate prefix minimum:** The later equal value is dominated and is not stacked.
- **Two elements:** The method returns one if the first value is at most the second, otherwise zero.
- **Early empty stack:** It means every candidate already received its best possible right endpoint.
- **Input preservation:** The algorithm stores indices and does not modify `nums`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be array length.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
