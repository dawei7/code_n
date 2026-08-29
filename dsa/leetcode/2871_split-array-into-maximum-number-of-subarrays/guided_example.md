# Guided Example: Split Array Into Maximum Number of Subarrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 0, 2, 0, 1, 2]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `nums` consisting of **non-negative** integers.

The objective is to compute `3` from `{"nums": [1, 0, 2, 0, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

**First determine the minimum score, then maximize the number of pieces.** Let

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 0, 2, 0, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

$$
A = \text{nums}[0] \text{ AND } \text{nums}[1] \text{ AND } \cdots \text{ AND } \text{nums}[n-1]
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

be the bitwise AND of the whole array. Keeping the entire array as one subarray always achieves total score $A$, so the minimum total can never be greater than $A$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 0, 2, 0, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Compute the whole AND first:** One may explicitly branch on $A$ and then run a second greedy pass when it is zero. The source combines discovery and cutting in one pass.
- **Dynamic programming over cut positions:** It can model partitions but is unnecessary because AND only loses bits and the earliest valid cut is always optimal.
- **Whole AND positive:** Return one; every additional subarray contributes at least the same positive common-bit value.
- **Trailing nonzero remainder:** Merge it into the final zero-score segment, whose AND stays zero.
- **A zero element:** Encountering literal zero immediately makes the current segment AND zero and forces the earliest possible cut.
- **All zeros:** Every single element forms a zero-score segment, so the maximum number is $n$.
- **Single element:** The result is one whether its value is zero or positive, because at least one subarray is required.
- **Identity value `-1`:** This Python idiom is safe for non-negative inputs; a fixed-width implementation can initialize from the first element or use an all-ones mask.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The loop reads every element once and performs one constant-width bitwise AND plus constant scalar work. Since `nums[i] <= 10^6`, integer width is bounded by the constraints. Time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
