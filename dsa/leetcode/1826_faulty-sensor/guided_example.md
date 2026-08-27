# Guided Example: Faulty Sensor

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"sensor1": [2, 3, 4, 5], "sensor2": [2, 1, 3, 4]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An experiment is being conducted in a lab. To ensure accuracy, there are** two **sensors collecting data simultaneously. You are given two arrays `sensor1` and `sensor2`, where $\text{sensor1}[i]$ and $\text{sensor2}[i]$ are the $$i^{\text{th}}$$ data points collected by the two sensors.

The objective is to compute `1` from `{"sensor1": [2, 3, 4, 5], "sensor2": [2, 1, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

**A dropped value creates one of two shifts.** Before any defect becomes visible, both sensor arrays have the same values at the same indices. If sensor 1 is defective, then after its missing data point, its values are shifted one place left relative to the correct sensor 2. From the first visible disagreement onward, the relationship should therefore be

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"sensor1": [2, 3, 4, 5], "sensor2": [2, 1, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

for every position `t` before the final random slot. Conversely, if sensor 2 is defective, the required shifted relationship is

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | for every position `t` before the final random slot.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"sensor1": [2, 3, 4, 5], "sensor2": [2, 1, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Build both reconstructed candidates:** One cou:** - **Build both reconstructed candidates:** One could delete a candidate position from each presumed correct array and compare resulting sequences, but trying positions directly can take `O(n^2)` time and allocates unnecessary arrays.
- **Run two separate full hypothesis checks:** Independently validating “sensor 1 faulty” and “sensor 2 faulty” is still `O(n)` and can be clear, but the paired loop shares the common scan and returns as soon as one direction fails.
- **Mismatch only at the last index:** The replacement value is unconstrained except that it differs from the dropped value, so the defective sensor cannot be identified and the answer is `-1`.
- **Completely equal arrays:** There may be no defect, or duplicate readings may hide a possible drop; there is no unique defective sensor, so the answer is `-1`.
- **Array length one:** There is no nonfinal position at which a shift can be tested. Both loops skip their bodies and return `-1`.
- **Repeated values around the drop:** They may delay the first visible mismatch. Starting the shifted comparisons at that mismatch still tests every informative position.
- **Both shifted alignments remain valid:** This is genuine ambiguity, not a reason to choose the first sensor. The final `-1` handles it.
- **One alignment fails late:** A hypothesis must hold at every informative suffix position, so even a failure near the end conclusively eliminates it.
- **Random final value:** The algorithm intentionally never compares it as though it had to continue the shift; doing so would reject valid defective readings.
- **Return-number interpretation:** Failure of `sensor1[i + 1] == sensor2[i]` disproves sensor 2 and returns one; failure of `sensor1[i] == sensor2[i + 1]` disproves sensor 1 and returns two.
- **Model guarantee:** The early-return order relies on the stated setting that at most one sensor is defective. Arbitrary unrelated arrays could violate both hypotheses, but such data is outside the promised experiment model.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the common array length. The first loop scans a matching prefix, and the second loop scans the remaining suffix. They are sequential rather than nested: an index passed by the first loop is not revisited by the second except for the boundary mismatch. Thus the total number of comparisons is linear, giving `O(n)` time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
