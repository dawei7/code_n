# Minimum Flips in Binary Tree to Get Result

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2313 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/) |

## Problem Description

### Goal

A binary tree encodes a Boolean expression. Every leaf is `0` or `1`, representing false or true. Every internal node is an operator: `2` means OR, `3` means AND, `4` means XOR, and `5` means NOT. OR, AND, and XOR nodes have two children; a NOT node has exactly one child, which may be on either side.

Evaluating a leaf yields its Boolean value. Evaluating an internal node first evaluates its child subtrees and then applies the encoded operator. In one operation, you may flip a leaf between `0` and `1`. Given a desired Boolean `result`, return the fewest leaf flips that make the root evaluate to that value. A solution is always possible.

### Function Contract

**Inputs**

- `root`: The root of a nonempty encoded expression tree containing between $1$ and $10^5$ nodes.
- `result`: The Boolean value that the root must produce after the flips.

Leaves have values `0` or `1`. Internal nodes have values from `2` through `5` and have the child counts required by their operators.

**Return value**

Return the minimum number of leaf values that must be flipped so the complete tree evaluates to `result`.

### Examples

#### Example 1

- **Input:** `root = [3,5,4,2,null,1,1,1,0], result = true`
- **Output:** `2`

At least two leaves must change for the AND expression at the root to become true.

#### Example 2

- **Input:** `root = [0], result = false`
- **Output:** `0`

The single leaf already has the desired value.
