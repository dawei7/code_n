# Maximize Value of Function in a Ball Passing Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2836 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/) |

## Problem Description

### Goal

An array `receiver` of length $n$ describes a deterministic ball-passing game among players numbered from $0$ through $n-1$. Whenever player $i$ holds the ball, the next player is `receiver[i]`. Different players may pass to the same receiver, and a player may pass to themself.

Choose the starting player, then perform exactly `k` passes. The game's score is the sum of every player index that touches the ball: the starting index and the receiver after each of the `k` passes are all included, with repeated visits counted repeatedly. Return the maximum score attainable over all choices of starting player.

### Function Contract

**Inputs**

- `receiver`: A list of length $n$, where $1 \le n \le 10^5$ and $0 \le \texttt{receiver[i]} < n$.
- `k`: The exact number of passes, where $1 \le k \le 10^{10}$.

**Return value**

Return the greatest sum of the $k+1$ visited player indices over every possible starting player.

### Examples

#### Example 1

- **Input:** `receiver = [2, 0, 1], k = 4`
- **Output:** `6`
- **Explanation:** Starting at player `2` visits `2, 1, 0, 2, 1`, whose indices sum to $6$.

#### Example 2

- **Input:** `receiver = [1, 1, 1, 2, 3], k = 3`
- **Output:** `10`
- **Explanation:** Starting at player `4` visits `4, 3, 2, 1`, producing the maximum score $10$.
