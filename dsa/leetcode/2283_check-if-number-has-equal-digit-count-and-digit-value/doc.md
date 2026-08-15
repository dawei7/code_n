# Check if Number Has Equal Digit Count and Digit Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2283 |
| Difficulty | Easy |
| Topics | Hash Table, String, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/) |

## Problem Description

### Goal

The string `num` contains $n$ decimal digits and is indexed from zero. For
each index $i$, interpret `num[i]` as a numeric count.

Return `true` exactly when, for every $0 \le i < n$, digit $i$ occurs in the
whole string exactly `num[i]` times. Return `false` if any index's required
count differs from its actual frequency. Every comparison uses frequencies
from the complete original string.

### Function Contract

**Inputs**

- `num`: A string of $n$ decimal digits.

Here, $1 \le n \le 10$.

**Return value**

`true` if every indexed digit frequency equals the value stored at that index;
otherwise, `false`.

### Examples

#### Example 1

- **Input:** `num = "1210"`
- **Output:** `true`

#### Example 2

- **Input:** `num = "030"`
- **Output:** `false`

#### Example 3

- **Input:** `num = "2020"`
- **Output:** `true`
