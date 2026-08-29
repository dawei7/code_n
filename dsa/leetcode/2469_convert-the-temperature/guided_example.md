# Guided Example: Convert the Temperature

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"celsius": 36.5}`
- **Required output:** `[309.65, 97.7]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a non-negative floating point number rounded to two decimal places `celsius`, that denotes the **temperature in Celsius**.

The objective is to compute `[309.65, 97.7]` from `{"celsius": 36.5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Apply the two definitions directly

The problem supplies both conversion formulas:

$$
\text{Kelvin}=\text{Celsius}+273.15
$$

and

$$
\text{Fahrenheit}=1.8\cdot\text{Celsius}+32.
$$

The method returns these two computed values in the required order:

`[celsius + 273.15, celsius * 1.8 + 32]`.

No loop, search, or conditional case is needed because both target scales are affine transformations of the same input.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"celsius": 36.5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why Kelvin uses only an offset

Celsius and Kelvin degrees have the same size. Their zero points differ: zero Celsius corresponds to 273.15 Kelvin. Adding that constant shifts the scale without changing temperature intervals.

For 36.50 Celsius, the result is `36.50+273.15=309.65` Kelvin.

The input is non-negative, so the produced Kelvin value is at least 273.15. The formula would also work for valid negative Celsius values even though they are outside this problem's range.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why Fahrenheit uses a scale and an offset

A Fahrenheit degree is smaller than a Celsius degree. A change of 100 Celsius degrees corresponds to 180 Fahrenheit degrees, giving scale factor $180/100=1.8$. The freezing points differ by 32 after scaling, producing the added offset.

For 36.50 Celsius:

$$
36.50\cdot1.8+32
=65.70+32
=97.70.
$$

For 122.11 Celsius, multiplication and addition yield 251.798 Fahrenheit, matching the example.

The order of operations in `celsius * 1.8 + 32` follows the mathematical formula directly. Adding 32 before multiplying would scale the offset and produce a different temperature. Ordinary arithmetic precedence evaluates multiplication first, so no parentheses are required for correctness.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[309.65, 97.7]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"celsius": 36.5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[309.65, 97.7]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Use fractional scale `9/5`:** Fahrenheit can be written `celsius*9/5+32`. It is mathematically identical; `1.8` follows the statement directly.
- **Round to five decimals:** This is unnecessary because the judge uses tolerance, and forced rounding can discard useful precision.
- **Use decimal arithmetic:** It can represent decimal constants exactly but adds complexity without need at the accepted tolerance.
- **Zero Celsius:** The result is 273.15 Kelvin and 32 Fahrenheit.
- **Maximum input:** At 1000 Celsius, both formulas remain comfortably within ordinary floating-point range.
- **Fractional Celsius:** Multiplication and addition handle values such as 36.50 directly.
- **Trailing output zeros:** They are formatting only and need not be stored in a numeric float.
- **Result ordering:** Kelvin must precede Fahrenheit.
- **No mutation:** The scalar input is read twice and cannot be changed in place.
- **Tolerance:** Minor binary floating-point representation error is explicitly accepted.
- **Affine formulas:** Each output depends only on the input and fixed constants, so no iterative approximation is necessary.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The method performs a fixed number of floating-point arithmetic operations and creates a two-element list. Running time is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
