# Closest Divisors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1362 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/closest-divisors/) |

## Problem Description

### Goal

Given a positive integer `num`, consider the two consecutive values `num + 1` and `num + 2`. Choose two positive integers whose product equals either one of those values.

Among every eligible factor pair for both products, return a pair whose two members have the smallest absolute difference. Either order is acceptable. If more than one pair has the same minimum difference, any such pair may be returned.

### Function Contract

**Inputs**

- `num`: a positive integer.
- Let $n=\texttt{num}+2$, the larger of the two candidate products.

**Return value**

- Two positive integers `[a, b]` such that $ab$ equals `num + 1` or `num + 2`, minimizing $\lvert a-b \rvert$ across both products.

### Examples

**Example 1**

- Input: `num = 8`
- Output: `[3,3]`
- Explanation: $3\cdot3=9=\texttt{num}+1$, and the difference is zero.

**Example 2**

- Input: `num = 123`
- Output: `[5,25]`
- Explanation: $5\cdot25=125=\texttt{num}+2$ is closer than every factor pair of 124.

**Example 3**

- Input: `num = 999`
- Output: `[25,40]`
- Explanation: $25\cdot40=1000=\texttt{num}+1$.
