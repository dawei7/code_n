# Level Order Traversal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BTLVLORDER |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [BTLVLORDER](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/BTLVLORDER) |

---

## Problem Statement

Given a binary tree, print the level order traversal of its nodes. (i.e., from left to right, on each level).

For example, the level order traversal of the following binary tree is: \
1 \
2 3 \
4 5

![BTLVLORDER](https://cdn.codechef.com/images/learning/graphs-trees/leve-order-traversal.png)

---

## Input Format

- The first line of the input contains a single integer $N$ — the number of nodes in the binary tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Output on the L separate lines, $N$ space separated integers - its nodes in the level order traversal of the given tree, where L is total no. of levels in the given tree.

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
5
1 2 L
1 3 R
3 4 L
3 5 R
```

**Output**

```text
1
2 3
4 5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Binary tree, Queue data structure.

**Problem:** Given a binary tree, print the level order traversal of its nodes. (i.e., from left to right, on each level).

**Solution Approach:**

Level order traversal of a binary tree is similar to bread first search traversal. We need a queue data structure

to keep track of all the nodes at a particular level. We start with the root node, push it to the queue.

Then we print/store it and push all its children while popping the root node. In 2nd iteration, the queue is popped till its size which essentially prints nodes at the next level. Simultaneously we keep pushing the children of children and the process goes on like this, until the leaf nodes are printed.

Idea will become more clear once we take a look at the solution.

**Time Complexity:** O(N), as we need to visit each node once.

**Space Complexity:** O(N), as we need to store each node in the queue so that later its children can

be visited in level order.

</details>
