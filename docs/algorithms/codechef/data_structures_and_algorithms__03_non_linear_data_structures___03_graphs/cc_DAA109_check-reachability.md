# Check Reachability

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DAA109 |
| Difficulty Rating | 932 |
| Difficulty Band | Graphs |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Graphs |
| Official Link | [DAA109](https://www.codechef.com/learn/course/graphs/GRAPHTRAVERS/problems/DAA109) |

---

## Problem Statement

You are given a graph of $N$ vertices - numbered from $1$ to $N$ and $M$ edges between them. \
The $i^{th}$ edge connects the $A_i$ node to $B_i$. The edges are directed.

You live at the vertex $1$, output all the vertices that you can visit. You can travel using the given edges.

---

## Input Format

- The first line of input will contain a two integers $N$ and $M$, denoting the number of vertices and edges.
- Next $M$ lines describes the edges. $i-th$ of these $M$ lines contains two space-separated integers $A_i$ and $B_i$ denoting there exists a directed edge from $A_i$ to $B_i$.

---

## Output Format

Output all the nodes you can visit from the node 1, in increasing order of their index.

---

## Constraints

- $2 \leq N, M \leq 2 \cdot 10^5$
- $1 \leq A_i, B_i \leq N$

---

## Examples

**Example 1**

**Input**

```text
5 6
1 3
4 3
3 2
2 4
5 4
3 1
```

**Output**

```text
1 2 3 4
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** DFS

**Problem:** Given a directed graph with N vertices and M directed edges, the task is to output all the vertices that are reachable from the starting vertex 1.

**Solution Approach:** The solution is quite simple. Use Depth-First Search (DFS) algorithm to traverse the directed graph and mark the nodes that are reachable from the starting vertex 1. At the end print/output only those nodes who were visited from node 1.

**Time complexity:** O(V + E) as we use DFS.

**Space complexity:** O(V) for extra boolean array to mark the nodes visited.

</details>
