# Convert Sorted Array to Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 108 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) |

## Problem Description
### Goal
Given an integer array whose distinct elements are sorted in ascending order, convert it to a binary search tree containing every array value exactly once. For each node, all values in its left subtree must be smaller and all values in its right subtree must be larger.

The returned tree must also be height-balanced: at every node, the heights of the left and right subtrees may differ by no more than one. More than one tree can satisfy these conditions, so any valid balanced shape is acceptable. Preserve all input values without duplication, and return `null` for an empty array.

### Function Contract
**Inputs**

- `nums`: a strictly increasing list of distinct integers

**Return value**

A height-balanced `TreeNode` root. Multiple valid shapes may exist; app results are checked by their values, BST ordering, and balance.

### Examples
**Example 1**

- Input: `nums = [-10, -3, 0, 5, 9]`
- Output: a valid balanced BST such as `[0, -10, 5, null, -3, null, 9]`

**Example 2**

- Input: `nums = [1, 3]`
- Output: either `[1, null, 3]` or `[3, 1]`

**Example 3**

- Input: `nums = []`
- Output: `[]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(\log n)$

<details>
<summary>Approach</summary>

#### General

**The middle element simultaneously enforces ordering and balanced sizes**

For inclusive interval `[left,right]`, choose a middle index. Strict array ordering makes every value on the left smaller than the root and every value on the right larger, so the recursive intervals are exactly valid BST key sets.

Either middle may be chosen for an even-length interval. The problem accepts multiple balanced shapes, and both choices keep subtree sizes within one.

**Repeated midpoint splits bound subtree-height difference**

Splitting at a midpoint makes child interval sizes differ by at most one. Each recursive level roughly halves interval size, so both child heights are determined by sizes that differ by at most one and can differ in height by at most one. Applying the same midpoint rule at every node establishes height balance throughout the tree.

**Each recursive interval owns every one of its values exactly once**

`build(left, right)` returns a height-balanced BST containing exactly the values in `nums[left:right+1]`, with no value duplicated or omitted.

**Trace an odd-sized interval and its even children**

For `[-10, -3, 0, 5, 9]`, choose `0` as the root. Recursing on `[-10, -3]` and `[5, 9]` creates two balanced BST subtrees whose values are respectively smaller and larger than the root.

**Middle splits preserve both order and height balance**

Choosing the middle value leaves only smaller keys in the left interval and larger keys in the right, so recursively attaching those intervals satisfies BST ordering at the root.

The two interval sizes differ by at most one. Repeating middle splits gives balanced child trees whose heights differ by at most one, and every input value belongs to exactly one interval and creates one node. The completed tree is therefore a height-balanced BST containing the full array.

#### Complexity detail

Every one of the `n` values creates exactly one node, giving $O(n)$ time. Balanced interval splitting limits recursion depth to $O(\log n)$; returned nodes are output rather than auxiliary storage.

#### Alternatives and edge cases

- **Insert values one at a time:** can require $O(n \log n)$ time even with a careful insertion order.
- **Always choose an endpoint:** preserves BST ordering but creates an unbalanced chain.
- **Array slicing:** remains correct but copies subarrays and adds avoidable allocation.
- Empty input maps to a null root. A one-element interval creates a leaf with two empty children.
- The array must be strictly increasing for the strict BST contract; duplicate-key placement would require a stated policy.

</details>
