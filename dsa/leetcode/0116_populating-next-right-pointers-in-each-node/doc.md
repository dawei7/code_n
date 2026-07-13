# Populating Next Right Pointers in Each Node

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 116 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) |

## Problem Description
### Goal
You are given a perfect binary tree: every internal node has exactly two children, and all leaves occur at the same depth. Each node also has a `next` field that should link horizontally to another node on its own level.

Populate every `next` pointer so that it refers to the immediately adjacent node to the right at the same depth. This may connect nodes belonging to different parents. The rightmost node of every level has no neighbor and must point to `null`. Return the original root after modifying the existing nodes, and leave an empty tree unchanged.

### Function Contract
**Inputs**

- `root`: root of a perfect binary tree, encoded as a level-order `List[int | null]` in app cases

**Return value**

The same root object after all horizontal `next` links are populated. The app validates pointer identity at every level.

### Examples
**Example 1**

- Input: `root = [1, 2, 3, 4, 5, 6, 7]`
- Output links: `[1, #, 2, 3, #, 4, 5, 6, 7, #]`

**Example 2**

- Input: `root = []`
- Output links: `[]`

**Example 3**

- Input: `root = [1]`
- Output links: `[1, #]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Perfect-tree shape guarantees every child needed by the wiring rules**

Every internal node has both children and all leaves share a depth. Therefore, while the current level has children, every parent can safely connect `parent.left.next = parent.right`. The leftmost node of the child level is always `level_start.left`.

**Cross-parent links use the already-built current level**

If `parent.next` exists, connect `parent.right.next = parent.next.left`. The parent's `next` pointer was established while building the current level on the preceding outer iteration, so it provides constant-space access to the adjacent parent's child.

If no neighbor exists, the right child remains the last node of its level and its `next` stays null.

**Use completed horizontal links as the next level's traversal structure**

Start `parent` at the current level's leftmost node and move horizontally via `parent.next`, wiring children for every parent. After the scan, descend `level_start = level_start.left`. Stop when the leftmost node has no children, meaning the leaf level needs no outgoing child wiring.

**Each completed level bootstraps construction of the next**

Before scanning a level, every node on that level is already linked left to right and the last link is null. Processing it establishes the same invariant for the next level.

**Trace sibling and cousin links**

For `[1,2,3,4,5,6,7]`, parent `1` connects `2 -> 3`. On the next level, parent `2` connects sibling pair `4 -> 5` and bridges `5 -> 6` through `2.next.left`; parent `3` connects `6 -> 7`. Node `7` remains null-terminated.

**Sibling links and parent bridges exhaust child adjacency**

In a perfect tree, two neighboring nodes on a child level are either the left and right children of one parent or the right child of one parent and left child of its horizontal neighbor. The two pointer assignments connect exactly these cases.

Traversing a parent level through its already established `next` chain creates every adjacency on the level below and no non-neighbor link. The final parent's right child correctly remains null-terminated.

#### Complexity detail

Each of the `n` nodes participates in constant pointer operations, giving $O(n)$ time. Only traversal pointers are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Breadth-first queue:** is straightforward but uses $O(w)$ extra space.
- **Recursive paired children:** uses $O(h)$ call-stack space.
- **Apply perfect-tree assumptions to sparse trees:** can dereference absent children; Problem 117 requires a general method.
- Empty and one-node trees return unchanged. Existing stale `next` values are outside the normal input contract; robust implementations should ensure each level's final link is null.
- The algorithm uses tree nodes' output `next` fields as traversal state, not additional auxiliary storage.

</details>
