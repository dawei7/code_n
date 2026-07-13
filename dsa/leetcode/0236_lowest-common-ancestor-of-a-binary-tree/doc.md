# Lowest Common Ancestor of a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 236 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) |

## Problem Description
### Goal
Given an ordinary binary tree with unique values and two target nodes known to occur in it, find their lowest common ancestor. A node counts as its own ancestor, so one target is the answer when the other lies within that target's subtree.

Return the value of the deepest node whose subtree contains both targets. Unlike a binary search tree, node values provide no ordering shortcut; ancestry is determined solely by child relationships. If the targets lie in different branches, their first shared branching ancestor is the answer. Return only that node's value under the app contract rather than a path or depth.

### Function Contract
**Inputs**

- `root`: the root of a binary tree with unique values
- `p`: the value of the first target node
- `q`: the value of the second target node

**Return value**

The value of the targets' lowest common ancestor.

### Examples
**Example 1**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1`
- Output: `3`

**Example 2**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4`
- Output: `5`

**Example 3**

- Input: `root = [1,2], p = 1, q = 2`
- Output: `1`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Let each subtree report the surviving target path**

Depth-first search returns a target node when it encounters one. Otherwise it recursively searches both children.

**Two non-null child reports meet at the answer**

If both child searches return a match, the current node is the first place their paths meet and is the LCA. If only one child returns a match, propagate it upward.

For every completed recursive call, its return value is null when its subtree contains neither target; otherwise it is the target or LCA that must be propagated to the caller.

A target node correctly represents a subtree already containing that target and possibly the other below it. When non-null results arrive from both children, no descendant can contain both targets, so the current node is the lowest common ancestor. A single result remains the only possible answer in that subtree and is safely propagated.

When the current node is itself a target, returning it also handles the case where the other target lies below it: ancestors propagate this target unless a separate branch report proves that an even higher node is required. With both targets guaranteed to exist, the report that reaches the root is exactly their lowest common ancestor.

#### Complexity detail

In the worst case every node is visited once, giving $O(n)$ time. Recursion occupies one root-to-leaf path, or $O(h)$ space.

#### Alternatives and edge cases

- **Parent map plus ancestor set:** is iterative but uses $O(n)$ space.
- **Two root-to-target paths:** traverses more than once and stores both paths.
- One target may itself be the ancestor; targets can occur in opposite or identical-side subtrees.

</details>
