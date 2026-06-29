# Diameter of the tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TREEDIAMETER |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [TREEDIAMETER](https://www.codechef.com/learn/course/trees/TREESPRO/problems/TREEDIAMETER) |

---

## Problem Statement

Given an undirected connected tree with **N** nodes, numbered from **1** to **N**, and rooted at node **1**, find the length of the diameter of the tree (**Note:** Diameter of a tree is the longest path between any two nodes. There can be more than one diameter of a tree with the same length).

For example, in the following tree, length of the tree's diameter is 4. (one of the diameters is 5-2-1-4-7)

![Kth Nodes](https://cdn.codechef.com/images/learning/graphs-trees/sample-tree.png)

---

## Input Format

- The first line of the input contains a single intege $N$ — the number of nodes.
- The next $N - 1$ lines describe the edges. The $i$-th of these $N - 1$ lines contains two space-separated integers $u_i$ and $v_i$, denoting a bidirectional edge between $u_i$ and $v_i$.

---

## Output Format

- Output on the single line, the length of the diameter of given tree.

---

## Constraints

- $1 \leq N \leq 100000$
- $1 \leq u_i, v_i \leq N$

---

## Examples

**Example 1**

**Input**

```text
7 
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

**Prerequisites :-** DFS

**Problem :-** Given an undirected connected tree with N nodes, numbered from 1 to N, and rooted at node 1, find the length of the diameter of the tree (Note: Diameter of a tree is the longest path between any two nodes. There can be more than one diameter of a tree with the same length).

**Solution Approach:**

First of all, what’s the diameter of a tree?

The diameter of a tree is the number of nodes on the longest path between two leaves in the tree.

The problem can be solved using a two-step Depth-First Search (DFS) approach

*First DFS for Farthest Node:*

- Perform the first DFS to find the farthest node from the starting node (node 1).

- This is done by updating the distance array during the DFS traversal.

*Second DFS for Diameter:*

- Use the farthest node found in the first DFS as the starting node for the second DFS.

- Traverse the tree from the farthest node and update the distance array again.

- The maximum distance encountered during this traversal is the diameter of the tree.

Finally, print the diameter of the tree.

**Time Complexity:** O(N + E) = O(N), where N is the number of nodes and E is the no. of edges in the tree. The two DFS traversals visit each node and edge once.

**Space Complexity:** O(N), as the algorithm utilizes an array to store distances for each node.

</details>
