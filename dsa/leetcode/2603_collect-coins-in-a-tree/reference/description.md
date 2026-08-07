## Description

There exists an undirected and unrooted tree with `n` nodes indexed from `0` to $n - 1$. You are given an integer `n` and a 2D integer array edges of length $n - 1$, where $\text{edges}[i] = [a_{i}, b_{i}]$ indicates that there is an edge between nodes $a_{i}$ and $b_{i}$ in the tree. You are also given an array `coins` of size `n` where $\text{coins}[i]$ can be either `0` or `1`, where `1` indicates the presence of a coin in the vertex `i`.

Initially, you choose to start at any vertex in the tree. Then, you can perform the following operations any number of times:

- Collect all the coins that are at a distance of at most `2` from the current vertex, or

- Move to any adjacent vertex in the tree.

Find *the minimum number of edges you need to go through to collect all the coins and go back to the initial vertex*.

Note that if you pass an edge several times, you need to count it into the answer several times.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

![](images/graph-2.png)

- **Input:** $coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]$
- **Output:** `2`
- **Explanation:** Start at vertex 2, collect the coin at vertex 0, move to vertex 3, collect the coin at vertex 5 then move back to vertex 2.
#### Example 2

![](images/graph-4.png)

- **Input:** $coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]$
- **Output:** `2`
- **Explanation:** Start at vertex 0, collect the coins at vertices 4 and 3, move to vertex 2,  collect the coin at vertex 7, then move back to vertex 0.
### Constraints

- $n = \text{coins.length}$

- $1 \le n \le 3 * 10^{4}$

- $0 \le \text{coins}[i] \le 1$

- $\text{edges.length} = n - 1$

- $\text{edges}[i].length = 2$

- $0 \le a_{i}, b_{i} < n$

- $a_{i} \neq b_{i}$

- `edges` represents a valid tree.