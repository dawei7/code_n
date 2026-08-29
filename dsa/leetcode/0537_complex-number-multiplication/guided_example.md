# Guided Example: Complex Number Multiplication

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num1": "1+1i", "num2": "1+1i"}`
- **Required output:** `"0+2i"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A <a href="https://en.wikipedia.org/wiki/Complex_number" target="_blank">complex number</a> can be represented as a string on the form `"**real**+**imaginary**i"` where:

The objective is to compute `"0+2i"` from `{"num1": "1+1i", "num2": "1+1i"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 2

$$
(a_1+b_1i)\quad\text{and}\quad(a_2+b_2i).
$$

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num1": "1+1i", "num2": "1+1i"}` | Initial boundary validation | Setup completed |
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
| Target Output | Accumulator state | Synthesize final result | `"0+2i"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num1": "1+1i", "num2": "1+1i"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"0+2i"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Use a regular expression:** It can capture signed components, but the fixed plus-delimited format makes slicing and splitting simpler.
- **Use a built-in complex type:** It introduces floating-point representation and output-format concerns for an integer-only task.
- **Four-term direct string manipulation:** Arithmetic should occur after integer parsing; manipulating signs as text is more error-prone.
- **Negative imaginary input:** The format appears as `"+-"`, and splitting at plus preserves the negative sign.
- **Negative real input:** Its leading minus remains part of the first split component.
- **Zero real part:** Formatting still includes it, such as `"0+2i"`.
- **Zero imaginary part:** The result ends with `"+0i"`.
- **Negative imaginary result:** The required fixed separator produces `"+-"`.
- **Both inputs purely real:** Both imaginary coefficients are zero and the formula reduces to real multiplication.
- **Both inputs purely imaginary:** The product is negative real because `i^2=-1`.
- **Valid-format guarantee:** It allows direct two-value unpacking without error handling.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The source bounds both coefficients between minus one hundred and one hundred, so input strings have bounded length. Under those fixed constraints, parsing, arithmetic, and formatting all take $O(1)$ time and $O(1)$ auxiliary space, matching the manifest.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
