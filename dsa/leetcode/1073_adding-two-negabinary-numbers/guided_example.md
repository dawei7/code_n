# Guided Example: Adding Two Negabinary Numbers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr1": [1, 1, 1, 1, 1], "arr2": [1, 0, 1]}`
- **Required output:** `[1, 0, 0, 0, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two numbers `arr1` and `arr2` in base **-2**, return the result of adding them together.

The objective is to compute `[1, 0, 0, 0, 0]` from `{"arr1": [1, 1, 1, 1, 1], "arr2": [1, 0, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Add from the least significant position

The arrays store their most significant bit first, but addition propagates carry toward more significant positions. The solution therefore starts at the ends:



`i` and `j` point to the current equal-power positions in the two inputs. `c` is the carry arriving from the previously processed lower power. `ans` receives result bits from least significant to most significant, so it will be reversed before return.

Base negative two still uses binary digits zero and one. What changes from ordinary binary addition is the meaning of the carry.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr1": [1, 1, 1, 1, 1], "arr2": [1, 0, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Relate one column total to the next carry

Suppose the current position has weight `(-2)^p`. Let `x` be the two input bits plus the incoming carry. We need an output bit `r` and next carry `c_next` satisfying:



This equation comes from:



Since the next place value is negative two times the current place value, a positive excess at the current column creates a negative carry, while a negative current total creates a positive carry.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suppose the current position has weight `(-2)^p`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Read missing input positions as zero

The main loop continues while either input has a bit left or carry remains:



The current input bits are:



Once one array is exhausted, its higher positions are implicit zeros. Continuing for a nonzero carry is essential because the carry may create one or more additional most-significant bits.

Given input bits and possible carry values, `x` lies between minus one and three.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 0, 0, 0, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr1": [1, 1, 1, 1, 1], "arr2": [1, 0, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 0, 0, 0, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Convert to an integer and back:** It is concep:** - **Convert to an integer and back:** It is conceptually simple in arbitrary-precision languages but abandons digitwise constraints and requires careful negative-base conversion.
- **Use divmod with base minus two:** One can normalize each column total through arithmetic division, but language remainder rules for negative divisors can be less transparent than the explicit three cases.
- **Both inputs zero:** One zero bit is appended, cleanup keeps it, and the result is `[0]`.
- **One input zero:** The algorithm reproduces the other value, subject to normal carry processing and canonical cleanup.
- **Final negative carry:** A carry of minus one enters the next iteration and is converted to bit one with positive carry, which may require another position.
- **Final positive carry:** It is processed even after both input pointers become negative because `c` keeps the loop active.
- **Total two:** Produces bit zero and carry minus one, not ordinary binary carry plus one.
- **Total minus one:** Produces bit one and carry plus one.
- **No leading zeros:** Cleanup removes high zeros but never removes the only digit.
- **Maximum lengths:** Work remains linear and does not depend on the potentially large numeric value represented.
- **Input preservation:** The arrays are read from right to left and never modified.
- **Bit constraint:** The case range relies on input digits being only zero or one.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(A + B)$. Let `A` and `B` be the input lengths.
- **Auxiliary Space Complexity:** $O(A + B)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
