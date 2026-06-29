# Min Difference in BST

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BSTMINDIFF |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary search trees |
| Official Link | [BSTMINDIFF](https://www.codechef.com/learn/course/trees/BSTREESPRO/problems/BSTMINDIFF) |

---

## Problem Statement

Given a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

For eg., the min difference between any two is 1 in the following tree.

![BSTSEARCH](https://cdn.codechef.com/images/learning/graphs-trees/bst-search.png)

---

## Input Format

- The first line of the input contains s single integer $N$ — the number of nodes in the binary search tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Output on a single line - the min difference between any two nodes in given BST.

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
7
4 2 L
4 6 R
2 3 R
2 1 L
6 5 L
6 7 R
```

**Output**

```text
1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** Binary Search Trees, BT traversals.

**Problem :-** Given a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

**Solution Approach :-** To find the minimum difference between the values of any two nodes in a BST, we can perform an inorder traversal of the tree. During the traversal, we keep track of the previous visited node’s value and update the minimum difference as we encounter each node. The minimum difference occurs when we compare adjacent nodes in the sorted order of a BST.

**Time complexity:** O(N), because the algorithm visits all the nodes in the given BST.

**Space complexity:** O(1), as no extra space is needed.

</details>
