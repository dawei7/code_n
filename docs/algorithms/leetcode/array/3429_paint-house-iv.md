# Paint House IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3429 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [paint-house-iv](https://leetcode.com/problems/paint-house-iv/) |

## Problem Description & Examples
### Goal
You are tasked with painting a row of $n$ houses using $m$ available colors. The houses are arranged in a line, and you must paint them such that no two adjacent houses share the same color. Additionally, the first and last houses must also have different colors. Given a cost matrix where `cost[i][j]` represents the cost of painting house $i$ with color $j$, determine the minimum total cost to paint all houses while satisfying these constraints.

### Function Contract
**Inputs**

- `n`: An integer representing the number of houses (where $n$ is even).
- `cost`: A 2D list of integers of size $(n \times m)$, where `cost[i][j]` is the cost of painting house $i$ with color $j$.

**Return value**

- An integer representing the minimum cost to paint all houses, or -1 if it is impossible to satisfy the constraints.

### Examples
**Example 1**

- Input: `n = 4, cost = [[3,5,7],[6,2,9],[4,8,1],[7,3,5]]`
- Output: `12`

**Example 2**

- Input: `n = 2, cost = [[1,2,3],[2,3,4]]`
- Output: `4`

**Example 3**

- Input: `n = 4, cost = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]`
- Output: `24`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming. Since the constraints involve the first and last houses, we can observe that the houses can be paired from the outside in (house $i$ and house $n-1-i$). We define `dp[i][c1][c2]` as the minimum cost to paint the first $i$ pairs of houses (from the ends) such that the $i$-th house from the start has color `c1` and the $i$-th house from the end has color `c2`.

---

## Complexity Analysis
- **Time Complexity**: $O(n \cdot m^2)$, where $n$ is the number of houses and $m$ is the number of colors. We iterate through $n/2$ pairs, and for each pair, we transition between $m^2$ color combinations.
- **Space Complexity**: $O(m^2)$, as we only need the results from the previous pair to calculate the current pair.
