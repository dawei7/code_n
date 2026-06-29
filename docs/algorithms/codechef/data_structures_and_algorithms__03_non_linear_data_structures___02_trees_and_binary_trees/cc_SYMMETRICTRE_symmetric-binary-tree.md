# Symmetric binary tree

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SYMMETRICTRE |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary Trees |
| Official Link | [SYMMETRICTRE](https://www.codechef.com/learn/course/trees/BTREESPRO/problems/SYMMETRICTRE) |

---

## Problem Statement

You are given the **root** of a binary tree.
Your task is to **determine whether the tree is symmetric**, meaning it is a mirror reflection of itself around its center.

---

### Function Declaration

- **Function Name**
  - $isSymmetric$

- **Parameters**
  - $root$: The root node of the binary tree.

- **Return Value**
  - Returns a boolean value — `true` if the binary tree is symmetric (a mirror of itself), otherwise `false`.

---
### Constraints
- The number of nodes in the tree is in the range $[1, 1000]$.
- Each node’s value lies in the range $-100 \leq \text{Node.val} \leq 100$.

---

---

## Input Format

* The first line contains a single integer $T$, denoting the number of test cases.
* Each test case consists of **two lines of input**:

  * The first line contains a single integer $N$ — the number of nodes in the binary tree.
  * The second line contains $N$ space-separated values representing the **level-order traversal** of the tree.
    Use **`null`** (or `-1` if preferred) to denote missing children.

---

---

## Output Format

For each test case, output on a new line either:

* `true`  — if the binary tree is symmetric
* `false` — otherwise

---

---

## Constraints

- The number of nodes in the tree is in the range $[1, 1000]$.
- Each node’s value lies in the range $-100 \leq \text{Node.val} \leq 100$.

---

## Examples

**Example 1**

**Input**

```text
2
7
1 2 2 null 5 5 null
7
1 2 2 null 3 null 4
```

**Output**

```text
true
false
```

**Explanation**

* For first test case
```
        1
      /   \
     2     2
      \   /
       5  5
```

The left and right subtrees are mirror images of each other.

* For second test case
The tree looks like this:

```
        1
      /   \
     2     2
      \     \
       3     4
```

The structure is not symmetric.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7
1 2 2 null 5 5 null
```

**Output for this case**

```text
true
```



#### Test case 2

**Input for this case**

```text
7
1 2 2 null 3 null 4
```

**Output for this case**

```text
false
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### **Problem Summary**

You are given a binary tree. The task is to determine whether the tree is **symmetric**, i.e., it is a mirror of itself around its center.

A tree is symmetric if:

* The left and right subtrees are mirror images.
* Both structure and node values must match when mirrored.

---

### **Understanding the Problem**

Consider a tree:

```
        1
      /   \
     2     2
    / \   / \
   3  4  4   3
```

* This tree is symmetric because:

  * Left subtree (2 → 3,4) is the mirror of the right subtree (2 → 4,3).
  * Node values match in mirrored positions.

Now consider:

```
        1
      /   \
     2     2
      \      \
       3      3
```

* Not symmetric because:

  * The left and right subtrees don’t have the same structure in mirrored positions.

---

### **Approach**

#### **1. Recursive Approach (Natural and Simple)**

We can define a helper function `isMirror(left, right)`:

1. **Base cases**:

   * Both `left` and `right` are `null` → return true.
   * One is `null` and the other is not → return false.
   * Values at `left` and `right` nodes are different → return false.

2. **Recursive case**:

   * Check that the **left child of left subtree** is a mirror of the **right child of right subtree**, AND
   * The **right child of left subtree** is a mirror of the **left child of right subtree**.

**Time complexity:** O(N) — every node is visited once
**Space complexity:** O(H) — recursion stack, H = height of the tree (≤ N)

---

#### **2. Iterative Approach (Using Queue)**

* Use a queue (or stack) to store pairs of nodes to compare.
* Start with `(root.left, root.right)`.
* While queue is not empty:

  1. Pop a pair `(a, b)`.
  2. If both are null, continue.
  3. If one is null or values differ → return false.
  4. Push children in mirrored order:

     * `(a.left, b.right)`
     * `(a.right, b.left)`
* If all pairs match → return true.

**Time complexity:** O(N)
**Space complexity:** O(N) for the queue in the worst case.

---

### **Input/Output Notes**

* Input is often given as **level-order array** (with `"null"` for missing nodes).
* Convert the array into a tree first, then run the symmetry check.
* Output: `true` if symmetric, `false` otherwise.

---

### **Edge Cases to Consider**

1. **Single node tree** → symmetric.
2. **Empty tree** → symmetric (depending on definition).
3. **Tree with only left or right subtree** → not symmetric.
4. **Trees with `null`s in between nodes** → check structure carefully.
5. **Large trees** → recursion depth can reach N, iterative approach avoids stack overflow.

---

### **Summary**

* The problem is about **mirror symmetry in binary trees**.
* Recursive solution is intuitive and elegant.
* Iterative solution is safer for very deep trees.
* Complexity is **O(N)** in both approaches, which is efficient for N ≤ 1000 nodes.

</details>
