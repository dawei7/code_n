# Binary Search Tree Iterator II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1586 |
| Difficulty | Medium |
| Topics | Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-search-tree-iterator-ii/) |

## Problem Description
### Goal

Design a bidirectional iterator over the inorder traversal of a binary search tree. The inorder values form the iterator's ordered sequence. At construction, place the cursor before the smallest value, rather than on a tree node.

`next()` moves the cursor one position to the right and returns that value, while `hasNext()` reports whether such a move is possible. Symmetrically, `prev()` moves one position to the left and returns the new current value, while `hasPrev()` reports whether a value exists on that side. Calls to `next()` and `prev()` are guaranteed to be valid.

The same iterator must preserve its position across an arbitrary valid mixture of forward and backward calls. In particular, moving backward and then forward must revisit already discovered values without advancing the underlying inorder traversal twice.

### Function Contract
**Inputs**

- `root`: The root of a binary search tree with $N$ nodes, encoded for the app as a level-order list.
- `operations`: A sequence of $Q$ calls beginning with `BSTIterator`, followed by valid uses of `next`, `hasNext`, `prev`, and `hasPrev`.

**Return value**

Return one result per operation: `None` for construction, an integer for `next` or `prev`, and a boolean for `hasNext` or `hasPrev`.

### Examples
**Example 1**

- Input: `root = [7,3,15,null,null,9,20], operations = ["BSTIterator","next","next","prev","next"]`
- Output: `[null,3,7,3,7]`

**Example 2**

- Input: `root = [1], operations = ["BSTIterator","hasNext","next","hasPrev","hasNext"]`
- Output: `[null,true,1,false,false]`

**Example 3**

- Input: `root = [2,1,3], operations = ["BSTIterator","next","next","next","prev","next"]`
- Output: `[null,1,2,3,2,3]`

### Required Complexity

- **Time:** $O(N+Q)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Pause an inorder traversal at its next undiscovered node**

Maintain a stack containing the left spine of the still-unvisited part of the tree. Construction pushes the root and all of its left descendants, so the stack top is the smallest value. Whenever a genuinely new value is requested, pop that node and push the left spine of its right subtree. This is the standard iterative inorder transition, and each tree node enters and leaves the stack once.

**Cache only values that the cursor has reached**

Store discovered inorder values in `values` and keep `index`, the cursor's current position in that list. Initially `index = -1`, representing the required position before the first value.

For `next()`, increment the cursor. If the new index already exists in `values`, the caller had previously moved backward, so return the cached value. Otherwise pop the next inorder node from the stack, append its value, prepare its right subtree, and return the newly appended value. This distinction prevents a forward revisit from consuming another tree node.

For `prev()`, decrement the cursor and return the cached value at that position. No tree work is needed because every value to the left of the cursor must already have been discovered. Consequently `hasPrev()` is exactly the test `index > 0`.

`hasNext()` is true when either a cached value exists to the right of the cursor or the traversal stack still contains an undiscovered node. These two sources are disjoint: the cache represents the visited inorder prefix, while the stack represents the resumable suffix. Their union therefore describes every valid forward move.

The stack transition discovers nodes in inorder order, so `values` is always the exact traversal prefix. Cursor moves never reorder or duplicate that prefix. By induction over operations, the cursor's cached entry is the same value a materialized inorder sequence would hold at that position, proving that all four methods report and move through the required sequence correctly.

#### Complexity detail

Each of the $N$ tree nodes is pushed and popped at most once, and each of the $Q$ operations performs constant work besides those one-time stack transitions. Total time is $O(N+Q)$; `next()` is $O(1)$ amortized, while `prev()`, `hasNext()`, and `hasPrev()` are $O(1)$ worst case.

The cache can hold $N$ values. The traversal stack holds at most the tree height $H$, so total auxiliary space is $O(N+H)=O(N)$.

#### Alternatives and edge cases

- **Eager inorder array:** materialize all values during construction and move an index through the array. It gives constant-time iterator calls and the same $O(N)$ total space, but performs all traversal work even if the client reads only a prefix.
- **Recompute inorder on every move:** derive the whole sequence again for each `next()` or `prev()`. It is correct but can require $O(NQ)$ total time.
- **Predecessor and successor searches from the root:** avoid a full value cache, but each move can cost $O(H)$ and duplicate searches after direction changes.
- **First value:** after the first `next()`, `hasPrev()` is false because the cursor cannot return to the conceptual position before the sequence by calling `prev()`.
- **Direction reversal:** a `prev()` followed by `next()` must return the value already in the cache, not discover a new node.
- **Traversal exhaustion:** after the maximum value is reached, `hasNext()` is false even though `hasPrev()` may remain true.
- **Skewed trees:** the stack can grow to $O(N)$ on a left chain, while a right chain discovers one node per forward step.

</details>
