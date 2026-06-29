# Create BST from given sorted array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BSTCREATE |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary search trees |
| Official Link | [BSTCREATE](https://www.codechef.com/learn/course/trees/BSTREESPRO/problems/BSTCREATE) |

---

## Problem Statement

Create a height-balanced binary search tree from the given sorted integer array.

(**Note:** A height-balanced binary tree is defined as a binary tree in which the depth difference between the two subtrees of every node is never more than one.)

For eg., the BST that can be created from the sorted array [1, 2, 3, 4, 5, 6, 7] is as follows:

![BSTSEARCH](https://cdn.codechef.com/images/learning/graphs-trees/bst-search.png)

---

## Input Format

- The first line of the input contains s single integer $N$ — the number of integers in the sorted array.
- Next line contains $N$ space separated sorted integers of the array.

---

## Output Format

Complete the given function which returns the root of created BST.

---

## Constraints

- $1 \leq N \leq 10000$
- $1 \leq nums_i \leq 100000$

---

## Examples

**Example 1**

**Input**

```text
13
13 26 54 59 69 71 76 78 84 91 95 96 100
```

**Output**

```text
Successfully created BST!
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites :-** Binary Search Trees.

**Problem :-** Create a height-balanced binary search tree from the given sorted integer array.

(*Note*: A height-balanced binary tree is defined as a binary tree in which the depth difference between the two subtrees of every node is never more than one.)

**Solution Approach :-**

To create a height-balanced binary search tree (BST) from a sorted array, the key idea is to choose the middle element as the root of the tree. This ensures that the tree remains balanced, as it divides the array into two halves, and each half can then be recursively used to create the left and right subtrees.

Algorithm:

- 1.Check the base cases:

- If the array is empty, return NULL (empty tree).

- If the array has only one element, create a new node with that value and return it.

- 2.Calculate the middle index of the array.

- 3.Create a new node with the value at the middle index as the root.

- 4.Recursively apply the algorithm to the left and right halves of the array:

- For the left subtree, use the elements from the beginning of the array up to the middle index (exclusive).

- For the right subtree, use the elements from the middle index + 1 to the end of the array.

5.Set the left and right pointers of the root node to the nodes obtained from the recursive calls on the left and right halves.

6.Return the root node.

**Time complexity:** O(N), because the algorithm creates all the nodes from the given sorted array.

**Space complexity:** O(N),  because the algorithm creates all the nodes from the given sorted array.

</details>
