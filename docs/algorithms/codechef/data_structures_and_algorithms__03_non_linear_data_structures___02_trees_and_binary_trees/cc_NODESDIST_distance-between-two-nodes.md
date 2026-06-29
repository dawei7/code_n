# Distance between two nodes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NODESDIST |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [NODESDIST](https://www.codechef.com/learn/course/trees/TREESPRO/problems/NODESDIST) |

---

## Problem Statement

Given an undirected connected tree with **N** nodes, numbered from **1** to **N**, and rooted at node **1**, and two nodes $u$ and $v$, find the distance between these two nodes. (**Note:** the distance between two nodes is the no. of edges in the simple path between them.)

For example, in the following tree, the distance between nodes $3$ and $7$ is $4$.

![Kth Nodes](https://cdn.codechef.com/images/learning/graphs-trees/sample-tree.png)

---

## Input Format

- The first line of the input contains three space separated integers $N$, $u$ and $v$ — the number of nodes, and two given nodes.
- The next $N - 1$ lines describe the edges. The $i$-th of these $N - 1$ lines contains two space-separated integers $u_i$ and $v_i$, denoting a bidirectional edge between $u_i$ and $v_i$.

---

## Output Format

- Output on the single line, the distance between the nodes $u$ and $v$.

---

## Constraints

- $1 \leq N \leq 100000$
- $1 \leq u_i, v_i \leq N$
- $1 \leq u, v \leq N$

---

## Examples

**Example 1**

**Input**

```text
7 3 7
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

**Prerequisites:-** DFS, LCA + Binary Lifting Technique.

**Problem :-** Given an undirected connected tree with N nodes, numbered from 1 to N, and rooted at node 1, and two nodes u and v, find the distance between these two nodes. (Note: the distance between two nodes is the no. of edges in the simple path between them.)

**Solution Approach:-** The distance between two nodes can be determined using the Lowest Common Ancestor (LCA) (using Binary Lifting or other RMQ approach, we’ll talk about only Binary lifting here). The idea is to preprocess the tree to efficiently find the LCA of two nodes and then calculate the distance between them using their levels in the tree. In case you don’t know how the binary lifting technique works in determining the LCA of two nodes, refer to the problem [TREELCA](https://discuss.codechef.com/t/treelca-editorial/116329) and its solution.

Once we find the LCA(u, v), we can easily get the distance between node u and v.

Let’s walk through a proof of why the distance formula,

distance(u, v) = level[u] + level[v] − 2 × level[lca(u, v)] is correct.

### [](#key-observations-1)Key Observations:

- Path Decomposition:

- The distance between two nodes u and v in a tree can be decomposed into the sum of their depths minus twice the depth of their lowest common ancestor (LCA).

- Shared Portion:

- The LCA represents the common portion of the paths from the root to u and v. Subtracting twice its depth ensures that this common portion is not double-counted in the distance calculation.

### [](#proof-2)Proof:

-

Individual Paths:

- Let Pu be the path from the root to node u. Similarly, let Pv be the path from the root to node v.

-

Decomposition of Distance:

- The distance between u and v is the sum of the lengths of Pu and Pv, minus twice the length of the common portion (Plca) shared by both paths.

-

Distance = ∣Pu∣ + ∣Pv∣ − 2  ×  ∣Plca∣

-

Path Length in Terms of Levels:

- The length of a path P is equivalent to the number of edges in the path.

- ∣P∣ = level[`x`] for any node x in the path.

-

Substitute Level Representation:

- Substitute the length of paths in terms of their levels into the distance formula:

-

distance(u, v) = level[u] + level[v] − 2 × level[lca(u, v)]

**Time Complexity:** O(NlogN), as for each node the we need to find the at most LogN ancestors during the preprocessing step.

**Space Complexity:** O(NLogN) as we need to store the LogN ancestors details for each of the N nodes.

</details>
