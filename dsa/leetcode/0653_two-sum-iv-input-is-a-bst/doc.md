# Two Sum IV - Input is a BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 653 |
| Difficulty | Easy |
| Topics | Hash Table, Two Pointers, Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) |

## Problem Description
### Goal
Given the root of a valid binary search tree and an integer `k`, determine whether there are two elements in the tree whose values add up exactly to `k`.

Return `True` when such a pair exists and `False` otherwise. The two elements must come from distinct tree nodes; one node cannot be used twice, even when doubling its value would equal `k`. Equal values in separate nodes may form a valid pair if the tree representation permits them.

### Function Contract
**Inputs**

- `root`: the root node of a binary search tree
- `k`: the target integer sum

**Return value**

- `True` if a pair of distinct nodes sums to `k`; otherwise `False`

### Examples
**Example 1**

- Input: `root = [5, 3, 6, 2, 4, null, 7]`, `k = 9`
- Output: `True`

**Example 2**

- Input: `root = [5, 3, 6, 2, 4, null, 7]`, `k = 28`
- Output: `False`

**Example 3**

- Input: `root = [2, 1, 3]`, `k = 4`
- Output: `True`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Turn the pair condition into a complement lookup**

When visiting a node with value `x`, the only value that can pair with it is $k - x$. Store every previously visited value in a hash set. If the complement is already present, the stored value belongs to an earlier node, so the two nodes are necessarily distinct.

**Traverse every possible participant once**

Use an explicit stack to visit the tree. For each node, check its complement before inserting its own value, then push its children. The traversal order does not affect correctness because every unordered node pair has one endpoint visited second; that second visit tests the first endpoint's value.

If a valid pair exists, the later endpoint finds its complement and returns `True`. If the traversal finishes, every node has checked against all earlier values, so every pair has been considered and no valid pair exists.

**Why the BST ordering is optional for this method**

The hash-set method works for any binary tree and avoids repeated searches from the root. The BST property offers a different inorder two-pointer solution, but it is not needed to achieve linear time.

#### Complexity detail

Each of the `N` nodes is pushed, popped, and checked once, for $O(N)$ expected time. The visited-value set and traversal stack can each contain $O(N)$ entries, giving $O(N)$ auxiliary space.

#### Alternatives and edge cases

- **Inorder list plus two pointers:** uses the BST ordering to create a sorted array, then scans its ends in linear time; it also needs $O(N)$ space.
- **Two coordinated BST iterators:** advances the smallest and largest remaining values without materializing the full inorder list, using $O(H)$ space but more intricate identity handling.
- **Search the tree for each complement:** is simple, but can take $O(NH)$ time and becomes quadratic on a skewed tree.
- A one-node tree cannot form a pair even when twice its value equals `k`.
- Negative values and negative targets use the same complement rule.
- The two selected nodes must be distinct; checking before insertion enforces this directly.

</details>
