# Is Array a Preorder of Some Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2764 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Stack, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Is Array a Preorder of Some Binary Tree](https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/) |

## Problem Description

### Goal

You are given a 0-indexed two-dimensional integer array `nodes`. Each entry `nodes[i] = [id, parentId]` describes the node appearing at index $i$: `id` is that node's identifier, and `parentId` identifies its parent. The unique root has no parent and therefore uses `parentId = -1`. The supplied pairs are guaranteed to describe a binary tree.

Determine whether the entries occur in a preorder traversal of some orientation of that tree. A preorder traversal visits the current node first, then traverses one child subtree completely, and finally traverses the other child subtree. Return whether the given ordering can follow those rules.

### Function Contract

**Inputs**

- `nodes`: An array of $n$ node-parent pairs, where $1 \leq n \leq 10^5$, every pair has length $2$, $0 \leq \texttt{id} \leq 10^5$, and $-1 \leq \texttt{parentId} \leq 10^5$. The pairs collectively form a binary tree.

**Return value**

Return `true` if the array can be the preorder traversal of that tree; otherwise, return `false`.

### Examples

#### Example 1

- **Input:** `nodes = [[0,-1],[1,0],[2,0],[3,2],[4,2]]`
- **Output:** `true`
- **Explanation:** After visiting node `0`, the traversal may finish the singleton subtree rooted at `1`, then traverse the subtree rooted at `2` as `[2,3,4]`.

#### Example 2

- **Input:** `nodes = [[0,-1],[1,0],[2,0],[3,1],[4,1]]`
- **Output:** `false`
- **Explanation:** Visiting node `2` closes the unfinished subtree rooted at `1`; nodes `3` and `4` cannot later return to `1` in a preorder traversal.
