# Sum of Digits of String After Convert

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1945 |
| Difficulty | Easy |
| Topics | String, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-digits-of-string-after-convert/) |

## Problem Description
### Goal
You are given a lowercase English string `s` and an integer `k`. First replace
each letter by its one-based alphabet position: `a` becomes `1`, `b` becomes
`2`, and so on through `z`, which becomes `26`. Concatenate those decimal
representations to form the converted integer.

A transform replaces the current integer with the sum of its decimal digits.
Apply this transform exactly `k` times in total and return the resulting
integer. The first transform therefore sums every digit contributed by the
alphabet positions; each later transform sums the digits of the preceding
result.

### Function Contract
**Inputs**

- `s`: a lowercase English string of length $N$, where
  $1 \le N \le 100$.
- `k`: the number of digit-sum transforms, where $1 \le k \le 10$.

**Return value**

- The integer remaining after converting `s` and applying the digit-sum
  transform exactly `k` times.

### Examples
**Example 1**

- Input: `s = "iiii", k = 1`
- Output: `36`
- Explanation: The conversion is `9999`, whose digits sum to 36.

**Example 2**

- Input: `s = "leetcode", k = 2`
- Output: `6`
- Explanation: The first digit sum is 33, and the second is 6.

**Example 3**

- Input: `s = "zbax", k = 2`
- Output: `8`
- Explanation: The converted digits sum to 17, then to 8.
