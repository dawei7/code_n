### 1. Description

There exist two **undirected **trees with `n` and `m` nodes, with **distinct** labels in ranges `[0, n - 1]` and `[0, m - 1]`, respectively.

You are given two 2D integer arrays `edges1` and `edges2` of lengths $n - 1$ and $m - 1$, respectively, where $\text{edges1}[i] = [a_{i}, b_{i}]$ indicates that there is an edge between nodes $a_{i}$ and $b_{i}$ in the first tree and $\text{edges2}[i] = [u_{i}, v_{i}]$ indicates that there is an edge between nodes $u_{i}$ and $v_{i}$ in the second tree. You are also given an integer `k`.

Node `u` is **target** to node `v` if the number of edges on the path from `u` to `v` is less than or equal to `k`. **Note** that a node is *always* **target** to itself.

Return an array of `n` integers `answer`, where $\text{answer}[i]$ is the **maximum** possible number of nodes **target** to node `i` of the first tree if you have to connect one node from the first tree to another node in the second tree.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

### 4. Examples

#### Example 1

<div class="example-block">
**Input:** edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2

**Output:** [9,7,9,8,8]

**Explanation:**

- For $i = 0$, connect node 0 from the first tree to node 0 from the second tree.

- For $i = 1$, connect node 1 from the first tree to node 0 from the second tree.

- For $i = 2$, connect node 2 from the first tree to node 4 from the second tree.

- For $i = 3$, connect node 3 from the first tree to node 4 from the second tree.

- For $i = 4$, connect node 4 from the first tree to node 4 from the second tree.

![](images/3982-1.png)

</div>
#### Example 2

<div class="example-block">
**Input:** edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1

**Output:** [6,3,3,3,3]

**Explanation:**

For every `i`, connect node `i` of the first tree with any node of the second tree.

![](images/3928-2.png)

</div>

### 5. Constraints

- $2 \le n, m \le 1000$

- $\text{edges1.length} = n - 1$

- $\text{edges2.length} = m - 1$

- $\text{edges1}[i].length = \text{edges2}[i].length = 2$

- $\text{edges1}[i] = [a_{i}, b_{i}]$

- $0 \le a_{i}, b_{i} < n$

- $\text{edges2}[i] = [u_{i}, v_{i}]$

- $0 \le u_{i}, v_{i} < m$

- The input is generated such that `edges1` and `edges2` represent valid trees.

- $0 \le k \le 1000$