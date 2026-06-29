# Topological Sort - Using BFS 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TOPOSORTBFS |
| Difficulty Band | Graphs |
| Path | Data Structures and Algorithms |
| Lesson | Topological Sorting |
| Official Link | [TOPOSORTBFS](https://www.codechef.com/learn/course/graphs/TOPOSORT/problems/TOPOSORTBFS) |

---

## Problem Statement

This is also known as The *Kahn's Algorithm*.
### The Algorithm

The core idea behind Kahn's Algorithm for topological sorting is to process vertices in a way that respects their dependencies. It achieves this by iteratively selecting vertices with no incoming edges (in-degree 0) and gradually removing them from the graph.

In summary, Kahn's Algorithm identifies vertices that can be processed first (those without dependencies) and ensures that each vertex is processed only after its dependencies have been satisfied. This systematic approach leads to a topological ordering of the vertices in a directed acyclic graph (DAG).

```plaintext
Procedure TopologicalSort(graph):
    Initialize an array 'inDegree' for each vertex
    Initialize an empty queue

    // Calculate In-Degrees
    for each vertex v in graph:
        Calculate in-degree of v and store in 'inDegree' array

    // Enqueue vertices with in-degree 0
    for each vertex v in graph:
        if in-degree of v is 0:
            Enqueue v

    // Process Vertices
    while queue is not empty:
        Dequeue a vertex u
        Output u as part of the topological order

        for each neighbor v of u:
            Decrease in-degree of v by 1
            if in-degree of v is 0:
                Enqueue v

    // Check for Cycles
    if number of processed vertices is not equal to the total number of vertices:
        Output "Graph contains a cycle"
```
### Task
- Print a topological ordering of the given directed graph.

---

## Input Format

- The first line consists of two space separated integers, `N` and `M`, representing the number of nodes and edges.
- Nodes are numbered from `1` to `N`.
- The subsequent `M` lines describe the edges, each containing two integers, `u` and `v`, describing the directed edge between nodes `u` and `v`.
- Each edge links two distinct nodes, and at most one edge exists between any two nodes.

---

## Output Format

- Output N space separated integers, the topological ordering of the given graph, if possible. Else print -1.

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
1 2 3 4 5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Graphs, DFS

**Problem:** Check  if for the given directed graph, topological ordering can be found or not.

**Solution Approach:** As mentioned in the problem statement, the core idea behind finding topological ordering using BFS(Kahn’s Algorithm) is to process vertices in a way that respects their dependencies. It achieves this by iteratively selecting vertices with no incoming edges (in-degree 0) and gradually removing them from the graph.

Kahn’s Algorithm identifies vertices that can be processed first (those without dependencies) and ensures that each vertex is processed only after its dependencies have been satisfied. This systematic approach leads to a topological ordering of the vertices in a directed acyclic graph (DAG).

If the graph is not a DAG and contains a cycle then those nodes in cycle shall not be processed and hence not be added in topological order list. At the end, if the size of topological order list is not equal to total no. of nodes in graph, it means the graph had cycle and hence topological ordering is not possible.

**Time complexity:** O(N + M) as we are using BFS.

**Space complexity:** O(N) as we need to use a queue in BFS.

</details>
