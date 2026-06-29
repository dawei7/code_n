# Check for BST

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BSTCHECK |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary search trees |
| Official Link | [BSTCHECK](https://www.codechef.com/learn/course/trees/BSTREESPRO/problems/BSTCHECK) |

---

## Problem Statement

Check if the given binary tree is a valid Binary Search Tree (BST).

A valid BST adheres to the following criteria:

1. The left subtree of a node comprises only nodes with keys less than the node's key.
2. The right subtree of a node comprises only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be valid Binary Search Trees.

For eg., the given binary tree is a valid BST.

![BSTSEARCH](https://cdn.codechef.com/images/learning/graphs-trees/bst-search.png)

## Function Declaration

### Function Name

$isBST$ – This function checks whether the given binary tree is a valid Binary Search Tree (BST).

### Parameters

* $root$ : A pointer to the root node of the binary tree

  * Each node is defined as:

    ```cpp
    struct Node {
        int val;
        Node *left;
        Node *right;
    };
    ```

### Return Value

* The function does **not return any value**.
* It should **print**:

  * `"YES"` if the binary tree is a valid Binary Search Tree
  * `"NO"` otherwise

## Constraints

* $1 \leq N \leq 10000$
* $1 \leq p_i, c_i \leq 100000$
* $R_i \in {L, R}$
* All node values are **distinct**
* The input represents a **valid binary tree structure**

---

## Input Format

* The first line contains a single integer $N$ — the number of nodes in the binary tree.
* The next $N - 1$ lines each contain three space-separated values:

  * $p_i$ — parent node value
  * $c_i$ — child node value
  * $R_i$ — either `L` or `R`, indicating whether the child is a left or right child

---

## Output Format

* Output a single line:

  * `"YES"` if the binary tree satisfies all Binary Search Tree properties
  * `"NO"` otherwise

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
YES
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** Binary Search Trees, BT traversals.

**Problem :-** Check if the given binary tree is a valid Binary Search Tree (BST).

A valid BST adheres to the following criteria:

- The left subtree of a node comprises only nodes with keys less than the node’s key.

- The right subtree of a node comprises only nodes with keys greater than the node’s key.

- Both the left and right subtrees must also be valid Binary Search Trees.

**Solution Approach :-**

To check if a binary tree is a valid BST, we can use a recursive approach. The key observation is that for each node, its value must be within a specific range. The left subtree of a node must have values less than the node’s value, and the right subtree must have values greater than the node’s value. These ranges change as we traverse down the tree.

Please take a deeper look at the solution to understand this.

**Time complexity :-** O(N), because in the worst case, the algorithm visits all the nodes in the given BST.

**Space complexity :-** O(1), as no extra space is needed.

</details>
