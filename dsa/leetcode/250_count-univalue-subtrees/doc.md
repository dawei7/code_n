# Count Univalue Subtrees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 250 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-univalue-subtrees/) |

## Problem Description
### Goal
Given the root of a binary tree, consider the complete subtree rooted at every existing node. A rooted subtree is univalue when that node and every descendant contained beneath it all store the same value.

Return the number of nodes whose full rooted subtree satisfies this condition. Every leaf contributes one because it contains only its own value. A parent does not qualify merely because its immediate children match if a deeper descendant differs, while an empty tree contributes zero subtrees. Count overlapping qualifying subtrees independently, such as qualifying children inside a larger qualifying parent subtree.

### Function Contract
**Inputs**

- `root`: the root of a binary tree

**Return value**

The number of nodes whose complete rooted subtree is univalue.

### Examples
**Example 1**

- Input: `root = [5,1,5,5,5,null,5]`
- Output: `4`

**Example 2**

- Input: `root = []`
- Output: `0`

**Example 3**

- Input: `root = [1,1,1]`
- Output: `3`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**A parent can be decided only after both children**

Postorder DFS returns whether each child subtree is univalue. A node qualifies only when both children qualify and every existing child root equals the node value.

When a call returns true, every node in that call's subtree equals its root value; the running count includes every qualifying subtree already completed.

**Each qualifying subtree is counted at its root**

A missing child imposes no restriction, and a leaf therefore qualifies immediately. For an existing child, both the child's entire subtree must be uniform and its root value must equal the current value. Those conditions are necessary and sufficient for every node below the current root to share its value. Incrementing at precisely those roots counts every univalue subtree once.

#### Complexity detail

Every node is visited once for $O(n)$ time. Recursion stores one root-to-leaf path, or $O(h)$ space.

#### Alternatives and edge cases

- **Re-scan each subtree:** can take $O(n^2)$ on skewed or uniform trees.
- Empty trees contribute zero; null children do not invalidate an otherwise univalue subtree.

</details>
