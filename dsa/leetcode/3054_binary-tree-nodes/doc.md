# Binary Tree Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3054 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-nodes/) |

## Problem Description

### Goal

The `Tree` table stores one binary-tree node per row. `N` is the node's value,
while `P` is its parent's value. The unique root has no parent and therefore
stores null in `P`. A leaf is a non-root node whose value never appears as
another row's parent; every remaining node is internal.

Classify every node as `Root`, `Leaf`, or `Inner`. Return the node value as `N`
and its label as `Type`, with rows ordered by `N` in ascending numeric order.
Node values need not be consecutive, so classification must use relationships
rather than arithmetic on the IDs.

### Function Contract

**Inputs**

- `Tree(N, P)`: `N` uniquely identifies a node; `P` is its parent's node value
  or null for the root.

Let $n$ be the number of nodes.

**Return value**

- An ordered table with columns `N` and `Type`, containing one classification
  per node and sorted by `N` ascending.

### Examples

#### Example 1

In the supplied seven-node tree, node `5` has no parent and is `Root`; nodes
`2` and `8` occur as parent values and are `Inner`; nodes `1`, `3`, `6`, and
`9` are `Leaf` nodes.

#### Example 2

A one-row tree `(42, null)` contains only its root, so node `42` is `Root`
rather than a leaf.

#### Example 3

For the chain `(10, null)`, `(20, 10)`, `(30, 20)`, node `10` is `Root`, node
`20` is `Inner`, and node `30` is `Leaf`.
