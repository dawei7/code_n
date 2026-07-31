# Extract Kth Character From The Rope Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2689 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/) |

## Problem Description

### Goal

A rope binary tree represents a string without requiring every internal node to store the complete concatenation. Each node has ordinary `left` and `right` children plus a string `val` and a nonnegative integer `len`.

A leaf has no children, has `len = 0`, and stores a non-empty lowercase string in `val`. An internal node has at least one child, stores an empty string in `val`, and has a positive `len` equal to the length of the complete string represented by its subtree. The string of an internal node is the string of its left subtree followed by the string of its right subtree; a missing child contributes an empty string.

Given the rope root and a valid one-based position `k`, return the $k$-th character of the represented root string.

### Function Contract

**Inputs**

- `root`: The root `RopeTreeNode`. Each node exposes `len`, `val`, `left`, and `right`; each child is another `RopeTreeNode` or `None`. The app judge constructs this node tree from the nested object shown in a case input. The tree has at most $10^3$ nodes, leaf strings have lengths from 1 through 50, and internal lengths are at most $10^4$.
- `k`: A one-based character position satisfying $1 \le k \le \lvert S[\texttt{root}]\rvert$.

**Return value**

Return the single lowercase character at one-based position `k` in the rope's represented string.

### Examples

**Example 1**

- Input: A root of length `10` whose left subtree represents `"grta"` and whose right leaf is `"abcpoe"`, with `k = 6`.
- Output: `"b"`
- Explanation: The rope represents `"grtaabcpoe"`; its sixth character is `"b"`.

**Example 2**

- Input: A length-`12` root joining `"abcefg"` and `"hijklm"`, with `k = 3`.
- Output: `"c"`

**Example 3**

- Input: A single leaf containing `"ropetree"`, with `k = 8`.
- Output: `"e"`
