# Construct Binary Tree from Preorder and Inorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 105 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Divide and Conquer, Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) |

## Problem Description
### Goal
You are given two traversal sequences produced from the same binary tree. `preorder` visits each root before its left and right subtrees, while `inorder` visits the left subtree before the root and then the right subtree. Every node value is distinct, and both arrays contain exactly the same values.

Reconstruct and return the binary tree that yields both sequences. The traversal rules and distinct values determine one unique arrangement, including which nodes belong to each subtree. Preserve the integer values exactly, return `null` when both traversals are empty, and do not return either traversal array as a substitute for the linked tree structure.

### Function Contract
**Inputs**

- `preorder`: node values in root-left-right order
- `inorder`: the same node values in left-root-right order

**Return value**

The reconstructed `TreeNode` root, displayed as a level-order list in app results.

### Examples
**Example 1**

- Input: `preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]`
- Output tree: `[3, 9, 20, null, null, 15, 7]`

**Example 2**

- Input: `preorder = [1], inorder = [1]`
- Output tree: `[1]`

**Example 3**

- Input: `preorder = [2, 1], inorder = [1, 2]`
- Output tree: `[2, 1]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Inorder boundaries determine exact subtree membership**

Build a map from each distinct value to its inorder index. For root index `mid` inside interval `[left,right]`, values in `[left,mid)` belong exactly to the left subtree and values in `(mid,right]` belong exactly to the right subtree. Constant-time lookup avoids rescanning this interval for every root.

**Preorder's cursor exposes each subtree root before its children**

Preorder is root-left-right. Maintain one shared cursor pointing to the next unbuilt preorder value. On a nonempty inorder interval, consume that value as the root, then recursively build the left interval before the right interval. That order consumes exactly the contiguous preorder blocks belonging to those subtrees.

An empty inorder interval returns null without advancing the cursor, because it contains no node in preorder either.

**Cursor movement and interval size stay synchronized**

On entry to `build(left,right)`, the preorder cursor points to the root of the unique subtree containing exactly those inorder positions. The call consumes exactly `right - left + 1` preorder values and leaves the cursor at the next subtree root. The returned tree contains the same interval values with their prescribed traversal orders.

**Trace cursor movement across left and right intervals**

For root `3`, the inorder index separates `[9]` on the left from `[15, 20, 7]` on the right. The next preorder value builds node `9`; after that interval closes, value `20` becomes the right root with children `15` and `7`.

**Preorder root choice and inorder partition are unique**

The first value in any preorder subtree segment is its root. Because values are unique, locating that root in inorder divides the segment unambiguously into exactly the left-subtree and right-subtree values.

Their sizes identify the corresponding preorder segments, and the same reasoning determines each child recursively. Every constructed node respects both traversal orders, and no alternative root or partition is possible, so the only compatible tree is reconstructed.

#### Complexity detail

The map is built in $O(n)$ time, and every node is created once with constant-time lookup, for $O(n)$ total time. The map, output nodes, and recursion stack together use $O(n)$ space; auxiliary recursion depth is $O(h)$.

#### Alternatives and edge cases

- **Search inorder on every call:** is correct but becomes $O(n^2)$ on a skewed tree.
- **Slice traversal arrays:** simplifies boundaries but repeatedly copies data and can also become quadratic.
- **Iterative stack construction:** achieves $O(n)$ time but has a less direct interval proof.
- Empty traversals return an empty tree. Distinct values are essential because the inorder position map must identify one unambiguous split.
- The inputs are guaranteed consistent; validating mismatched value sets or impossible traversal pairs would be a separate concern.

</details>
