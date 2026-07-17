# Correct a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1660 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/correct-a-binary-tree/) |

## Problem Description
### Goal
A binary tree contains exactly one invalid node. Instead of a normal right child, that node's `right` pointer incorrectly references another node at the same depth that lies to its right. Remove the invalid node and its entire genuine descendant subtree while preserving the node reached by the erroneous pointer and every other valid part of the tree.

For serialized custom tests, `root` describes the tree before corruption. The node whose value is `fromNode` initially has no right child; after parsing, its `right` pointer is redirected to the same-depth node whose value is `toNode`. These two values are supplied only to construct the test and are not arguments of LeetCode's native `correctBinaryTree(root)` method.

### Function Contract
**Inputs**

- `root`: the root node of a binary tree containing between 3 and $10^4$ uniquely valued nodes, represented by level order in local cases, with each value in $[-10^9,10^9]$.
- `fromNode`: the unique value of the invalid node used by the local custom-test adapter.
- `toNode`: the unique value of a node at the same depth and to the right of `fromNode`.

The original parsed node identified by `fromNode` has `right = null`; the judge replaces that pointer with the node identified by `toNode` before invoking the native method. Let $N$ be the number of tree nodes.

**Return value**

Return the corrected tree root after removing the invalid node and all of its genuine descendants. The incorrectly referenced `toNode` subtree remains in its original location.

### Examples
**Example 1**

- Input: `root = [1, 2, 3], fromNode = 2, toNode = 3`
- Output: `[1, null, 3]`

Node 2 is invalid, so its parent link is cleared.

**Example 2**

- Input: `root = [8, 3, 1, 7, null, 9, 4, 2, null, null, null, 5, 6], fromNode = 7, toNode = 4`
- Output: `[8, 3, 1, null, null, 9, 4, null, null, 5, 6]`

Removing invalid node 7 also removes its genuine descendant 2, while node 4 remains attached beneath node 1.

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Traverse every depth from right to left.** Process a node's right subtree before its left subtree and retain the identities of nodes already encountered. The defect always points from the invalid node to a same-depth node on its right. Therefore the erroneous target has already been visited when traversal reaches the invalid node.

**Detect the pointer before following it.** For each node, first test whether its current `right` object is in the visited set. If so, this is the unique invalid node: return `null` to its caller, which replaces the parent's link and discards the invalid node's genuine subtree. Crucially, the traversal never follows the erroneous pointer, so the target is neither duplicated nor removed.

**Repair ordinary links recursively.** If the right pointer is not already known, record the current node, recursively repair its right child, then repair its left child, and return the node. The right-first order ensures all nodes on the relevant portion of a level are known in the direction required by the defect guarantee.

**Why the detected node is unique.** A valid child points to the next depth, so it cannot already have been visited by a right-to-left depth-first traversal before its parent examines that edge. The only edge pointing sideways is the promised corrupted right pointer, and its target lies to the right, which has already been traversed. Thus exactly that edge triggers the membership test, and returning `null` removes precisely its source subtree.

#### Complexity detail

Each of the $N$ nodes is inserted into and queried against a hash set a constant number of times, giving $O(N)$ time. The visited set and recursion stack can each contain $O(N)$ nodes, so auxiliary space is $O(N)$.

#### Alternatives and edge cases

- **Right-to-left breadth-first search:** Process each level from right to left while retaining parent links; detecting an already-seen right target also gives $O(N)$ time and space.
- **List instead of a hash set:** Linear membership checks make a skewed or broad traversal cost $O(N^2)$.
- **Ordinary left-first DFS:** The target to the invalid node's right may not have been visited yet, so the sideways pointer can be followed as though it were a child.
- The invalid node may be a leaf, in which case only that single node is detached.
- The invalid node may have a large genuine left subtree, all of which must be removed with it.
- `toNode` is not part of the removed subtree even though the corrupted pointer reaches it.
- Unique values let the local adapter identify custom-test endpoints, but the repair itself relies on object identity rather than values.
- Extreme positive or negative node values do not affect traversal or pointer detection.

</details>
