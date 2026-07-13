# Balanced Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 110 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/balanced-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree, determine whether the tree is height-balanced. The height of a subtree is the length of its longest downward node path, and the balance condition must be evaluated independently at every node.

Return `True` only if each node's left and right subtree heights differ by at most one. A balanced root does not guarantee a balanced tree when a deeper descendant violates the condition, so the entire structure matters. Empty subtrees have height zero, making an empty tree and any single-node tree balanced; return `False` as soon as any level contains an excessive height difference.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

`True` if the entire tree is height-balanced; otherwise `False`.

### Examples
**Example 1**

- Input: `root = [3, 9, 20, null, null, 15, 7]`
- Output: `True`

**Example 2**

- Input: `root = [1, 2, 2, 3, 3, null, null, 4, 4]`
- Output: `False`

**Example 3**

- Input: `root = []`
- Output: `True`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Balance cannot be decided until both child heights are known**

Use postorder recursion. An empty subtree has height zero. For a real node, first obtain the left height and then the right height; only after both balanced child heights are known can the node check `abs(left_height - right_height) <= 1` and return one plus their maximum.

**One sentinel carries both height and validity information**

All valid heights are nonnegative, so reserve `-1` to mean “this subtree is unbalanced.” If the left child returns `-1`, return immediately without traversing the right child; if the right child fails or the current height difference exceeds one, return `-1`. Ancestors propagate the sentinel rather than treating it as a numeric height.

**The helper has a precise two-case contract**

The helper returns the exact nonnegative height of a balanced subtree, and returns `-1` exactly when some node within that subtree violates the balance condition.

**Trace a deep imbalance propagating to the root**

In `[1, 2, 2, 3, 3, null, null, 4, 4]`, node `2` on the left has a subtree two levels deeper on one side than the absent corresponding branch. Its helper returns `-1`, which propagates to the root.

**One sentinel carries both height and failure**

After recursively obtaining child results, any `-1` proves that child subtree already violates balance and the parent must fail as well. Otherwise the values are exact child heights; a difference above one is precisely a balance violation, while a permitted difference yields the parent's exact height $1 + \max(\ldots)$.

These cases match the recursive definition of a balanced tree at every node. The root returns a non-sentinel height exactly when the whole tree is balanced.

#### Complexity detail

Each of the `n` nodes has its height computed once, giving $O(n)$ time. Recursive calls occupy one root-to-leaf path, so auxiliary space is $O(h)$.

#### Alternatives and edge cases

- **Recompute height at every node:** is simple but can take $O(n^2)$ time on a skewed tree.
- **Iterative postorder:** avoids recursion limits but requires explicit node-state bookkeeping.
- **Compare only root heights:** misses an imbalance deeper in an otherwise equal-height tree.
- Empty and one-node trees are balanced. Balance must hold at every node, not only at the root.
- Early sentinel propagation may skip work after finding an imbalance, but the worst case still visits all nodes.

</details>
