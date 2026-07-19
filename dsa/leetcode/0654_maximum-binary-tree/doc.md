# Maximum Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 654 |
| Difficulty | Medium |
| Topics | Array, Divide and Conquer, Stack, Tree, Monotonic Stack, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-binary-tree/) |

## Problem Description
### Goal
Given a nonempty integer array `nums` with no duplicates, build its maximum binary tree recursively. Create the root from the maximum value in the current array; build its left subtree from the subarray prefix to the left of that maximum, and its right subtree from the suffix to the right.

Apply the same rule recursively to each nonempty subarray, using no node for an empty part. Return the root of the completed maximum binary tree. The original array order determines which values belong on each side and must not be sorted or otherwise rearranged.

### Function Contract
**Inputs**

- `nums`: a nonempty list of distinct integers

**Return value**

- The root node of the maximum binary tree defined by `nums`

### Examples
**Example 1**

- Input: `nums = [3, 2, 1, 6, 0, 5]`
- Output: `[6, 3, 5, null, 2, 0, null, null, 1]`

**Example 2**

- Input: `nums = [3, 2, 1]`
- Output: `[3, null, 2, null, 1]`

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `[3, 2, null, 1]`
