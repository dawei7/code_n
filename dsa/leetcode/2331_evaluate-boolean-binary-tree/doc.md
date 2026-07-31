# Evaluate Boolean Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2331 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/evaluate-boolean-binary-tree/) |

## Problem Description

### Goal

Evaluate a full binary tree whose values encode booleans and binary boolean
operators. Every leaf stores `0` for false or `1` for true. Every non-leaf
stores `2` for boolean OR or `3` for boolean AND, and has exactly two
children.

A leaf evaluates directly to its represented boolean. An operator node first
evaluates both child subtrees, then applies its encoded operator to those two
results. Return the boolean produced at the root. A full binary tree has
either zero or two children at every node.

### Function Contract

**Inputs**

- `root`: The root of a nonempty full binary tree containing between 1 and
  1000 nodes. Leaves contain `0` or `1`; internal nodes contain `2` or `3`.

**Return value**

The boolean result obtained by recursively evaluating the encoded expression
at `root`.

### Examples

**Example 1**

- Input: `root = [2,1,3,null,null,0,1]`
- Output: `true`
- Explanation: The right AND subtree is false, and the root computes
  `true OR false`.

**Example 2**

- Input: `root = [0]`
- Output: `false`
- Explanation: A leaf evaluates directly to the boolean encoded by its value.

**Example 3**

- Input: `root = [3,1,1]`
- Output: `true`
- Explanation: Both children of the AND root evaluate to true.
