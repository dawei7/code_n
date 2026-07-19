# Sum of Root To Leaf Binary Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1022 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/) |

## Problem Description

### Goal

You are given the root of a binary tree in which every node value is `0` or `1`. Each root-to-leaf path spells a binary number from its most-significant bit at the root to its least-significant bit at the leaf.

Interpret every such path as a base-2 integer and return their sum over all leaves. Leading zeroes are allowed on a path and do not change its numeric value. The test data guarantees that the final sum fits in a 32-bit integer.

### Function Contract

**Inputs**

- `root`: the root of a nonempty binary tree with $N$ nodes, where $1\le N\le1000$ and every `Node.val` is `0` or `1`.

Let $H$ denote the tree height, measured as the maximum number of nodes on a root-to-leaf path.

**Return value**

- The sum of the binary integers represented by all root-to-leaf paths.

### Examples

**Example 1**

- Input: `root = [1, 0, 1, 0, 1, 0, 1]`
- Output: `22`
- Explanation: The paths represent `100`, `101`, `110`, and `111`, whose values sum to `22`.

**Example 2**

- Input: `root = [0]`
- Output: `0`

**Example 3**

- Input: `root = [1, 1]`
- Output: `3`
- Explanation: The only path represents binary `11`.
