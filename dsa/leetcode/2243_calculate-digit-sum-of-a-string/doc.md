# Calculate Digit Sum of a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2243 |
| Difficulty | Easy |
| Topics | String, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/calculate-digit-sum-of-a-string/) |

## Problem Description

### Goal

You are given a string `s` made only of decimal digits and an integer group
size `k`. Whenever the current string is longer than `k`, divide it from left
to right into consecutive groups of `k` characters. The final group may be
shorter.

Replace every group by the ordinary decimal representation of the sum of its
digits, then concatenate those representations in their original order. Apply
the same round to the resulting string while its length is still greater than
`k`. Return the string once no further round is permitted. A group sum is not
padded with leading zeroes, although distinct zero-sum groups each contribute
one `"0"`.

### Function Contract

**Inputs**

- `s`: A digit string whose length is between $1$ and $100$, inclusive.
- `k`: The group size, where $2\le k\le100$.

**Return value**

Return the digit string remaining after repeatedly replacing every consecutive
group by its digit sum until the string's length is at most `k`.

### Examples

**Example 1**

- Input: `s = "11111222223", k = 3`
- Output: `"135"`

**Example 2**

- Input: `s = "00000000", k = 3`
- Output: `"000"`

**Example 3**

- Input: `s = "123", k = 3`
- Output: `"123"`
