# Even Odd Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1609 |
| Difficulty | Medium |
| Topics | Tree, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/even-odd-tree/) |

## Problem Description
### Goal
A binary tree's root is on level 0, its children are on level 1, and each later generation increases the level index by one. The tree is Even-Odd only when every level obeys rules determined by that index's parity.

On each even-indexed level, every node value must be odd and the values must be strictly increasing from left to right. On each odd-indexed level, every value must be even and the values must be strictly decreasing from left to right. Return whether the entire tree satisfies both the parity and ordering requirements at every level.

### Function Contract
**Inputs**

- `root`: the non-null root of a binary tree containing between 1 and $10^5$ nodes.
- Every node value is an integer from 1 through $10^6$.

**Return value**

Return `true` if all even-indexed and odd-indexed levels satisfy their respective value parity and strict left-to-right order; otherwise return `false`.

### Examples
**Example 1**

- Input: `root = [1, 10, 4, 3, null, 7, 9, 12, 8, 6, null, null, 2]`
- Output: `true`
- Explanation: Levels `[1]` and `[3, 7, 9]` are odd and increasing, while `[10, 4]` and `[12, 8, 6, 2]` are even and decreasing.

**Example 2**

- Input: `root = [5, 4, 2, 3, 3, 7]`
- Output: `false`
- Explanation: The duplicate 3 values on level 2 violate strict increase.

**Example 3**

- Input: `root = [5, 9, 1, 3, 5, 7]`
- Output: `false`
- Explanation: Level 1 contains odd values, but an odd-indexed level requires even values.
