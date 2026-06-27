# Find the Maximum Sum of Node Values

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3068 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Greedy, Bit Manipulation, Tree, Sorting |
| Official Link | [find-the-maximum-sum-of-node-values](https://leetcode.com/problems/find-the-maximum-sum-of-node-values/) |

## Problem Description & Examples
### Goal
Given an array of node values and an integer `k`, you can perform an operation any number of times: select any two connected nodes and XOR their values with `k`. The objective is to maximize the total sum of all node values after performing any number of these operations.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial values of the nodes.
- `k`: An integer used for the XOR operation.
- `edges`: A list of pairs representing the connections between nodes (note: since the operation can be applied to any connected pair, the graph structure allows us to propagate the XOR operation to any two nodes, effectively allowing us to XOR any pair of nodes).

**Return value**

- An integer representing the maximum possible sum of all node values.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1], k = 3, edges = [[0, 1], [0, 2]]`
- Output: `6`

**Example 2**

- Input: `nums = [2, 3], k = 7, edges = [[0, 1]]`
- Output: `9`

**Example 3**

- Input: `nums = [7, 7, 7, 7, 7, 7], k = 3, edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]`
- Output: `42`

---

## Underlying Base Algorithm(s)
The problem can be reduced to a greedy strategy. XORing two nodes with `k` twice is equivalent to doing nothing. XORing any two nodes with `k` is always possible if they are connected. By transitivity, we can XOR any pair of nodes with `k`. The core insight is that we want to maximize the sum by choosing an even number of nodes to XOR with `k`. For each node, we decide whether to keep `nums[i]` or change it to `nums[i] ^ k`. We track the net gain `(nums[i] ^ k) - nums[i]` and ensure we only apply the XOR to an even number of nodes to maintain the parity constraint.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of nodes, as we iterate through the array once to calculate gains and parity.
- **Space Complexity**: `O(1)`, as we only store a few variables regardless of the input size.
