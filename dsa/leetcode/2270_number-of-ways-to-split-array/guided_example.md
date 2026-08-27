# Guided Example: Number of Ways to Split Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [10, 4, -8, 7]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums` of length `n`.

The objective is to compute `2` from `{"nums": [10, 4, -8, 7]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A split needs one prefix sum and the total

For a split after index `i`, the left part is `nums[0:i + 1]` and the right part is `nums[i + 1:n]`. If the total array sum is `s` and the current left sum is `t`, then the right sum is `s - t`.

This identity removes the need to sum both parts for every candidate. The solution computes `s = sum(nums)` once, then grows `t` as the split moves from left to right.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [10, 4, -8, 7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Exclude the last element from split positions

The loop is `for x in nums[:-1]`. The slice contains every array value except the final one. After processing an element `x`, the conceptual split lies immediately after that element.

Stopping before the last element is essential because the problem requires at least one value on the right. If the loop included the last element, it would test an illegal split whose right side is empty.

The source guarantees at least two elements, so `nums[:-1]` always contains at least the first element and every legal split position is represented.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The loop is `for x in nums[:-1]`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Move the current value into the left sum

Before the first iteration, `t = 0` means no elements have entered the left side. When the loop reads `x = nums[i]`, it performs `t += x`. After this update,

$$
\texttt{t} = \sum_{j=0}^{i}\texttt{nums}[j].
$$

Since `s` is the sum of the whole array,

$$
\texttt{s} - \texttt{t}
=
\sum_{j=i+1}^{n-1}\texttt{nums}[j].
$$

The comparison `t >= s - t` therefore tests exactly the validity condition for the split after index `i`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [10, 4, -8, 7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Index-based rolling scan:** Loop through indic:** - **Index-based rolling scan:** Loop through indices zero to `n - 2` without slicing. It keeps the same `O(n)` time and achieves genuine `O(1)` auxiliary space.
- **Prefix-sum array:** It computes every split correctly in `O(n)` time but intentionally stores `O(n)` cumulative sums that the rolling method does not logically need.
- **Recompute both sides for each split:** Summing ranges independently takes `O(n^2)` time.
- **Compare** `2t \ge s`: This algebraically equivalent condition can shorten the expression, but doubling may overflow a narrow fixed-width type; Python is safe either way.
- **Two pointers:** Negative values destroy the monotonicity such a method would normally rely on.
- **Exactly two elements:** There is one legal split after index zero, and the loop evaluates it once.
- **All positive values:** Prefix sums increase, but the general comparison remains unchanged.
- **All negative values:** A more negative right side may make a split valid; exact sums handle this without assumptions.
- **Zero values:** Moving zero leaves `t` unchanged, but the new boundary is still a distinct split and is tested separately.
- **Equality of sums:** The comparison uses `>=`, so equal left and right sums count as valid.
- **Final index:** It is deliberately excluded so the right part never becomes empty.
- **Boolean arithmetic:** `true` contributes one and `false` contributes zero in Python.
- **Large magnitude total:** Wide signed arithmetic is required outside Python because sums may be positive or negative.
- **Temporary slice:** The exact source copies all but one list entry; this is the reason its actual space is linear.
- **Input values:** The original elements are never changed, even though a shallow slice is created.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the array length. `sum(nums)` takes `O(n)` time. Creating `nums[:-1]` copies `n - 1` list entries in `O(n)` time, and the loop scans those entries in another `O(n)` pass. Sequential linear passes combine to `O(n)` total time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
