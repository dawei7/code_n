# Find the Maximum Sum of Node Values

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3068 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy, Bit Manipulation, Tree, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-maximum-sum-of-node-values/) |

## Problem Description

### Goal

An undirected tree has $n$ nodes numbered from $0$ through $n-1$. The zero-indexed array `nums` gives their non-negative values, while each entry `edges[i] = [u_i, v_i]` identifies one tree edge. You are also given a positive integer `k`.

In one operation, choose any edge `[u, v]` and replace both endpoint values: set `nums[u] = nums[u] XOR k` and `nums[v] = nums[v] XOR k`. You may perform this operation any number of times, including zero.

Return the maximum possible sum of all node values after the chosen operations.

### Function Contract

**Inputs**

- `nums`: A zero-indexed array of $n$ non-negative node values.
- `k`: The positive integer XOR operand applied to both endpoints of an operated edge.
- `edges`: The $n-1$ undirected edges of a valid tree on nodes $0$ through $n-1$.

The constraints are $2 \le n \le 2 \cdot 10^4$, $1 \le k \le 10^9$, $0 \le \texttt{nums[i]} \le 10^9$, and `edges` forms a valid tree.

**Return value**

Return the maximum achievable sum of the final node values.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 1], k = 3, edges = [[0, 1], [0, 2]]`
- **Output:** `6`
- **Explanation:** Operating on `[0, 2]` changes both endpoint values from `1` to `2`, producing `[2, 2, 2]`.

#### Example 2

- **Input:** `nums = [2, 3], k = 7, edges = [[0, 1]]`
- **Output:** `9`
- **Explanation:** Operating on the only edge produces `[5, 4]`.

#### Example 3

- **Input:** `nums = [7, 7, 7, 7, 7, 7], k = 3, edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]`
- **Output:** `42`
- **Explanation:** Performing no operation preserves the maximum sum.
