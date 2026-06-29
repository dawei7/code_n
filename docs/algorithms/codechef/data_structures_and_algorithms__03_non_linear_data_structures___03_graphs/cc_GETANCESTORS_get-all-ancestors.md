# Get all ancestors

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GETANCESTORS |
| Difficulty Band | Graphs |
| Path | Data Structures and Algorithms |
| Lesson | Topological Sorting |
| Official Link | [GETANCESTORS](https://www.codechef.com/learn/course/graphs/TOPOSORT/problems/GETANCESTORS) |

---

## Problem Statement

Given a Directed Acyclic Graph (**DAG**) with $N$ nodes numbered from $0$ to $N$ - $1$, print in sorted ascending order of ancestors for the $i^{\text{th}}$ node for each node $0$ to $N$ - $1$.

A node `u` is an ancestor of another node `v` if `u` can reach `v` via a set of edges.

---

## Input Format

- The first line consists of two space separated integers, `N` and `M`, representing the number of nodes and edges.
- Nodes are numbered from `0` to `N-1`.
- The subsequent `M` lines describe the edges, each containing two integers, `u` and `v`, describing the directed edge between nodes `u` and `v`.
- The given graph is a **DAG**.

---

## Output Format

- Output N lines, ancestors of each node from $0$ to $N - 1$. In case some node doesn't have any ancestor, keep that line empty.

---

## Constraints

- $1 \leq N \leq 1000$
- $1 \leq M \leq min(2000, N(N-1))/2$
- $0 \leq u_i, v_i \leq N - 1$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.

---

## Examples

**Example 1**

**Input**

```text
5 6
0 1
1 2
0 2
2 4
1 3
3 4
```

**Output**

```text
0 
0 1 
0 1 
0 1 2 3
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Graphs, DFS/BFS, Topological order.

**Problem:** Given a Directed Acyclic Graph (**DAG**) with N nodes numbered from 0 to N - 1, print in sorted ascending order, the ancestors of ith node for each node 0 to N - 1. An ancestor of a node u in this context is defined as a node v that can be reached from u through a set of directed edges in the graph.

**Solution Approach:** The core of the solution’s algorithm is a breadth-first search (BFS) traversal(in the same manner we use it to find topological ordering) of the Directed Acyclic Graph starting from nodes with an indegree of 0. For each node processed in the BFS, its ancestors are updated by adding its own ancestors and the ancestors of its adjacent nodes. This is achieved by maintaining a set for each node to store its ancestors. The BFS continues until all nodes have been processed, ensuring that every node’s ancestors are correctly identified. Finally, the ancestors for each node are printed in sorted ascending order, as determined by the set data structure.

**Time complexity:** O(M + NlogN) as we are using BFS and also using set data structure which has logN time for insert operation.

**Space complexity:** O(N) as we need to use a queue and set in BFS.

</details>
