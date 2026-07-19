# Maximum Product of the Length of Two Palindromic Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2002 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/) |

## Problem Description

### Goal

Given a lowercase string `s`, choose two subsequences. Each subsequence must preserve the order of its selected characters and must read identically from left to right and right to left.

The two selections must be disjoint by source index: no position of `s` may contribute a character to both subsequences, even when equal characters occur elsewhere. Among every valid pair of palindromic subsequences, maximize the product of their lengths and return that product.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $N$, where $2 \le N \le 12$.

**Return value**

Return the maximum value of $\lvert A\rvert\lvert B\rvert$ over two palindromic subsequences $A$ and $B$ selected from disjoint index sets.

### Examples

**Example 1**

- Input: `s = "leetcodecom"`
- Output: `9`
- Explanation: `"ete"` and `"cdc"` use disjoint positions and give $3\cdot3=9$.

**Example 2**

- Input: `s = "bb"`
- Output: `1`
- Explanation: Select one `b` from each of the two source positions.

**Example 3**

- Input: `s = "accbcaxxcxx"`
- Output: `25`
- Explanation: Disjoint subsequences `"accca"` and `"xxcxx"` each have length $5$.
