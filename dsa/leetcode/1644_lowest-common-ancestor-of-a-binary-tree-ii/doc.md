# Lowest Common Ancestor of a Binary Tree II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1644 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/) |

## Problem Description
### Goal
Given the root of a binary tree and two distinct target nodes `p` and `q`, return their lowest common ancestor. The lowest common ancestor is the deepest node whose subtree contains both targets; a node counts as its own descendant.

Unlike the standard version of this problem, either target may be absent from the tree. Return `null` unless both `p` and `q` exist. Every node value in the tree is unique.

### Function Contract
**Inputs**

- `root`: the root of a binary tree containing $n$ nodes, where $1 \le n \le 10^4$.
- Every node value is unique and lies between $-10^9$ and $10^9$.
- `p` and `q`: distinct target nodes; either or both may not belong to the tree.

In the app-local adapter, `p` and `q` are represented by their unique integer values.

**Return value**

Return the lowest common ancestor when both targets occur in the tree; otherwise return `null`. The app-local result is the ancestor's unique value.

### Examples
**Example 1**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1`
- Output: `3`

The targets lie in different subtrees of the root.

**Example 2**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4`
- Output: `5`

Node 5 is an ancestor of node 4 and also counts as its own descendant.

**Example 3**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10`
- Output: `null`

The value 10 is absent, so no result may be returned even though node 5 exists.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Return both structural and existence information.** A postorder DFS returns two values for every subtree: an LCA candidate and the number of targets found there. A null subtree contributes no candidate and count zero. The count combines the left count, right count, and whether the current node is either target.

**Build the candidate during the same traversal.** When both child subtrees return candidates, the current node is their first meeting point and becomes the candidate. When the current node is a target, it becomes the candidate so it can later serve as the ancestor of the other target. Otherwise propagate whichever child candidate exists.

This candidate follows the standard LCA structure, but it is not returned immediately. At the root, return it only when the accumulated count is exactly two. If a target is absent, the count is below two and the result is `null`. Thus existence verification and ancestor discovery share one traversal rather than incorrectly treating the one present target as an answer.

#### Complexity detail

Each of the $n$ nodes is visited once and performs constant work, so time is $O(n)$. The recursive call stack follows at most the tree height $h$, using $O(h)$ auxiliary space; $h$ is $O(\log n)$ for a balanced tree and $O(n)$ for a skewed tree.

#### Alternatives and edge cases

- **Verify existence, then run ordinary LCA:** Two membership scans followed by a standard LCA traversal remain $O(n)$ but revisit the tree unnecessarily.
- **Parent pointers and ancestor sets:** Build a parent map while locating both targets, then walk their ancestor chains. This takes $O(n)$ time and $O(n)$ additional space.
- **Repeated subtree membership tests:** Choosing a branch by searching for both targets inside each subtree is correct but can take $O(n^2)$ time on a skewed tree.
- If one target is an ancestor of the other, that target is the LCA.
- If either or both targets are absent, the required answer is `null`.
- Targets are distinct, so the found count cannot reach two by matching one node twice.
- Unique node values make the app-local value representation unambiguous; the native artifact compares node identity.
- A one-node tree cannot contain both distinct targets.

</details>
