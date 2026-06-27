# Painting the Walls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2742 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [painting-the-walls](https://leetcode.com/problems/painting-the-walls/) |

## Problem Description & Examples
### Goal
You are given $n$ walls that need to be painted. You have two painters available:
1. A **paid painter** who charges `cost[i]` to paint the $i$-th wall and takes `time[i]` units of time to complete it.
2. A **free painter** who paints any wall for free, taking exactly $1$ unit of time per wall. However, the free painter can only work while the paid painter is occupied.

Determine the minimum cost required to paint all $n$ walls.

### Function Contract
**Inputs**

- `cost`: `List[int]` — The cost of hiring the paid painter for each wall.
- `time`: `List[int]` — The time the paid painter takes to paint each wall.

**Return value**

- `int` — The minimum cost to paint all $n$ walls.

### Examples
**Example 1**

- Input: `cost = [1,2,3,2], time = [1,2,3,2]`
- Output: `3`
- Explanation: We can hire the paid painter to paint wall 0 (cost 1, time 1) and wall 3 (cost 2, time 2). While the paid painter is busy for 3 units of time, the free painter can paint the remaining 2 walls (wall 1 and wall 2). The total cost is $1 + 2 = 3$.

**Example 2**

- Input: `cost = [2,3,4,2], time = [1,1,1,1]`
- Output: `4`
- Explanation: We can hire the paid painter to paint wall 0 (cost 2, time 1) and wall 3 (cost 2, time 1). While the paid painter is busy for 2 units of time, the free painter can paint wall 1 and wall 2. The total cost is $2 + 2 = 4$.

---

## Underlying Base Algorithm(s)
This problem can be modeled as a variation of the **0/1 Knapsack Problem** using **Dynamic Programming**.

### Key Insight
When we hire the paid painter to paint wall $i$:
1. Wall $i$ is painted.
2. The paid painter is occupied for `time[i]` units of time.
3. During this time, the free painter can paint up to `time[i]` walls.

Thus, choosing to paint wall $i$ with the paid painter effectively covers **$1 + \text{time}[i]$** walls at a cost of **$\text{cost}[i]$**. 

Our goal is to select a subset of walls to paint with the paid painter such that the total number of walls covered is at least $n$, while minimizing the total cost.

### DP State and Transition
Let `dp[j]` represent the minimum cost to paint at least `j` walls.
- **Base Case**: `dp[0] = 0` (0 cost to paint 0 walls), and `dp[j] = infinity` for all $j > 0$.
- **Transition**: For each wall $i$ with cost $c = \text{cost}[i]$ and time $t = \text{time}[i]$:
  $$dp[j] = \min(dp[j], dp[\max(0, j - (t + 1))] + c)$$
  We iterate $j$ backwards from $n$ down to $1$ to ensure each wall is considered at most once (standard 0/1 knapsack space optimization).

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n^2)$ where $n$ is the number of walls. We iterate through $n$ walls, and for each wall, we update the DP array of size $n + 1$.
- **Space Complexity**: $\mathcal{O}(n)$ to store the 1D DP state array of size $n + 1$.
