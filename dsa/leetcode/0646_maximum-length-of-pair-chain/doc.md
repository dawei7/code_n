# Maximum Length of Pair Chain

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 646 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-length-of-pair-chain/) |

## Problem Description
### Goal
You are given pairs `[left_i, right_i]` with $\mathit{left}_{i} < \mathit{right}_{i}$. Pair `[c, d]` can follow pair `[a, b]` in a chain only when $b < c$, so equality at the boundary is not sufficient.

Return the length of the longest pair chain that can be formed. You may select the input pairs in any order, use each pair at most once, and leave unused pairs behind. The answer counts pairs in the chain rather than the number of links between them.

### Function Contract
**Inputs**

- `pairs`: a nonempty list of two-element lists `[left, right]` with `left < right`
- Pairs may be reordered freely, and each input pair may be used at most once

**Return value**

- The maximum number of pairs in a valid chain

### Examples
**Example 1**

- Input: `pairs = [[1,2],[2,3],[3,4]]`
- Output: `2`

**Example 2**

- Input: `pairs = [[1,2],[7,8],[4,5]]`
- Output: `3`

**Example 3**

- Input: `pairs = [[1,10],[2,3],[4,5],[6,7]]`
- Output: `3`
