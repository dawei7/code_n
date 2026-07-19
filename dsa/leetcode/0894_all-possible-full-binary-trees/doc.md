# All Possible Full Binary Trees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 894 |
| Difficulty | Medium |
| Topics | Dynamic Programming, Tree, Recursion, Memoization, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/all-possible-full-binary-trees/) |

## Problem Description
### Goal
A full binary tree is a binary tree in which every node has either exactly zero children or exactly two children. Every node in this problem must store the value `0`.

Given `n`, construct all structurally distinct full binary trees containing exactly `n` nodes. Return a list of their root nodes in any order. Each returned root represents one possible tree shape; when no full binary tree can contain `n` nodes, return an empty list.

### Function Contract
Let $F(n)$ be the number of full binary tree shapes with $n$ nodes. For odd $n=2m+1$,

$$
F(n)=\frac{1}{m+1}\binom{2m}{m},
$$

and $F(n)=0$ for even $n$.

**Inputs**

- `n`: the required number of nodes, where $1 \leq n \leq 20$.

**Return value**

Return the roots of all $F(n)$ structurally distinct full binary trees with `n` nodes and value `0` at every node; the root-list order is unrestricted.

### Examples
**Example 1**

- Input: `n = 7`
- Output: `[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]`

**Example 2**

- Input: `n = 3`
- Output: `[[0,0,0]]`

**Example 3**

- Input: `n = 2`
- Output: `[]`

A full binary tree always has an odd number of nodes.
