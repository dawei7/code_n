# Depth of BST Given Insertion Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1902 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Tree, Binary Search Tree, Binary Tree, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Depth of BST Given Insertion Order](https://leetcode.com/problems/depth-of-bst-given-insertion-order/) |

## Problem Description

### Goal

`order` is a permutation of the integers from $1$ through $n$ and describes how those keys are inserted into an initially empty binary search tree. The first key becomes the root. Each later key follows left links while it is smaller than the current node and right links while it is larger, becoming a leaf at the first empty child position.

Return the resulting tree's depth: the number of nodes on its longest root-to-leaf path. The root alone has depth one. The task asks only for this depth; the tree does not need to be returned.

### Function Contract

**Inputs**

- `order`: a permutation of every integer from $1$ through $n$, where $1 \le n \le 10^5$.

**Return value**

Return the maximum number of nodes on a root-to-leaf path in the BST produced by inserting the keys in the given order.

### Examples

**Example 1**

- Input: `order = [2, 1, 4, 3]`
- Output: `3`
- Explanation: One longest path is `2 -> 4 -> 3`.

**Example 2**

- Input: `order = [2, 1, 3, 4]`
- Output: `3`
- Explanation: The path `2 -> 3 -> 4` has three nodes.

**Example 3**

- Input: `order = [1, 2, 3, 4]`
- Output: `4`
- Explanation: Increasing insertion order creates a right-only chain.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**View keys in sorted order.** Record `insertion_time[value - 1]`, the position at which each key entered the BST. An inorder traversal of the final BST is exactly the keys $1,2,\ldots,n$. Its root is the earliest-inserted key; the same rule recursively selects the roots of the key ranges on either side.

**Recognize a Cartesian tree.** These two properties—keys in inorder order and insertion times obeying a min-heap—uniquely define the final BST as the min-Cartesian tree of the insertion-time array. Construct it from left to right with a monotonic stack. Pop later insertion times until the current node can attach beneath an earlier one. The current node's left child is the last popped subtree, while it becomes the right child of the remaining stack top.

Every node is pushed once and popped at most once. After construction, traverse from the stack's bottom root while carrying depths and retain the largest value. The Cartesian tree has the same parent-child relationships as literal BST insertion, so this traversal returns the requested depth.

#### Complexity detail

Building insertion times costs $O(n)$. Monotonic-stack construction and the final traversal each process every node a constant number of times, giving $O(n)$ total time. The insertion-time array, child arrays, stack, and traversal worklist use $O(n)$ space.

#### Alternatives and edge cases

- **Literal BST insertion:** It is simple and correct but takes $O(n^2)$ time for increasing or decreasing input.
- **Ordered predecessor and successor depths:** A balanced ordered map derives each new depth in $O(\log n)$ time, for $O(n\log n)$ total, but is not needed for this permutation domain.
- **Single key:** The sole node is the root and the answer is one.
- **Monotone order:** Increasing or decreasing input produces the maximum possible depth $n$.
- **Balanced order:** Inserting middle keys before the keys of their subranges can produce logarithmic depth even though the construction still processes all $n$ entries.
- **Permutation guarantee:** There are no duplicate-key insertion rules to resolve, and direct indexing by key is valid.

</details>
