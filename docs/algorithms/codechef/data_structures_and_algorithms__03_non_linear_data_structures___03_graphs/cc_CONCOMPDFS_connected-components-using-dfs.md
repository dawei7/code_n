# Connected Components - using DFS

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CONCOMPDFS |
| Difficulty Band | Graphs |
| Path | Data Structures and Algorithms |
| Lesson | Connectivity and Cycles in Graphs |
| Official Link | [CONCOMPDFS](https://www.codechef.com/learn/course/graphs/GRAPHCOMP/problems/CONCOMPDFS) |

---

## Problem Statement

We can find the number of connected components in a graph using the Depth-First Search (DFS) traversal algorithm.

Here's a simple pseudocode for finding the number of connected components using DFS in an undirected graph (same algorithm can be used for directed graphs as well):

```plaintext
procedure DFS(node, visited)
    mark node as visited
    for each neighbor in neighbors of node
        if neighbor is not visited
            DFS(neighbor, visited)

procedure FindConnectedComponents(graph)
    initialize connected components counter with 0

    for each node in graph
        if node is not visited
            DFS(node, visited)
            increment connected components counter by 1

    return connected components counter
```

Explanation:

- The `DFS` procedure recursively explores the graph starting from a given node. It marks each visited node . It then continues the exploration to its neighbors.

- The `FindConnectedComponents` procedure initializes a counter variable to 0 which stores the count of connected components. It iterates through each node in the graph. If the node is not visited, it calls the `DFS` procedure to explore all nodes in that component and increment the connected component counter by 1.

### Task
- Implement the above given algorithm to find out the no. of connected components in given undirected graph.
- Just output the count of connected component, not the actual nodes in each components.

---

## Input Format

- The first line consists of two space separated integers, `N` and `M`, representing the number of nodes and edges.
- Nodes are numbered from `1` to `N`.
- The subsequent `M` lines describe the connections, each containing two integers, `u` and `v`, describing the bidirectional edges.
- Each edge links two distinct nodes, and at most one edge exists between any two nodes.

---

## Output Format

- Output the number of connected components in the given graph.

---

## Constraints

- $1 \leq N \leq 200000$
- $1 \leq M \leq N(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.

---

## Examples

**Example 1**

**Input**

```text
5 6
1 2
2 3
1 3
3 5
2 4
4 5
```

**Output**

```text
1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Graph Traversal Algorithms like DFS or BFS

**Problem:** Find the Number of Connected Components in an Undirected Graph

**Solution Approach:** This problem can be solved by either using DFS or BFS algorithm (DFS in our solution). The approach is to traverse the graph and mark the vertices belonging to each connected component. The algorithm iterates through all vertices, applying DFS to each unvisited vertex, and increments the count of connected components.

**Time complexity:** O(V + E) where V is no. of vertices and E is no. of edges. Mainly because we’re using DFS under the hood.

**Space complexity:** O(V) as we need an extra boolean array to store the visited/unvisited states of each vertices.

</details>
