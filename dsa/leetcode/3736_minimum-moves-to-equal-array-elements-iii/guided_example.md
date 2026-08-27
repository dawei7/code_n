# Guided Example: Minimum Moves to Equal Array Elements III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 1, 3]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `3` from `{"nums": [2, 1, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The common final value cannot be below the current maximum

Only increments are allowed. If

$$
M=\max(\texttt{nums}),
$$

then an element already equal to `M` can never be decreased. Therefore any common final value `T` must satisfy `T >= M`.

Choosing `T=M` is feasible: increase every smaller value until it reaches the maximum and leave maximum elements unchanged. Choosing any larger target adds `T-M` extra increments to every one of the `n` elements, so it can never improve the total. The unique best target value is therefore the existing maximum.

This is the central reason the problem is simpler than variants that permit both increments and decrements. With two-way movement, a median can be optimal. With increases only, the largest current value is an unavoidable lower bound and is itself reachable.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 1, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sum each element's deficit

An element `nums[i]` needs exactly

$$
M-\texttt{nums}[i]
$$

moves to reach `M`. It cannot use fewer because each move changes it by only one, and that many increments directly achieve the target.

Summing gives

$$
\sum_{i=0}^{n-1}(M-\texttt{nums}[i]).
$$

Distribute the sum:

$$
\sum_{i=0}^{n-1}M-\sum_{i=0}^{n-1}\texttt{nums}[i]
=nM-S,
$$

where `S = sum(nums)`.

The exact source computes `n`, `mx`, and `s`, then returns `mx * n - s`. This compact formula is exactly the sum of individual deficits; it is not an approximation.

Notice that maximum-valued elements are included correctly even though they are not handled by a branch. Each contributes `M` to `nM` and the same `M` to `S`, so its net deficit is zero. Every smaller element contributes precisely the missing difference.

For `[2,1,3]`, `M=3` and `S=6`. The result is `3*3-6=3`, corresponding to one move for two, two moves for one, and zero for three.

For `[4,4,5]`, the result is `5*3-13=2`. Both fours receive one increment.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | An element `nums[i]` needs exactly

$$
M-\texttt{nums}[i]
$$... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why operations on different elements do not interact

Each move changes only one selected element. Increasing one value neither helps nor obstructs another value's progress. Once the final target is fixed at `M`, the minimum cost is therefore the sum of independent per-index minimum costs.

The order of moves is irrelevant. One may finish an element completely before touching the next or interleave increments arbitrarily; the total number remains the same.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 1, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Simulate one increment at a time:** This produ:** - **Simulate one increment at a time:** This produces the correct result but its running time depends on the numerical answer rather than just `n`. Algebraic deficits avoid all simulation.
- **Sort the array:** The maximum would then be at the end, but sorting costs $O(n\log n)$ and is unnecessary because order has no role.
- **Raise values to the average:** The average may be below the maximum and therefore unreachable without decreasing a maximum element.
- **Use the median:** A median minimizes absolute deviations when both increases and decreases are allowed. It is not valid under increase-only operations.
- **Choose a value above the maximum:** Every extra unit raises all `n` elements and adds `n` moves, so it is strictly worse.
- **All elements already equal:** `S=nM`, and the formula returns zero.
- **Single element:** It is already equal to every element in the array, so the result is zero.
- **Several maximum elements:** Their deficits are zero; only smaller elements contribute.
- **One very small element:** Its complete difference to `M` appears directly in `nM-S`.
- **Input order:** Reordering does not affect maximum, sum, or required moves.
- **Positive-value guarantee:** The proof actually works for arbitrary integers as long as increments are the only operation, but no extra handling is needed.
- **No input mutation:** Unlike a sorting approach, the aggregation leaves `nums` unchanged.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the array length. `max(nums)` scans all elements in $O(n)$ time, and `sum(nums)` performs another $O(n)$ scan. Constantly many linear passes remain $O(n)$ total time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
