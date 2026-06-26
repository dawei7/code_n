# Create Components With Same Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2440 |
| Difficulty | Hard |
| Topics | Array, Math, Tree, Depth-First Search, Enumeration |
| Official Link | [create-components-with-same-value](https://leetcode.com/problems/create-components-with-same-value/) |

## Problem Description & Examples
### Goal
Given an undirected tree represented by node values and edges, determine the maximum number of components the tree can be partitioned into by removing edges such that the sum of node values in every resulting component is identical.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the value of each node.
- `edges`: A list of pairs representing the undirected connections between nodes.

**Return value**

- An integer representing the maximum number of components (k) such that the total sum of the tree is divisible by k, and each component sums to `total_sum / k`.

### Examples
**Example 1**

- Input: `nums = [6,2,2,2,6], edges = [[0,1],[1,2],[1,3],[3,4]]`
- Output: `2`

**Example 2**

- Input: `nums = [2], edges = []`
- Output: `1`

**Example 3**

- Input: `nums = [1,2,1,2,1], edges = [[0,1],[1,2],[2,3],[3,4]]`
- Output: `5`

---

## Underlying Base Algorithm(s)
The problem relies on **DFS (Depth-First Search)** for tree traversal and **Divisor Enumeration**. Since the total sum of the tree must be partitioned into $k$ equal parts, $k$ must be a divisor of the total sum. We iterate through possible values of $k$ (starting from the largest possible) and use a post-order DFS to check if the tree can be partitioned into components of size `total_sum / k`.

---

## Complexity Analysis
- **Time Complexity**: $O(N \cdot d(S))$, where $N$ is the number of nodes and $d(S)$ is the number of divisors of the total sum $S$. For each divisor, we perform a linear time DFS traversal.
- **Space Complexity**: $O(N)$ to store the adjacency list and the recursion stack.
