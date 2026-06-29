# Binary Search Tree Iterator

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BSTITERATOR |
| Difficulty Band | Trees and Binary trees |
| Path | Data Structures and Algorithms |
| Lesson | Binary search trees |
| Official Link | [BSTITERATOR](https://www.codechef.com/learn/course/trees/BSTREESPRO/problems/BSTITERATOR) |

---

## Problem Statement

You are required to implement a class **`BSTIterator`** that acts as an iterator over the **in-order traversal** of a **Binary Search Tree (BST)**.

---

### Class Definition

Implement the following methods:

1. **`BSTIterator(root)`**
   Initializes the iterator with the root of the BST.
   The iterator’s position starts *before* the smallest element in the tree (conceptually at a number smaller than all node values).

2. **`int next()`**
   Moves the iterator to the next node in the in-order sequence and returns its value. `next()` is never called when no next element exists.

3. **`boolean hasNext()`**
   Returns `true` if there are still elements left to traverse; otherwise, returns `false`.

---

#### Notes

* The iterator should perform **in-order traversal** of the BST (Left → Node → Right).
* The first call to `next()` should return the smallest element in the BST.
* You may assume that `next()` is never called when no next element exists.

#### Follow-Up

Can you implement `next()` and `hasNext()` such that:

* Each runs in **average O(1)** time, and
* The memory usage is **O(h)**, where *h* is the height of the tree?

---

## Input Format

* The first line contains a single integer **T**, the number of test cases.
* Each test case consists of **three lines**:

  1. The first line contains a single integer **N** — the number of nodes in the level-order representation of the BST.
  2. The second line contains **N space-separated integers** — the level-order traversal of the tree, where **-1 represents a null node**.
  3. The third line contains space-separated **operations**, each one being either:

     * `BSTIterator`
     * `next`
     * `hasNext`

---

## Output Format

For each test case:

* Print a single line containing the results of each operation in order:

  * `null` for `BSTIterator`
  * integer value for `next()`
  * `true` or `false` for `hasNext()`

Each output value is separated by a space.

---

## Constraints

- $1 \leq T \leq 10^5$
- The number of nodes in the tree is in the range $[1, 10^5]$.
- $0 \leq \text{Node.val} \leq 10^6$
- There will be at most $10^5$ calls to $\texttt{next()}$ and $\texttt{hasNext()}.$

---

## Examples

**Example 1**

**Input**

```text
1
7
7 3 15 -1 -1 9 20
BSTIterator next next hasNext next hasNext next hasNext next hasNext
```

**Output**

```text
null 3 7 true 9 true 15 true 20 false
```

**Explanation**

The BST structure from `arr1`:

```
        7
       / \
      3   15
         /  \
        9   20
```

The operations sequence (`arr2`) works as follows:

```
BSTIterator iterator = new BSTIterator([7, 3, 15, -1, -1, 9, 20]);
iterator.next();     // returns 3
iterator.next();     // returns 7
iterator.hasNext();  // returns true
iterator.next();     // returns 9
iterator.hasNext();  // returns true
iterator.next();     // returns 15
iterator.hasNext();  // returns true
iterator.next();     // returns 20
iterator.hasNext();  // returns false
```

Hence, the output is:

```
null 3 7 true 9 true 15 true 20 false
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Summary

You are given a Binary Search Tree (BST). You must design an iterator that returns the **next smallest element** in the BST each time `next()` is called. The iterator must also support a function `hasNext()` that returns whether more nodes remain to be visited.

The traversal order required is the **inorder traversal** of the BST.

The challenge:
Implement this functionality **efficiently**, both in terms of time and space.

---

## Key Insight

An inorder traversal of a BST yields values in **strictly increasing order**.
A naive solution would be to:

1. Perform a full inorder traversal first.
2. Store all values in an array.
3. Iterate through that array.

However, this uses **O(n)** extra memory and requires **O(n)** preprocessing time.

The optimal approach requires:

* **O(h)** space, where h = height of the tree
* **Amortized O(1)** time for each operation (`next` or `hasNext`)

This is done by simulating the inorder traversal using a **stack**, but performing only the necessary work when needed.

---

## Core Idea: Controlled Inorder Traversal

Instead of traversing the whole tree upfront, keep a stack that stores the path from the root down to the leftmost node of the current subtree. This ensures the smallest unvisited value is always on top of the stack.

### Initialization

Push all left children of the root into the stack.
Top of the stack now contains the next smallest element.

### next()

1. Pop the top element (this is the next smallest value).
2. If this node has a right child:

   * Move to that right child.
   * Push all its left children into the stack.

This ensures that the stack always contains the next unvisited nodes in the correct inorder sequence.

### hasNext()

`return stack is not empty`

---

## Why This Works

The stack always represents the current frontier of nodes whose left subtrees are fully processed but whose values are still pending. By pushing left chains and processing right subtrees on-demand, we guarantee correctness and optimal performance.

---

## Complexity Analysis

### Time Complexity

* `next()` and `hasNext()` run in **amortized O(1)** time.
* Each node is pushed to the stack once and popped once.

### Space Complexity

* At most **O(h)** entries in the stack, where h is the tree height.
* This is optimal.

---

## Common Pitfalls

### 1. Calling next() when hasNext() is false

This produces errors like "pop from empty stack".
Real testcases (like online judges) ensure that this **never happens**.
If the input includes such cases, the input itself is invalid.

### 2. Forgetting to process the right subtree correctly

After popping a node, failing to push the left chain of its right child breaks the inorder sequence.

### 3. Treating empty nodes incorrectly

If representing missing children using values like -1, ensure they do not become actual nodes in the tree.

---

## Summary

* Use a stack and simulate inorder traversal.
* On initialization, push the root and all left descendants.
* On `next()`, pop and process the right subtree’s left chain.
* Maintain O(h) space and amortized O(1) time.

</details>
