# Neighbours of node

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TNEIGHBOUR |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [TNEIGHBOUR](https://www.codechef.com/learn/course/trees/TREESPRO/problems/TNEIGHBOUR) |

---

## Problem Statement

Given an undirected connected tree with **N** nodes, numbered from **1** to **N**, and rooted at node **1**, along with a node `v`, count the number of neighbours of the node `v`.

For example, if `v` is 2, then in the following tree, the no. of its neighbours is 4 (1, 5, 3 and 6).

![Kth Nodes](https://cdn.codechef.com/images/learning/graphs-trees/sample-tree.png)

---

## Input Format

- The first line of the input contains two space separated integer $N$ and `v` — the number of vertices and the node `v`, whose neighbours needs to be counted.
- The next $N - 1$ lines describe the edges. The $i$-th of these $N - 1$ lines contains two space-separated integers $u_i$ and $v_i$, denoting a bidirectional edge between $u_i$ and $v_i$.

---

## Output Format

Output the no. of neighbours of node `v`.

---

## Constraints

- $1 \leq N \leq 100000$
- $1 \leq u_i, v_i \leq N$
- $1 \leq v \leq N$

---

## Examples

**Example 1**

**Input**

```text
7 2
1 2
1 4
2 5
2 3
2 6
4 7
```

**Output**

```text
4
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** Indegree/Outdegree in Trees

**Problem :-** Given an undirected connected tree with N nodes, numbered from 1 to N, and rooted at node 1, along with a node v, count the number of neighbors of the node v.

**Solution Approach:**

The solution uses a straightforward approach to count the number of neighbors for the specified node in the given tree. While taking tree inputs, mark the indegree of each node, in an array called indegree and later get the indegree of node v, which shall be the no. of its neighbors.

*Note:* Outdegree of a node is total number of leaving vertices.Similarly, Indegree of a node is total number of entering vertices. Both of them are the same in case of undirected trees.

**Time Complexity:**  O(E) = O(N), where N is the number of nodes and E = N - 1 is the no. of edges in the tree. The algorithm iterates through all edges once to populate the degree array.

**Space Complexity:** O(N), as the degree array stores information for each node.

</details>
