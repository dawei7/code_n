# Insert a node in BST

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INSERTBST |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary search trees |
| Official Link | [INSERTBST](https://www.codechef.com/learn/course/trees/BSTREESPRO/problems/INSERTBST) |

---

## Problem Statement

You are given a Binary Search Tree (BST) and a value that needs to be inserted into this tree.
Your task is to insert the given value into the BST while maintaining all BST properties and return the resulting tree.
It is guaranteed that the value to be inserted does **not** already exist in the BST.

There may be multiple correct BST structures after insertion depending on how you traverse the tree.
Any valid BST that results from inserting the value is acceptable.

The BST will be provided in **level-order array format**, where `null` represents an empty child.

## Function Declaration

### Function Name

$insertIntoBST$ – Inserts a value into a Binary Search Tree (BST) while maintaining BST properties.

### Parameters

* $root$ : Pointer to the root of the Binary Search Tree.
* $val$ : Integer value that needs to be inserted into the BST.

### Return Value

Returns a pointer to the root of the updated BST after inserting the given value. You don't need to print anything in this question.

## Constraints:
- $1 \leq T \leq 1000$
- $0 \leq N \leq 10^{4}$
- $-10^{8} \leq \text{Node.val} \leq 10^{8}$
- $-10^{8} \leq \text{VAL} \leq 10^{8}$
- All node values in the tree are unique.
- The BST is given in level-order, and $\texttt{-1}$ represents a null node.
- It is guaranteed that $\text{VAL}$ does not exist in the original BST.
- The sum of $N$ over all test cases does not exceed $10^{4}$.

---

## Input Format

* The first line of input will contain a single integer **T**, denoting the number of test cases.
* Each test case consists of multiple lines of input:

  * The first line of each test case contains two space-separated integers
    **N** and **VAL** —
    where **N** is the number of nodes in the BST array representation and **VAL** is the value to be inserted.
  * The second line contains **N** space-separated elements representing the BST in **level-order**.
    Use **-1** to represent a `null` child.

---

## Output Format

For each test case, print the **level-order traversal** of the BST **after inserting** the value.
All `null` nodes must again be printed as **-1**.
Print each test case output on a new line.

---

## Examples

**Example 1**

**Input**

```text
2
5 12
8 5 15 2 7
6 9
5 2 13 1 4 -1 -1
```

**Output**

```text
8 5 15 2 7 12
5 2 13 1 4 9
```

**Explanation**

***First Test case:*** \
The value `12` is inserted as the left child of `15`.
Any equivalent valid BST representation is acceptable.
 \
***Second Test case:*** \
`9` is inserted as the left child of `13`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 12
8 5 15 2 7
```

**Output for this case**

```text
8 5 15 2 7 12
```



#### Test case 2

**Input for this case**

```text
6 9
5 2 13 1 4 -1 -1
```

**Output for this case**

```text
5 2 13 1 4 9
```



**Example 2**

**Input**

```text
1
7 3
10 4 20 1 6 15 30
```

**Output**

```text
10 4 20 1 6 15 30 -1 3
```

**Explanation**

Here, `3` becomes the left child of `1`.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## 1. Problem Summary

You are given the task of designing two functions:

1. `serialize(root)`
   Convert a binary tree into a sequence of values so that it can be stored or transmitted.

2. `deserialize(data)`
   Convert the stored representation back into the original binary tree structure.

There are no restrictions on the format as long as the tree reconstructed from the serialized data is exactly the same as the original tree.

This is an important problem because it captures how complex data structures can be transformed between in-memory and external representations without losing structure or meaning.

---

# 2. Key Idea

A binary tree node contains three pieces of information:

* value
* pointer to left child
* pointer to right child

The central challenge is encoding and decoding both the **values** and the **structure** of the tree.

The most reliable way is to record the tree in **level-order (breadth-first traversal)**, explicitly marking missing children (null pointers). This approach ensures that every node's position is preserved.

When we include null markers, the representation uniquely determines the entire tree.

---

# 3. Serialization Strategy (Level-Order)

### Why Level-Order

Level-order traversal naturally preserves the structure of the tree based on the parent-child relationships. Using a queue, we can visit each node in the exact order needed to rebuild the tree layer by layer.

### Process

1. Use a queue and perform BFS.
2. For every node:

   * Append its value to the output.
   * Append placeholders (such as `-1` or `null`) for missing children.
3. Continue until the entire tree has been processed.

This produces a sequence like:

```
1 2 3 4 -1 -1 5 -1 -1 -1 -1
```

Such a sequence contains enough information to reproduce the structure.

### Properties

* Linear time complexity: O(n)
* Linear space complexity: O(n)
* Works for all types of binary trees:

  * Complete
  * Perfect
  * Skewed
  * Sparse
  * Large or small

---

# 4. Deserialization Strategy

### Goal

Recreate the binary tree using the sequence generated during serialization.

### Process

1. Read the first element as the root.
2. Use a queue to reconstruct the tree level by level.
3. For each node dequeued:

   * Read next value as left child.
   * Read next value as right child.
   * If either value is a non-null placeholder, skip creating a node.
   * Otherwise, create node and push it into the queue.

### Why This Works

Because the serialization stored values and null-marks in fixed BFS order, the parent-child relationship is exactly reconstructable.

---

# 5. Complexity Analysis

### Time

* Serialization: O(n)
* Deserialization: O(n)

### Space

* Both operations use a queue, so O(n)

This is optimal since any solution must read or write each node at least once.

---

# 6. Edge Cases to Consider

You should always test the following scenarios:

1. Empty tree
2. Tree with a single node
3. Completely skewed left tree
4. Completely skewed right tree
5. Balanced tree
6. Tree containing repeated values
7. Tree where many interior nodes have null children
8. Very large tree
9. Trees containing negative values or zero
10. Random unbalanced trees

These ensure correct behavior across all structural patterns.

---

# 7. Why BFS-Based Serialization Is a Standard Choice

* Predictable
* Easy to implement
* No ambiguity
* Suitable for file or network transmission
* Works consistently across all binary tree shapes
* Can handle very large tree sizes without stack overflow (unlike recursive DFS)

Although DFS-based serialization (pre-order + null markers) is also valid, BFS remains more intuitive and widely used in platform problems requiring iterative tree construction.

---

# 8. Conclusion

The serialization and deserialization problem is a fundamental exercise in representing hierarchical data structures. Using BFS with explicit null markers ensures:

* Unambiguous reconstruction
* Linear complexity
* Compatibility with any binary tree configuration

This method is efficient, reliable, and scalable, making it the standard solution used in competitive programming and interviews.

</details>
