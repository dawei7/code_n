# Topological Sort - using DFS

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TOPOSORTDFS |
| Difficulty Band | Graphs |
| Path | Data Structures and Algorithms |
| Lesson | Topological Sorting |
| Official Link | [TOPOSORTDFS](https://www.codechef.com/learn/course/graphs/TOPOSORT/problems/TOPOSORTDFS) |

---

## Problem Statement

### The Algorithm

Let's assume that the graph is acyclic. If unsure, first check. As discussed earlier, topological sort can only be found in DAGs.

When starting from some vertex $v$ , DFS tries to traverse along all edges outgoing from  
$v$. It stops at the edges for which the ends have been already been visited previously, and traverses along the rest of the edges and continues recursively at their ends.

Thus, by the time of the function call  
$\text{dfs}(v)$  has finished, all vertices that are reachable from  
$v$  have been either directly (via one edge) or indirectly visited by the search.

Let's append the vertex  
$v$  to a list, when we finish  
$\text{dfs}(v)$ . Since all reachable vertices have already been visited, they will already be in the list when we append  
$v$ . Let's do this for every vertex in the graph, with one or multiple depth-first search runs. For every directed edge  
$v \rightarrow u$  in the graph,  
$u$  will appear earlier in this list than  
$v$ , because  
$u$  is reachable from  
$v$ . So if we just label the vertices in this list with  
$n-1, n-2, \dots, 1, 0$ , we have found a topological order of the graph. In other words, the list represents the reversed topological order.

**Pseudocode:**
```plaintext
Procedure DFS(v):
    Mark v as visited
    For each unvisited neighbor u of v:
        Call DFS(u)
    Append v to 'topologicalOrder'

Procedure TopologicalSort():
    Initialize an empty list 'topologicalOrder' to store the topological order
    Create a boolean array 'visited' of size n, initially set to false

    For each vertex i from 0 to n-1:
        If i is not visited:
            Call DFS(i)

    Reverse the 'topologicalOrder' list  // This is the topological order
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

- Output `N` space separated integers, the topological ordering of the given graph, if possible. Else print -1.

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

**Solution Approach:** The solution utilizes DFS to perform two main tasks:

- Check if the given graph is a Directed Acyclic Graph (DAG).

- If it is a DAG, find and print a topological ordering of the vertices.

We’ve already discussed how to perform task 1 in previous sections, lets focus and reiterate the core idea behind task 2:

When starting from some vertex v , DFS tries to traverse along all edges outgoing from

v. It stops at the edges for which the ends have been already been visited previously, and traverses along the rest of the edges and continues recursively at their ends.

Thus, by the time of the function call  \text{dfs}(v)  has finished, all vertices that are reachable from  v  have been either directly (via one edge) or indirectly visited by the search.

Let’s append the vertex  v  to a list, when we finish  \text{dfs}(v) . Since all reachable vertices have already been visited, they will already be in the list when we append  v . Let’s do this for every vertex in the graph, with one or multiple depth first search runs. For every directed edge  v \rightarrow u  in the graph,  u  will appear earlier in this list than  v , because  u  is reachable from  v . So if we just label the vertices in this list with  n-1, n-2, \dots, 1, 0 , we have found a topological order of the graph. In other words, the list represents the reversed topological order. So just reverse the topological order list if you need it else just checking the acyclicity is enough to tell whether topological ordering is possible or not.

**Time complexity:** O(N + M) as we are using DFS.

**Space complexity:** O(N) as we need to use additional space in DFS.

</details>
