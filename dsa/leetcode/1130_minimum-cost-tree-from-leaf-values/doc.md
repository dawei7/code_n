# Minimum Cost Tree From Leaf Values

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1130 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Stack, Greedy, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/) |

## Problem Description

### Goal

Given an array `arr` of positive integers, consider every binary tree in which each node has either zero or two children and the leaf values encountered by an in-order traversal are exactly the values of `arr` in their given order. A node is a leaf if and only if it has no children.

For every non-leaf node, its value is the product of the largest leaf value in its left subtree and the largest leaf value in its right subtree. Among all trees satisfying these rules, return the smallest possible sum of all non-leaf node values. The answer is guaranteed to fit in a signed 32-bit integer.

### Function Contract

**Inputs**

- `arr`: an array of $n$ positive leaf values, where $2 \le n \le 40$ and $1 \le \texttt{arr[i]} \le 15$.

**Return value**

The minimum possible sum of the non-leaf node values over all valid full binary trees whose in-order leaf sequence is `arr`.

### Examples

**Example 1**

- Input: `arr = [6,2,4]`
- Output: `32`
- Explanation: The lower-cost tree has internal values `8` and `24`, whose sum is `32`; the other possible grouping costs `36`.

**Example 2**

- Input: `arr = [4,11]`
- Output: `44`
