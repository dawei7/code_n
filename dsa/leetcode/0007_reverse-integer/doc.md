# Reverse Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 7 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-integer/) |

## Problem Description
### Goal
Given a signed 32-bit integer `x`, reverse the order of the digits in its decimal magnitude while preserving its sign. Zeroes that move to the front of the reversed magnitude are discarded by ordinary integer notation, so reversing `120` produces `21`.

Return the reversed integer only when it still lies in the signed 32-bit interval $[- 2 ^{31}, 2 ^{31} - 1]$. If the reversed magnitude would overflow that range, return `0` instead. The task assumes no wider integer type is available merely to hold an overflowing intermediate result.

### Function Contract
**Inputs**

- `x`: signed 32-bit `int`

**Return value**

An `int` containing the reversed value, or `0` when reversal overflows the signed 32-bit range.

### Examples
**Example 1**

- Input: `x = 123`
- Output: `321`

**Example 2**

- Input: `x = -123`
- Output: `-321`

**Example 3**

- Input: `x = 120`
- Output: `21`

### Required Complexity

- **Time:** $O(\log |x|)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Transfer digits arithmetically from right to left**

Remember whether `x` is negative and work with its nonnegative magnitude. Repeatedly divide the remaining magnitude by `10`: the remainder is its last decimal digit, and the quotient is the still-unprocessed prefix. Appending a popped digit `digit` to a partial reversal `reversed_value` would produce:

```text
reversed_value * 10 + digit
```

Because zero contributes nothing when appended to an initially zero result, trailing zeroes in the original number disappear naturally. For example, the popped digits of `120` are `0`, `2`, and `1`, producing partial results `0`, `2`, and `21`.

**Account for the asymmetric signed range**

A signed 32-bit integer ranges from $-2^{31}$ through $2^{31} - 1$. The negative side permits a magnitude of $2^{31}$, one greater than the largest positive value. Choose the allowed magnitude before processing digits:

- $2^{31} - 1$ when the original number is nonnegative;
- $2^{31}$ when it is negative.

This distinction matters for boundary inputs. Treating both signs with the positive limit would incorrectly reject the valid result `-2147483648` if its digit reversal produced that exact value.

**Detect overflow before performing the risky operation**

Do not calculate the next partial value and then ask whether it overflowed. In fixed-width languages, the multiplication may already have wrapped or become invalid. Instead, rearrange the desired inequality:

```text
reversed_value * 10 + digit <= limit
```

Since all terms are nonnegative, it is safe to append the digit exactly when:

```text
reversed_value <= (limit - digit) // 10
```

If the condition fails, the mathematical reversal lies outside the permitted signed range, so return `0` immediately. Otherwise perform the multiplication and addition, then pop the next input digit.

**Digit transfer and overflow stay exact together**

Before each pop, `reversed_value` contains the digits already removed from the input magnitude in their final reversed order, while the remaining quotient contains exactly the unprocessed prefix. Appending the next remainder preserves this division of the original decimal representation, so exhaustion yields the mathematical digit reversal.

The preflight inequality is algebraically equivalent to the proposed append staying within the sign-specific magnitude limit. If it fails, the next reversed prefix is already too large; appending further nonnegative decimal digits cannot bring the eventual value back into range. Returning zero is therefore required at that exact point. If every append passes, all arithmetic remains representable, and restoring the saved sign produces the requested integer.

#### Complexity detail

Each division by `10` removes one decimal digit, so an input with $d = \Theta(\log_{10} \lvert x \rvert)$ digits takes $O(\log \lvert x \rvert)$ time. The algorithm stores only the sign, remaining magnitude, current digit, limit, and partial reversal, giving $O(1)$ auxiliary space. The $x = 0$ case performs constant work.

#### Alternatives and edge cases

- Converting to a string, reversing it, and parsing it back is concise but uses $O(\log |x|)$ additional storage and still requires a range check.
- Reversing first and checking afterward is unsafe in languages with fixed-width integer overflow.
- Using an arbitrarily wide or wider integer type can mask the central overflow issue and is unnecessary when the preflight inequality is available.
- Negative values should not use language-specific remainder behavior directly unless it is understood; processing the magnitude keeps every digit nonnegative.
- Inputs ending in one or more zeroes lose those zeroes in the result, and `0` remains `0`.

</details>
