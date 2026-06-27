# Check if DFS Strings Are Palindromes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3327 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, Tree, Depth-First Search, Hash Function |
| Official Link | [check-if-dfs-strings-are-palindromes](https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/) |

## Problem Description & Examples
### Goal
Given a tree represented by parent pointers and a string of characters associated with each node, determine for every node whether the string formed by the DFS traversal of its subtree is a palindrome. The DFS traversal order is defined by visiting children in increasing order of their indices.

### Function Contract
**Inputs**

- `parent`: A list of integers where `parent[i]` is the parent of node `i` (root is 0 with `parent[0] = -1`).
- `s`: A string where `s[i]` is the character at node `i`.

**Return value**

- A list of booleans of length `n`, where the `i`-th element is `True` if the DFS string of the subtree rooted at `i` is a palindrome, and `False` otherwise.

### Examples
**Example 1**

- Input: `parent = [-1, 0, 0, 1, 1, 2, 2], s = "aabcbab"`
- Output: `[true, true, true, true, true, true, true]`

**Example 2**

- Input: `parent = [-1, 0, 0, 1, 1, 2, 2], s = "abcdeff"`
- Output: `[false, false, false, true, true, true, true]`

**Example 3**

- Input: `parent = [-1, 0], s = "ab"`
- Output: `[false, true]`

---

## Underlying Base Algorithm(s)
The problem is solved using a combination of DFS traversal to determine subtree ranges (entry and exit times) and Rolling Hashing to verify palindromic properties in constant time. By mapping the tree to a linear array via DFS entry/exit times, the subtree of any node becomes a contiguous segment. We maintain prefix and suffix hashes of the DFS string to check if the segment is equal to its reverse.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of nodes. We perform a single DFS to compute entry/exit times and subtree sizes, and another pass to compute hashes.
- **Space Complexity**: `O(n)` to store the adjacency list, entry/exit arrays, and hash tables.
