# Longest Palindromic Path in Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3615 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Bit Manipulation, Graph Theory, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-palindromic-path-in-graph/) |

## Problem Description

### Goal

An undirected graph has `n` nodes numbered from $0$ through $n-1`. Each pair `[u, v]` in `edges` connects two different nodes, and `label[i]` is the lowercase English letter assigned to node `i`.

Choose any starting node and follow adjacent edges to form a path, visiting every node at most once. Reading the labels in visitation order produces a string. Return the greatest possible number of nodes in a valid path whose label string is a palindrome. A path containing one node is always allowed and palindromic.

### Function Contract

**Inputs**

- `n`: The number of labeled graph nodes.
- `edges`: The undirected edges as distinct `[u, v]` pairs.
- `label`: A length-`n` string whose character at each index labels that node.

The constraints are $1 \le n \le 14$ and $n-1 \le \lvert\texttt{edges}\rvert \le n(n-1)/2$. Edges contain no self-loops or duplicates.

**Return value**

Return the maximum length of a simple graph path whose sequence of node labels reads the same forward and backward.

### Examples

#### Example 1

- **Input:** `n = 3, edges = [[0, 1], [1, 2]], label = "aba"`
- **Output:** `3`
- **Explanation:** Path `0 -> 1 -> 2` spells `"aba"`.

#### Example 2

- **Input:** `n = 3, edges = [[0, 1], [0, 2]], label = "abc"`
- **Output:** `1`
- **Explanation:** No adjacent pair has equal labels, so only a one-node palindrome is possible.

#### Example 3

- **Input:** `n = 4, edges = [[0, 2], [0, 3], [3, 1]], label = "bbac"`
- **Output:** `3`
- **Explanation:** Path `0 -> 3 -> 1` spells `"bcb"`.
