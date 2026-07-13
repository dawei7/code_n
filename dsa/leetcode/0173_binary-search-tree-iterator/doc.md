# Binary Search Tree Iterator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 173 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-search-tree-iterator/) |

## Problem Description
### Goal
Design an iterator over a binary search tree that exposes its nodes in inorder, which yields values from smallest to largest under the tree's ordering. Constructing the iterator establishes its initial position before any value has been returned.

`next()` must advance and return the next smallest remaining value, while `hasNext()` reports whether such a value exists without consuming it. Process repeated calls against the same iterator state; `next()` is invoked only when another node is available. Avoid materializing the complete traversal: use $O(h)$ memory for tree height `h`, with construction and operations meeting the required amortized efficiency.

### Function Contract
**Inputs**

- `root`: a `TreeNode` encoded as a level-order list
- `operations`: calls beginning with `BSTIterator`, followed by `next` and `hasNext`

**Return value**

A result list aligned with operations: `None` for construction, the next integer for next, and a boolean for hasNext.

### Examples
**Example 1**

- Input: `root = [7,3,15,null,null,9,20]`
- Output sequence from next calls: `3,7,9,15,20`

**Example 2**

- Input: `root = [1]`
- Output: first hasNext is true, next is `1`, final hasNext is false

**Example 3**

- Input: `root = []`
- Output: hasNext is false

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

An inorder traversal of a binary search tree produces values in ascending order, but eagerly storing that entire traversal would use $O(n)$ memory. The iterator instead pauses an iterative inorder traversal and stores only the path needed to resume it.

At construction, descend from the root through left children, pushing every visited node. This **left spine** ends at the smallest node in the tree, so the stack top is exactly the first value to return. For an empty tree, the stack remains empty.

`next()` performs two actions:

1. Pop the stack top and return its value.
2. If that node has a right child, descend through the right child's entire left spine and push those nodes.

The second action matters because, after visiting a node in inorder, its right subtree is next—but the first node within that subtree is its leftmost descendant. No other part of the tree becomes newly eligible.

For `[7,3,15,null,null,9,20]`, initialization pushes `7` and then `3`. Popping `3` exposes `7`. Popping `7` introduces the right subtree by pushing `15` and then `9`, making `9` the next value. After `9`, the stack again exposes `15`; processing `15` pushes `20`. The iterator therefore emits `3, 7, 9, 15, 20` without materializing that sequence in advance.

At every public-method boundary, the stack top is the smallest unreturned node. Nodes below it are ancestors whose left side has been exhausted but whose own visit or right-side work is still pending. Consequently `hasNext()` needs only to test whether the stack is nonempty.

Initialization follows inorder's first step—repeatedly enter the left subtree—so the stack top is the smallest node. Assume before a call that the top is the next inorder node. Popping returns that node. If it has no right subtree, the next pending ancestor is already exposed. If it has a right subtree, pushing that subtree's left spine places its smallest node on top, which is exactly inorder's next node. Thus the property is restored after every call. By induction, `next()` returns every node exactly once in ascending order, and the stack is empty exactly when no node remains.

#### Complexity detail

A single `next()` may push as many as `h` nodes, but each tree node is pushed and popped exactly once over the iterator's lifetime. Therefore `next()` is $O(1)$ amortized and `hasNext()` is worst-case $O(1)$. The stack contains at most one root-to-leaf path, using $O(h)$ space: $O(\log n)$ for a balanced tree and $O(n)$ for a skewed one.

#### Alternatives and edge cases

- Precomputing the full inorder traversal gives worst-case constant-time calls but costs $O(n)$ construction time and memory even if the client consumes only a few values.
- Searching again from the root for every successor avoids a traversal buffer but can cost $O(h)$ per call and needs predecessor state.
- Morris traversal has $O(1)$ auxiliary space, but it temporarily rewires tree pointers and is awkward to suspend safely across iterator calls.
- An empty tree makes `hasNext()` false immediately. The contract assumes `next()` is called only when another value exists.

</details>
