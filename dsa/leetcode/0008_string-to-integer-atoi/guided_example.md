# Guided Example: String to Integer (atoi)

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "42"}`
- **Required output:** `42`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

The objective is to compute `42` from `{"s": "42"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Parsing rules are ordered phases, not independent character filters

`myAtoi` does not search the whole string for characters that look useful. It reads a prefix from left to right under a strict order:

1. skip only leading space characters;
2. consume at most one optional sign;
3. consume one consecutive run of decimal digits;
4. stop permanently at the first non-digit after that point;
5. clamp the numerical result to the signed 32-bit range.

Once a phase ends, it never restarts. A space after digits is not skipped, a sign after a digit is not reconsidered, and digits after a letter are ignored. This is why `"1337c0d3"` becomes `1337` rather than `133703`, and `"0-1"` becomes `0` rather than `-1`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "42"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Handle empty input before indexing

The method begins with



An empty string has no digits, so zero is correct. More importantly, this guard makes the later access to `s[i]` safe.

The following check



is redundant because `not s` already covered exactly that case. It does not alter behavior; it simply repeats the same protection.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Skip leading spaces without running past the end

The loop



advances over ordinary space characters at the beginning. The bounds check occurs immediately after incrementing. If the string consists entirely of spaces, the method returns before the next loop condition can evaluate `s[n]`, which would be out of range.

The Reference names the exact leading whitespace character as `" "`, and the input alphabet contains no tabs or newlines, so comparing with `' '` matches the contract. A parser intended for broader text would need to decide deliberately whether other Unicode or ASCII whitespace should count.

Once the first non-space character is reached, later spaces are no longer skippable. They are non-digits that terminate conversion.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `42` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "42"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `42` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Deterministic finite automaton:** Model “start,” “sign seen,” “reading digits,” and “dead” as explicit states. This makes transition rules reusable and formal, but the small fixed sequence here is clearer with direct control flow.
- **Regular expression plus integer conversion:** A pattern can extract the allowed prefix, but it adds a parsing engine, still requires careful clamping, and may build a large intermediate integer unless overflow is checked separately.
- **Use a wider integer then clamp:** Easy in Python, but it does not honor a no-wider-integer environment. The pre-push threshold handles the limit portably.
- **Empty string:** The first guard returns zero before any indexing.
- **Only spaces:** The whitespace loop reaches `n` and returns zero without reading `s[n]`.
- **Only a sign:** The sign is consumed, no digit is read, and zero is returned.
- **Two signs:** The first is consumed as the optional sign; the second terminates the digit scan, so the result is zero.
- **Leading zeros:** They are processed normally and do not change `res`; `"-00042"` becomes `-42`.
- **Non-digit first character:** No whitespace or sign phase consumes it, the digit loop stops immediately, and zero is returned.
- **Non-digit after digits:** Conversion returns the completed prefix and ignores everything from that character onward.
- **Space after digits:** It is a terminator, not skippable whitespace, because only the initial phase ignores spaces.
- **Positive overflow:** The function returns `2147483647` before performing the unsafe push.
- **Negative boundary or underflow:** Both `"-2147483648"` and any smaller mathematical value return `-2147483648`; the former is an exact boundary, while the latter is clamped.
- **Plus sign:** It is consumed but leaves `sign = 1`.
- **Decimal point:** `'.'` is not a digit, so `"3.14"` parses as `3`; the function does not parse floating-point syntax.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(s)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
