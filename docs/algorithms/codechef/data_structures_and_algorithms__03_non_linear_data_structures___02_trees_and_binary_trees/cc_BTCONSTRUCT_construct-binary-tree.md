# Construct Binary Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BTCONSTRUCT |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [BTCONSTRUCT](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/BTCONSTRUCT) |

---

## Problem Statement

Construct and return a binary tree using two integer arrays, `preorder` and `inorder`. The `preorder` array represents the preorder traversal of the binary tree, while the `inorder` array represents the inorder traversal of the same tree.

**Example:** \
`Preorder` array: [1, 2, 3, 4, 5] \
`Inorder` array: [2, 1, 4, 3, 5]

The constructed tree

![BTCONSTRUCT](https://cdn.codechef.com/images/learning/graphs-trees/leve-order-traversal.png)

---

## Input Format

- The first line of the input contains a single integer $N$ — the number of nodes in the binary tree.
- The next line contains $N$ space separated integers, the preorder array.
- The next line contains $N$ space separated integers, the inorder array.

---

## Output Format

Complete the given function in the IDE which returns the root of the constructed binary tree.
Output will be `Well Done!` if the tree is constructed correctly, otherwise Runtime errors.

---

## Constraints

- $1 \leq N \leq 10000$
- $1 \leq preorder_i \leq 100000$
- $1 \leq inorder_i \leq 100000$

---

## Examples

**Example 1**

**Input**

```text
5
1 2 3 4 5
2 1 4 3 5
```

**Output**

```text

```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Binary trees, Binary tree traversal techniques.

**Problem:** Construct and return a binary tree using two integer arrays, preorder and inorder. The preorder array represents the preorder traversal of the binary tree, while the inorder array represents the inorder traversal of the same tree.

**Solution Approach:**

We need to understand preorder and postorder traversal first, and then go ahead.

Basic idea is:

preorder[0] is the root node of the tree.

preorder[`x`] is a root node of a sub tree.

In inorder traversal:

When inorder[index] is an item in the inorder traversal,

inorder[0]-inorder[index-1] are on the left subtree.

inorder[index+1]-inorder[size()-1] are on the right subtree.

if there is nothing on the left, that means the left child of the node is NULL

if there is nothing on the right, that means the right child of the node is NULL

*Algorithm:*

-

Start from rootIdx 0

-

Find preorder[rootIdx] from inorder, let’s call the index pivot

-

Create a new node with inorder[pivot]

-

Create its left child recursively

-

Create its right child recursively

-

return the created node.

**Time complexity:** O(N), as we need to iterate through each element of inorder and recursively

create the tree for each node as some subtree.

**Space complexity:** O(N), as creation for each node shall take O(N) space.

</details>
