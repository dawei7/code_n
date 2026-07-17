# Change the Root of a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1666 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/change-the-root-of-a-binary-tree/) |

## Problem Description
### Goal
Every node in a binary tree has `left`, `right`, and `parent` pointers. Given the original `root` and an existing leaf node, restructure the tree so that `leaf` becomes the new root while preserving every node and every subtree not on the leaf-to-root path.

For each path node `cur` other than the old root, move an existing left child to `cur.right`, make `cur`'s former parent its new left child, and clear the former parent's link back to `cur`. The contract guarantees each such `cur` has at most one child when processed. All child and `parent` pointers must agree in the returned tree.

### Function Contract
**Inputs**

- `root`: the root node of a parent-linked binary tree containing between 2 and 100 uniquely valued nodes.
- `leaf`: a leaf node in that same tree, represented by a shared-tree target fixture in local cases.

Node values lie in $[-10^9,10^9]$. Let $h$ be the number of nodes on the path from `leaf` to `root`.

**Return value**

Return the supplied leaf node as the root of the correctly rerooted tree, with its `parent` set to `null`.

### Examples
**Example 1**

- Input: `root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], leaf = 7`
- Output: `[7, 2, null, 5, 4, 3, 6, null, null, null, 1, null, null, 0, 8]`

**Example 2**

- Input: `root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], leaf = 0`
- Output: `[0, 1, null, 3, 8, 5, null, null, null, 6, 2, null, null, 7, 4]`

### Required Complexity
- **Time:** $O(h)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Walk upward before changing each link.** Start at `leaf` and retain its current parent. Before rewiring a step, save the grandparent; otherwise replacing parent pointers would lose the remaining route to the old root.

**Apply the required local rotation.** If the current node has a left child, move that subtree to its right. Make the old parent the current node's left child and set the old parent's `parent` back to the current node. Then clear whichever child pointer of the old parent previously referenced the current node. This prevents the reversed edge from existing in both directions as child links.

**Advance until the old root is incorporated.** Move `current` to the old parent and `parent` to the saved grandparent. The old root needs no parent-to-child reversal above it, so the loop stops once it becomes current. Finally clear the original leaf's parent pointer and return that leaf.

**Why all structure is preserved.** Each iteration reverses exactly one edge on the unique leaf-to-root path. The path node's possible off-path child is retained—moving a left child to the right only to free the mandated left slot—and the old parent's other child remains untouched. Clearing the old direction prevents cycles. Inductively, the processed suffix is a valid parent-linked tree rooted at the original leaf, and attaching the next parent extends it without changing any off-path subtree.

#### Complexity detail

The loop visits each of the $h$ path nodes once and performs constant pointer work, so time is $O(h)$. Only current, parent, and grandparent pointers are stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Recursive path reversal:** Recursively climb or record the leaf-to-root path, then apply the same rewiring while unwinding. This costs $O(h)$ additional stack or path storage.
- **Repeated root searches:** Finding the current node's parent from the root after every reversal avoids `parent` pointers but can cost $O(h^2)$ on a chain.
- **Reverse child links without clearing old links:** This creates cycles and duplicates path edges in the returned structure.
- If the tree has two nodes, the leaf becomes root and the old root becomes its left child.
- The chosen leaf may originate in either a left or right branch of its parent.
- Off-path subtrees attached to path nodes must remain attached after rerooting.
- When a path node has a left off-path child, that child moves to the right before the former parent occupies the left slot.
- Correct child pointers are insufficient unless every corresponding `parent` pointer is also updated.

</details>
