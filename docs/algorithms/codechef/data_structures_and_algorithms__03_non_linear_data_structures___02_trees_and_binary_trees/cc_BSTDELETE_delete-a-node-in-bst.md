# Delete a Node in BST

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BSTDELETE |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary search trees |
| Official Link | [BSTDELETE](https://www.codechef.com/learn/course/trees/BSTREESPRO/problems/BSTDELETE) |

---

## Problem Statement

Given a Binary Search Tree (BST) and a target node $X$, delete the node from the BST. The goal is to return the reference to the root node, which may be modified after the deletion process.
The solution can be achieved into two main steps:

- Search for the given node.
- If the node is found, delete it and return the updated reference to the root node of the modified BST.

### Video Explanation

For eg., in the following BST, node 2 is deleted:

![BSTSEARCH](https://cdn.codechef.com/images/learning/graphs-trees/bst-delete.png)

---

## Input Format

- The first line of the input contains two space separated integers $N$ and $X$ — the number of nodes in the binary search tree, and the node to be deleted.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Complete the given function and return the root of modified BST after node $X$'s deletion.

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
10 8
3 1 L
8 3 L
8 11 R
11 9 L
13 8 L
13 19 R
18 16 L
19 18 L
19 20 R
```

**Output**

```text
Successfully deleted the node!
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** Binary Search Trees, BT traversals.

**Problem :-** Given a Binary Search Tree (BST) and a target node X, delete the node from the BST. The goal is to return the reference to the root node, which may be modified after the deletion process.

**Solution Approach :-**

The provided solution implements the deletion of a node in a BST through a recursive approach. The process involves searching for the target node and then performing the deletion based on different cases.

*Algorithm:*

-

- If the root is null, return null (base case).

-

- If the target value x is less than the root’s value, recursively call deleteNode on the left subtree.

-

- If x is greater than the root’s value, recursively call deleteNode on the right subtree.

-

- If x is equal to the root’s value:

- If the node has no children (both left and right are null), return null.

- If the node has only one child, return that child.

- If the node has two children, find the inorder successor (the smallest node in the right subtree), replace the root’s value with the successor’s value, and recursively call deleteNode on the right subtree to delete the successor.

-

- Return the modified root.

**Time Complexity:** The time complexity of this algorithm is O(h), where h is the height of the BST. In the worst case, for an unbalanced tree, the height can be equal to the number of nodes, resulting in O(n) time complexity.

**Space Complexity:** The space complexity is O(h) due to the recursive call stack. In the worst case, for an unbalanced tree, the height can be equal to the number of nodes, resulting in O(n) space complexity.

</details>
