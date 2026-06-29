# Height Balanced Binary Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HBBTREE |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [HBBTREE](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/HBBTREE) |

---

## Problem Statement

Given a connected binary tree with **N** nodes, determine if it is height-balanced. (**Note:** A binary tree is height-balanced if the depth of the two subtrees of every node never differs by more than one.)

For example, the following binary tree is height balanced:

![Height Balanced Tree](https://cdn.codechef.com/images/learning/graphs-trees/hbbt.png)

---

## Input Format

- The first line of the input contains a single integer $N$ — the number of nodes in the binary tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Output on the single line, `YES` if the tree is height balanced, else `NO`.

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
6 1 L
7 6 L
7 8 R
10 7 L
10 14 R
14 13 L
14 15 R
```

**Output**

```text
YES
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Binary Trees, Binary Trees Traversal Techniques.

**Problem:** Given a connected binary tree with N nodes, determine if it is height-balanced.

(Note: A binary tree is height-balanced if the depth of the two subtrees of every node never differs by more than one.)

**Solution Approach:** This problem also can be solved using a recursive approach to check if a binary tree is height-balanced. For each node, calculate the height of its left and right subtrees. If the heights differ by more than one, or if any subtree is unbalanced, the tree is considered unbalanced.

*Algorithm:*

-

- Implement a recursive function checkHeight() that calculates the height of the subtree rooted at a given node.

- If the node is NULL, return 0 (base case).

- Recursively calculate the height of the left and right subtrees.

- If either subtree is unbalanced (height = -1), return -1.

- If the heights of the left and right subtrees differ by more than 1, return -1.

- Otherwise, return the height of the subtree as 1 + max(leftHeight, rightHeight).

-

- In the main function *isHeightBalanced()*, call *checkHeight()* with the root of the binary tree.

-

- Print “YES” if the tree is height-balanced and “NO” otherwise.

**Time Complexity:** O(N), as we need to traverse each node once.

**Space Complexity:** O(1), as we don’t need any extra space.

</details>
