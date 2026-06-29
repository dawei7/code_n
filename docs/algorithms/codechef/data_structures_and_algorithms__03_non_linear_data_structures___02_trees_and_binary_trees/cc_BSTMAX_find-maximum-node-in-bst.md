# Find maximum node in BST

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BSTMAX |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary search trees |
| Official Link | [BSTMAX](https://www.codechef.com/learn/course/trees/BSTREES/problems/BSTMAX) |

---

## Problem Statement

Given a binary search tree, find the maximum/largest node in it.

For eg., the maximum node in the given BST is 7.

![BSTSEARCH](https://cdn.codechef.com/images/learning/graphs-trees/bst-search.png)

---

## Input Format

- The first line of the input contains s single integer $N$ — the number of nodes in the binary search tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Output on a single line - the the maximum node value of the given BST.

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
7
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** Binary Search Trees, BinaryTree traversal.

**Problem :-** Given a binary search tree, find the maximum/largest node in it.

**Solution Approach :-** The solution uses the property of a binary search tree where the rightmost node in the tree is the maximum/largest node. Therefore, to find the maximum value in the BST, you need to traverse down the right subtree until you reach the rightmost leaf.

*Algorithm*:

-

- Start from the root of the BST.

-

- Loop down to find the rightmost leaf of the BST.

-

- The rightmost leaf represents the maximum/largest node in the BST.

-

- Return the value of the rightmost leaf.

**Time complexity :-** O(h), where h is the height of the BST, if the tree is skewed, the complexity can go upto O(N).

**Space complexity :-** O(1), as no extra space is required.

</details>
