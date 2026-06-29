# Top view of the Binary Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BTTOPVIEW |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [BTTOPVIEW](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/BTTOPVIEW) |

---

## Problem Statement

Given a binary tree, print the top view of the tree. The top view of a binary tree is the set of nodes visible when the tree is viewed from the top. It is defined as the nodes visible from the top along the vertical line passing through the leftmost node to rightmost node of the tree.

Examples:

![TOPVIEW](https://cdn.codechef.com/images/learning/graphs-trees/bt-top-view.png)

---

## Input Format

- The first line of the input contains a single integer $N$ — the number of nodes in the binary tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Print on the single line, $K$ (if there are $K$ nodes visible from the top) space separated node values - the top view nodes of the given binary tree from left to right.

---

## Constraints

- $1 \leq N \leq 10000$
- $1 \leq p_i, c_i \leq 100000$
- $R_i$ = `L` or `R`
- All $p_i$'s and $c_i$'s are distinct.

---

## Examples

**Example 1**

**Input**

```text
8
1 2 L
1 3 R
3 4 L
3 5 R
2 6 L
2 7 R
7 8 R
```

**Output**

```text
6 2 1 3 5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Binary tree, BT traversal.

**Problem:** Given a binary tree, print the top view of the tree.

The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

It is defined as the nodes visible from the top along the vertical line passing through the

leftmost node to rightmost node of the tree.

**Solution Approach:** This can be solved using a level-order traversal (BFS) to traverse the tree and calculate the top view of the binary tree. We can use a map to store the first encountered node at each vertical level. The key idea is to traverse the tree level by level, and at each level, only consider the first encountered node for that vertical line.

*Algorithm:*

-

- Implement the topView() function that takes the root of the binary tree as its parameter.

-

- Initialize a map v to store the top view nodes with their vertical indices.

-

- Use a queue to perform level-order traversal.

-

- Enqueue the root along with its vertical index (initially 0) into the queue.

-

- While the queue is not empty, perform the following steps:

- Dequeue a node and its vertical index from the front of the queue.

- If the vertical index is not already present in the map, insert the node’s value into the map at that vertical index.

- Enqueue the left child (if it exists) with a decremented vertical index.

- Enqueue the right child (if it exists) with an incremented vertical index.

-

- The map now contains the top view nodes at each vertical level. Iterate through the map and print the values.

**Time Complexity:** O(NlogN), as we need to visit each node once and use an ordered map to store the nodes.

**Space Complexity:** O(N), as we need to store each node in a map.

</details>
