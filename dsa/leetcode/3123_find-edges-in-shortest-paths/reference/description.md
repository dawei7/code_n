## Description

You are given an undirected weighted graph of `n` nodes numbered from 0 to $n - 1$. The graph consists of `m` edges represented by a 2D array `edges`, where $\text{edges}[i] = [a_{i}, b_{i}, w_{i}]$ indicates that there is an edge between nodes $a_{i}$ and $b_{i}$ with weight $w_{i}$.

Consider all the shortest paths from node 0 to node $n - 1$ in the graph. You need to find a **boolean** array `answer` where $\text{answer}[i]$ is `true` if the edge $\text{edges}[i]$ is part of **at least** one shortest path. Otherwise, $\text{answer}[i]$ is `false`.

Return the array `answer`.

**Note** that the graph may not be connected.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

![](images/graph35drawio-1.png)

<div class="example-block">
**Input:** n = 6, edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]

**Output:** [true,true,true,false,true,true,true,false]

**Explanation:**

The following are **all** the shortest paths between nodes 0 and 5:

- The path `0 -> 1 -> 5`: The sum of weights is $4 + 1 = 5$.

- The path `0 -> 2 -> 3 -> 5`: The sum of weights is $1 + 1 + 3 = 5$.

- The path `0 -> 2 -> 3 -> 1 -> 5`: The sum of weights is $1 + 1 + 2 + 1 = 5$.

</div>
#### Example 2

![](images/graphhhh.png)

<div class="example-block">
**Input:** n = 4, edges = [[2,0,1],[0,1,1],[0,3,4],[3,2,2]]

**Output:** [true,false,false,true]

**Explanation:**

There is one shortest path between nodes 0 and 3, which is the path `0 -> 2 -> 3` with the sum of weights $1 + 2 = 3$.

</div>
### Constraints

- $2 \le n \le 5 * 10^{4}$

- $m = \text{edges.length}$

- $1 \le m \le min(5 * 10^{4}, n * (n - 1) / 2)$

- $0 \le a_{i}, b_{i} < n$

- $a_{i} \neq b_{i}$

- $1 \le w_{i} \le 10^{5}$

- There are no repeated edges.