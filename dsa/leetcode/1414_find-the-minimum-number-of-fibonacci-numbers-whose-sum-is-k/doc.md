# Find the Minimum Number of Fibonacci Numbers Whose Sum Is K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1414 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/) |

## Problem Description

### Goal

Fibonacci numbers begin with $1, 1$, and every later number is the sum of the previous two. Given a positive integer `k`, choose Fibonacci numbers whose sum is exactly `k`. A Fibonacci value may be chosen more than once when forming the sum.

Return the minimum possible number of chosen terms. Only the count is required, not the particular representation, and `k` can be large enough that enumerating all sums is impractical.

### Function Contract

**Inputs**

- `k`: the required positive sum, where $1 \le k \le 10^9$.

**Return value**

- The minimum number of Fibonacci terms whose sum equals `k`.

### Examples

**Example 1**

- Input: `k = 7`
- Output: `2`

**Example 2**

- Input: `k = 10`
- Output: `2`

**Example 3**

- Input: `k = 19`
- Output: `3`
