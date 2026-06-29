# LCA in the BST

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BSTLCA |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary search trees |
| Official Link | [BSTLCA](https://www.codechef.com/learn/course/trees/BSTREESPRO/problems/BSTLCA) |

---

## Problem Statement

Given a binary search tree, and two nodes values $X$ and $Y$, find the LCA (lowest common ancestor) of these two nodes.

For eg., in the following BST, the LCA of nodes with values 3 and 5 is the root node 4:

![BSTSEARCH](https://cdn.codechef.com/images/learning/graphs-trees/bst-search.png)

---

## Input Format

- The first line of the input contains three space separated integers $N$, $X$ and $Y$ — the number of nodes in the binary search tree, and the two given nodes.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Output on the single line, the LCA of node $X$ and $Y$.

---

## Constraints

- $1 \leq N \leq 10000$
- $1 \leq p_i, c_i \leq 100000$
- $R_i$ = `L` or `R`
- All $p_i$'s and $c_i$'s are distinct (same pairs are not repeated).
- $1 \leq X, Y \leq 100000$

---

## Examples

**Example 1**

**Input**

```text
17 22 3
3 1 L
6 3 L
6 21 R
22 6 L
22 31 R
31 23 L
31 32 R
51 22 L
51 94 R
66 63 L
73 66 L
73 93 R
94 73 L
94 97 R
97 95 L
97 99 R
```

**Output**

```text
22
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** Binary Search Trees, BT traversals, LCA in Binary tree.

**Problem :-** Given a binary search tree, and two nodes values X and Y, find the LCA (lowest common ancestor) of these two nodes.

**Solution Approach :-** The solution utilizes the properties of a binary search tree to efficiently find the Lowest Common Ancestor of two given nodes. The key observation is that the LCA will be a node where one node lies in the left subtree, and the other lies in the right subtree.

*Algorithm:*

-

- Start from the root.

-

- If both nodes X and Y are greater than the current node’s value, move to the right subtree.

-

- If both nodes X and Y are smaller than the current node’s value, move to the left subtree.

-

- If neither of the above conditions is true, it means one node lies in the left subtree, and the other lies in the right subtree, so the current node is the LCA.

-

- Return the LCA.

**Time Complexity:** O(N), because in the worst case, the algorithm visits all the nodes in the given BST.

**Space complexity:** O(1), because only constant space (for few variables) is used.

</details>
