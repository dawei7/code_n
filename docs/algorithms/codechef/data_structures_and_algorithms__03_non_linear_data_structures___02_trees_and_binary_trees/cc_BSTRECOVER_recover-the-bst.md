# Recover the BST

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BSTRECOVER |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary search trees |
| Official Link | [BSTRECOVER](https://www.codechef.com/learn/course/trees/BSTREESPRO/problems/BSTRECOVER) |

---

## Problem Statement

Given a binary search tree, where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Example:

![BSTSEARCH](https://cdn.codechef.com/images/learning/graphs-trees/bst-recover.png)

---

## Input Format

- The first line of the input contains s single integer $N$ — the number of nodes in the binary search tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Complete the given function by recovering the BST without modifying its structure and return the root of the BST.

---

## Constraints

- $1 \leq N \leq 10000$
- $1 \leq p_i, c_i \leq 100000$
- $R_i$ = `L` or `R`
- No pair of $p_i$ and $c_i$ is repeated in any test case.
- There are no duplicate nodes.

---

## Examples

**Example 1**

**Input**

```text
12
29 9 L
29 37 R
39 29 L
39 58 R
58 56 L
100 39 L
100 96 R
89 81 L
96 89 L
96 65 R
65 97 L
```

**Output**

```text
OK! BST recovered. Well done!
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** Binary Search Trees, BT traversals.

**Problem :-** Given a binary search tree, where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

**Solution Approach :-** The approach involves performing an inorder traversal of the BST to detect the misplaced nodes. The key insight is that in an inorder traversal of a BST, the values should be in ascending order. If there are misplaced nodes, there will be points where the current node’s value is smaller than the previous node’s value. The goal is to identify the first and second misplaced nodes and then swap their values.

*Algorithm:*

-

- Initialize three pointers: first_node, second_node, and prev_node.

-

- Implement an inorderTraversal function to traverse the BST in inorder.

-

- In the traversal:

- If first_node is not assigned and the current node’s value is smaller than the previous node’s value, set first_node to the prev_node.

- If first_node is assigned and the current node’s value is smaller than the previous node’s value, set second_node to the current node.

- Update prev_node to the current node.

-

- After the traversal, swap the values of first_node and second_node.

-

- Return the modified root.

**Time Complexity:** O(N), because in the worst case, the algorithm visits all the nodes in the given BST.

**Space complexity:** O(1), because constant space (for few variables) is used.

</details>
