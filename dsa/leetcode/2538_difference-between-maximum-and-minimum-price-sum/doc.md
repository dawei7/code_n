
# Difference Between Maximum and Minimum Price Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2538 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [difference-between-maximum-and-minimum-price-sum](https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/) |

## Problem Description

### Goal

An undirected, initially unrooted tree contains `n` nodes numbered from `0` through `n - 1`. Its `n - 1` edges are given by `edges`, and `price[i]` is the positive price attached to node `i`. The price sum of a path is the sum of every node price on that path.

Choose any node as `root`. Consider all paths that start at this root, including the one-node path. The cost of this choice is the maximum such path sum minus the minimum such path sum. Return the maximum cost obtainable over every possible choice of root.

### Function Contract

**Inputs**

- `n`: The positive number of nodes in the tree.
- `edges`: The `n - 1` undirected edges, each represented as `[first, second]`.
- `price`: The positive node prices, where `price[i]` belongs to node `i`.

The nodes are 0-indexed, `edges` forms a valid tree, and `price` has length `n`. The public constraints permit $n \leq 10^5$ and $1 \leq \texttt{price[i]} \leq 10^5$.

**Return value**

Return the maximum possible difference between the largest and smallest price sums of paths beginning at the chosen root.

### Examples

**Example 1**

- Input: `n = 6, edges = [[0,1],[1,2],[1,3],[3,4],[3,5]], price = [9,8,7,6,10,5]`
- Output: `24`
- Explanation: With node 2 as root, the path through nodes `[2,1,3,4]` sums to $31$, while the one-node root path sums to $7$. Their difference is $24$.

**Example 2**

- Input: `n = 3, edges = [[0,1],[1,2]], price = [1,1,1]`
- Output: `2`
- Explanation: Rooting at an endpoint gives path sums $1$ and $3$, producing cost $2$.
