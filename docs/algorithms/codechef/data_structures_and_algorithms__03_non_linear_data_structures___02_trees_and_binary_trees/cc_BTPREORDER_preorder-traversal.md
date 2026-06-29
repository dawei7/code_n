# PreOrder Traversal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BTPREORDER |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [BTPREORDER](https://www.codechef.com/learn/course/trees/BINARYTREES/problems/BTPREORDER) |

---

## Problem Statement

Traversing a binary tree is involves visiting all the nodes in the tree in a specific order. The purpose of tree traversal is to access each node exactly once so that the data within the nodes can be processed. There are several methods to traverse a binary tree.

Let's learn about Pre Order traversal.

Pre-order traversal involves visiting the root node first, then recursively visiting the left subtree, and finally the right subtree.

Pseudo code:
```txt
void preOrder(node root) {
    if (root == null) {
        return
    }
    print(root->value)
    preOrder(root->left)
    preOrder(root->right)
}
```

### Video Explanation

For example, check the preorder traversal of the following binary tree
![Preorder traversal](https://cdn.codechef.com/images/learning/graphs-trees/preorder-traversal.gif)

### Task
Given a binary tree, complete the function *preOrderTraversal* to print the Preorder traversal of the tree.

---

## Input Format

- The first line of the input contains a single integer $N$ — the number of nodes in the binary tree.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Output on the single line, $N$ space separated integers - the preorder traversal of the given tree.

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
1 2 3 4 5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Prerequisites :- Binary Trees.

Problem: Print nodes of given binary tree in preorder manner.

Solution Approach: Preorder traversal is one of the fundamental depth-first traversal methods for binary trees. In a binary tree, each node has at most two children: a left child and a right child. Preorder traversal follows the order of visiting nodes in the following sequence:

-

- Visit the Root Node:

- Start at the root of the tree.

- Process/visit the data (or perform an operation) associated with the root node.

-

- Traverse the Left Subtree:

- Recursively perform a preorder traversal on the left subtree of the current node.

- For each node in the left subtree, repeat steps 1 and 2.

-

- Traverse the Right Subtree:

- Recursively perform a preorder traversal on the right subtree of the current node.

- For each node in the right subtree, repeat steps 1 and 2.

**Time complexity:** O(N), where N is the number of  nodes in the tree. Each node is visited once.

**Space complexity:** O(1), as we don’t need any extra space.

</details>
