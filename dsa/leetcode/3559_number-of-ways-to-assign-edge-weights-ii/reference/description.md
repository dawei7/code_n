### 1. Description

There is an undirected tree with `n` nodes labeled from 1 to `n`, rooted at node 1. The tree is represented by a 2D integer array `edges` of length $n - 1$, where $\text{edges}[i] = [u_{i}, v_{i}]$ indicates that there is an edge between nodes $u_{i}$ and $v_{i}$.

Initially, all edges have a weight of 0. You must assign each edge a weight of either **1** or **2**.

The **cost** of a path between any two nodes `u` and `v` is the total weight of all edges in the path connecting them.

You are given a 2D integer array `queries`. For each $\text{queries}[i] = [u_{i}, v_{i}]$, determine the number of ways to assign weights to edges **in the path** such that the cost of the path between $u_{i}$ and $v_{i}$ is **odd**.

Return an array `answer`, where $\text{answer}[i]$ is the number of valid assignments for $\text{queries}[i]$.

Since the answer may be large, apply **modulo** $10^{9} + 7$ to each $\text{answer}[i]$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

For each query, disregard all edges **not** in the path between node $u_{i}$ and $v_{i}$.

### 4. Examples

#### Example 1

<div class="example-block">

![](images/screenshot-2025-03-24-at-060006.png)

**Input:** edges = [[1,2]], queries = [[1,1],[1,2]]

**Output:** [0,1]

**Explanation:**

- Query `[1,1]`: The path from Node 1 to itself consists of no edges, so the cost is 0. Thus, the number of valid assignments is 0.

- Query `[1,2]`: The path from Node 1 to Node 2 consists of one edge (`1 → 2`). Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.

</div>
#### Example 2

![](images/screenshot-2025-03-24-at-055820.png)

<div class="example-block">
**Input:** edges = [[1,2],[1,3],[3,4],[3,5]], queries = [[1,4],[3,4],[2,5]]

**Output:** [2,1,4]

**Explanation:**

- Query `[1,4]`: The path from Node 1 to Node 4 consists of two edges (`1 → 3` and `3 → 4`). Assigning weights (1,2) or (2,1) results in an odd cost. Thus, the number of valid assignments is 2.

- Query `[3,4]`: The path from Node 3 to Node 4 consists of one edge (`3 → 4`). Assigning weight 1 makes the cost odd, while 2 makes it even. Thus, the number of valid assignments is 1.

- Query `[2,5]`: The path from Node 2 to Node 5 consists of three edges (`2 → 1, 1 → 3`, and `3 → 5`). Assigning (1,2,2), (2,1,2), (2,2,1), or (1,1,1) makes the cost odd. Thus, the number of valid assignments is 4.

</div>

### 5. Constraints

- $2 \le n \le 10^{5}$

- $\text{edges.length} = n - 1$

- $\text{edges}[i] = [u_{i}, v_{i}]$

- $1 \le \text{queries.length} \le 10^{5}$

- $\text{queries}[i] = [u_{i}, v_{i}]$

- $1 \le u_{i}, v_{i} \le n$

- `edges` represents a valid tree.