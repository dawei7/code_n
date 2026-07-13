# Search in a Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 700 |
| Difficulty | Easy |
| Topics | Tree, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/search-in-a-binary-search-tree/) |

## Problem Description
### Goal
Given the root of a binary search tree and an integer `val`, find the tree node whose value equals `val`.

If the node exists, return that same node as the root of its complete existing subtree, including all of its descendants. If no node has the requested value, return `null`. The binary-search-tree ordering may guide the search, but the returned structure must not be rebuilt, trimmed, or reduced to only the matching value.

### Function Contract
**Inputs**

- `root`: the root of a binary search tree, represented in cases by level-order values
- `val`: the value to locate

**Return value**

- The matching tree node with all of its original descendants, or `null` when no node has value `val`

### Examples
**Example 1**

- Input: `root = [4,2,7,1,3], val = 2`
- Output: `[2,1,3]`

**Example 2**

- Input: `root = [4,2,7,1,3], val = 5`
- Output: `[]`

**Example 3**

- Input: `root = [8,4,12,2,6,10,14], val = 10`
- Output: `[10]`

### Required Complexity

- **Time:** $O(h)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Use the ordering at every node**

At a binary search tree node, every value in the left subtree is smaller and every value in the right subtree is larger. Comparing `val` with the current node therefore rules out one entire subtree.

**Descend along one path**

While a node exists, return it immediately when its value matches. Move left when `val` is smaller and right when it is larger. If the selected child is absent, the search ends without a result.

**Return the node rather than reconstructing output**

The requested result is the original matching node. Returning its reference automatically preserves the complete subtree rooted there; the judge serializes that subtree only for comparison.

**Why the discarded side cannot contain the target**

Each move follows the only subtree whose allowed value range still contains `val`. The BST invariant proves the other subtree cannot contain it. Thus a match is genuine, and reaching `null` after repeatedly preserving the only possible region proves the value is absent.

#### Complexity detail

The algorithm visits one node per tree level along a single root-to-node path, taking $O(h)$ time for tree height `h`. It uses one moving node reference and no traversal stack, so the extra space is $O(1)$.

#### Alternatives and edge cases

- **Recursive BST search:** recurse into only the ordered child; it also takes $O(h)$ time but uses $O(h)$ call-stack space.
- **Generic depth-first traversal:** search both subtrees without using their ordering; it is correct for any binary tree but can take $O(n)$ time here.
- A match at the root returns the entire original tree.
- A leaf match returns a one-node subtree.
- An absent value eventually selects a missing child and returns `null`.
- A skewed BST has $h = n$, so the worst-case running time is linear even though balanced-tree search is logarithmic.

</details>
