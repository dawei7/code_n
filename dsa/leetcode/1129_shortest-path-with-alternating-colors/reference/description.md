## Description

You are given an integer `n`, the number of nodes in a directed graph where the nodes are labeled from `0` to $n - 1$. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays `redEdges` and `blueEdges` where:

- $\text{redEdges}[i] = [a_{i}, b_{i}]$ indicates that there is a directed red edge from node $a_{i}$ to node $b_{i}$ in the graph, and

- $\text{blueEdges}[j] = [u_{j}, v_{j}]$ indicates that there is a directed blue edge from node $u_{j}$ to node $v_{j}$ in the graph.

Return an array `answer` of length `n`, where each $\text{answer}[x]$ is the length of the shortest path from node `0` to node `x` such that the edge colors alternate along the path, or `-1` if such a path does not exist.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $n = 3, redEdges = [[0,1],[1,2]], blueEdges = []$
- **Output:** `[0,1,-1]`
#### Example 2

- **Input:** $n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]$
- **Output:** `[0,1,-1]`
### Constraints

- $1 \le n \le 100$

- $0 \le \text{redEdges.length}, \text{blueEdges.length} \le 400$

- $\text{redEdges}[i].length = \text{blueEdges}[j].length = 2$

- $0 \le a_{i}, b_{i}, u_{j}, v_{j} < n$