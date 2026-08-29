# Guided Example: Make Array Elements Equal to Zero

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 0, 2, 0, 3]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `2` from `{"nums": [1, 0, 2, 0, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Replace the movement simulation with mass on each side.** A valid starting position must contain zero. For such a position, let $L$ be the sum of all values strictly to its left and $R$ the sum strictly to its right. Because the starting value itself is zero, the total array sum is $S=L+R$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 0, 2, 0, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Each unit of value represents one decrement the moving process must eventually perform. The exact locations within one side affect travel distance, but not the order in which the two sides receive decrements.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Positive encounters force alternating sides.** Whenever the cursor reaches a positive element, it subtracts one and reverses direction. It then travels across any intervening zeros until it finds positive mass on the opposite side or leaves the array. Therefore successful decrements alternate between the right side and the left side.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 0, 2, 0, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Direct simulation:** Copy the array and simulate both directions from every zero. It follows the statement literally but can require $O(n^2m)$ time when values are as large as $m$.
- **Prefix-sum array:** It provides $L$ and $R$ in constant time per zero but spends $O(n)$ space; the running sum is sufficient.
- **Equal side sums:** Both starting directions are distinct valid selections and contribute two.
- **Right side heavier by one:** Only starting right is valid.
- **Left side heavier by one:** Only starting left is valid.
- **Imbalance greater than one:** Alternation guarantees failure in both directions.
- **All values zero:** Every index is a legal start and both directions immediately leave an already-zero array, so the answer is $2n$.
- **Zero at the first index:** Its left sum is zero; it is valid only when the right sum is zero or one.
- **Zero at the last index:** The symmetric right sum is zero.
- **Consecutive zeros:** Each zero is a different starting-position choice and must be counted separately, even though their side sums may match.
- **Positive values only affect sums:** Their exact distances from the start change the path length but not validity.
- **Nonnegative constraint:** The mass interpretation relies on values never being negative.
- **Input preservation:** Using arithmetic conditions avoids the copies and mutations required by simulation.
- **At least one zero:** The contract guarantees a possible starting position to inspect, though it does not guarantee any valid selection.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(nums)`. Computing `s` takes $O(n)$ time, and the second pass takes another $O(n)$ time. The total is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
