# K-th Largest Perfect Subtree Size in Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3319 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Sorting, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/) |

## Problem Description

### Goal

Given the root of a binary tree, consider every node as the root of its own subtree. A perfect binary tree has two children at every internal node and places every leaf at the same depth. Single leaves therefore count as perfect subtrees of size one.

Collect the node counts of all perfect subtrees, preserving duplicates from different subtree roots, and order those sizes from largest to smallest. Return the $k$th entry in that ordering. If the tree contains fewer than $k$ perfect subtrees, return `-1`.

### Function Contract

**Inputs**

- `root`: The root of a nonempty binary tree containing between 1 and 2000 nodes; every node value lies in $[1,2000]$.
- `k`: A one-based rank, where $1\leq k\leq1024$.

**Return value**

Return the size of the $k$th largest perfect subtree, counting equal sizes separately, or `-1` when that rank does not exist.

### Examples

#### Example 1

- **Input:** `root = [5, 3, 6, 5, 2, 5, 7, 1, 8, null, null, 6, 8], k = 2`
- **Output:** `3`

The perfect-subtree sizes in non-increasing order begin `[3, 3, 1, 1, 1, 1, 1, 1]`.

#### Example 2

- **Input:** `root = [1, 2, 3, 4, 5, 6, 7], k = 1`
- **Output:** `7`

The entire tree is perfect and is the largest qualifying subtree.

#### Example 3

- **Input:** `root = [1, 2, 3, null, 4], k = 3`
- **Output:** `-1`

Only the two leaves form perfect subtrees, so a third size does not exist.
