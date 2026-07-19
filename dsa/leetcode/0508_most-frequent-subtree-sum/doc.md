# Most Frequent Subtree Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 508 |
| Difficulty | Medium |
| Topics | Hash Table, Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/most-frequent-subtree-sum/) |

## Problem Description
### Goal
Given a nonempty binary tree, define the subtree rooted at a node to include that node and every descendant below it. Its subtree sum is the total of all node values in that rooted subtree, so overlapping subtrees at different roots are counted independently.

Compute one subtree sum per node and return every sum value having the highest frequency, in any order. If several different sums tie, include all of them once; repeated occurrences affect frequency but do not repeat the same modal value in the output. Negative node values and equal sums from differently shaped subtrees are handled normally.

### Function Contract
**Inputs**

- `root`: the root of a nonempty binary tree

**Return value**

- Every subtree-sum value having maximum frequency, in any order

### Examples
**Example 1**

- Input: `root = [5, 2, -3]`
- Output: `[2, -3, 4]`

**Example 2**

- Input: `root = [5, 2, -5]`
- Output: `[2]`

**Example 3**

- Input: `root = [1]`
- Output: `[1]`
