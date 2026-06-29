# Largest value at each level

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LARGESTVAL |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [LARGESTVAL](https://www.codechef.com/learn/course/trees/TREESPRO/problems/LARGESTVAL) |

---

## Problem Statement

Given an undirected connected tree with **N** nodes, numbered from **1** to **N**, and rooted at node **1**, find the largest node value at each level.

For example, in the following tree, largest node values at each level are: 1 (at level 1), 4 (at level 2) and 7 (at level 3).

![Kth Nodes](https://cdn.codechef.com/images/learning/graphs-trees/sample-tree.png)

---

## Input Format

- The first line of the input contains a single intege $N$ — the number of nodes.
- The next $N - 1$ lines describe the edges. The $i$-th of these $N - 1$ lines contains two space-separated integers $u_i$ and $v_i$, denoting a bidirectional edge between $u_i$ and $v_i$.

---

## Output Format

- On the first line, output a single number L - the no. of levels in the tree
- On the second line, output $L$ space separated values - the largest values at each of the $L$ levels.

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
3
1 4 7
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** DFS

**Problem :-** Given an undirected connected tree with N nodes, numbered from 1 to N, and rooted at node 1, find the largest node value at each level.

**Solution Approach:**

The solution uses dfs for identifying the largest node value at each level in an undirected connected tree rooted at node 1.

Let’s take a look at it step by step:

- DFS Traversal:

- Initiate a DFS traversal from the root node (node 1).

- During the traversal, maintain a map that stores the largest node value encountered at each level.

- Update Maximum Node Values:

- At each node, compare the current node value with the maximum value stored for its level.

- Update the map with the larger value.

- Output:

- Once the DFS traversal is complete, output the maximum node values for each level.

**Time Complexity:** O(N + E) = O(N), where N is the number of nodes and E is the no. of edges in the tree. The two DFS traversals visit each node and edge once. Instead of map, an array/vector can be also used to achieve the runtime complexity.

**Space Complexity:** O(N), as the algorithm utilizes an array to store max value at each level and in worst case, if the tree is linear it can take upto O(N) space.

</details>
