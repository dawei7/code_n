# Guided Example: Maximum Value of a String in an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"strs": ["alic3", "bob", "3", "4", "00000"]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The **value** of an alphanumeric string can be defined as:

The objective is to compute `5` from `{"strs": ["alic3", "bob", "3", "4", "00000"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Each string has one of two definitions of value

The rule is conditional:

- if every character is a digit, interpret the complete string as a base-ten integer;
- otherwise, use the number of characters in the string.

These cases must be kept separate. A mixed string such as `"alic3"` is not partially parsed as a number and does not receive the value of its digit characters. The presence of even one letter makes its value the full string length.

The helper `f(s)` implements this definition directly:

`int(s) if all(c.isdigit() for c in s) else len(s)`.

After evaluating each string, the outer `max` returns the greatest value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"strs": ["alic3", "bob", "3", "4", "00000"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Recognize a digits-only string

The generator `c.isdigit() for c in s` produces one Boolean per character. `all` returns true only if every Boolean is true. Therefore, the numeric branch is selected precisely when every character is a digit.

The input guarantees non-empty strings containing lowercase English letters and digits. Consequently:

- `all` always examines at least one character;
- the true branch always gives `int` a valid non-empty decimal representation;
- no sign, decimal point, whitespace, or other punctuation needs special handling.

Python's `isdigit` recognizes some Unicode digits beyond `0` through `9`, but that broader behavior is irrelevant under the ASCII-like challenge alphabet.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why leading zeroes do not change numeric value

`int` performs numeric conversion, so leading zeroes contribute no place value. For example:

`int("00000") == 0`

and

`int("001") == 1`.

The string length must not be used merely because a numeric string is long. In the second sample, `"1"`, `"01"`, `"001"`, and `"0001"` all have numeric value one even though their lengths differ.

This is one reason that comparing the strings lexicographically or by length would be incorrect.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"strs": ["alic3", "bob", "3", "4", "00000"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`str.isdigit()` directly:** `s.isdigit()` expresses the same classification more compactly for non-empty valid strings.
- **Exception-based parsing:** Trying `int(s)` and catching `ValueError` works but uses exceptions for normal control flow.
- **Manual decimal accumulation:** Build the integer digit by digit; it avoids `int` but adds unnecessary code.
- **Leading zeroes:** They are ignored by numeric conversion rather than counted as length.
- **All letters:** The value is the full string length.
- **Mixed letters and digits:** Even one letter selects the length rule for the whole string.
- **Equal maximum values:** Returning the shared numeric maximum is sufficient.
- **One input string:** Its evaluated value is necessarily the answer.
- **Non-empty guarantee:** It makes both `all` behavior and `max` safe without special defaults.
- **Input alphabet:** No signs or decimal separators need to be parsed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
