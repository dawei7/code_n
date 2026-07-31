# Maximum Fruits Harvested After at Most K Steps

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2106 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [maximum-fruits-harvested-after-at-most-k-steps](https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/) |

## Problem Description

### Goal

Fruit piles occupy distinct positions on an infinite x-axis. Each entry `fruits[i] = [position_i, amount_i]` gives the fruit available at one position. The entries are already sorted by `position_i` in ascending order. You begin at `startPos` and may move either left or right, spending one step for each unit of coordinate distance.

You may walk at most `k` steps in total. Whenever you reach a position containing fruit, you harvest the entire pile and that fruit disappears, so no position can contribute more than once. Choose the route, including whether and where to change direction, that maximizes the total harvested amount, and return that maximum.

### Function Contract

**Inputs**

- `fruits`: An array of $n$ unique `[position, amount]` pairs in ascending position order, where $1 \le n \le 10^5$, $0 \le \texttt{position} \le 2 \cdot 10^5$, and $1 \le \texttt{amount} \le 10^4$.
- `startPos`: The initial coordinate, where $0 \le \texttt{startPos} \le 2 \cdot 10^5$.
- `k`: The maximum total number of steps, where $0 \le k \le 2 \cdot 10^5$.

**Return value**

Return the maximum total amount of fruit harvestable in at most `k` steps.

### Examples

**Example 1**

- Input: `fruits = [[2, 8], [6, 3], [8, 6]], startPos = 5, k = 4`
- Output: `9`
- Explanation: Moving right through positions $6$ and $8$ costs three steps and harvests $3+6=9$ fruits.

**Example 2**

- Input: `fruits = [[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]], startPos = 5, k = 4`
- Output: `14`
- Explanation: Harvest at position $5$, visit $4$, then reverse and walk through $6$ to $7$. The four-step route collects $7+1+2+4=14$.

**Example 3**

- Input: `fruits = [[0, 3], [6, 4], [8, 5]], startPos = 3, k = 2`
- Output: `0`
- Explanation: No fruit position is reachable within two steps.
