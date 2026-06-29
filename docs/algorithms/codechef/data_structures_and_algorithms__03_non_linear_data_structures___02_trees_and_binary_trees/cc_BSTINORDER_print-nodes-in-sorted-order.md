# Print nodes in sorted order

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BSTINORDER |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary search trees |
| Official Link | [BSTINORDER](https://www.codechef.com/learn/course/trees/BSTREES/problems/BSTINORDER) |

---

## Problem Statement

Given a binary search tree, print its nodes in sorted order.

For eg., the nodes in sorted order of the given BST are: 1 2 3 4 5 6 7

![BSTSEARCH](https://cdn.codechef.com/images/learning/graphs-trees/bst-search.png)

---

## Input Format

- The first line of the input contains s single integer $N$ — the number of nodes in the binary search tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Output on a single line $N$ space separated integers - the node values of given BST in sorted order.

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
1 2 3 4 5 6 7
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** Binary Search Trees, Binary Tree traversal.

**Problem :-**  Given a binary search tree, print its nodes in sorted order.

**Solution Approach :-**

The inorder traversal of a Binary Search Tree (BST) prints nodes in sorted order because of the inherent property of a BST: nodes in the left subtree have smaller values, and nodes in the right subtree have larger values. In the inorder traversal algorithm, the left subtree is visited first, followed by the current node, and then the right subtree. This order ensures that nodes are visited in ascending order, resulting in a sorted output.

**Time complexity :-** O(N), because the algorithm visits all the nodes in the given BST.

**Space complexity :-** O(1), as no extra space is needed.

</details>
