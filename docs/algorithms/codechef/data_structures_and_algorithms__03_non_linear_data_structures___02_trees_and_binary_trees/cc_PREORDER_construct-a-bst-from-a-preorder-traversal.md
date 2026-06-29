# Construct a BST from a preorder traversal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREORDER |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary search trees |
| Official Link | [PREORDER](https://www.codechef.com/learn/course/trees/BSTREESPRO/problems/PREORDER) |

---

## Problem Statement

You are given an array of integers `preorder`, which represents the **preorder traversal** of a **Binary Search Tree (BST)**.
Your task is to **construct the BST** from this traversal and return the **root node** of the tree.

It is **guaranteed** that a valid BST can always be constructed from the given `preorder` traversal.

A **Binary Search Tree (BST)** is a binary tree where:

* Every node’s left child and its descendants have values **less than** the node’s value.
* Every node’s right child and its descendants have values **greater than** the node’s value.

A **preorder traversal** of a binary tree visits:

1. The node itself,
2. Then its left subtree,
3. Then its right subtree.

---
### Function Declaration

- **Function Name**
  - $bstFromPreorder$

- **Parameters**
  - $preorder$: A list (or array) of integers representing the preorder traversal of a Binary Search Tree (BST).

- **Return Value**
  - Returns the root node of the Binary Search Tree constructed from the given preorder traversal.

---
### Constraints
* $1 \leq T \leq 10$
* $1 \leq N \leq 100$
* $1 \leq \text{preorder}[i] \leq 1000$
* All elements in each `preorder` are **unique**.

---

---

## Input Format

* The first line contains a single integer $T$, denoting the number of test cases.
* Each test case consists of **two lines of input**:

  * The first line contains a single integer $N$ — the number of nodes in the preorder traversal.
  * The second line contains $N$ space-separated integers representing the **preorder traversal** of the BST.

---

---

## Output Format

* For each test case, output on a new line the **level-order traversal** of the constructed BST.
* Print all node values separated by spaces.

---

---

## Examples

**Example 1**

**Input**

```text
2
7
6 3 1 4 9 7 10
3
5 2 8
```

**Output**

```text
6 3 9 1 4 7 10
5 2 8
```

**Explanation**

For the first test case, the BST constructed from preorder `[6,3,1,4,9,7,10]` is:

```
        6
       / \
      3   9
     / \  / \
    1  4 7  10
```

Its level order traversal is `[6,3,9,1,4,7,10]`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7
6 3 1 4 9 7 10
```

**Output for this case**

```text
6 3 9 1 4 7 10
```



#### Test case 2

**Input for this case**

```text
3
5 2 8
```

**Output for this case**

```text
5 2 8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Overview

You are given an array representing the **preorder traversal** of a Binary Search Tree (BST).
The task is to reconstruct the BST and return its root.

A **Binary Search Tree (BST)** satisfies:

* All values in the left subtree of a node are strictly smaller than the node’s value.
* All values in the right subtree are strictly greater than the node’s value.

**Preorder traversal** means:
Visit the root first, then the left subtree, and then the right subtree.

---

## Intuition

In preorder traversal, the first element is always the root of the BST.

For example:
`[8, 5, 1, 7, 10, 12]`

* `8` is the root.
* Elements smaller than `8` (`5, 1, 7`) form the left subtree.
* Elements greater than `8` (`10, 12`) form the right subtree.

This observation reflects the recursive nature of BST construction.

---

## Naive Approach (Recursive Splitting)

### Idea

1. Take the first element as the root.
2. Split the remaining list into two parts:

   * Left subtree → elements smaller than the root.
   * Right subtree → elements larger than the root.
3. Recursively build the left and right subtrees.

### Complexity

* **Time:** O(N²), because each recursion may scan the remaining elements.
* **Space:** O(N²), due to repeated array slicing.

This approach is simple but inefficient for large inputs.

---

## Optimized Approach (Using Value Boundaries)

### Key Idea

Use the nature of preorder traversal.
Maintain:

* A global index `i` for the current node in the preorder array.
* A variable `bound` to limit the maximum value allowed in the current subtree.

### Algorithm

1. Start with `bound = +∞` and `i = 0`.
2. If the current value is greater than `bound`, return `NULL` (it does not belong to this subtree).
3. Otherwise:

   * Create a node with the current value.
   * Increment `i`.
   * Recursively build the left subtree with `bound = node.value`.
   * Recursively build the right subtree with the previous bound.

### Complexity

* **Time:** O(N), since each node is processed once.
* **Space:** O(H), where H is the height of the tree (recursion depth).

This method is efficient and elegant but can cause stack overflow for very deep trees (e.g., skewed ones).

---

## Iterative Approach (Stack-Based)

The recursive method can fail for large skewed trees due to deep recursion.
An iterative method using a stack avoids this problem.

### Algorithm

1. Create the root from the first element.
2. Push the root onto a stack.
3. For each next element:

   * If it is smaller than the top of the stack, it becomes the left child.
   * Otherwise, pop elements from the stack until the top has a greater value.
     The last popped node becomes the parent, and the current element becomes its right child.
4. Push the new node onto the stack.

### Complexity

* **Time:** O(N)
* **Space:** O(N)

This approach is efficient and safe for large inputs.

---

## Example Walkthrough

Input:
`preorder = [8, 5, 1, 7, 10, 12]`

| Step | Stack (top at right) | Action                                      |
| ---- | -------------------- | ------------------------------------------- |
| 1    | [8]                  | 8 is the root                               |
| 2    | [8, 5]               | 5 < 8 → left child                          |
| 3    | [8, 5, 1]            | 1 < 5 → left child                          |
| 4    | [8, 5]               | 7 > 5 → pop 1, attach 7 as right child of 5 |
| 5    | [8, 10]              | 10 > 8 → right child of 8                   |
| 6    | [8, 10, 12]          | 12 > 10 → right child of 10                 |

Resulting BST:

```
        8
       / \
      5   10
     / \    \
    1   7    12
```

---

## Edge Cases

1. **Single element**
   Input: `[5]`
   Output: Tree with one node.

2. **Strictly increasing sequence**
   Input: `[1, 2, 3, 4, 5]`
   Output: Skewed right tree (like a linked list).

3. **Strictly decreasing sequence**
   Input: `[5, 4, 3, 2, 1]`
   Output: Skewed left tree.

4. **Mixed order**
   Input: `[10, 5, 2, 7, 15, 12, 20]`
   Output: Balanced BST.

5. **Large input (stress test)**
   Random or increasing order with up to 50,000 nodes to test performance and memory.

---

## Summary

| Approach                  | Time  | Space | Handles Large Inputs | Notes                           |
| ------------------------- | ----- | ----- | -------------------- | ------------------------------- |
| Recursive Split           | O(N²) | O(N²) | No                   | Easy to understand              |
| Recursion with Boundaries | O(N)  | O(H)  | Partially            | May overflow for large depth    |
| Iterative (Stack)         | O(N)  | O(N)  | Yes                  | Fast, reliable, and memory-safe |

---

## Conclusion

The main insight is that the **preorder traversal alone** provides enough information to reconstruct a BST in **linear time** if we use value boundaries or a stack.

Understanding the relationship between traversal order and BST properties allows efficient reconstruction of the tree structure without any auxiliary arrays or complex data structures.

</details>
