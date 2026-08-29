# Guided Example: Minimum Unlocked Indices to Sort Nums

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 1, 2, 3, 2], "locked": [1, 0, 1, 1, 0, 1]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `nums` consisting of integers between 1 and 3, and a **binary** array `locked` of the same size.

The objective is to compute `0` from `{"nums": [1, 2, 1, 2, 3, 2], "locked": [1, 0, 1, 1, 0, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

**Only two adjacent inversions are swappable.** Values are restricted to $1$, $2$, and $3$. A swap at boundary $i$ is allowed only when

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 1, 2, 3, 2], "locked": [1, 0, 1, 1, 0, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

$$
\texttt{nums}[i]-\texttt{nums}[i+1]=1.
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Therefore, the only value pairs that can swap are $(2,1)$ and $(3,2)$. A pair $(3,1)$ differs by two and can never swap directly.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 1, 2, 3, 2], "locked": [1, 0, 1, 1, 0, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Simulate swaps after every unlock choice:** Exploring subsets of locked boundaries is exponential and unnecessary once mandatory intervals are characterized.
- **Unlock every inversion position in the original array only:** Swaps create new adjacent inversions at different boundaries. Entire movement intervals, not just initially inverted adjacencies, must be available.
- **Standard unrestricted inversion count:** This problem does not allow arbitrary adjacent swaps. A $3$ and $1$ can never cross, which creates the explicit impossibility test.
- **Already sorted input:** Both mandatory intervals are empty, so the answer is zero regardless of unrelated locked positions.
- **No value \(2\):** A $3$ before a $1$ is impossible; otherwise the array already has all $1$s before all $3$s and no unlock is needed.
- **Only values \(1\) and \(2\):** Feasibility is automatic, and only `[first2,last1)` matters.
- **Only values \(2\) and \(3\):** Only `[first3,last2)` matters.
- **Overlapping intervals:** A locked boundary in both is counted once because one unlock operation changes that single `locked[i]` to zero.
- **Boundary versus element index:** `locked[i]` controls the swap between positions $i$ and $i+1$. Half-open endpoint intervals correctly enumerate those boundaries.
- **Sentinel values:** `n` for a missing first occurrence and `-1` for a missing last occurrence make all empty intervals fail their chained comparisons naturally.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n=\lvert\texttt{nums}\rvert$. The first scan visits every value once, and the final sum visits every lock once. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
