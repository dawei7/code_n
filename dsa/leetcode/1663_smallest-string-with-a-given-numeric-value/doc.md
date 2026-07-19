# Smallest String With A Given Numeric Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1663 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/) |

## Problem Description
### Goal
Assign each lowercase letter its 1-indexed alphabet position: `a` has value 1, `b` has value 2, through `z` with value 26. The numeric value of a string is the sum of all its character values; for example, `"abe"` has value $1+2+5=8$.

Given a required length `n` and numeric value `k`, construct the lexicographically smallest lowercase string having exactly that length and sum. The constraints guarantee that at least one such string exists. Lexicographic comparison uses the first position where two equal-length strings differ.

### Function Contract
**Inputs**

- `n`: the required string length, where $1 \le n \le 10^5$.
- `k`: the required numeric value, where $n \le k \le 26n$.

**Return value**

Return the lexicographically smallest length-$n$ lowercase string whose character values sum to $k$.

### Examples
**Example 1**

- Input: `n = 3, k = 27`
- Output: `"aay"`

Its value is $1+1+25=27$, and keeping the extra value at the right makes the prefix smallest.

**Example 2**

- Input: `n = 5, k = 73`
- Output: `"aaszz"`
