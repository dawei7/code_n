# Complete Binary Tree Inserter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 919 |
| Difficulty | Medium |
| Topics | Tree, Breadth-First Search, Design, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/complete-binary-tree-inserter/) |

## Problem Description
### Goal

A complete binary tree has every level fully occupied except possibly its last, and the nodes on that last level occupy the leftmost positions without gaps. Starting from the root of a non-empty complete binary tree, maintain that shape while new nodes are added.

The data structure supports three operations. Its constructor receives the current root. `insert(val)` creates a node whose value is `val`, places it in the next position of level order so the tree remains complete, and returns the value of the new node's parent. `get_root()` returns the root of the updated tree.

### Function Contract
**Inputs**

- `root`: the root node of an initially complete binary tree containing between $1$ and $1000$ nodes. Cases serialize the tree in level order.
- `operations`: a sequence containing `["insert", val]` and `["get_root"]` operations. Each `val` is between $0$ and $5000$, inclusive, and the sequence contains at most $10^4$ operations.

Let $n$ be the initial number of nodes, $q$ the number of operations, and $m$ the maximum number of nodes present after those operations.

**Return value**

A result list in operation order. An `insert` entry contributes its inserted node's parent value; a `get_root` entry contributes the current tree in level order.

### Examples
**Example 1**

- Input: `root = [1,2], operations = [["insert",3],["insert",4],["get_root"]]`
- Output: `[1,2,[1,2,3,4]]`

**Example 2**

- Input: `root = [1], operations = [["insert",2],["get_root"]]`
- Output: `[1,[1,2]]`

**Example 3**

- Input: `root = [1,2,3,4,5,6], operations = [["insert",7],["insert",8],["get_root"]]`
- Output: `[3,4,[1,2,3,4,5,6,7,8]]`

### Required Complexity
- **Time:** $O(n + q)$
- **Space:** $O(m)$

<details>
<summary>Approach</summary>

#### General

**Keep only parents that still have an opening**

In a complete tree, the next inserted node belongs to the first node in breadth-first order that has fewer than two children. Perform one breadth-first traversal during construction and append every such node to a queue. Their order is exactly the order in which they will receive future children.

**Update the queue with each insertion**

The parent is always the queue's front node. Attach the new node as its left child if that position is empty. Otherwise attach it as the right child and remove the now-full parent from the queue. The new node itself has two open child positions, so append it to the back.

This transition preserves the queue meaning: all earlier nodes are full, the front is the earliest incomplete node, and every later queued node is also incomplete in breadth-first order. Filling the earliest available child position therefore keeps the last level left-aligned, so the tree remains complete after every insertion. Returning the selected parent's value and retaining the original root then implements the two query operations directly.

#### Complexity detail

The constructor visits each of the $n$ initial nodes once, taking $O(n)$ time. Each insertion performs a constant number of queue and pointer operations, and `get_root()` returns the stored root reference, so $q$ operations take $O(q)$ time after construction. The queue and the final tree together hold $O(m)$ nodes. In the app-local adapter, serializing a root snapshot costs time and output space proportional to that snapshot; this is output handling rather than data-structure maintenance.

#### Alternatives and edge cases

- **Search from the root before every insertion:** A fresh breadth-first traversal finds the correct opening but can take $O(m)$ time per insertion and quadratic time over a long sequence.
- **Store every node by heap index:** Keeping the entire level-order array also identifies the parent at index `(i - 1) // 2` in constant time, but the incomplete-parent queue mirrors the native tree interface without a separate full index.
- **Queue every node:** Retaining full nodes is unnecessary; removing a parent immediately after its right child is filled keeps the queue focused on valid insertion positions.
- **One missing child:** The front parent receives its left child before its right child, which is essential to completeness.
- **Full last level:** Once a level becomes full, the next insertion automatically uses the left child position of the first node on the following parent level.
- **Duplicate values:** Shape, not value uniqueness, determines the parent, so repeated values require no special handling.
- **Root identity:** `get_root()` returns the same root object supplied to the constructor, now connected to all inserted nodes.

</details>
