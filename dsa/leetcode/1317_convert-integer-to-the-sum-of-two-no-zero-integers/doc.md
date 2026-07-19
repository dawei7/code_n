# Convert Integer to the Sum of Two No-Zero Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1317 |
| Difficulty | Easy |
| Topics | Math |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/) |

## Problem Description
### Goal
A positive integer is a **No-Zero integer** when none of the digits in its decimal representation is `0`.

Given an integer `n`, find two positive No-Zero integers `a` and `b` whose sum is `n`. The answer is guaranteed to exist. More than one pair may satisfy the conditions, and any valid pair may be returned.

The two values do not need to be different, and the target itself may contain zero digits; the restriction applies only to the returned addends.

### Function Contract
**Inputs**

- `n`: an integer with $2\le n\le 10^4$.

**Return value**

A two-element list `[a, b]` such that $a>0$, $b>0$, $a+b=n$, and neither decimal representation contains the digit `0`.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `[1, 1]`
- Explanation: Both values are positive, contain no zero digit, and sum to 2.

**Example 2**

- Input: `n = 11`
- Output: `[2, 9]`
- Explanation: `2 + 9 = 11`, and both addends are No-Zero integers. Other valid pairs are also accepted.

**Example 3**

- Input: `n = 10000`
- Output: `[1, 9999]`
- Explanation: Although the target contains zero digits, neither returned addend does.
