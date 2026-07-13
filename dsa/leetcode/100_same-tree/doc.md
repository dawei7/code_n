# Same Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 100 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/same-tree/) |

## Problem Description
### Goal
You are given roots `p` and `q` of two binary trees. Compare them recursively by position: corresponding nodes must either both be absent or both exist with equal stored values.

Return `True` only when the trees have identical shapes and every corresponding value matches. Equal traversal value sequences are insufficient if child placements differ. Two empty trees are the same, while one empty and one nonempty tree are different.

### Function Contract
**Inputs**

- `p`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases
- `q`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

`True` when the trees are identical in both shape and values; otherwise `False`.

### Examples
**Example 1**

- Input: `p = [1, 2, 3], q = [1, 2, 3]`
- Output: `True`

**Example 2**

- Input: `p = [1, 2], q = [1, null, 2]`
- Output: `False`

**Example 3**

- Input: `p = [1, 2, 1], q = [1, 1, 2]`
- Output: `False`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Null placement is part of tree equality**

Process one node from each tree as an ordered pair. Two absent nodes represent matching empty subtrees. Exactly one absent node is an immediate structural mismatch. When both are present, unequal values fail before child traversal.

This null comparison is essential: trees can contain the same values and even the same traversal sequence while attaching nodes on different sides.

**Corresponding directions must match recursively**

When a pair matches locally, compare left with left and right with right. Both comparisons must succeed. Comparing crossed directions would test whether trees mirror each other, which is a different relation.

**Each call decides equality of exactly two rooted subtrees**

Each recursive call returns true exactly when the two subtrees rooted at its arguments are identical. No node outside those subtrees affects the decision.

**Trace equal values in different shapes**

For `[1, 2]` and `[1, null, 2]`, the roots match, but the first tree's left child is paired with an absent node. The comparison stops with `False` even though both trees contain the same values.

**Paired null and value checks are the tree-equality definition**

Two empty positions match, while one empty and one present position prove a structural difference. For two present nodes, equal values plus equal left subtrees and equal right subtrees are necessary for the rooted trees to match.

Those conditions are also sufficient: they recursively establish the same node at every corresponding path and the same absence everywhere else. The paired traversal therefore returns true exactly for structurally and numerically identical trees.

#### Complexity detail

In the matching case, every one of the `n` corresponding nodes is examined once, giving $O(n)$ time. Recursive calls occupy at most one root-to-leaf path, so auxiliary space is $O(h)$.

#### Alternatives and edge cases

- **Breadth-first paired traversal:** is also $O(n)$ time but can use $O(w)$ space for tree width `w`.
- **Serialize both trees:** can work if null positions are preserved, but allocates two complete representations.
- **Compare only traversal values:** can mistake different shapes for the same tree if null markers are omitted.
- Two empty trees are the same. One empty and one nonempty tree differ immediately.
- Recursive stack space follows height, becoming $O(n)$ for skewed trees and $O(\log n)$ for balanced trees.

</details>
