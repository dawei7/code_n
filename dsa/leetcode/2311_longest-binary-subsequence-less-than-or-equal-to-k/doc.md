# Longest Binary Subsequence Less Than or Equal to K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2311 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming, Greedy, Memoization |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/) |

## Problem Description

### Goal

Given the binary string `s` and the positive integer `k`, select a subsequence
whose bits, read in their retained order, form a binary number no greater than
`k`. A subsequence may delete any positions but cannot reorder the remaining
characters.

Leading zeroes are allowed and contribute to the subsequence length without
changing its numeric value. The empty string represents zero. Return the
greatest length achievable under the numeric limit.

### Function Contract

**Inputs**

- `s`: A binary string of length $n$.
- `k`: The inclusive upper bound for the represented binary value.

The contract guarantees $1\le n\le1000$ and $1\le\texttt{k}\le10^9$.

**Return value**

The maximum number of retained characters among subsequences whose binary
value is at most `k`.

### Examples

#### Example 1

- **Input:** `s = "1001010"`, `k = 5`
- **Output:** `5`
- **Explanation:** `"00010"` has length 5 and value 2; no longer valid
  subsequence exists.

#### Example 2

- **Input:** `s = "00101001"`, `k = 1`
- **Output:** `6`
- **Explanation:** `"000001"` is a length-6 subsequence with value 1.
