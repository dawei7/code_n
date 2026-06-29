# Height of the tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TREELVL |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [TREELVL](https://www.codechef.com/learn/course/trees/TREESPRO/problems/TREELVL) |

---

## Problem Statement

Given an undirected connected tree with **N** nodes, numbered from **1** to **N**, and rooted at node **1**, find the height of the tree.

For example, in the following tree, the height is **2**. (**Note:** The height of a tree is the number of edges on the longest downward path between its root node and any of the leaves.)

![Kth Nodes](https://cdn.codechef.com/images/learning/graphs-trees/sample-tree.png)

---

## Input Format

- The first line of the input contains a single integer $N$ — the number of vertices.
- The next $N - 1$ lines describe the edges. The $i$-th of these $N - 1$ lines contains two space-separated integers $u_i$ and $v_i$, denoting a bidirectional edge between $u_i$ and $v_i$.

---

## Output Format

Output on the single line, the depth of the given tree.

---

## Constraints

- $1 \leq N \leq 100000$
- $1 \leq u_i, v_i \leq N$

---

## Examples

**Example 1**

**Input**

```text
8
1 2
1 3
3 4
3 5
3 6
2 7 
2 8
```

**Output**

```text
2
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** DFS or BFS

**Problem :-** Given an undirected connected tree with N nodes, numbered from 1 to N, and rooted at node 1, find the height of the tree.

**Solution Approach:**

The problem can be efficiently solved using Depth First Search (DFS) on the tree. Please note that BFS can also be used.

Kindly note that, the height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

The basic idea is to perform a DFS traversal starting from the root node and keep track of the depth (distance from the root) of each node. The maximum depth encountered during the traversal will be the height of the tree.

- Start a DFS traversal from the root node (node 1) with an initial depth of 0.

- For each neighbor v of the current node, if v is not the parent node (to avoid going back to the parent), recursively call DFS on v with depth increased by 1.

- Update the maximum depth encountered during the traversal.

**Time Complexity:**

The DFS traversal visits each node and edge once, leading to a time complexity of O(N + E), where N is the number of nodes and E is the number of edges (= N - 1, in case of tree). Hence the overall time complexity is O(N).

**Space Complexity:**

The space complexity is O(N) for storing the adjacency list and recursion stack during DFS.

</details>
