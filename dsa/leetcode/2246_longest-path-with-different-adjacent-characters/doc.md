# Longest Path With Different Adjacent Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2246 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Tree, Depth-First Search, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-path-with-different-adjacent-characters](https://leetcode.com/problems/longest-path-with-different-adjacent-characters/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-path-with-different-adjacent-characters/).

### Goal
Find the longest path in a rooted tree such that every adjacent pair of nodes has different assigned characters. The path may begin and end anywhere.

### Function Contract
**Inputs**

- `parent`: parent indices, with `parent[0] = -1` for the root.
- `s`: node characters, where `s[i]` belongs to node `i`.

**Return value**

The maximum number of nodes on a valid path.

### Examples
**Example 1**

- Input: `parent = [-1, 0, 0, 1, 1, 2]`, `s = "abacbe"`
- Output: `3`

**Example 2**

- Input: `parent = [-1, 0, 0, 0]`, `s = "aabc"`
- Output: `3`

**Example 3**

- Input: `parent = [-1, 0, 1, 2]`, `s = "abcd"`
- Output: `4`

---

## Solution
### Approach
Build child lists and run postorder depth-first search. For each node, obtain the longest downward valid chain from every child whose character differs, keep the two largest, and combine them through the node for a path candidate. Return the largest chain plus the node to the parent while tracking the global best combined path.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
