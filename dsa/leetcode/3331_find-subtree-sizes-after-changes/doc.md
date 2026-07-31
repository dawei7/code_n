# Find Subtree Sizes After Changes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3331 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-subtree-sizes-after-changes/) |

## Problem Description

### Goal

You are given a rooted tree with nodes numbered from $0$ to $n-1$. The array `parent` describes its original edges: node $0$ is the root with `parent[0] = -1`, and `parent[x]` is the parent of every other node $x$. The string `s` assigns the character `s[x]` to node $x$.

Change the tree simultaneously for every non-root node. For a node $x$, inspect only its ancestors in the original tree and find the closest ancestor $y$ for which `s[x] == s[y]`. If such an ancestor exists, make $y$ the new parent of $x$; otherwise, retain `parent[x]`. Because all changes are simultaneous, a parent changed for one node cannot affect another node's ancestor search. Return the subtree size of every node after all new parent relationships have taken effect.

### Function Contract

**Inputs**

- `parent`: A list of $n$ integers describing a valid rooted tree, where `parent[0] = -1` and $1 \le n \le 10^5$.
- `s`: A lowercase English string of length $n$ whose character at index $x$ labels node $x$.

**Return value**

- A list `answer` of length $n$ where `answer[x]` is the number of nodes in the subtree rooted at $x$ after the simultaneous changes.

### Examples

**Example 1**

- Input: `parent = [-1, 0, 0, 1, 1, 1], s = "abaabc"`
- Output: `[6, 3, 1, 1, 1, 1]`
- Explanation: Node $3$ moves from node $1$ to node $0$, its closest original ancestor carrying `a`.

**Example 2**

- Input: `parent = [-1, 0, 4, 0, 1], s = "abbba"`
- Output: `[5, 2, 1, 1, 1]`
- Explanation: Node $4$ moves to node $0$, while node $2$ moves to node $1$ by following the original ancestry through node $4$.
