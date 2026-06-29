# Largest bst in binary tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LARGESTBST |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary search trees |
| Official Link | [LARGESTBST](https://www.codechef.com/learn/course/trees/BSTREESPRO/problems/LARGESTBST) |

---

## Problem Statement

You are given multiple test cases, each describing a binary tree.
For every test case, determine the **size (number of nodes)** of the **largest subtree** that is also a **Binary Search Tree (BST)**.

A **Binary Search Tree (BST)** follows these properties:

1. The left subtree of a node contains only nodes with values **less than** the node’s value.
2. The right subtree of a node contains only nodes with values **greater than** the node’s value.
3. Both the left and right subtrees must themselves be valid BSTs.

---
### Function Declaration

- **Function Name**
  - $largestBST$

- **Parameters**
  - $root$: A pointer to the root node of the binary tree.

- **Return Value**
  - Returns an integer representing the **size (number of nodes)** of the largest subtree that is a valid **Binary Search Tree (BST)**.

---
### Constraints
- $1 \leq T \leq 100 $
- $1 \leq N \leq 10^4 $
- $1 \leq \text{Node.val} \leq 10^5$

---

---

## Input Format

* The first line contains an integer **T** — the number of test cases.
* For each test case:

  * The first line contains an integer **N** — the number of nodes in the tree.
  * The next line contains **N** space-separated integers — the node values in **level-order** traversal of the binary tree (use `-1` to represent `null` or missing nodes).

---

---

## Output Format

For each test case, print a single integer — the size of the **largest BST subtree** in the given binary tree.

---

---

## Examples

**Example 1**

**Input**

```text
2
5
5 2 4 1 3
7
8 5 15 1 7 -1 20
```

**Output**

```text
3
6
```

**Explanation**

**Test Case 1:**
```
       5
      / \
     2   4
    / \
   1   3
```

The subtree `[2, 1, 3]` is a valid BST of size 3.

```
     2
    / \
   1   3
```

**Test Case 2:**
```
        8
       / \
      5   15
     / \    \
    1   7    20

```
The subtree `[8, 5, 15, 1, 7, -1, 20]` is the largest BST of size 6.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
5 2 4 1 3
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
7
8 5 15 1 7 -1 20
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem Overview

We are given a binary tree, and the task is to determine the size (number of nodes) of the largest subtree that forms a Binary Search Tree (BST).

A BST is defined as a binary tree where:

1. The left subtree of every node contains only values smaller than the node’s value.
2. The right subtree of every node contains only values greater than the node’s value.
3. Both the left and right subtrees must also be BSTs.

We must find the maximum number of nodes that can form such a valid BST within the given binary tree.

---

### Intuition and Observations

A naive approach might check every subtree to see if it forms a BST. However, this approach would have a time complexity of **O(N²)** since each subtree check could traverse multiple nodes.

We can solve this efficiently using a **bottom-up recursive traversal (postorder)**.
At each node, we gather information from its left and right subtrees and decide whether the current subtree forms a valid BST.

For each node, we need:

* Whether its left subtree is a BST.
* Whether its right subtree is a BST.
* The maximum value in the left subtree.
* The minimum value in the right subtree.
* The size of the largest BST found so far.

---

### Core Idea

For a node to be the root of a valid BST:

1. Both left and right subtrees must be BSTs.
2. The current node’s value must be greater than the maximum value of the left subtree and smaller than the minimum value of the right subtree.

Formally:

```
if left_is_bst and right_is_bst and left_max < node.val < right_min:
    current subtree is a BST
```

If this condition is satisfied,

```
current_bst_size = left_size + right_size + 1
```

Otherwise, this node’s subtree is not a BST, and we take the maximum size found in its children.

---

### Algorithm (Language-Neutral Steps)

1. **Base Case:**
   If the node is null (empty), return that it is a BST with size `0`, min = +∞, max = −∞.

2. **Recursive Case:**

   * Recursively call the function for the left and right children.
   * From each call, retrieve whether the subtree is a BST, its size, min, and max values.
   * Check if the current node satisfies the BST condition using this information.

3. **If valid BST:**

   * Compute the size of the current subtree.
   * Update the global maximum BST size.
   * Return `(isBST=True, size, new_min, new_max)`.

4. **If not valid:**

   * Return `(isBST=False, size_of_largest_child_BST, 0, 0)`.

5. After processing all nodes, the global maximum holds the answer.

---

### Time and Space Complexity

* **Time Complexity:** O(N), since each node is visited exactly once.
* **Space Complexity:** O(H), where H is the height of the tree (due to recursion stack).

  * Worst case: O(N) for skewed trees.
  * Average case: O(log N) for balanced trees.

---

**Example**

Consider the binary tree:

```
        5
       / \
      2   4
     / \
    1   3
```

Steps:

* Subtrees rooted at 1 and 3 are BSTs of size 1.
* Subtree rooted at 2: left_max < 2 < right_min → valid BST of size 3.
* Subtree rooted at 4: single node BST of size 1.
* The subtree rooted at 5 is **not** a BST because `5 < right_min` fails (right_min = 4).
* Therefore the largest BST is the subtree rooted at 2 with size 3.

Result: **Largest BST size = 3**.

---

### Edge Cases to Consider

1. **Single-node tree:** Always a BST (size 1).
2. **All nodes have equal values:** Only one node can form a BST (size 1).
3. **Skewed tree:** Should still return correct size depending on ordering.
4. **Tree with some invalid subtrees:** Should correctly skip non-BST regions.
5. **Empty tree:** Size 0.

---

### Summary

* The problem is solved efficiently using postorder traversal.
* Each recursive step computes all necessary information in constant time.
* The algorithm maintains a global maximum to track the largest BST found.
* The approach works across languages since it relies purely on tree traversal logic, not syntax or specific language features.

</details>
