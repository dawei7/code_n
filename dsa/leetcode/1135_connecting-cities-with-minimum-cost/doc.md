# Connecting Cities With Minimum Cost

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1135 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Union-Find, Graph Theory, Heap (Priority Queue), Minimum Spanning Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/connecting-cities-with-minimum-cost/) |

## Problem Description

### Goal

There are `n` cities labeled from `1` through `n`. Each entry `connections[i] = [x_i, y_i, cost_i]` describes an available bidirectional connection between cities `x_i` and `y_i`, together with the cost of using that connection.

Choose available connections so that every pair of cities has at least one path between them. The total cost is the sum of the costs of all chosen connections. Return the minimum possible total cost, or return `-1` when even all available connections cannot make every city reachable from every other city.

### Function Contract

**Inputs**

- `n`: the number of cities, with $1 \le n \le 10^4$.
- `connections`: an array of $m$ available bidirectional connections, where $1 \le m \le 10^4$.
- Every connection has the form `[x_i, y_i, cost_i]`, where $1 \le x_i,y_i \le n$, $x_i \ne y_i$, and $0 \le cost_i \le 10^5$.

Let $m=\lvert\texttt{connections}\rvert$.

**Return value**

The minimum sum of chosen connection costs that connects all `n` cities, or `-1` if no such selection exists.

### Examples

**Example 1**

- Input: `n = 3, connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]`
- Output: `6`
- Explanation: Using the connections of costs `1` and `5` reaches all three cities for the smallest possible sum.

**Example 2**

- Input: `n = 4, connections = [[1, 2, 3], [3, 4, 4]]`
- Output: `-1`
- Explanation: The two connected pairs remain separate even when every available connection is used.
