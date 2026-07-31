# Check If Digits Are Equal in String After Operations I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3461 |
| Difficulty | Easy |
| Topics | Math, String, Simulation, Combinatorics, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/) |

## Problem Description
### Goal
Start with a decimal digit string `s`. In one operation, replace every adjacent pair by a single digit equal to the pair's sum modulo $10$. Compute these new digits from left to right and keep them in that order, so a string of length $L$ becomes one of length $L-1$.

Repeat the operation until exactly two digits remain. Return whether those final digits are equal. Each round uses all digits from the preceding round simultaneously; a newly computed digit must not be reused during the same round.

### Function Contract
**Inputs**

- `s`: A string containing only decimal digits.

Let $n=\lvert s\rvert$. The constraints are $3 \le n \le 100$.

**Return value**

Return `True` if the final two digits are equal after all required rounds; otherwise return `False`.

### Examples
**Example 1**

- Input: `s = "3902"`
- Output: `true`

The successive strings are `"3902"`, `"292"`, and `"11"`.

**Example 2**

- Input: `s = "34789"`
- Output: `false`

The transformations produce `"7157"`, then `"862"`, and finally `"48"`.

**Example 3**

- Input: `s = "111"`
- Output: `true`

The single required round produces `"22"`.
