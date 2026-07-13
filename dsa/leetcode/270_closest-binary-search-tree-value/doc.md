# Closest Binary Search Tree Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 270 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Binary Search, Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/closest-binary-search-tree-value/) |

## Problem Description
### Goal
Given the nonempty root of a binary search tree and a floating-point `target`, compare the absolute distance between the target and every stored node value. The target does not need to be an integer or occur in the tree.

Return the tree value with the smallest absolute difference from `target`. Use the binary-search ordering to avoid exploring irrelevant branches. If two values are equally close under the app contract, choose the smaller value so the result is deterministic. Return the node's integer value rather than the node object, its depth, or the numerical distance itself.

### Function Contract
**Inputs**

- `root`: the nonempty root of a binary search tree
- `target`: the value to approximate

**Return value**

The tree value with minimum absolute distance from `target`, choosing the smaller value on a tie.

### Examples
**Example 1**

- Input: `root = [4,2,5,1,3], target = 3.714286`
- Output: `4`

**Example 2**

- Input: `root = [1], target = 4.428571`
- Output: `1`

**Example 3**

- Input: `root = [2,1,3], target = 1.2`
- Output: `1`

### Required Complexity

- **Time:** $O(h)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Update the best value along one search path**

Keep the closest value seen so far. At each node, update it if the node is nearer, using the smaller value to break a tie, then move left when the target is smaller and right otherwise.

Before leaving a node, `closest` is optimal among the visited path. The discarded subtree lies entirely on the opposite side of the current value from the target and therefore cannot improve over the current node.

**The opposite subtree cannot beat the current node**

If the target is below the current value, every value in the right subtree is at least the current value and therefore no closer than the current node; only the left subtree can improve the answer. The symmetric argument holds when the target is larger. Updating before following that sole promising child preserves the best candidate until the search path ends.

#### Complexity detail

One node per tree level is examined, for $O(h)$ time. Iteration stores only the current node and best value.

#### Alternatives and edge cases

- **Traverse the whole tree:** is correct but takes $O(n)$ instead of exploiting BST order.
- Exact matches may return immediately; targets outside the value range converge to an extreme node.

</details>
