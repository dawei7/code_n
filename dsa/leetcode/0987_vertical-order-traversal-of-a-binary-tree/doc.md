# Vertical Order Traversal of a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 987 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Sorting, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) |

## Problem Description

### Goal

Given the root of a binary tree, return its vertical order traversal. Place the root at position $(0,0)$. A node at $(r,c)$ places its left child at $(r+1,c-1)$ and its right child at $(r+1,c+1)$.

Produce one list for each column, beginning with the leftmost column and continuing to the rightmost. Within a column, list nodes from the smallest row to the largest row, which is top to bottom. When several nodes occupy the same row and column, order those nodes by increasing value. Return the resulting list of column lists.

### Function Contract

**Inputs**

- `root`: the root of a binary tree containing $N$ nodes, where $1\le N\le1000$ and $0\le\texttt{node.val}\le1000$.

**Return value**

- Column groups ordered from left to right, with each group ordered by row and then value.

### Examples

**Example 1**

- Input: `root = [3, 9, 20, null, null, 15, 7]`
- Output: `[[9], [3, 15], [20], [7]]`

**Example 2**

- Input: `root = [1, 2, 3, 4, 5, 6, 7]`
- Output: `[[4], [2], [1, 5, 6], [3], [7]]`
- Explanation: nodes `5` and `6` share position $(2,0)$, so their values decide their order.

**Example 3**

- Input: `root = [1, 2, 3, 4, 6, 5, 7]`
- Output: `[[4], [2], [1, 5, 6], [3], [7]]`
- Explanation: swapping the two same-position values in the tree does not change their required increasing output order.

### Required Complexity

- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Record complete ordering keys:** Traverse the tree while carrying each node's row and column. Store `(column, row, value)` for every node. An iterative stack avoids recursion-depth concerns on a tree with up to $1000$ nodes.

**Sort by the contract's priority:** Lexicographic tuple sorting first orders all nodes by column, then orders nodes within a column by row, and finally resolves equal-position ties by value. These are exactly the required priorities, so no separate per-column tie handling is needed.

**Group consecutive columns:** Scan the sorted tuples. Start a new output group whenever the column changes; otherwise append the value to the current group. Sorting makes every node of one column contiguous and already places its values in their final internal order.

Every node receives the unique coordinates obtained by following its root-to-node child directions. Tuple sorting applies the required comparison to every pair of nodes, and grouping removes only the coordinate keys without changing that order. The output therefore matches the vertical traversal definition.

#### Complexity detail

Traversal visits $N$ nodes in $O(N)$ time. Sorting $N$ coordinate tuples costs $O(N\log N)$ time, and grouping is linear. The tuple collection, traversal stack, and returned values use $O(N)$ space.

#### Alternatives and edge cases

- **Column map with per-column sorting:** Grouping during traversal is valid, but each column still needs sorting by row and value, and the column keys themselves must be ordered.
- **Breadth-first traversal alone:** Level order supplies row order, but nodes sharing a row and column still require value sorting.
- **Repeated insertion into sorted order:** Maintaining a sorted tuple list after each node is correct but can take $O(N^2)$ time.
- **Same position:** Values, including duplicates, must appear in non-decreasing order.
- **Skewed tree:** Every node may occupy a different column; the grouping scan then produces singleton columns.

</details>
