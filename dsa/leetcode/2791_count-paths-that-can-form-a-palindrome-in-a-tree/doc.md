# Count Paths That Can Form a Palindrome in a Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2791 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, Bit Manipulation, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/) |

## Problem Description

### Goal

A connected, undirected tree with $n$ nodes is rooted at node $0$. The 0-indexed array `parent` describes its rooted edges: `parent[i]` is the parent of node $i$, and the root has `parent[0] = -1`.

The string `s` also has length $n$. For every non-root node $i$, `s[i]` labels the edge joining $i$ to `parent[i]`; `s[0]` has no edge and must be ignored. Count pairs of distinct nodes $(u,v)$ with $u < v$ for which the edge-label characters along their unique path can be rearranged into a palindrome.

### Function Contract

**Inputs**

- `parent`: A length-$n$ parent array describing a valid tree rooted at node $0$, where `parent[0] = -1` and $0 \le \texttt{parent[i]} < n$ for every $i \ge 1$.
- `s`: A length-$n$ string of lowercase English letters. Character `s[i]` labels the edge from node $i$ to its parent for $i \ge 1$; `s[0]` is ignored.

The shared size satisfies $1 \le n \le 10^5$.

**Return value**

Return the number of node pairs $(u,v)$ with $u < v$ whose path-label multiset can be reordered into a palindrome.

### Examples

**Example 1**

- Input: `parent = [-1, 0, 0, 1, 1, 2], s = "acaabc"`
- Output: `8`
- Explanation: Five parent-child paths are valid immediately, and three longer paths have character parities that permit a palindromic arrangement.

**Example 2**

- Input: `parent = [-1, 0, 0, 0, 0], s = "aaaaa"`
- Output: `10`
- Explanation: Every one of the $\binom{5}{2}=10$ node pairs has a path containing only the letter `a`, so every pair is valid.
