# Guided Example: Mirror Distance of an Integer

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1221}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n`.

The objective is to compute `0` from `{"n": 1221}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Follow the decimal definition directly

The mirror value is obtained by writing `n` in ordinary decimal form, reversing that finite digit sequence, and interpreting the result as an integer. The source expresses those three steps as

`int(str(n)[::-1])`.

`str(n)` produces the digits with no sign or leading zeros because `n` is positive. The slice `[::-1]` visits the complete string backward. Finally, `int(...)` converts the reversed spelling back to its numeric value.

The method returns the absolute difference between the original and this reversed value:

`abs(n - int(str(n)[::-1]))`.

Absolute value is needed because reversal may make the number either larger or smaller.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1221}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand the reversal slice

Python slicing has the form `sequence[start:stop:step]`. Omitting start and stop selects the whole string, while step `-1` traverses it from the final character to the first.

For `n=25`:

- `str(n)` is `"25"`;
- reversing gives `"52"`;
- integer conversion gives 52;
- `abs(25-52)` is 27.

For a one-digit number such as 7, reversal produces the same one-character string, so the mirror distance is zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Python slicing has the form `sequence[start:stop:step]`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Let integer conversion handle newly leading zeros

Trailing zeros in the original number become leading zeros in the reversed digit sequence. Decimal integer values do not retain leading zeros, and `int` applies exactly that rule.

For `n=10`, the intermediate reversed string is `"01"`. Converting it yields integer 1, so the result is nine.

For `n=1200`, the reversed string is `"0021"` and the mirror integer is 21. The source does not need to strip zeros manually.

Zeros in other positions remain meaningful. Reversing 102 produces `"201"`, so its mirror is 201 rather than 21.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1221}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Arithmetic reversal:** Repeatedly append `n%10:** - **Arithmetic reversal:** Repeatedly append `n%10` to a numeric accumulator and apply `n//=10`. It uses constant scalar storage and matches the editorial, but is not the exact source.
- **Manual character loop:** Prepending or collecting digits can reproduce the slice but is more verbose.
- **Forget `int` conversion:** Subtracting strings is invalid, and preserving `"01"` as text misses its numeric value of one.
- **Strip every zero:** Only leading zeros of the reversed spelling lose significance; internal and trailing reversed zeros remain part of the number.
- **One-digit input:** Reversal is identical and the result is zero.
- **Decimal palindrome:** The two numeric values match, so the result is zero.
- **Original trailing zeros:** They become harmless leading zeros in the reversed string.
- **Original internal zeros:** They move to new internal positions and remain significant.
- **Reversal larger than `n`:** `abs` handles the negative raw difference.
- **Reversal smaller than `n`:** `abs` preserves the positive distance.
- **Maximum legal input:** At most ten digits are processed.
- **Positive-input guarantee:** There is no minus sign to position during string reversal.
- **Source/manifest mismatch:** This exact implementation uses $O(D)$ temporary string storage even though the arithmetic alternative can use $O(1)$.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(D)$. Let $D$ be the number of decimal digits, where $D=\lfloor\log_{10}n\rfloor+1$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
