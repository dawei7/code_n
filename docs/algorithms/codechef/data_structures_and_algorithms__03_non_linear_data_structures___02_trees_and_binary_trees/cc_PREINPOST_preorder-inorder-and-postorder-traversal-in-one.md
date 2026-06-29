# Preorder, Inorder, and Postorder Traversal in one 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREINPOST |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary search trees |
| Official Link | [PREINPOST](https://www.codechef.com/learn/course/trees/BSTREESPRO/problems/PREINPOST) |

---

## Problem Statement

You are given the root of a binary tree represented as an array in level order format.
Your task is to return **three traversals** of the binary tree:

1. **In-order Traversal**
2. **Pre-order Traversal**
3. **Post-order Traversal**

Each traversal should be returned as a list of integers.

---
### Function Declaration

- **Function Name**
  - $getTraversals$

- **Parameters**
  - $root$: A pointer to the root node of the binary tree.

- **Return Value**
  - Returns a 2D vector of integers containing **three traversals** of the binary tree in the following order:
    1. **In-order Traversal**
    2. **Pre-order Traversal**
    3. **Post-order Traversal**

---
### Constraints
- $ 1 \leq T \leq 10 $
- $ 1 \leq N \leq 10^5 $
- $ 0 \leq \text{Node.val} \leq 10^5 $
- $ (-1)$ denotes a null node

---

---

## Input Format

* The first line contains an integer **T**, the number of test cases.
* For each test case:

  * The first line contains an integer **N**, the number of elements in the array.
  * The second line contains **N** space-separated values, representing the tree in **level order**.
  * The value `-1` represents a **null** node.

---

---

## Output Format

[ [InOrder], [PreOrder], [PostOrder] ]

---

---

## Examples

**Example 1**

**Input**

```text
1
7
10 5 15 3 7 -1 18
```

**Output**

```text
[[3, 5, 7, 10, 15, 18], [10, 5, 3, 7, 15, 18], [3, 7, 5, 18, 15, 10]]
```

**Explanation**

The binary tree is:

```
        10
       /  \
      5    15
     / \     \
    3   7     18
```

* In-order: [3, 5, 7, 10, 15, 18]
* Pre-order: [10, 5, 3, 7, 15, 18]
* Post-order: [3, 7, 5, 18, 15, 10]

**Example 2**

**Input**

```text
1
7
1 2 3 -1 -1 4 5
```

**Output**

```text
[[2, 1, 4, 3, 5], [1, 2, 3, 4, 5], [2, 4, 5, 3, 1]]
```

**Explanation**

The binary tree is:

```
       1
      / \
     2   3
        / \
       4   5
```

* In-order: [2, 1, 4, 3, 5]
* Pre-order: [1, 2, 3, 4, 5]
* Post-order: [2, 4, 5, 3, 1]

**Example 3**

**Input**

```text
1
11
8 4 10 2 6 9 12 -1 -1 5 7
```

**Output**

```text
[[2, 4, 5, 6, 7, 8, 9, 10, 12], [8, 4, 2, 6, 5, 7, 10, 9, 12], [2, 5, 7, 6, 4, 9, 12, 10, 8]]
```

**Explanation**

The binary tree is:

```
          8
        /   \
       4     10
      / \    / \
     2   6  9  12
        / \
       5   7
```

* In-order: [2, 4, 5, 6, 7, 8, 9, 10, 12]
* Pre-order: [8, 4, 2, 6, 5, 7, 10, 9, 12]
* Post-order: [2, 5, 7, 6, 4, 9, 12, 10, 8]

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#### **Problem Restatement**

You are given the root of a binary tree.
Your task is to return three lists representing the **Inorder**, **Preorder**, and **Postorder** traversals of the tree.

---

#### **Understanding Tree Traversals**

A **binary tree traversal** defines the order in which nodes are visited.

1. **Inorder Traversal (Left → Root → Right)**

   * Visit the left subtree.
   * Visit the root node.
   * Visit the right subtree.

2. **Preorder Traversal (Root → Left → Right)**

   * Visit the root node first.
   * Then the left subtree.
   * Then the right subtree.

3. **Postorder Traversal (Left → Right → Root)**

   * Visit the left subtree first.
   * Then the right subtree.
   * Finally, the root node.

Each traversal provides a unique perspective of the tree structure.

---

#### **Example**

Consider the binary tree represented as:

```
Input array: [1, 2, 3, -1, -1, 4, 5]
```

This represents the tree:

```
        1
       / \
      2   3
         / \
        4   5
```

* **Inorder (Left → Root → Right):** [2, 1, 4, 3, 5]
* **Preorder (Root → Left → Right):** [1, 2, 3, 4, 5]
* **Postorder (Left → Right → Root):** [2, 4, 5, 3, 1]

---

#### **Approach**

1. **Tree Construction (Level Order)**

   * The input is given in level-order form.
   * `-1` represents a null node.
   * Use a queue to construct the tree by linking left and right children in order.

2. **Traversal Functions**

   * Use recursion to perform each traversal type.
   * Each function will visit nodes in its respective order and store their values in a list.

3. **Combining Results**

   * After all traversals are completed, combine them in a single list as:
     `[inorder, preorder, postorder]`.

4. **Output Formatting**

   * The result should follow the format:

     ```
     [[inorder], [preorder], [postorder]]
     ```

---

#### **Algorithm Steps**

1. Build the tree from the input array.
2. Define three traversal functions:

   * `inorder(node)`
   * `preorder(node)`
   * `postorder(node)`
3. For each traversal:

   * If the node is null, return.
   * Otherwise, visit nodes in the required order.
4. Store the results in separate lists.
5. Combine and print them in the expected format.

---

#### **Complexity Analysis**

* **Time Complexity:**
  ( O(N) )
  Each traversal visits every node exactly once.

* **Space Complexity:**
  ( O(H) )
  where ( H ) is the height of the tree (stack space for recursion).
  In the worst case (skewed tree), ( H = N ).

---

#### **Edge Cases**

1. Tree with only one node.
2. All nodes are `-1` (empty tree).
3. Perfect binary tree (all levels filled).
4. Skewed tree (left or right-heavy).
5. Large input size to test efficiency.

---

#### **Conclusion**

This problem tests understanding of tree traversal fundamentals.
The key challenge lies in:

* Building the tree correctly from level-order input.
* Implementing all three traversal strategies independently.

Once the tree is built, the traversal logic remains standard and consistent across all languages.

</details>
