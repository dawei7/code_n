# Guided Example: Check If All 1's Are at Least Length K Places Away

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 0, 0, 0, 1, 0, 0, 1], "k": 2}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an binary array `nums` and an integer `k`, return `true`* if all *`1`*'s are at least *`k`* places away from each other, otherwise return *`false`.

The objective is to compute `true` from `{"nums": [1, 0, 0, 0, 1, 0, 0, 1], "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only consecutive ones need to be compared

Suppose the indices of ones are:

$$
p_1<p_2<\cdots<p_r.
$$

If every consecutive pair has at least $k$ zeros between it, then any nonconsecutive pair is even farther apart and also satisfies the condition. Therefore, the scan only needs to remember the index of the most recently seen one.

The variable `j` holds that index.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 0, 0, 0, 1, 0, 0, 1], "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initialize so the first one always passes

uses negative infinity as a sentinel meaning no earlier one exists. When the first one appears at finite index `i`, the calculated distance `i - j - 1` is positive infinity, so it cannot be less than finite `k`.

This avoids a separate Boolean flag or special branch for the first one. After the first one, `j` becomes an ordinary integer index.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | uses negative infinity as a sentinel meaning no earlier one ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Scan every array position once

provides the zero-based index and binary value. The condition `if x` is true exactly when `x == 1` under the input guarantee.

Zeros need no direct action. They contribute to the gap automatically through the difference between one indices.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 0, 0, 0, 1, 0, 0, 1], "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Count zeros since the last one:** Reset a coun:** - **Count zeros since the last one:** Reset a counter to zero after each one and increment it on zeros. This is equivalent and avoids using infinity.
- **Store every one index:** Compare adjacent stored positions afterward. It is correct but uses $O(n)$ space unnecessarily.
- **Convert to a large integer:** Bit tricks can count zeros between set bits, but conversion is less direct and fixed-width languages may overflow.
- **First one:** It has no predecessor, so it must never cause failure.
- **No ones:** The condition is vacuously true.
- **One one:** There is no pair to compare, so true is returned.
- **Adjacent ones:** They have zero positions between them and pass only for `k = 0`.
- **Exactly `k` zeros:** The strict `< k` test accepts equality.
- **Trailing zeros:** They do not matter because spacing is required only between ones.
- **Early return:** Once one violating pair is found, later values cannot make that already-observed gap larger.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. The loop visits each element at most once and performs constant work. It can stop early on a violation, while worst-case time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
