# Consecutive Numbers Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 829 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/consecutive-numbers-sum/) |

## Problem Description

### Goal

Given a positive integer `n`, count how many different sequences of one or more consecutive positive integers have sum `n`. A sequence is determined by its positive starting value and its length, and the one-term sequence containing `n` itself is valid.

Return the number of such representations. Terms must increase by exactly `1`, remain positive, and appear once each within their sequence; rearranging the same terms does not create another representation.

### Function Contract

**Inputs**

- `n`: an integer satisfying $1 \le n \le 10^9$

**Return value**

- The number of ways to express `n` as a sum of consecutive positive integers

### Examples

**Example 1**

- Input: `n = 5`
- Output: `2`
- Explanation: The representations are $5$ and $2+3$.

**Example 2**

- Input: `n = 9`
- Output: `3`
- Explanation: The representations are $9$, $4+5$, and $2+3+4$.

**Example 3**

- Input: `n = 15`
- Output: `4`
- Explanation: The representations are $15$, $7+8$, $4+5+6$, and $1+2+3+4+5$.
