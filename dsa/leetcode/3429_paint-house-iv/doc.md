# Paint House IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3429 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/paint-house-iv/) |

## Problem Description

### Goal

Paint an even number $n$ of houses arranged in a row. Exactly three colors are available, and `cost[i][j]` is the price of assigning color $j$ to house $i$.

A valid assignment obeys two rules. Adjacent houses must have different colors. In addition, every two houses equally far from the two ends must have different colors: house $i$ cannot match house $n-1-i$. Determine the minimum total painting cost among all assignments satisfying both conditions.

### Function Contract

**Inputs**

- `n`: The even number of houses, with $2 \le n \le 10^5$.
- `cost`: An $n\times3$ matrix where `cost[i][j]` is the cost of painting house $i$ with color $j$, and $0 \le \texttt{cost[i][j]} \le 10^5$.

**Return value**

Return the minimum total cost of a valid coloring.

### Examples

#### Example 1

- **Input:** `n = 4, cost = [[3,5,7],[6,2,9],[4,8,1],[7,3,5]]`
- **Output:** `9`

#### Example 2

- **Input:** `n = 6, cost = [[2,4,6],[5,3,8],[7,1,9],[4,6,2],[3,5,7],[8,2,4]]`
- **Output:** `18`
