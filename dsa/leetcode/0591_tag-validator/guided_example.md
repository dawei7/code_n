# Guided Example: Tag Validator

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"code": "<DIV>This is <![CDATA[<raw>]]></DIV>"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string representing a code snippet, implement a tag validator to parse the code and return whether it is valid.

The objective is to compute `true` from `{"code": "<DIV>This is <![CDATA[<raw>]]></DIV>"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Validating tag names

The helper `check(tag)` requires length from 1 through 9 and requires every character to satisfy `isupper()`. Under the stated input alphabet, this is equivalent to allowing only uppercase English letters: digits, lowercase letters, punctuation, and the empty string fail.

This validation is applied to both opening and closing names. Finding a `>` is not enough; `<TOO_LONG_NAME>`, `<a>`, and `<>` must all be rejected.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"code": "<DIV>This is <![CDATA[<raw>]]></DIV>"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The outer-wrapper invariant

At the start of every iteration, the source checks:



Once scanning has moved beyond position zero, an empty stack means the one outer root tag has already closed—or no root was opened—and more input remains. Rejecting at that moment prevents text after the root and prevents a second top-level tag.

For valid `<A></A>`, popping `A` happens at the end of the string, so the loop terminates before the invariant is checked again. For `<A></A>x`, another iteration begins with a nonzero index and empty stack, so trailing `x` is rejected.

This is intended to enforce that all content stays inside one root. However, the exact condition has a gap at index zero, discussed below: it does not explicitly record that a root start tag was ever opened.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | At the start of every iteration, the source checks:



Once ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: CDATA must be recognized before generic tags

The first syntax branch tests the exact nine-character prefix `<![CDATA[`. Once recognized, `find(']]>', i + 9)` locates the first subsequent terminator. If none exists, the code is invalid.

The index then jumps across the closing `]]>`. Everything between the prefix and that first terminator is ignored by the parser. It may contain lowercase tags, unmatched angle brackets, or text resembling another CDATA opener; those are plain CDATA content.

This branch must come before generic `<...>` parsing. Otherwise, the parser would interpret `![CDATA[` as a tag name and reject valid CDATA.

Inside an already-open tag, CDATA handling is correct. A malformed `<!...` that lacks the exact prefix falls through to opening-tag parsing, obtains an invalid name containing punctuation, and is rejected.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"code": "<DIV>This is <![CDATA[<raw>]]></DIV>"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Add `seen_root`:** Set it on the first valid o:** - **Add `seen_root`:** Set it on the first valid opening tag, reject CDATA or text while the stack is empty, and return `seen_root and not stk`. This repairs the exact source’s root-presence defect.
- **Require `code[0] == '<'` plus an opener parse:** An explicit initial-root check can also prevent standalone text and CDATA, provided it distinguishes `<TAG>` from `</TAG>` and `<![CDATA[`.
- **Recursive-descent parser:** Parse one closed tag and recursively parse nested content. It can closely match the grammar but must still special-case CDATA and depth limits.
- **Regular expressions alone:** Backreferences and arbitrary nesting make a single regex fragile or expensive. A stack expresses nesting more reliably.
- **Crossed tags:** `<A><B></A></B>` fails because the closer does not match the stack top.
- **Unclosed opener:** A nonempty stack at end fails.
- **Closer without opener:** An empty stack in the closing branch fails.
- **Second root tag:** Once the first root closes, the next loop sees an empty stack at nonzero index and fails.
- **Trailing text:** Rejected for the same reason after root closure.
- **Standalone CDATA:** The contract says invalid, but the exact source incorrectly accepts it at index zero; require nonempty stack.
- **One-character plain text:** Also incorrectly accepted by the exact source; require a seen root.
- **First CDATA terminator:** `find(']]>')` intentionally ends CDATA at the first subsequent terminator, leaving later characters to normal parsing.
- **Tag-like text inside CDATA:** Ignored completely, even if malformed.
- **Invalid CDATA prefix:** Falls into tag-name validation and fails because punctuation is not uppercase letters.
- **Unmatched `<`:** Missing subsequent `>` makes `find` return -1 and fails.
- **Ordinary `>`:** Allowed as text because only `<` starts special syntax.
- **Name length:** Empty and ten-character names fail; lengths one through nine pass only with uppercase letters.
- **Unicode nuance:** `isupper()` recognizes more than ASCII in general, but the input alphabet is restricted to English letters and listed symbols, so this does not expand accepted test characters.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the code length. The main index only moves forward. Each delimiter search scans from the current construct to its closing delimiter, and the parser then jumps past that construct; tag-name checks cover disjoint extracted names. Under this forward-scan accounting, total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
