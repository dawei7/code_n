# Guided Example: Valid Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "-90E3"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, return whether `s` is a **valid number**.

The objective is to compute `true` from `{"s": "-90E3"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Validate structure rather than converting the value

The task asks whether the entire string follows a numeric grammar. Calling a floating-point conversion would mix parsing with language-specific behavior and might accept formats outside the contract. The selected solution instead scans every character and records whether a decimal point or exponent has already appeared.

The accepted high-level shape is a signed or unsigned integer/decimal mantissa followed by an optional signed integer exponent. A sign is legal only at the very beginning or immediately after `e` or `E`. A dot is legal only in the mantissa and at most once. An exponent marker is legal at most once and must have digits on both sides in the required senses.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "-90E3"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Consume the optional leading sign

`i` begins at zero. If `s[i]` is `'+'` or `'-'`, the source advances `i`. The contract guarantees `len(s) >= 1`, so the initial access is safe.

If advancing the sign reaches `n`, the string contains only a sign and is invalid. This check also establishes that `s[i]` is the first mantissa character for all later position reasoning.

Signs appearing later are not accepted by the ordinary-character branch because they are not numeric. The only exception is handled explicitly after an exponent marker.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Reject a mantissa dot with no digit around it

The condition for `s[i] == '.'` rejects the dot when it is the final character or when the following character is an exponent marker. This rules out `"."`, `"+."`, `".e1"`, and `"-.E2"`.

If a dot is first but followed by a digit, forms such as `".9"` remain possible. If digits precede a dot, forms such as `"4."` are valid even when no digit follows the dot. The targeted check captures the only digitless-dot case that could otherwise slip through the later flag logic.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "-90E3"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Deterministic finite automaton:** Classify each character and transition between grammar states. It is systematic and linear but requires a carefully verified state table.
- **Split around `e` or `E`:** Validate a decimal/integer mantissa and integer exponent separately. This can be readable but must reject multiple markers and avoid substring-allocation assumptions.
- **Regular expression:** A complete anchored expression can encode the grammar concisely, though it is harder for beginners to debug and may obscure why cases fail.
- **Built-in numeric conversion:** It may accept whitespace, infinity, or other implementation-specific formats and should not define this exact grammar.
- **Only a sign:** Rejected immediately after leading-sign consumption.
- **Only a dot:** Rejected because no adjacent digit exists.
- **Dot before digits:** Valid when a digit follows, as in `"-.9"`.
- **Dot after digits:** Valid without a following fractional digit, as in `"4."`.
- **Exponent sign:** Legal only immediately after `e` or `E` and only when followed by a digit.
- **Whitespace:** This scanner rejects it; whitespace is absent from the stated input alphabet.
- **Unicode numerics outside the contract:** `isnumeric()` may accept them even though the formal grammar names only ASCII digits.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Every character is examined at most once. Consuming an exponent sign increments `j` early but does not cause any character to be revisited. Time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
