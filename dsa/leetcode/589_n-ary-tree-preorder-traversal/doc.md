# N-ary Tree Preorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 589 |
| Difficulty | Easy |
| Topics | Stack, Tree, Depth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/n-ary-tree-preorder-traversal/) |

## Problem Description
### Goal
Given the root of an n-ary tree, return the preorder traversal of its node values. In preorder, visit the current node first and then traverse each of its children from left to right using the same rule.

Return the values in exactly that visitation order. An empty tree produces an empty list, and a node may have any number of children. The level-order serialization used to describe inputs does not change the traversal rule: null separators identify child groups but are not tree nodes or output values.

### Function Contract
**Inputs**

- `root`: the app representation of an N-ary node as `[value, children]`, recursively, or `None` for an empty tree

**Return value**

- A list of node values in root-first, left-to-right preorder

### Examples
**Example 1**

- Input: `[1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]`
- Output: `[1, 3, 5, 6, 2, 4]`

**Example 2**

- Input: `[7, []]`
- Output: `[7]`

**Example 3**

- Input: `None`
- Output: `[]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Visit a node before its descendants**

Preorder emits the current node as soon as it is reached, then processes each child subtree in the stored left-to-right order. An explicit stack avoids dependence on recursion depth.

**Reverse children when pushing**

A stack removes its most recently added item first. Push the current node's children from right to left so the leftmost child becomes the next node removed and visited. Each later sibling remains below the complete subtree of the sibling to its left.

**Why the produced order is preorder**

The root is the only initial stack item and is emitted first. After any node is emitted, its children are arranged so its first child is processed next; descendants pushed by that child sit above the remaining siblings, so the entire child subtree completes before the next sibling. Induction over the tree therefore matches recursive root-then-children preorder exactly.

#### Complexity detail

Every one of the `n` nodes is pushed, popped, and appended once, taking $O(n)$ time. The explicit stack may hold $O(n)$ nodes in a wide tree, and the returned traversal also stores `n` values, so total auxiliary and output space is $O(n)$.

#### Alternatives and edge cases

- **Recursive traversal with one shared output list:** is also $O(n)$, but a very deep tree may exceed the recursion limit.
- **Recursive list concatenation:** is correct, yet repeatedly copying descendant results on a deep chain can take $O(n^2)$ time.
- **Queue traversal:** produces breadth-first order and is incorrect for preorder.
- **Empty tree:** returns an empty list.
- **Leaf node:** contributes its value and no children.
- **Wide root:** sibling order must be preserved.
- **Deep chain:** an explicit stack avoids call-stack overflow.
- **Child push direction:** pushing left to right reverses the requested traversal order.
- **Repeated values:** do not identify nodes; visit every node occurrence.

</details>
