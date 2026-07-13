# Second Minimum Node In a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 671 |
| Difficulty | Easy |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/) |

## Problem Description
### Goal
You are given a non-empty special binary tree with non-negative node values. Every node has either zero or exactly two children, and each internal node's value equals the smaller value of its two children's values.

Return the second minimum value in the set of all node values in the tree: the smallest value strictly greater than the overall minimum. Repeated occurrences of the minimum do not become a second distinct value. If no greater node value exists, return `-1`.

### Function Contract
**Inputs**

- `root`: the root of a special binary tree satisfying the child-count and minimum-value rules

**Return value**

- The second smallest distinct value in the tree, or `-1` if all nodes have the same value

### Examples
**Example 1**

- Input: `root = [2,2,5,null,null,5,7]`
- Output: `5`

**Example 2**

- Input: `root = [2,2,2]`
- Output: `-1`

**Example 3**

- Input: `root = [1,1,3,1,1,3,4]`
- Output: `3`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(H)$

<details>
<summary>Approach</summary>

#### General

**The root supplies the global minimum**

Every internal node equals the minimum of its children. Repeating this relation down the tree shows that no descendant can be smaller than an ancestor, so the root value is the minimum of the entire tree. The target is therefore the smallest value encountered that differs from this root value.

**Prune as soon as a larger value appears**

When a node value is greater than the root minimum, that node is already the smallest value in its subtree: every descendant is at least its ancestor under the special-tree rule. Return the node value immediately without inspecting its children. A node equal to the minimum cannot itself be the answer, so recursively request candidates from both children.

**Combine subtree candidates without confusing absence**

A leaf equal to the minimum has no candidate and returns `-1`. When both child calls produce candidates, keep their smaller value; when only one does, propagate it. Each subtree result is consequently its smallest value above the global minimum or `-1` if none exists. Applying that statement at the root gives exactly the second smallest distinct value.

#### Complexity detail

Each node is visited at most once, and candidate subtrees can be pruned at their roots, for $O(N)$ worst-case time. Recursion stores at most one frame per tree level, using $O(H)$ space for height `H`. A balanced tree has logarithmic height, while a legal comb-shaped tree can have linear height.

#### Alternatives and edge cases

- **Full traversal with two running minima:** ignores the special pruning opportunity but still finds the answer in $O(N)$ time and $O(H)$ stack space.
- **Pairwise candidate validation:** collect all nodes, then test every larger value against every other value to determine whether a smaller candidate exists; it is correct but takes $O(N^2)$ time.
- **Enumerate every root-to-leaf path:** is correct because every node occurs on some path, but copying shared prefixes can take $O(NH)$ time and space.
- **Collect distinct values in a set and sort:** is straightforward, but uses $O(N)$ extra space and $O(N \log N)$ sorting time.
- The second minimum must be distinct from the root value; repeated minimum nodes do not qualify.
- A single-node tree has no second distinct value and returns `-1`.
- Large candidate values must be compared normally rather than replaced by a narrow numeric sentinel.

</details>
