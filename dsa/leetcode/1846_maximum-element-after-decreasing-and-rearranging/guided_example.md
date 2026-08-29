# Guided Example: Maximum Element After Decreasing and Rearranging

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [2, 2, 1, 2, 1]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of positive integers `arr`. Perform some operations (possibly none) on `arr` so that it satisfies these conditions:

The objective is to compute `2` from `{"arr": [2, 2, 1, 2, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

**Use rearrangement to put small values first.** The final array must start at one and adjacent values may rise by at most one. Since elements can be rearranged freely, their original order carries no useful restriction. Sorting `arr` in ascending order assigns the smallest original values to the earliest, lowest positions, preserving larger values for positions that may reach greater heights.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [2, 2, 1, 2, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The exact solution then modifies this sorted list in place. First, `arr[0] = 1`. Because all original values are positive, changing the smallest value to one is either no change or an allowed decrease.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Choose the largest feasible value at every later position.** At index `i`, two upper bounds apply:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [2, 2, 1, 2, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Counting by capped value:** Since no final maximum can exceed `n`, count each original value as `min(value, n)` and process capacities in linear time with `O(n)` space.
- **Track only the endpoint after sorting:** A scalar answer can replace rewriting every later array entry, but the exact source stores the full valid witness.
- **Already valid ascending array:** Every minimum keeps the original value, and the existing maximum is returned.
- **No original one:** The smallest positive value is decreased to one, satisfying the required first element.
- **Many duplicate small values:** They create flat portions, which are allowed because adjacent difference may be zero.
- **Very large values:** Each is reduced only as much as the previous-plus-one rule requires.
- **Single element:** It is set to one and returned, which is the only valid first value.
- **Maximum possible result:** No length-`n` valid sequence starting at one can exceed `n`, and the recurrence reaches `n` exactly when capacities support every step.
- **Only decreases:** The `min` assignment never raises a sorted capacity, so every modification is legal.
- **Absolute difference:** The produced sequence is nondecreasing with rises at most one, which is a sufficient stronger structure.
- **Input mutation:** Sorting and overwriting values permanently transform `arr`. Use a copy if the caller needs the original data.
- **Positive-value guarantee:** Setting the first sorted entry to one is always a decrease or no-op; zero or negative inputs would require separate reasoning.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = arr.length`. Sorting takes `O(n log n)` time, and the recurrence scans the array once in `O(n)`, for total `O(n log n)` time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
