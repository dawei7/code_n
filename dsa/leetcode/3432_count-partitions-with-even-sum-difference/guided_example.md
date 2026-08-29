# Guided Example: Count Partitions with Even Sum Difference

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [10, 10, 3, 7, 6]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n`.

The objective is to compute `4` from `{"nums": [10, 10, 3, 7, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

**Track the two sums at each legal split.** A partition after index $i$ is legal only for $0\le i<n-1$, because both sides must be non-empty. The source starts with

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [10, 10, 3, 7, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Invariant Preservation

Ensure every candidate decision satisfies the required constraints.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [10, 10, 3, 7, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Total-parity formula:** Return `len(nums) - 1 if sum(nums) % 2 == 0 else 0`. This is equally linear in time and genuinely $O(1)$ auxiliary space.
- **Prefix-sum array:** It can calculate both side sums at every boundary, but storing all prefixes uses unnecessary $O(n)$ space beyond the slice already present here.
- **Recompute each side:** Summing left and right subarrays separately for every partition takes $O(n^2)$ time.
- **Two elements:** There is exactly one legal partition. It qualifies precisely when the total of the two elements is even.
- **Even total:** Left and right sums have the same parity, so their difference is even at every boundary.
- **Odd total:** One side sum is even and the other odd, so every difference is odd.
- **Negative difference:** Modulo two classifies its parity correctly; absolute value would not change the result.
- **Non-empty sides:** Iterating only through `nums[:-1]` prevents a split after the final element.
- **Boolean arithmetic:** In Python, adding the comparison result increments by one only for true, making the compact count valid.
- **Input preservation:** Slicing copies references but does not modify `nums`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n=\lvert\texttt{nums}\rvert$. `sum(nums)` takes $O(n)$ time. Creating `nums[:-1]` takes $O(n)$ time, and the loop scans its $n-1$ entries in $O(n)$ time. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
