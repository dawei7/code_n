# Predecessor of a Node in BST

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BSTPREDECR |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary search trees |
| Official Link | [BSTPREDECR](https://www.codechef.com/learn/course/trees/BSTREESPRO/problems/BSTPREDECR) |

---

## Problem Statement

Determine the inorder predecessor of a given node `X` in a binary search tree. The inorder predecessor, denoted as node `Y`, is the node that immediately precedes `X` in the inorder traversal of the binary tree. If no such predecessor exists, return `-1`.

For eg., the inorder predecessor of node 6 is node 5 in the following BST:

![BSTSEARCH](https://cdn.codechef.com/images/learning/graphs-trees/bst-search.png)

---

## Input Format

- The first line of the input contains two space separated integers $N$ and $X$ — the number of nodes in the binary search tree, and the node whose predecessor we're looking for.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Output on a single line - the predecessor node value of node $X$, if it exists, else `-1`.

---

## Constraints

- $1 \leq N \leq 10000$
- $1 \leq p_i, c_i \leq 100000$
- $R_i$ = `L` or `R`
- All $p_i$'s and $c_i$'s are distinct.
- $1 \leq X \leq 100000$

---

## Examples

**Example 1**

**Input**

```text
7 6
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

**Problem :-** Find the inorder predecessor of a given node X in a binary search tree. The inorder predecessor, denoted as node Y, is the node that immediately precedes X in the inorder traversal of the binary tree. If no such predecessor exists, return -1.

**Solution Approach :-**

The solution uses an iterative approach to find the inorder predecessor of a given node in a Binary Search Tree (BST). The key observation is that the inorder predecessor is the largest node in the left subtree of the given node (if it has a left subtree). If the given node doesn’t have a left subtree, we need to traverse up the tree until we find a node whose right child is an ancestor of the given node.

*Algorithm:*

-

- Initialize a pointer predecessor to NULL.

-

- Iterate through the tree:

- If the current node’s value is less than the target value x, update the predecessor and move to the right subtree.

- If the current node’s value is greater than or equal to x, move to the left subtree.

-

- After the iteration, if the predecessor is still NULL, return -1 as no predecessor exists. 4. Otherwise, return the value of the predecessor.

**Time complexity:** O(N), because in the worst case, the algorithm visits all the nodes in the given BST.

**Space complexity:** O(1), as no extra space is needed.

</details>
