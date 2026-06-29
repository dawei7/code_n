# Cycle in Undirected Graph

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GCYCLEDFS |
| Difficulty Band | Graphs |
| Path | Data Structures and Algorithms |
| Lesson | Connectivity and Cycles in Graphs |
| Official Link | [GCYCLEDFS](https://www.codechef.com/learn/course/graphs/GRAPHCYCLE/problems/GCYCLEDFS) |

---

## Problem Statement

The key idea behind this cycle detection algorithm for an undirected graph is to use depth-first search (DFS) and track the parent of each node during the traversal. While exploring the neighbors of a node, if a neighbor is encountered that has been already visited but is not the parent of the current node, then there is a back edge, indicating the presence of a cycle in the graph. The algorithm iterates through all vertices, performing DFS from each unvisited vertex, and detects cycles if any during the process.

Here's a simplified pseudocode for finding cycles in an undirected graph using Depth-First Search (DFS):

```plaintext
Procedure DFS(node, parent):
    Mark node as visited
    For each neighbor in neighbors of node:
        If neighbor is not visited:
            If DFS(neighbor, node) returns true:
                Return true
        Else if neighbor is not equal to parent:
            Return true
    Return false

Procedure HasCycle(graphSize):
    Initialize visited array for all vertices, initially set to false

    For each vertex v from 1 to graphSize:
        If v is not visited and DFS(v, -1) returns true:
            Return true (cycle found)

    Return false (no cycle found)

```

**Explanation:**
1. The `DFS` procedure explores the graph from a given node and marks it as visited. During the exploration of neighbors, it checks for back edges, indicating the presence of a cycle. If a node is encountered which is not the parent of current node and was already visited, it indicates the presence of a back edge ultimately the presence of a cycle in the given graph is detected.

2. The `HasCycle` procedure initializes an array to track visited nodes. It iterates through all nodes, initiating DFS from unvisited nodes. Since it starts DFS from an unvisited node, -1 is passed as dummy marker parent of that node and inside the DFS procedure, when it starts the exploration of a neighbour ,the current node is passed as parent of the neighbour.
The `HasCycle` procedure returns `true` if cycle is found else return `false` at the end of procedure if there is no cycle in the given graph.

### Video Explanation

### Task
- Implement the given algorithm to check if given graph contains any cycle.

---

## Input Format

- The first line consists of two space separated integers, `N` and `M`, representing the number of nodes and edges.
- Nodes are numbered from `1` to `N`.
- The subsequent `M` lines describe the edges in , each containing two integers, `u` and `v`, describing the bidirectional edges.
- Each edge links two distinct nodes, and at most one edge exists between any two nodes.

---

## Output Format

- Output `YES` if there is cycle in graph, else `NO`.

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
YES
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Graphs, DFS

**Problem:** Implement the algorithm to check if a given undirected graph contains any cycle.

**Solution Approach:** As mentioned on the problem statement page, we  use depth-first search (DFS) and track the parent of each node during the traversal. While exploring the neighbors of a node, if a neighbor is encountered that has been already visited but is not the parent of the current node, then there is a back edge, indicating the presence of a cycle in the graph. The algorithm iterates through all vertices, performing DFS from each unvisited vertex, and detects cycles if any during the process.

**Time complexity:**  O(N + M) as we need to explore all nodes using DFS.

**Space complexity:**  O(N) as we need to store the visited states of the nodes  in an array.

</details>
