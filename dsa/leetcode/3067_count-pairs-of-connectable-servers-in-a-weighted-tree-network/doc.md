# Count Pairs of Connectable Servers in a Weighted Tree Network

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3067 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/) |

## Problem Description

### Goal

An unrooted weighted tree models a network of $n$ servers numbered from $0$ through $n-1$. Each entry `edges[i] = [a_i, b_i, weight_i]` describes a bidirectional connection between servers `a_i` and `b_i` whose weight contributes to the distance along any path using that edge. You are also given an integer `signalSpeed`.

Two distinct servers `a` and `b` are connectable through a server `c` when $a < b$, neither endpoint equals `c`, and both distances from `c` are divisible by `signalSpeed`. In addition, the path from `c` to `a` and the path from `c` to `b` must share no edge.

Return an integer array `count` of length $n$ where `count[c]` is the number of server pairs connectable through server `c`.

### Function Contract

**Inputs**

- `edges`: The $n-1$ weighted edges of a valid undirected tree, with each edge represented as `[a_i, b_i, weight_i]`.
- `signalSpeed`: The positive divisor used to test path distances.

The constraints are $2 \le n \le 1000$, $0 \le a_i, b_i < n$, $1 \le \texttt{weight_i} \le 10^6$, and $1 \le \texttt{signalSpeed} \le 10^6$.

**Return value**

Return `count`, where `count[c]` is the number of unordered endpoint pairs satisfying all connectability conditions through `c`.

### Examples

#### Example 1

- **Input:** `edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]], signalSpeed = 1`
- **Output:** `[0,4,6,6,4,0]`
- **Explanation:** Every distance is divisible by `1`. In this path, choosing `c` separates the possible endpoints into the servers on its two sides, so their count is the product of the two side lengths.

#### Example 2

- **Input:** `edges = [[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]], signalSpeed = 3`
- **Output:** `[2,0,0,0,0,0,2]`
- **Explanation:** Pairs `(4, 5)` and `(4, 6)` qualify through server `0`; pairs `(4, 5)` and `(0, 5)` qualify through server `6`. No pair qualifies through another server.
