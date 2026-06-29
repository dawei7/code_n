# Subtree Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBTREESUM |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [SUBTREESUM](https://www.codechef.com/learn/course/trees/TREESPRO/problems/SUBTREESUM) |

---

## Problem Statement

Given an undirected connected tree with **N** nodes, numbered from **1** to **N**, and rooted at node **1**, find the subtree sum of each node $i$. (**Note:** Subtree of any node $i$ contains all nodes which are descendants of it including node $i$ )

For example, in the following tree, subtree sum of each nodes (from 1 to N = 7) are : 28, 16, 3, 11, 5, 6 and 7.

![Kth Nodes](https://cdn.codechef.com/images/learning/graphs-trees/sample-tree.png)

---

## Input Format

- The first line of the input contains a single intege $N$ — the number of nodes.
- The next $N - 1$ lines describe the edges. The $i$-th of these $N - 1$ lines contains two space-separated integers $u_i$ and $v_i$, denoting a bidirectional edge between $u_i$ and $v_i$.

---

## Output Format

Output one single line $N$ space separated values, the subtree sum of each subtrees rooted at each node from $1$ to $N$.

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
28 16 3 11 5 6 7
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** DFS

**Problem :-** Given an undirected connected tree with N nodes, numbered from 1 to N, and rooted at node 1, find the subtree sum of each node i. (Note: Subtree of any node i contains all nodes which are descendants of it including node i)

**Solution Approach:**

The problem can be solved using the Depth-First Search (DFS) traversal, which helps in computing the subtree sum for each node.

**1.** Maintain an array to store the cumulative sum of nodes in each subtree.

**2.**  Call the DFS function from the root node (node 1).

**3.** During the traversal, calculate the subtree sum for each node, including itself and its children.

**4.** Subtree Sum Calculation:

``     4a: For each node, add its own value to the subtree sum.
     4b: For each child of the current node, recursively call the DFS function.
     4c: Update the subtree sum of the current node by adding the subtree sums of its
               children.
``

**Time Complexity:** O(N + E) = O(N) as E = N - 1 in case of trees, where N is the number of nodes, E is no. of edges in the tree. The DFS traversal visits each node and edge once.

**Space Complexity:** O(N), as the algorithm utilizes an array to store subtree sums for each node.

</details>
