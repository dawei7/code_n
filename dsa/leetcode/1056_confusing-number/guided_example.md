# Guided Example: Confusing Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 8000}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **confusing number** is a number that when rotated `180` degrees becomes a different number with **each digit valid**.

The objective is to compute `true` from `{"n": 8000}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Rotation changes both each digit and the digit order

Rotating an entire decimal number by 180 degrees has two effects:

- Each digit changes according to the rotation map.
- The positions reverse: the original last digit becomes the rotated first digit.

Only five digits remain valid:



Every occurrence of two, three, four, five, or seven makes the whole rotation invalid. A number is confusing only if every digit is valid and the resulting numeric value differs from the original value.

The solution performs the transformation arithmetically. It extracts original digits from right to left, rotates each extracted digit, and appends it to the right side of a new integer. Extracting from the right already supplies the reversal required by geometric rotation, so no separate string reversal is needed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 8000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Preserve the original number

The first assignment is:



`x` is a working copy that will be shortened one decimal digit at a time. `y` is the rotated integer being constructed. The original `n` remains unchanged so the final result can be compared with it.

Starting `y` at zero also naturally handles leading zeros in the rotated representation. Appending a rotated zero to an integer currently equal to zero still gives zero. Integer arithmetic never stores leading zeros, exactly as the problem requires.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first assignment is:



`x` is a working copy that will ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use a table indexed directly by each digit

The rotation map is stored as a ten-element list:



The list index is the original digit, and the value is its rotated image. For example, `d[6]` is nine and `d[9]` is six.

The value minus one is a sentinel for an invalid digit. It cannot be confused with a legal rotated digit because all legal results lie between zero and nine.

An array is a convenient map here because every decimal digit is already a small integer in the fixed range zero through nine. Lookup takes constant time and needs no conditional chain.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 8000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **String transformation:** Convert `n` to text, :** - **String transformation:** Convert `n` to text, map each character, reverse the mapped characters, parse the result, and compare it with `n`. This is straightforward but uses `O(D)` auxiliary space for the transformed representation.
- **Dictionary mapping:** A dictionary from valid digits to rotated digits expresses the same rule. The fixed ten-entry list is simpler and guarantees direct constant-time indexing.
- **Large conditional chain:** Separate cases for zero, one, six, eight, and nine can avoid a table, but they are more verbose and easier to implement inconsistently.
- **Zero:** The loop is skipped and zero is compared with zero, correctly returning false.
- **Single six or nine:** Six becomes nine and nine becomes six, so either input is valid and confusing.
- **Single zero, one, or eight:** Each rotates to itself, so the result is valid but not confusing.
- **Any invalid digit:** Encountering two, three, four, five, or seven returns false immediately, even if all remaining digits would be valid.
- **Rotationally symmetric multi-digit number:** Values such as 11, 69, 88, and 96 remain equal after rotation and therefore return false.
- **Leading zeros after rotation:** Trailing zeros in the original number become leading zeros after rotation. Integer construction drops them naturally, as required.
- **Original leading zeros:** An integer input has no represented leading zeros, so there is nothing additional to preserve.
- **Upper bound:** The largest legal input still has only ten decimal digits at most under the stated bound, and the same loop handles it without a separate case.
- **Input preservation:** `x` is reduced destructively, but `n` is never changed. The final comparison therefore uses the true original value.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(D)$. Let `D` be the number of decimal digits in `n`, treating zero as one digit.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
