# Magnetic Force Between Two Balls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1552 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/magnetic-force-between-two-balls/) |

## Problem Description
### Goal
Baskets are placed at distinct integer coordinates listed in `position`. You must put exactly one ball into each of `m` chosen baskets. For any two balls, their magnetic force is defined as the absolute difference between their basket coordinates.

Choose the baskets so that the minimum force among every pair of placed balls is as large as possible. Return that greatest achievable minimum distance. The positions may arrive in any order and can be spread over a large coordinate range.

### Function Contract
**Inputs**

- `position`: $n$ distinct basket coordinates, where $2 \le n \le 10^5$ and $1 \le \texttt{position[i]} \le 10^9$.
- `m`: the number of balls, where $2 \le m \le n$.
- Let $R = \max(\texttt{position}) - \min(\texttt{position})$.

**Return value**

The maximum possible value of the minimum pairwise distance between the $m$ selected basket coordinates.

### Examples
**Example 1**

- Input: `position = [1, 2, 3, 4, 7], m = 3`
- Output: `3`
- Explanation: Choosing positions one, four, and seven makes the minimum pairwise distance three.

**Example 2**

- Input: `position = [5, 4, 3, 2, 1, 1000000000], m = 2`
- Output: `999999999`
- Explanation: With two balls, choosing the two extreme positions maximizes their distance.

**Example 3**

- Input: `position = [1, 2, 8, 12, 17], m = 3`
- Output: `7`
- Explanation: Positions one, eight, and seventeen have adjacent gaps seven and nine.
