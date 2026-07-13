# Convert Sorted List to Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 109 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Divide and Conquer, Tree, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/) |

## Problem Description
### Goal
Given the head of a singly linked list whose values are sorted in ascending order, construct a binary search tree containing every list element exactly once. The resulting node values must obey binary-search ordering throughout the entire tree, not only between each parent and its immediate children.

The tree must be height-balanced, meaning the left and right subtree heights differ by at most one at every node. Several balanced shapes may be valid, so the exact root is not prescribed when multiple choices work. Do not lose or duplicate repeated-position list nodes, and return `null` when the input list is empty.

### Function Contract
**Inputs**

- `head`: the head of a sorted linked list, encoded as a `List[int]` in app cases

**Return value**

A height-balanced `TreeNode` root. Multiple valid shapes may exist; app results are checked by values, ordering, and balance.

### Examples
**Example 1**

- Input: `head = [-10, -3, 0, 5, 9]`
- Output: a valid balanced BST such as `[0, -3, 9, -10, null, 5]`

**Example 2**

- Input: `head = []`
- Output: `[]`

**Example 3**

- Input: `head = [1, 3]`
- Output: either `[3, 1]` or `[1, null, 3]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(\log n)$

<details>
<summary>Approach</summary>

#### General

**Subtree sizes replace random access to a linked-list midpoint**

First traverse the list once to count `n`. The count lets recursion divide an inorder sequence by size without locating middle list nodes repeatedly. Keep a shared cursor at the list head; it will advance exactly once per constructed tree node.

**Simulate inorder construction while the list cursor moves forward**

To build `size` nodes, reserve `left_size = size // 2` for the left subtree and recursively construct it first. The cursor then points to the next inorder value, which must be this subtree's root. Create the root, advance the cursor once, and build `size - left_size - 1` right-subtree nodes.

This order matches left-root-right traversal and never needs to move the singly linked cursor backward.

**Each call consumes one consecutive list segment**

On entry to `build(size)`, the cursor points to the first value assigned to that subtree. The call returns a height-balanced BST containing exactly the next `size` values and leaves the cursor at the first unused list node. Its inorder traversal is precisely the consumed segment.

**Trace cursor movement through a two-node interval**

For `[1, 3]`, build one left node from `1`, then use `3` as the root and build an empty right side. The result `[3, 1]` is balanced and its inorder traversal reproduces the list.

**Inorder consumption matches the recursive size partition**

For a segment of known size, recursion first consumes exactly the left-subtree count. The cursor then points to the next sorted value, which must be the root, and the remaining designated values build the right subtree.

This inorder consumption places every left key before and below the root and every right key after and above it. Splitting counts as evenly as possible keeps subtree sizes within one, so the recursively constructed BST is balanced and contains every list node value once.

#### Complexity detail

One pass counts nodes and one cursor advance creates each output node, giving $O(n)$ time. Balanced recursion has depth $O(\log n)$; output tree nodes are excluded from auxiliary space.

#### Alternatives and edge cases

- **Copy values into an array:** is also $O(n)$ time but uses $O(n)$ additional storage.
- **Find the middle with slow and fast pointers recursively:** rescans sublists and can take $O(n \log n)$ time.
- **Insert values sequentially:** creates an unbalanced chain unless insertion order is rearranged.
- Empty input has size zero and returns a null root without reading the cursor. One node becomes a leaf.
- For even sizes, choosing the upper middle at index `floor(size / 2)` is valid; another convention may produce a different but equally balanced accepted tree.

</details>
