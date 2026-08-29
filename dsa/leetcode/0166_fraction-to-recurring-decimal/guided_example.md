# Guided Example: Fraction to Recurring Decimal

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"numerator": 1, "denominator": 2}`
- **Required output:** `"0.5"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two integers representing the `numerator` and `denominator` of a fraction, return *the fraction in string format*.

The objective is to compute `"0.5"` from `{"numerator": 1, "denominator": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate sign, integer part, and fractional part

The output is easiest to build in the same order as ordinary long division.
The source first handles a zero numerator, returning `"0"` before any sign
logic. A zero fraction should never be rendered as negative zero.

For a nonzero numerator, the fraction is negative exactly when one operand is
positive and the other is not. Because the denominator is guaranteed nonzero,
`(numerator > 0) ^ (denominator > 0)` is true precisely when their signs differ.
The method appends `"-"` in that case.

It then works with absolute values `a` and `b`. The integer part is
`a // b`, which is appended as decimal text. The new `a = a % b` is the
remainder that begins the fractional calculation.

If that remainder is zero, division is exact. The integer text is already the
complete finite representation, so the method returns without adding a decimal
point.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"numerator": 1, "denominator": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Generate decimal digits by long division

For a nonzero remainder, the source appends `"."` and repeatedly performs the
familiar long-division step:

1. multiply the remainder by ten;
2. divide by the positive denominator to obtain the next decimal digit;
3. keep the modulus as the remainder for the following position.

Because the incoming remainder is smaller than `b`, multiplying by ten makes
the quotient an integer from zero through nine. Thus each appended quotient is
one decimal digit, including necessary internal zeros.

For $1/2$, the integer part is zero and the remainder is one. Multiplying by
ten gives ten; quotient five is appended and the next remainder is zero. The
loop ends with `"0.5"`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A repeated remainder means repeated future digits

The next digit and next remainder are deterministic functions of the current
remainder and fixed denominator. If the same remainder occurs twice, every
subsequent long-division step will repeat in the same order forever.

The dictionary `d` maps each previously seen remainder to the position in
`ans` where the digit generated from that remainder begins. At the top of an
iteration, the source stores `d[a] = len(ans)`. It then generates one digit and
the next remainder.

If the new remainder already appears in `d`, the repeating cycle begins at the
saved output position. The method inserts `"("` there, appends `")"` at the
end, and stops.

The current remainder cannot already be present when the top assignment runs:
a repeat is detected immediately after the preceding step and breaks the loop.
Therefore the dictionary entry is not incorrectly overwritten.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"0.5"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"numerator": 1, "denominator": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"0.5"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Simulate with a string builder and saved positions:** Equivalent to the list representation; insertion may be expressed with final slicing instead.
- **Floating-point conversion:** Incorrect because finite precision cannot preserve arbitrary recurring structure or exact digits.
- **Reduce by the greatest common divisor first:** May shorten the denominator but is not required for correctness or asymptotic output work.
- **Zero numerator:** Return `"0"` without a negative sign or decimal point.
- **Exact integer:** A zero initial remainder omits the fractional part.
- **Terminating fraction:** The loop reaches remainder zero and adds no parentheses.
- **Recurring fraction:** The first repeated remainder marks the exact cycle start.
- **Negative operands:** Exactly one negative sign is emitted when signs differ.
- **Internal zero digits:** Quotient zero is appended normally during long division.
- **Fixed-width overflow:** Convert to a wider type before absolute value and multiplication outside Python.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(k)$. Let $k$ be the number of produced fractional digits before termination or cycle
- **Auxiliary Space Complexity:** $O(k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
