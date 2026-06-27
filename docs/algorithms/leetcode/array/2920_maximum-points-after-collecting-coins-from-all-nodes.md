# Maximum Points After Collecting Coins From All Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2920 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Bit Manipulation, Tree, Depth-First Search, Memoization |
| Official Link | [maximum-points-after-collecting-coins-from-all-nodes](https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/) |

## Problem Description & Examples
### Goal
Given a tree rooted at node 0, each node contains a specific number of coins. When visiting a node, you can collect its coins using one of two strategies: either take half the coins (integer division) or take all coins and then halve the coins of all its descendants. Because the halving effect compounds as you move deeper into the tree, the number of coins at any node depends on how many times its ancestors were halved. You must determine the maximum total coins collectable by traversing the tree optimally.

### Function Contract
**Inputs**

- `edges`: A list of lists representing the tree structure (undirected edges).
- `coins`: A list of integers where `coins[i]` is the initial value at node `i`.
- `k`: An integer representing the penalty reduction factor.

**Return value**

- An integer representing the maximum total coins that can be collected.

### Examples
**Example 1**

- Input: `edges = [[0,1],[1,2],[2,3]], coins = [10,10,3,3], k = 5`
- Output: `11`

**Example 2**

- Input: `edges = [[0,1],[0,2]], coins = [8,4,4], k = 0`
- Output: `16`

---

## Underlying Base Algorithm(s)
The problem is solved using Tree Dynamic Programming with Memoization. Since the halving effect only matters up to a certain depth (because `coins[i] // 2^14` eventually becomes 0), we can track the state as `(current_node, parent_node, halving_count)`. The `halving_count` is capped at 13 to prevent redundant states.

## Complexity Analysis
- **Time Complexity**: `O(N * K)`, where `N` is the number of nodes and `K` is the maximum number of effective halving operations (typically 14).
- **Space Complexity**: `O(N * K)` to store the memoization table.
