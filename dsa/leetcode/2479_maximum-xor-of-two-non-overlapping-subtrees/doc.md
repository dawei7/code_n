# Maximum XOR of Two Non-Overlapping Subtrees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2479 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Graph Theory, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/) |

## Problem Description

### Goal

An undirected tree contains `n` nodes numbered from `0` through `n - 1` and is rooted at node `0`. The array `edges` gives its `n - 1` connections, and `values[i]` is the positive integer value assigned to node `i`.

For any node, its subtree contains that node and every descendant determined by the root. Choose two subtrees that share no node. Their score is the bitwise XOR of their two value sums.

Return the maximum achievable score. If the rooted tree has no pair of non-overlapping subtrees, return `0`.

### Function Contract

**Inputs**

- `n`: The number of nodes in the tree.
- `edges`: The undirected edges, where each `[a, b]` connects nodes `a` and `b`.
- `values`: The positive node values, with `values[i]` belonging to node `i`.

The constraints satisfy $2 \le n \le 5 \cdot 10^4$, `edges` describes a valid tree, and $1 \le \texttt{values[i]} \le 10^9$.

Define the total value

$$
S = \sum_{i=0}^{n-1} \texttt{values[i]}.
$$

**Return value**

Return an integer: the maximum XOR of the sums of two non-overlapping subtrees, or `0` when no such pair exists.

### Examples

#### Example 1

- **Input:** `n = 6, edges = [[0,1],[0,2],[1,3],[1,4],[2,5]], values = [2,8,3,6,2,5]`
- **Output:** `24`
- **Explanation:** The subtrees rooted at nodes `1` and `2` have sums $16$ and $8$, so their score is $16 \mathbin{\mathrm{XOR}} 8 = 24$.

#### Example 2

- **Input:** `n = 3, edges = [[0,1],[1,2]], values = [4,6,1]`
- **Output:** `0`
- **Explanation:** Every two subtrees in this rooted chain overlap.

#### Example 3

- **Input:** `n = 3, edges = [[0,1],[0,2]], values = [1,2,4]`
- **Output:** `6`
- **Explanation:** The two leaf subtrees are disjoint and have score $2 \mathbin{\mathrm{XOR}} 4 = 6$.
