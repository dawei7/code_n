# Check If Digits Are Equal in String After Operations II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3463 |
| Difficulty | Hard |
| Topics | Math, String, Combinatorics, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/) |

## Problem Description

### Goal

Start with a decimal digit string `s`. One operation replaces every adjacent pair with a digit equal to the pair's sum modulo $10$. Compute all of a round's new digits from the unchanged current string, proceeding from left to right and preserving that order. Consequently, a string of length $L$ becomes a string of length $L-1$ after one operation.

Repeat this simultaneous transformation until exactly two digits remain. Return whether those final digits are equal. The input may contain as many as $10^5$ digits, so reproducing every shrinking intermediate string is too slow; the result must instead be determined without carrying out the full quadratic simulation.

### Function Contract

**Inputs**

- `s`: A string containing only decimal digits.

Let $n=\lvert s\rvert$. The constraints are $3 \le n \le 10^5$.

**Return value**

Return `True` if the final two digits are equal after all required operations; otherwise return `False`.

### Examples

#### Example 1

- **Input:** `s = "3902"`
- **Output:** `true`

The successive strings are `"3902"`, `"292"`, and `"11"`.

#### Example 2

- **Input:** `s = "34789"`
- **Output:** `false`

The transformations produce `"7157"`, then `"862"`, and finally `"48"`.

#### Example 3

- **Input:** `s = "111"`
- **Output:** `true`

The one required operation produces `"22"`.
