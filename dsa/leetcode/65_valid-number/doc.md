# Valid Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 65 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-number/) |

## Problem Description
### Goal
You are given a nonempty string and must decide whether the entire string is a valid decimal number. A valid mantissa may have an optional leading sign and may be an integer or decimal, but it must contain at least one digit; forms such as `2`, `-0.1`, `4.`, and `.9` are permitted.

The mantissa may be followed by one `e` or `E` and an exponent. An exponent may have its own sign but must be an integer containing at least one digit. No spaces, extra characters, misplaced signs, repeated decimal points, or decimal exponent parts are accepted. Return the resulting boolean classification.

### Function Contract
**Inputs**

- `s`: a nonempty string to classify

**Return value**

`True` if the entire string is a valid number and `False` otherwise.

### Examples
**Example 1**

- Input: `s = "2"`
- Output: `True`

**Example 2**

- Input: `s = "-90E3"`
- Output: `True`

**Example 3**

- Input: `s = "99e2.5"`
- Output: `False`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce the grammar to four facts about the consumed prefix**

Maintain whether any digit has appeared, whether a decimal point has appeared, whether an exponent marker has appeared, and whether a digit is currently required after the exponent. These flags summarize all history relevant to the next character; the exact digit values never matter.

Digits are always syntactically acceptable. A mantissa digit satisfies the requirement that an integer or decimal contain at least one digit, while a digit after `e` or `E` satisfies the exponent's mandatory integer body.

**Each non-digit has a precise legal location**

A sign is valid only at index zero or immediately after `e` or `E`; it cannot appear after a decimal point or ordinary digit unless an exponent has just begun. A decimal point is valid at most once and only before an exponent. It may appear before all mantissa digits (`.1`) or after them (`3.`), but the complete mantissa must contain at least one digit.

An exponent marker is valid at most once and only after a mantissa digit. It starts an integer-only exponent, so no later decimal point or second exponent is legal. It also resets the “digit seen in the current required component” condition: `2e` is only a valid prefix, not a valid complete number, until an exponent digit appears.

**Prefix validity is not enough—the final state must be accepting**

After each accepted character, the consumed prefix can still be extended into a valid number, and the flags precisely summarize its grammar components. Any rejected character or placement cannot be repaired by a later suffix because it violates ordering or uniqueness already fixed in the prefix.

The scan must still check an accepting final condition. A digit must have appeared in the mantissa, and if an exponent was opened, at least one digit must have appeared after it. This rejects otherwise extendable but incomplete prefixes such as `+`, `.`, `4e`, and `6e-`.

**Trace valid signs and an invalid late decimal point**

For `-90E-3`, the first sign is allowed, `9` and `0` establish a mantissa, `E` is allowed after digits, the next sign is allowed after `E`, and `3` satisfies the exponent-digit requirement. For `99e2.5`, the point is rejected because an exponent has already begun.

**The flags encode the complete numeric grammar**

Each sign is accepted only at the string start or immediately after an exponent marker; a decimal point is accepted only once and before any exponent; an exponent is accepted only after mantissa digits and only once. These conditions are exactly the legal positions of the grammar's optional components.

Digits update whether the mantissa or exponent has actual numeric content. Therefore a scan that finishes with mantissa digits and, when present, exponent digits describes a valid number. Every valid spelling follows the same transitions, while final content checks reject incomplete prefixes such as `+`, `.`, or `2e`.

#### Complexity detail

The scan examines each character once, giving $O(n)$ time. A fixed number of flags use $O(1)$ space.

#### Alternatives and edge cases

- **Regular expression:** can encode the grammar compactly but hides the state transitions this exercise tests.
- **Built-in floating-point parsing:** may accept unsupported forms such as whitespace, infinities, or language-specific literals.
- **Explicit finite-state table:** is equally linear and highly formal, but more verbose than the equivalent flag transitions.
- `46.e3`, `.8`, and `+6` are valid; `.`, `e9`, `1e`, `--6`, and `95a54e53` are not.
- The entire input must match. Trimming whitespace or accepting numeric prefixes would implement a different contract.

</details>
