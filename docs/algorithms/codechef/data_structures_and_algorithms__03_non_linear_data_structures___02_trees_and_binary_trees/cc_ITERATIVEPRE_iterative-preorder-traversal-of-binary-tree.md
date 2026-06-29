# Iterative Preorder Traversal of Binary Tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ITERATIVEPRE |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [ITERATIVEPRE](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/ITERATIVEPRE) |

---

## Problem Statement

You are given the level-order representation of a binary tree (with `null` representing missing nodes).
Your task is to print the **preorder traversal** (Root → Left → Right) of the binary tree.

#### Follow-up

The recursive approach is simple — can you implement it **iteratively** using a stack?

## **Function Declaration**

### **Function Name**

$preorderTraversal$

### **Parameters**

* $root$ : A pointer/reference to the root node of the binary tree.

### **Return Value**

* Returns an **array of integers**.

## Constraints:
- $1 \leq T \leq 10$
- $0 \leq N \leq 100$
- $-100 \leq \text{Node.val} \leq 100$
- The input represents a valid binary tree structure.

**The input and output formats given below are only if you want to test using custom inputs.**

---

## Input Format

* The first line contains an integer $T$, the number of test cases.
* For each test case:

  * The first line contains an integer $N$, the number of elements in the array.
  * The second line contains $N$ elements representing the **level-order traversal** of the binary tree.
    Use $null$ to denote a missing (non-existent) child.

---

## Output Format

For each test case, print the preorder traversal of the tree as space-separated values.

---

## Examples

**Example 1**

**Input**

```text
2
7
5 3 8 1 4 null 9
7
10 6 15 3 8 12 20
```

**Output**

```text
5 3 1 4 8 9
10 6 3 8 15 12 20
```

**Explanation**

Test case 1:

```
        5
       / \
      3   8
     / \   \
    1   4   9
```

Preorder traversal ? `[5, 3, 1, 4, 8, 9]`

Test case 2:

```
         10
        /  \
       6    15
      / \   / \
     3   8 12 20
```

Preorder traversal ? `[10, 6, 3, 8, 15, 12, 20]`

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7
5 3 8 1 4 null 9
```

**Output for this case**

```text
5 3 1 4 8 9
```



#### Test case 2

**Input for this case**

```text
7
10 6 15 3 8 12 20
```

**Output for this case**

```text
10 6 3 8 15 12 20
```



**Example 2**

**Input**

```text
1
5
1 null 2 null 3
```

**Output**

```text
1 2 3
```

**Explanation**

```
1
 \
  2
   \
    3
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#### **Problem Understanding**

You are given the root of a binary tree and are asked to return the **preorder traversal** of its nodes’ values.

In **preorder traversal**, the nodes are visited in the following order:

1. **Root**
2. **Left subtree**
3. **Right subtree**

For example, if the tree is:

```
      1
       \
        2
       /
      3
```

Then the preorder traversal is **[1, 2, 3]**.

---

#### **Input Format**

1. The first line contains an integer `T` — the number of test cases.
2. For each test case:

   * An integer `N` — the number of nodes in the tree.
   * `N` elements representing the tree in **level-order format**, where `"null"` represents a missing child.

Example:

```
1
7
1 null 2 3
```

---

#### **Output Format**

For each test case, output the preorder traversal of the tree on a new line.

---

#### **Approach**

There are two common approaches to perform preorder traversal:

---

### **1. Recursive Approach**

This is the most intuitive method.

* Visit the current node.
* Recursively traverse the left subtree.
* Recursively traverse the right subtree.

**Algorithm:**

1. If the current node is `null`, return.
2. Add the current node’s value to the result.
3. Recur for the left child.
4. Recur for the right child.

**Time Complexity:**
`O(N)` — each node is visited once.

**Space Complexity:**
`O(H)` — due to recursive call stack (where `H` is the height of the tree).

---

### **2. Iterative Approach (Using Stack)**

The recursive method is simple but can cause stack overflow for deep trees.
An iterative approach using an explicit **stack** avoids recursion.

**Algorithm:**

1. Create an empty stack and push the root node.
2. While the stack is not empty:

   * Pop the top node.
   * Record its value.
   * Push the right child (if it exists).
   * Push the left child (if it exists).
3. The recorded values form the preorder traversal.

**Reason for pushing right first:**
Since the stack is **LIFO**, pushing the right child first ensures the left child is processed first, maintaining preorder order (Root → Left → Right).

**Time Complexity:**
`O(N)` — every node is visited exactly once.

**Space Complexity:**
`O(N)` — stack may hold up to all nodes in worst case (skewed tree).

---

#### **Tree Construction**

The input is given in **level-order format**, which means nodes are read level by level:

* The first value is the root.
* Next values represent left and right children of each node in sequence.
* `"null"` indicates that the corresponding child is missing.

You can construct the tree using a queue:

1. Start with the root node.
2. For each node in the queue, assign left and right children sequentially using remaining elements.
3. Skip `"null"` values appropriately.

---

#### **Example Walkthrough**

**Input:**

```
1
7
1 2 3 4 5 null 8
```

**Tree formed:**

```
       1
     /   \
    2     3
   / \     \
  4   5     8
```

**Preorder traversal:**

```
[1, 2, 4, 5, 3, 8]
```

---

#### **Edge Cases**

1. **Empty Tree:**
   Input: `[]` → Output: `[]`

2. **Single Node:**
   Input: `[1]` → Output: `[1]`

3. **Tree with Null Children:**
   Input: `[1, null, 2, 3]` → Output: `[1, 2, 3]`

4. **Complete Tree:**
   Input: `[1, 2, 3, 4, 5, 6, 7]` → Output: `[1, 2, 4, 5, 3, 6, 7]`

5. **Skewed Tree:**
   Input: `[1, null, 2, null, 3]` → Output: `[1, 2, 3]`

---

#### **Conclusion**

* **Recursive** approach is shorter and easier to understand.
* **Iterative** approach is safer for large trees and avoids stack overflow.
* Both achieve the same time complexity of `O(N)`.

The key to solving this problem efficiently lies in understanding **tree traversal order** and **managing traversal state** (whether through recursion or explicit stacks).

</details>
