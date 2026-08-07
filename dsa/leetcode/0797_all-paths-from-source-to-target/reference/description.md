### 1. Description

Given a directed acyclic graph (**DAG**) of `n` nodes labeled from `0` to $n - 1$, find all possible paths from node `0` to node $n - 1$ and return them in **any order**.

The graph is given as follows: $\text{graph}[i]$ is a list of all nodes you can visit from node `i` (i.e., there is a directed edge from node `i` to node $\text{graph}[i][j]$).

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

![](images/all_1.jpg)

- **Input:** $graph = [[1,2],[3],[3],[]]$
- **Output:** `[[0,1,3],[0,2,3]]`
- **Explanation:** There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
#### Example 2

![](images/all_2.jpg)

- **Input:** $graph = [[4,3,1],[3,2,4],[3],[4],[]]$
- **Output:** `[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]`

### 4. Constraints

- $n = \text{graph.length}$

- $2 \le n \le 15$

- $0 \le \text{graph}[i][j] < n$

- $\text{graph}[i][j] \neq i$ (i.e., there will be no self-loops).

- All the elements of $\text{graph}[i]$ are **unique**.

- The input graph is **guaranteed** to be a **DAG**.