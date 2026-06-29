# Nodes at Kth Level

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KTHNODE |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Trees |
| Official Link | [KTHNODE](https://www.codechef.com/learn/course/trees/TREESPRO/problems/KTHNODE) |

---

## Problem Statement

Given an undirected connected tree with **N** nodes, numbered from **1** to **N**, rooted at node **1**, and a positive integer **K**. Print all the nodes at the level **K** from root node in sorted order.

For example, in the following tree, root node `1` is at level `0`. Similarly, nodes `2` and `4` are at level `1` from the root. Similarly, nodes 5, 3, 6 and 7 are at level 2 from the root node.

![Kth Nodes](https://cdn.codechef.com/images/learning/graphs-trees/sample-tree.png)

---

## Input Format

- The first line of the input contains two space-separated integers $N$ and $K$— the number of vertices and level at which we need to find the nodes.
- The next $N - 1$ lines describe the edges. The $i$-th of these $N - 1$ lines contains two space-separated integers $u_i$ and $v_i$, denoting a bidirectional edge between $u_i$ and $v_i$.

---

## Output Format

Output on the single line, the space separated nodes (in sorted order) which are present at the **Kth** level from root node **1**,

---

## Constraints

- $1 \leq N \leq 100000$
- $1 \leq u_i, v_i \leq N$
- $0 \leq K \leq maxLevelInTree $

---

## Examples

**Example 1**

**Input**

```text
8 2
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
4 5 6 7 8
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** DFS

**Problem :**- Given an undirected connected tree with N nodes, numbered from 1 to N, rooted at node 1, and a positive integer K. Print/Find all the nodes at the level K from root node in sorted order.

**Solution Approach:**

We can use Depth-First Search (DFS) to traverse the tree and find the  nodes at the specified level. The DFS algorithm is designed to handle the traversal, taking into account the current node, its parent, the target level, and the current level.

If the current level matches the target level, the current node is added to the list of nodes at the Kth level.

For each neighbor of the current node, the DFS function is called recursively, excluding the parent node.

After the traversal, the nodes found at the Kth level can be sorted and then printed.

**Time Complexity:**

The DFS traversal has a time complexity of O(N + E) = O(N), where N is the number of nodes, E is no of edges, which is equal to N - 1 in case of trees . Sorting the nodes at the Kth level adds an additional O(N log N) time, because in the worst case there could be O(N) nodes at Kth level. Consequently, the overall time complexity is O(N log N).

**Space Complexity:**

The space complexity is O(N) due to the adjacency list, the nodes at the Kth level, and the recursive call stack during DFS. The depth of the recursive call stack is at most the height of the tree, which is O(N) in the worst case for an unbalanced tree.

</details>
