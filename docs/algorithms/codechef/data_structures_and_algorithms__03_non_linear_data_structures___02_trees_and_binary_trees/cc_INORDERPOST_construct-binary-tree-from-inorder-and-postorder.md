# Construct binary tree from Inorder and Postorder

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INORDERPOST |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [INORDERPOST](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/INORDERPOST) |

---

## Problem Statement

You are given two integer arrays, **`inorder`** and **`postorder`**, representing the inorder and postorder traversal sequences of a **binary tree**.
Your task is to **reconstruct the original binary tree** from these traversals and return its root.

---
### Function Declaration

- **Function Name**
  - $buildTree$

- **Parameters**
  - $inorder$: A vector of integers representing the inorder traversal of the binary tree.
  - $postorder$: A vector of integers representing the postorder traversal of the binary tree.

- **Return Value**
  - Returns a pointer to the root node of the reconstructed binary tree.

---
### Constraints
- $1 \leq \text{inorder.length} \leq 3000$
- $\text{postorder.length} = \text{inorder.length}$
- $-3000 \leq \text{inorder}[i], \text{postorder}[i] \leq 3000$
- All elements in $\texttt{inorder}$ and $\texttt{postorder}$ are $\textbf{unique}.$
- Each element of $\texttt{postorder}$ appears in $\texttt{inorder}.$
- The given arrays are $\textbf{valid traversals}$ of the same binary tree.

---

---

## Input Format

* The first line contains a single integer $T$, denoting the number of test cases.
* Each test case consists of **three lines of input**:

  * The first line contains a single integer $N$ — the number of nodes in the binary tree.
  * The second line contains $N$ space-separated integers representing the **inorder traversal** of the tree.
  * The third line contains $N$ space-separated integers representing the **postorder traversal** of the tree.

---

---

## Output Format

* For each test case, output on a new line the **Pre-Order Traversal** of the reconstructed binary tree.
* Print the node values separated by spaces.

---

---

## Examples

**Example 1**

**Input**

```text
1
7
4 2 5 1 6 3 7
4 5 2 6 7 3 1
```

**Output**

```text
1 2 4 5 3 6 7
```

**Explanation**

The binary tree constructed from the given traversals is:

```
        1
       / \
      2   3
     / \ / \
    4  5 6  7
```

**Example 2**

**Input**

```text
1
2
2 1
2 1
```

**Output**

```text
1 2
```

**Explanation**

The binary tree looks like:

```
    1
   /
  2
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem Summary

You are given two arrays representing the inorder and postorder traversals of a binary tree.
The goal is to reconstruct the original binary tree from these traversals.

---

### Key Observations

1. **Traversal Definitions:**

   * Inorder traversal: Left → Root → Right
   * Postorder traversal: Left → Right → Root

2. The last element of the postorder array is always the **root** of the tree.

3. Once you know the root, you can locate it in the inorder array.

   * Elements to the left form the left subtree.
   * Elements to the right form the right subtree.

4. The size of the left and right subtrees in inorder determines how postorder should be divided.

---

### Step-by-Step Logic

1. **Identify the Root**

   * The last element of the postorder segment is the root.

2. **Split the Inorder Traversal**

   * Find the index of the root in inorder.
   * Left side → Left subtree.
     Right side → Right subtree.

3. **Split the Postorder Traversal**

   * Excluding the root (last element), divide the remaining nodes into left and right parts according to subtree sizes.

4. **Recur for Left and Right Subtrees**

   * Build the right subtree first (since we move backward in postorder).
   * Then build the left subtree.

5. **Base Case**

   * If the segment range is invalid (no nodes left), return null.

---

### Example

**Inorder:** [9, 3, 15, 20, 7]
**Postorder:** [9, 15, 7, 20, 3]

| Step | Action                          | Inorder Split                   | Postorder Split                 |
| ---- | ------------------------------- | ------------------------------- | ------------------------------- |
| 1    | Root = 3                        | Left = [9], Right = [15, 20, 7] | Left = [9], Right = [15, 7, 20] |
| 2    | Build Right Subtree (root = 20) | Left = [15], Right = [7]        | Left = [15], Right = [7]        |
| 3    | Build Left Subtree (root = 9)   | Leaf node                       | —                               |

Resulting tree:

```
       3
      / \
     9  20
        / \
       15  7
```

---

### Complexity Analysis

| Type  | Complexity | Explanation                                                        |
| ----- | ---------- | ------------------------------------------------------------------ |
| Time  | O(N)       | Each node is processed once, and index lookup is O(1) using a map. |
| Space | O(N)       | Recursion stack plus hashmap for index lookups.                    |

---

### Common Mistakes

1. **Not using a hashmap** for inorder indices — causes O(N²) time complexity.
2. **Building left before right** — causes wrong construction when using postorder.
3. **Incorrect index boundaries** — leads to invalid recursion.
4. **Stack overflow** — for large skewed trees, recursion depth may exceed limits.

---

### Test Case Design

| Case | Description        | Example                                            |
| ---- | ------------------ | -------------------------------------------------- |
| 1    | Single node        | inorder = [1], postorder = [1]                     |
| 2    | Perfectly balanced | inorder = [2,1,3], postorder = [2,3,1]             |
| 3    | Left skewed        | inorder = [3,2,1], postorder = [3,2,1]             |
| 4    | Right skewed       | inorder = [1,2,3], postorder = [3,2,1]             |
| 5    | Random structure   | inorder = [9,3,15,20,7], postorder = [9,15,7,20,3] |
| 6    | Large tree         | n = 3000, random valid structure                   |

---

### Optimization Tips

* Use a **map** to store inorder indices for O(1) lookups.
* Traverse postorder from the end.
* Build **right subtree first** before left.
* Increase recursion limit if necessary for deep trees.

---

### Takeaway

The core concept is:

**Postorder provides the root, and inorder defines the structure.**

By combining the two traversals, the tree can be reconstructed in linear time with proper indexing and recursion.

</details>
