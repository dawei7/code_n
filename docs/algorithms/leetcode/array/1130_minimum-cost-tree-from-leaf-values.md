# Minimum Cost Tree From Leaf Values

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1130 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Stack, Greedy, Monotonic Stack |
| Official Link | [minimum-cost-tree-from-leaf-values](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/) |

## Problem Description & Examples
### Goal
Given the leaf values of a binary tree in left-to-right order, build a tree with those leaves. Each internal node costs the product of the largest leaf value in its left subtree and the largest leaf value in its right subtree. Minimize the total internal-node cost.

### Function Contract
**Inputs**

- `arr`: positive leaf values in inorder leaf order.

**Return value**

The minimum possible sum of internal-node values.

### Examples
**Example 1**

- Input: `arr = [6,2,4]`
- Output: `32`

**Example 2**

- Input: `arr = [4,11]`
- Output: `44`

**Example 3**

- Input: `arr = [7,12,8,10]`
- Output: `284`

---

## Underlying Base Algorithm(s)
Greedy monotonic stack.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
