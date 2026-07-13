# Unique Binary Search Trees II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 95 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Backtracking, Tree, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-binary-search-trees-ii/) |

## Problem Description
### Goal
Given `n`, construct binary search trees using every integer key from `1` through `n` exactly once. Each tree must satisfy the strict ordering rule: all keys in a node's left subtree are smaller, and all keys in its right subtree are larger.

Return one root for every structurally unique valid tree, in any order. Trees that differ in at least one parent-child relationship are different structures even though their inorder value sequence is identical. No valid structure may be omitted or duplicated.

### Function Contract
**Inputs**

- `n`: the number of consecutive keys, with keys `1..n`

**Return value**

A list of `TreeNode` roots representing every distinct valid tree, in any order. App results are displayed as level-order lists.

### Examples
**Example 1**

- Input: `n = 3`
- Output: five distinct binary search trees

**Example 2**

- Input: `n = 1`
- Output: `[[1]]`

**Example 3**

- Input: `n = 2`
- Output: two trees, rooted at `1` and `2` respectively

### Required Complexity

- **Time:** $O(n C_n)$
- **Space:** $O(n C_n)$

<details>
<summary>Approach</summary>

#### General

**A root partitions consecutive keys into forced left and right intervals**

For key interval `[left, right]`, choose every `root_value` in turn. BST ordering forces all smaller interval keys into the left subtree and all larger keys into the right subtree. Recursively generate both forests, then create a new root for every Cartesian-product pair of left and right trees.

The child choices are independent once the root is fixed. If the left forest has `L` structures and the right has `R`, that root contributes `L × R` full trees.

**An empty side contributes one combinatorial choice**

Return a one-element forest containing `None` for an empty interval. It represents the single choice “no child” and acts as the multiplicative identity in the Cartesian product. Returning an empty forest would incorrectly prevent leaves and one-sided trees from being constructed at all.

**Memoize forests by interval boundaries**

Memoize the immutable tuple of roots generated for each interval. Different parent choices request the same consecutive ranges, whose possible structures depend only on their two endpoints.

This common implementation may share subtree objects between different returned roots. That is safe when generated trees are treated as immutable, as the judge does. If callers may mutate trees independently, clone cached children while assembling each output tree.

**Every interval forest is valid, complete, and structurally unique**

Every tree returned for `[left, right]` contains each key in that interval exactly once, satisfies the BST ordering rule, and has a structure distinct from every other returned tree.

**Trace all root choices for three keys**

For keys `1..3`, root `1` combines an empty left side with both trees over `2..3`; root `2` combines the single-node trees `1` and `3`; root `3` symmetrically combines both trees over `1..2` with an empty right side. The totals $2 + 1 + 2$ give five trees.

**The root uniquely decomposes every BST interval**

Choosing root `r` splits the key interval into keys smaller than `r` and keys greater than `r`. Combining any recursively valid left and right trees from those intervals produces a valid BST because all ordering relationships follow from the split.

Conversely, every BST over the interval has one root value and subtrees using exactly those two key intervals. The recursion enumerates that root and both subtree structures. Different root-or-subtree choices yield different trees, so every valid BST is produced exactly once.

#### Complexity detail

There are `C_n` Catalan-number output trees, each containing `n` nodes when materialized, so output construction and storage require $O(n C_n)$ time and space. The recursion and interval cache are smaller than the output at the problem scale.

#### Alternatives and edge cases

- **Generate all binary tree shapes then validate:** explores invalid assignments and repeats BST checks.
- **Insert keys in every permutation:** generates the same tree from many permutations, causing factorial duplication.
- **Unmemoized interval recursion:** remains correct but repeatedly rebuilds identical subproblem forests.
- $n = 1$ yields one node. The public constraint starts at one; a generalized $n = 0$ API must decide whether to return an empty list or a list containing the empty tree.
- Output order is unrestricted, but each root/left/right structural triple must occur only once.

</details>
