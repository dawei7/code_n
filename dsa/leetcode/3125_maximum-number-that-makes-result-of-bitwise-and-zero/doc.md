# Maximum Number That Makes Result of Bitwise AND Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3125 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/) |

## Problem Description

### Goal

Given a positive integer `n`, choose the maximum integer `x` with $x \le n$ such that the bitwise `AND` of every integer in the inclusive range `[x, n]` equals 0.

The range includes both endpoints. Thus a candidate `x` is valid only when applying bitwise `AND` across `x`, `x + 1`, and every subsequent integer through `n` clears every bit position.

### Function Contract

**Inputs**

- `n`: A positive integer satisfying $1 \le n \le 10^{15}$.

**Return value**

Return the greatest integer `x` no larger than `n` for which the cumulative bitwise `AND` of the inclusive range `[x, n]` is 0.

### Examples

**Example 1**

- Input: `n = 7`
- Output: `3`
- Explanation: The cumulative results for starts 6, 5, and 4 remain positive, whereas `3 & 4 & 5 & 6 & 7` is 0.

**Example 2**

- Input: `n = 9`
- Output: `7`
- Explanation: The bitwise `AND` of `7`, `8`, and `9` is 0.

**Example 3**

- Input: `n = 17`
- Output: `15`
- Explanation: The bitwise `AND` of `15`, `16`, and `17` is 0.
