# Search in BST

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BSTSEARCH |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary search trees |
| Official Link | [BSTSEARCH](https://www.codechef.com/learn/course/trees/BSTREES/problems/BSTSEARCH) |

---

## Problem Statement

Given a binary search tree and an integer **`X`**, search if **`X`** exists in the BST or not.

(**Note:** A binary search tree is a rooted binary tree data structure with the key of each internal node being greater than all the keys in the respective node's left subtree and less than the ones in its right subtree.)

For eg., the given tree is a binary search tree and we can easily search whether node $6$ exists in it or not.

![BSTSEARCH](https://cdn.codechef.com/images/learning/graphs-trees/bst-search.png)

## **Function Declaration**

### **Function Name**

$searchInBST$ – Searches for a given value in a Binary Search Tree (BST).

### **Parameters**

* $root$ : A pointer to the root node of the Binary Search Tree.
* $x$ : An integer value that needs to be searched in the BST.

### **Return Value**

* Returns a **boolean value**:

  * $true$ if the value $x$ exists in the BST.
  * $false$ otherwise.

---

## Input Format

- The first line of the input contains two space separated integer $N$ and $X$ — the number of nodes in the binary search tree and the node which we need to search.
- Next $N - 1$ lines contain three space separated characters $p_i, c_i, R_i$, describing the tree with edge informations - $p_i$ is an integer denoting the parent node of the $i$th edge, $c_i$ is child node, and the letter $R_i$ denotes whether the child is left child or right child, it's value is `L` if $c_i$ is left child of $p_i$, else `R`.

---

## Output Format

Output on a single line `YES` if $X$ is present in the given BST, otherwise `NO`.

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
2 1 L
2 3 R
6 5 L
6 7 R
```

**Output**

```text
YES
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** Binary Search Trees, BinaryTree traversal.

**Problem:-**  Given a binary search tree and an integer X, search if X exists in the BST or not.

(*Note*: A binary search tree is a rooted binary tree data structure with the key of each internal node being greater than all the keys in the respective node’s left subtree and less than the ones in its right subtree.)

**Solution Approach:-**

This problem can be solved using any of the normal binary tree traversal methods(inorder, preorder or postorder), however, an efficient search algorithm can be written using the BST property (The node value of any node is greater than all nodes’ values in its left subtree and less than all nodes’ values in its right subtree.).

Hence, instead of going through each node to match the value with given X, we can prune the search by going only in required subtree (see the code for more clarification). What we mean is if X is greater than the root node’s value, then search in the right subtree else search it in the left subtree.

**Time complexity :-** O(N), because in the worst case, the algorithm might visit all the nodes in the given BST.

**Space complexity :-**  O(1), as no extra space is needed.

</details>
