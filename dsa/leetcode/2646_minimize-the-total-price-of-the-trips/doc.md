# Minimize the Total Price of the Trips

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2646 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Tree, Depth-First Search, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimize-the-total-price-of-the-trips/) |

## Problem Description

### Goal

An undirected tree contains $n$ nodes numbered from $0$ through $n-1$. Node $i$ has the even positive visit price `price[i]`. Each requested trip follows the tree's unique path between its endpoints, and its price is the sum of all node prices on that path.

Before any trips occur, you may choose a set of pairwise non-adjacent nodes and halve each chosen node's price. This one selection applies to every trip. Return the minimum possible sum of all trip prices after choosing the discounted nodes optimally.

### Function Contract

**Inputs**

- `n`: The node count, where $1 \le n \le 50$.
- `edges`: The $n-1$ undirected edges of a valid tree.
- `price`: An even-valued length-$n$ array with $1 \le \texttt{price[i]} \le 1000$.
- `trips`: A list of $t$ endpoint pairs, where $1 \le t \le 100$.

**Return value**

- Return the minimum total price of all trips after halving any independent set of nodes.

### Examples

**Example 1**

- Input: `n = 4`, `edges = [[0,1],[1,2],[1,3]]`, `price = [2,2,10,6]`, `trips = [[0,3],[2,1],[2,3]]`
- Output: `23`

**Example 2**

- Input: `n = 2`, `edges = [[0,1]]`, `price = [2,2]`, `trips = [[0,0]]`
- Output: `1`
