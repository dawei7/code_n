# Count number of leaf nodes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSCPP86 |
| Difficulty Rating | 932 |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [DSCPP86](https://www.codechef.com/learn/course/trees/TREES/problems/DSCPP86) |

---

## Problem Statement

Given a tree, find the number of leaf nodes using DFS algorithm.

Write the algorithm forming an adjacency list yourself. In the end, output the number of leaf nodes in the tree.

Hint: Leaf nodes are the nodes which do not have any children. You will need to modify your DFS code to count when you encounter a leaf node.

---

## Input Format

- The first line of test case contains a single integer $N$, denoting the number of nodes in the tree (the nodes lie in range $[0, N-1]$).
- The next $N-1$ lines contain two integers $a$ and $b$ denoting there is an edge from node $a$ to node $b$.

---

## Output Format

Output a single integer denoting the number of leaves in the given tree.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
8
0 1
0 2
1 3
1 4
2 5
3 6
5 7
```

**Output**

```text
3
```

**Explanation**

Try to draw the tree on a paper using this testcase.
The leaf nodes are 4, 6 and 7

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:-** Tree, DFS.

**Problem :-** Given a tree, find the number of leaf nodes using DFS algorithm.

Write the algorithm forming an adjacency list yourself. In the end, output the number of leaf nodes in the tree.

*Hint:* Leaf nodes are the nodes which do not have any children. You will need to modify your DFS code to count when you encounter a leaf node.

**Solution Approach:-**

The algorithm uses Depth-First Search (DFS) to explore a tree represented as an adjacency matrix. During the traversal, it counts the number of leaf nodes, which are nodes without any children. The DFS function starts from the root node and recursively explores its children, updating the count whenever it encounters a leaf node. The final count of leaf nodes is then outputted. This approach ensures an efficient way to identify and tally leaf nodes in a tree.

**Time Complexity:** The time complexity of this approach is O(N+E) = O(N), where N is the number of nodes in the tree, and E is the number of edges.

**Space Complexity:** O(N)

</details>
