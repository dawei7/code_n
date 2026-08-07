### 1. Description

You are given a positive integer `n` representing the number of nodes in a tree, numbered from `0` to $n - 1$ (**inclusive**). You are also given a 2D integer array `edges` of length $n - 1$, where $\text{edges}[i] = [\text{node1}_{i}, \text{node2}_{i}]$ denotes that there is a **bidirectional** edge connecting $\text{node1}_{i}$ and $\text{node2}_{i}$ in the tree.

You are given a **0-indexed** integer array `query` of length `m` where $\text{query}[i] = [\text{start}_{i}, \text{end}_{i}, \text{node}_{i}]$ means that for the $$i^{\text{th}}$$ query, you are tasked with finding the node on the path from $\text{start}_{i}$ to $\text{end}_{i}$ that is **closest** to $\text{node}_{i}$.

Return *an integer array *`answer`* of length *`m`*, where *$\text{answer}[i]$* is the answer to the *$$i^{\text{th}}$$* query*.

### 2. Function Contract

**Inputs**

- `n`: The number of nodes in the tree ($1 \le n \le 1000$).
- `edges`: A list of $n-1$ pairs `[u, v]` representing undirected tree edges.
- `query`: A list of queries `[start, end, node]`, where $1 \le \text{query.length} \le 1000$.

**Return value**

Return a list of integers of length $\text{query.length}$, where the $i$-th element is the node on the simple path between `start` and `end` closest to `node` for query $i$.

### 3. Examples

#### Example 1

![](images/image-20220514132158-1.png)

- **Input:** $n = 7, edges = [[0,1],[0,2],[0,3],[1,4],[2,5],[2,6]], query = [[5,3,4],[5,3,6]]$
- **Output:** `[0,2]`
- **Explanation:**
The path from node 5 to node 3 consists of the nodes 5, 2, 0, and 3.
The distance between node 4 and node 0 is 2.
Node 0 is the node on the path closest to node 4, so the answer to the first query is 0.
The distance between node 6 and node 2 is 1.
Node 2 is the node on the path closest to node 6, so the answer to the second query is 2.
#### Example 2

![](images/image-20220514132318-2.png)

- **Input:** $n = 3, edges = [[0,1],[1,2]], query = [[0,1,2]]$
- **Output:** `[1]`
- **Explanation:**
The path from node 0 to node 1 consists of the nodes 0, 1.
The distance between node 2 and node 1 is 1.
Node 1 is the node on the path closest to node 2, so the answer to the first query is 1.
#### Example 3

![](images/image-20220514132333-3.png)

- **Input:** $n = 3, edges = [[0,1],[1,2]], query = [[0,0,0]]$
- **Output:** `[0]`
- **Explanation:**
The path from node 0 to node 0 consists of the node 0.
Since 0 is the only node on the path, the answer to the first query is 0.

### 4. Constraints

- $1 \le n \le 1000$

- $\text{edges.length} = n - 1$

- $\text{edges}[i].length = 2$

- $0 \le \text{node1}_{i}, \text{node2}_{i} \le n - 1$

- $\text{node1}_{i} \neq \text{node2}_{i}$

- $1 \le \text{query.length} \le 1000$

- $\text{query}[i].length = 3$

- $0 \le \text{start}_{i}, \text{end}_{i}, \text{node}_{i} \le n - 1$

- The graph is a tree.