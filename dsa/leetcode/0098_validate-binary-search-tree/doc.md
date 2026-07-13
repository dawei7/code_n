# Validate Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 98 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/validate-binary-search-tree/) |

## Problem Description
### Goal
You are given the root of a binary tree. Determine whether the complete tree satisfies the strict binary search tree ordering: every value anywhere in a node's left subtree is smaller than that node, and every value anywhere in its right subtree is larger.

Return a boolean result. The rule applies through all ancestors, not only between a node and its immediate children. Duplicate values are therefore invalid. An empty tree is valid, and integer boundary values must be compared without inventing unsafe fixed sentinels.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

`True` if the complete tree is a valid binary search tree; otherwise `False`.

### Examples
**Example 1**

- Input: `root = [2, 1, 3]`
- Output: `True`

**Example 2**

- Input: `root = [5, 1, 4, null, null, 3, 6]`
- Output: `False`

**Example 3**

- Input: `root = [2, 2, 2]`
- Output: `False`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Every ancestor contributes to an allowed open interval**

Associate each node with an open interval `(lower, upper)` containing every value allowed at that position. The root starts unbounded. A left child inherits the ancestor lower bound and tightens its upper bound to the parent value; a right child inherits the upper bound and tightens its lower bound.

Passing all bounds down the path is what detects a node that is locally ordered relative to its parent but lies on the wrong side of a more distant ancestor.

**Open bounds reject duplicate keys automatically**

Reject a value unless `lower < value < upper`. The inequalities are strict because this BST definition permits neither equal left descendants nor equal right descendants. Null children require no check and terminate that branch successfully.

**Pending nodes carry all ordering obligations with them**

Every pending stack entry has bounds implied by all of its ancestors, not merely its parent. Therefore, passing the check proves the node is correctly ordered relative to the entire path above it.

**Trace a distant-ancestor violation**

In `[5, 4, 6, null, null, 3, 7]`, node `3` is the left child of `6`, but it lies in the root's right subtree. Its inherited interval is `(5, 6)`, so `3` is rejected even though it is smaller than its parent.

**Ancestor bounds encode the full BST condition**

Entering a left subtree tightens the upper bound to the parent value; entering a right subtree tightens the lower bound. A node that satisfies its inherited open interval is therefore correctly ordered relative not only to its parent but to every ancestor that contributed a bound.

If every node passes, all left and right descendant relationships required by a BST hold. Conversely, any BST violation places some descendant on the wrong side of a relevant ancestor, causing it to cross the inherited bound and be rejected.

#### Complexity detail

Each of the `n` nodes is checked once, giving $O(n)$ time. The explicit stack stores at most a traversal frontier bounded by $O(h)$ for depth-first traversal, where `h` is the tree height.

#### Alternatives and edge cases

- **Inorder traversal:** checking for a strictly increasing sequence is also $O(n)$ time and $O(h)$ auxiliary space.
- **Compare only with the parent:** misses violations involving a more distant ancestor.
- An empty tree is valid. Boundary values at the integer type's minimum or maximum are safe when bounds use unbounded sentinels rather than arithmetic such as `value ± 1`.
- Comparing only immediate children is insufficient; every descendant must satisfy the ancestor interval.
- **Find subtree minima and maxima repeatedly:** is correct but can take $O(n^2)$ time on a skewed tree.

</details>
