# Path Sum IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 666 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/path-sum-iv/) |

## Problem Description
### Goal
A binary tree of depth at most four is encoded as three-digit integers. In each number, the hundreds digit gives the node's one-based depth, the tens digit gives its one-based position within that level as if the tree were full, and the units digit gives the node's value.

Decode the connected tree described by the input and compute every root-to-leaf path sum. Return the sum of all those path sums. A node contributes separately to every leaf path passing through it, and only nodes present in the encoding belong to the tree.

### Function Contract
**Inputs**

- `nums`: a sorted list of unique three-digit encodings; the hundreds digit is depth, the tens digit is the 1-based position within that level, and the ones digit is the node value

**Return value**

- The sum of the value sums along all root-to-leaf paths

### Examples
**Example 1**

- Input: `nums = [113, 215, 221]`
- Output: `12`

**Example 2**

- Input: `nums = [113, 221]`
- Output: `4`

**Example 3**

- Input: `nums = [111]`
- Output: `1`
