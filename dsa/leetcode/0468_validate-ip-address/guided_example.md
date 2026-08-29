# Guided Example: Validate IP Address

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"queryIP": "172.16.254.1"}`
- **Required output:** `"IPv4"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `queryIP`, return `"IPv4"` if IP is a valid IPv4 address, `"IPv6"` if IP is a valid IPv6 address or `"Neither"` if IP is not a correct IP of any type.

The objective is to compute `"IPv4"` from `{"queryIP": "172.16.254.1"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Validate IPv4 structure before values

`s.split(".")` separates the candidate at every dot. A valid IPv4 address must produce exactly four fields. Too few or too many dots fail this count immediately.

Splitting preserves empty fields. For example, a trailing dot in `"1.2.3."` produces an empty final field. Its total field count happens to be four, but the per-field digit check rejects the empty text. Consecutive dots similarly create an empty field and fail.

For each field `t`, the validator applies three ideas:

1. If its length exceeds one and its first character is `0`, reject it. A field consisting of exactly `"0"` is allowed, but `"00"` and `"01"` are not.
2. Require `t.isdigit()`. This rejects empty fields, signs, letters, and punctuation.
3. Convert the verified digits to an integer and require it to lie from 0 through 255 inclusive.

The condition is written as

`if not t.isdigit() or not 0 <= int(t) <= 255`.

Python's `or` short-circuits, so `int(t)` is evaluated only after `isdigit()` succeeds. Empty or nonnumeric fields therefore return false safely rather than raising a conversion error.

The source constraint limits characters to English letters, digits, dots, and colons. Under that domain, `isdigit()` exactly serves the decimal-digit check needed here.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"queryIP": "172.16.254.1"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Validate IPv6 structure and alphabet

`s.split(":")` must produce exactly eight fields. This rejects missing fields, extra fields, and compressed forms such as `::`. Compression is valid in real-world IPv6 syntax but intentionally outside this problem's accepted full-form grammar.

Every field must have length from one through four. Leading zeros are allowed, so no special first-character rule is applied.

The generator

`all(c in "0123456789abcdefABCDEF" for c in t)`

requires each character to be a decimal digit or hexadecimal letter in either case. A field such as `"8A2e"` passes; `"037j"` fails because `j` is outside the hexadecimal alphabet.

Checking length before character membership guarantees an empty field fails even though `all(...)` over an empty sequence would otherwise return `true`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why all rules are necessary and sufficient

For IPv4, exact field count establishes the dotted four-part structure. The leading-zero rule, digit rule, and numeric range establish exactly the allowed form of each part. If all four pass, the candidate matches the complete IPv4 grammar; if any grammar rule is violated, the corresponding test rejects it.

For IPv6, exact field count establishes eight colon-separated parts. Length and character checks establish exactly the required hexadecimal field grammar, including allowed leading zeros and mixed letter case. Again, passing every local field check is equivalent to passing the whole grammar because fields have no cross-field numerical constraints.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"IPv4"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"queryIP": "172.16.254.1"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"IPv4"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Regular expressions:** Fully anchored IPv4 and IPv6 patterns can encode the grammar, but range and leading-zero details make them harder to audit than explicit field checks.
- **Networking-library parser:** Real-world parsers may accept IPv6 compression or alternate IPv4 forms that this simplified problem rejects, so they are not authoritative here.
- **Try integer conversion first:** Exception-based validation is possible, but explicit digit checks avoid exceptions as control flow and make the grammar visible.
- **IPv4 field `"0"`:** Valid; only multi-character fields beginning with zero are rejected.
- **IPv4 value `255`:** Valid at the inclusive upper boundary; `256` is invalid.
- **Empty field:** Rejected in both formats, covering leading, trailing, or repeated delimiters.
- **IPv6 leading zeros:** Allowed as long as the field has at most four characters.
- **IPv6 mixed case:** Both `a-f` and `A-F` are explicitly accepted.
- **IPv6 `::` compression:** Rejected because all eight nonempty fields are required by this problem.
- **Mixed delimiters:** Such a string fails both exact field grammars and returns `"Neither"`.
- **Evaluation order:** IPv4 is tested first, but no valid IPv6 string can satisfy the four decimal-dot-field grammar, so classification is unambiguous.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `queryIP`. Splitting and examining fields processes $O(n)$ characters. IPv4 and IPv6 validation may both run, but two linear passes are still $O(n)$ total time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
