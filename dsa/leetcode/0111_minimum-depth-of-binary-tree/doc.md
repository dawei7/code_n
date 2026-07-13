# Minimum Depth of Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 111 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-depth-of-binary-tree/) |

## Problem Description
### Goal
Given the root of a binary tree, find the length of its shortest downward path that reaches a leaf. A leaf is specifically a node with neither a left nor a right child, and path length is measured by the number of nodes visited from the root through that leaf.

Return this minimum node count, or `0` when the tree is empty. A missing child beside a nonempty subtree is not itself a leaf and cannot create a shorter path, so a one-sided tree must be followed until an actual terminal node is reached. A tree containing only its root has minimum depth `1`.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

The minimum root-to-leaf depth, or `0` for an empty tree.

### Examples
**Example 1**

- Input: `root = [3, 9, 20, null, null, 15, 7]`
- Output: `2`

**Example 2**

- Input: `root = [2, null, 3, null, 4, null, 5, null, 6]`
- Output: `5`

**Example 3**

- Input: `root = []`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(w)$

<details>
<summary>Approach</summary>

#### General

**Breadth-first order makes the first leaf globally shallowest**

Use a queue of `(node, depth)` pairs beginning with `(root,1)`. Children receive `depth + 1`. FIFO order ensures all nodes at depth `d` are removed before any node at depth $d + 1$, so a leaf can terminate the search immediately.

**A missing child is not itself a root-to-leaf path**

Return only when a dequeued node has neither a left nor a right child. A node with one absent child is not a leaf, and the nonexistent branch does not define a path. Its existing child must still be explored.

**Queue order and stored depths remain synchronized**

The queue is ordered by nondecreasing exact root-to-node depth. Before a node is removed, every shallower real node has already been checked and was not a leaf.

**Trace why one-sided trees defeat a naive minimum formula**

For `[2, null, 3, null, 4, null, 5, null, 6]`, missing left children do not end a path. The only leaf is `6` at depth five, so the answer is `5`, not `1`.

**The first BFS leaf is necessarily shallowest**

The root starts at depth one, and each child is enqueued with its parent's depth plus one, so every queued depth is exact. Breadth-first order processes all nodes at a smaller depth before any node at a larger one.

Consequently, when the first true leaf—one with no children—is removed, no unprocessed leaf can be shallower. Its recorded depth is the minimum root-to-leaf length; a missing child alone is never mistaken for a leaf.

#### Complexity detail

In the worst case, the first leaf appears at the deepest level and all `n` nodes are processed, giving $O(n)$ time. The queue holds at most $O(w)$ nodes, where `w` is maximum width.

#### Alternatives and edge cases

- **Depth-first search:** is correct with careful one-child handling but cannot generally stop as early.
- **Take `1 + min(left, right)`:** is wrong when one child is absent unless absence is treated specially.
- **Compute all root-to-leaf paths:** stores unnecessary path data.
- Empty input has minimum depth zero; a single root is the first leaf at depth one.
- Use a deque or indexed queue to avoid the repeated shifting cost of removing index zero from an array.

</details>
