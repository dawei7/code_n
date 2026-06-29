# Kth Largest Node in BST

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BSTKTHMAX |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary search trees |
| Official Link | [BSTKTHMAX](https://www.codechef.com/learn/course/trees/BSTREESPRO/problems/BSTKTHMAX) |

---

## Problem Statement

Given a binary search tree and an integer $K$, find the $K$th largest node in it.

For eg., if K = 3, the answer would be 5 for the following BST:

![BSTSEARCH](https://cdn.codechef.com/images/learning/graphs-trees/bst-search.png)

---

## Input Format

- The first line of the input contains two space separated integers $N$ and $K$ — the number of nodes in the binary search tree, and the value of $K$.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Output on a single line - the $K$th largest node in the given BST.

---

## Constraints

- $1 \leq N \leq 10000$
- $1 \leq p_i, c_i \leq 100000$
- $R_i$ = `L` or `R`
- All $p_i$'s and $c_i$'s are distinct.
- $1 \leq K \leq N$

---

## Examples

**Example 1**

**Input**

```text
7 3
4 2 L
4 6 R
2 3 R
2 1 L
6 5 L
6 7 R
```

**Output**

```text
5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** Binary Search Trees, BT traversals.

**Problem :-** Given a binary search tree and an integer K, find the Kth largest node in it.

**Solution Approach :-**

To find the Kth largest element in a Binary Search Tree (BST), we can perform a reverse inorder traversal while maintaining a count of visited nodes. This approach takes advantage of the fact that reverse inorder traversal of a BST traverses nodes in descending order.

*Algorithm :-*

-

- Initialize a counter variable to keep track of the number of nodes visited.

-

- Perform a reverse inorder traversal (right, root, left):

- Traverse the right subtree.

- Visit the current node.

- Traverse the left subtree.

-

- At each step of the traversal, decrement the K value.

-

- When the counter becomes equal to K, stop the traversal and print the value of the current node as it represents the Kth largest element.

**Time complexity :-** O(N), because in the worst case, the algorithm visits all the nodes in the given BST.

**Space complexity :-** O(1), as no extra space is needed.

</details>
