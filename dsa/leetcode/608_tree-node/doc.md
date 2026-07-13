# Tree Node

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 608 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/tree-node/) |

## Problem Description
### Goal
Given a `Tree` table in which each row contains a unique node `id` and its parent `p_id`, classify every node in the valid tree as one of three types. A node with a null parent is `Root`; a non-root node that is the parent of at least one other row is `Inner`; and every remaining node is `Leaf`.

Return each node's `id` and its classification in a column named `type`, in any order. The classification depends on both the node's own parent field and whether its identifier appears as another node's parent; a one-node tree is a root rather than a leaf.

### Function Contract
**Inputs**

- `Tree(id, p_id)`: node identifiers and their optional parent identifiers

**Return value**

- Columns `id` and `type`
- `Root` when `p_id` is null
- `Inner` when the node is not a root and appears as another row's parent
- `Leaf` otherwise

### Examples
**Example 1**

- Input: node 1 has no parent, node 2 is its child, and node 3 is a child of node 2
- Output: node 1 is `Root`, node 2 is `Inner`, and node 3 is `Leaf`

**Example 2**

- Input: a tree containing one node
- Output: that node is `Root`

**Example 3**

- Input: a root with two children and no grandchildren
- Output: the root is `Root` and both children are `Leaf`

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Recognize the root from its own row**

A null `p_id` directly identifies the root. Test this condition first because the root may also appear as a parent and must still be labeled `Root`.

**Collect all actual parent identifiers**

Select distinct non-null `p_id` values. Any nonroot node whose `id` occurs in this set has at least one child and is therefore an inner node.

**Classify everything else as a leaf**

Left join every tree row to the parent-ID set. After the root case, a match means `Inner`; a missing match means the node has no children and is `Leaf`.

**Why the three labels are exact**

Every node either has a null parent or does not, separating the root from all others. Among nonroots, appearing in another row's `p_id` column is exactly the definition of having a child. That condition partitions the remaining nodes into inner nodes and leaves, so each row receives one correct label.

#### Complexity detail

For `n` rows, deduplicating parent IDs, joining them, and ordering output generally take $O(n \log n)$ time and $O(n)$ working space. Indexes on `id` and `p_id` can reduce join costs.

#### Alternatives and edge cases

- **Uncorrelated `IN` subquery:** test whether each nonroot ID belongs to the set of non-null parent IDs; it has the same semantic structure.
- **Correlated child existence:** is direct, but without an index it may rescan the tree for every node and take $O(n^2)$ time.
- **Root with children:** remains `Root`, not `Inner`.
- **Single-node tree:** the only node is the root.
- **Nonroot with one or two children:** is `Inner`.
- **Nonroot with no children:** is `Leaf`.
- **Nonconsecutive identifiers:** do not affect parent relationships.
- **Input order:** does not affect classification.

</details>
