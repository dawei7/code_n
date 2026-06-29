# InOrder Traversal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BTINORDER |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [BTINORDER](https://www.codechef.com/learn/course/trees/BINARYTREES/problems/BTINORDER) |

---

## Problem Statement

In-order traversal involves visiting the left subtree first, then the root node, and finally the right subtree.

**Algorithm**:
- Recursively traverse the left subtree.
- Visit the root node.
- Recursively traverse the right subtree.

### Video Explanation

For example, check the Inorder traversal in the following binary tree:

![Inorder traversal](https://cdn.codechef.com/images/learning/graphs-trees/inorder-traversal.gif)

### Task
Given a binary tree, print its nodes in Inorder traversal, by completing the given function.

---

## Input Format

- The first line of the input contains a single integer $N$ — the number of nodes in the binary tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Output on the single line, $N$ space separated integers - its nodes in the inorder traversal of the given tree.

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
2 1 4 3 5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** Binary Trees.

**Problem:** Print nodes of a given binary tree in an inorder manner.

**Solution Approach:** Inorder traversal is another fundamental depth-first traversal method for binary trees. In inorder traversal, the nodes are visited in the following sequence:

-

- Traverse the Left Subtree:

- Recursively perform an inorder traversal on the left subtree of the current node.

- For each node in the left subtree, repeat step 1.

-

- Visit the Root Node:

- Process/visit the data (or perform an operation) associated with the root node.

-

- Traverse the Right Subtree:

- Recursively perform an inorder traversal on the right subtree of the current node.

- For each node in the right subtree, repeat step 1.

**Time complexity:** O(N), where N is the number of  nodes in the tree. Each node is visited once.

**Space complexity:** O(1), as we don’t need any extra space.

</details>
