# Binary Tree Vertical Order Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 314 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Sorting, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) |

## Problem Description
### Goal
Assign the root of a binary tree to column zero. A left child is one column smaller than its parent, and a right child is one column larger. Group every node value by the column reached through these offsets.

Return columns from the smallest coordinate to the largest. Inside each column, list nodes from top to bottom; when nodes share both row and column, preserve their natural left-to-right level-order appearance. Include each existing node once and no missing placeholders. An empty tree returns an empty list, while repeated values remain separate entries according to their positions.

### Function Contract
**Inputs**

- `root`: the root of a binary tree, encoded as a level-order list in app cases

**Return value**

A list of vertical columns, each containing its node values in the required traversal order.

### Examples
**Example 1**

- Input: `root = [3,9,20,null,null,15,7]`
- Output: `[[9],[3,15],[20],[7]]`

**Example 2**

- Input: `root = [3,9,8,4,0,1,7]`
- Output: `[[4],[9],[3,0,1],[8],[7]]`

**Example 3**

- Input: `root = []`
- Output: `[]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Assign a horizontal coordinate during breadth-first search**

Give the root column zero. A left child has its parent's column minus one; a right child has its parent's column plus one. During traversal, append each value to the bucket for its column and track the smallest and largest columns encountered.

After traversal, read buckets consecutively from the minimum column through the maximum. Tree connectivity guarantees that every intermediate column has at least one node, so no sorting of column keys is required.

**BFS supplies both vertical ordering rules**

A breadth-first queue visits shallower rows before deeper rows, establishing top-to-bottom order in every bucket. Enqueueing the left child before the right child also makes nodes on the same row appear in left-to-right order.

For `[3,9,8,4,0,1,7]`, values `0` and `1` share the root's column and depth. BFS visits `0` first because it descends from the left subtree, so that column becomes `[3,0,1]` without a later sort.

**Each bucket append occurs in final order**

The assigned coordinate equals horizontal displacement from the root, so a node is placed in exactly its required vertical column. BFS ordering ensures that, before a node is appended, every earlier required node in that column has already been visited: all shallower nodes precede it, and same-depth nodes follow left-to-right queue order.

Thus each column bucket is final when traversal ends. Iterating the complete coordinate interval from minimum to maximum returns all buckets in left-to-right order, proving the output exact.

#### Complexity detail

Every node is enqueued, dequeued, and appended once, giving $O(n)$ time. The queue and column buckets together store $O(n)$ node values or references. Column bounds use constant additional state.

#### Alternatives and edge cases

- **DFS with row and visit-order records:** can be correct but requires sorting each column or all records afterward.
- **Traverse the tree separately for every column:** repeats node visits and can take $O(n^2)$ on a skewed tree.
- An empty tree returns no columns. A one-sided chain creates one new column per node.

</details>
