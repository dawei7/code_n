# Binary Tree Postorder Traversal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 145 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Stack, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-postorder-traversal/) |

## Problem Description
### Goal
Given the root of a binary tree, traverse every reachable node in postorder. For each subtree, completely visit its left branch, then completely visit its right branch, and record the subtree's root only after both branches are finished.

Return the node values in this precise left-right-root order. Existing nodes must each appear once, while missing children add no placeholders. Repeated values do not merge separate nodes or change their structural ordering. An empty root yields an empty list, and in every nonempty result the final value belongs to the original tree's root.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order list with `null` placeholders in app cases

**Return value**

A list of node values in left-right-root postorder.

### Examples
**Example 1**

- Input: `root = [1,null,2,3]`
- Output: `[3,2,1]`

**Example 2**

- Input: `root = []`
- Output: `[]`

**Example 3**

- Input: `root = [1,2,3,4,5,null,8]`
- Output: `[4,5,2,8,3,1]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**The stack holds ancestors whose visit is deliberately deferred**

Push each node while following its left spine. Postorder cannot emit an ancestor yet because at least its left subtree—and possibly its right subtree—remains unfinished. When the descent reaches null, inspect the stack top without immediately popping it.

**A node is ready only after its right subtree is absent or completed**

If the top node has a right child different from `last_visited`, set `current` to that child and descend its left spine. Otherwise the right subtree is absent or was the most recently completed subtree; the left subtree is already complete from the earlier descent, so pop and emit the parent.

**`last_visited` distinguishes first inspection from return**

After emitting a node, assign it to `last_visited`. When its parent next reaches the stack top, identity equality with `parent.right` proves that right subtree has just completed. Without this pointer, the algorithm would repeatedly descend into the same right subtree.

**Stack, current, and last-completed subtree partition pending work**

Nodes on the stack are ancestors whose own output is pending. Every value already in the result belongs to a fully completed subtree, and `last_visited` is the root of the most recently completed one.

**Trace a right child with its own left child**

For `[1,null,2,3]`, node `1` waits while the traversal enters right child `2`, whose left child `3` is emitted first. Node `2` is then emitted and becomes `last_visited`; returning to `1` now recognizes its right subtree as complete and emits `1`, producing `[3,2,1]`.

**`last_visited` distinguishes descent from completed return**

A stacked node is emitted only when it has no unprocessed right subtree: either no right child exists or that child is `last_visited`, proving the traversal has returned from it. Its left subtree was exhausted during the original left descent before this inspection.

Both child subtrees therefore precede the node. Marking the popped node as last visited lets its parent recognize the same completion state. Every node is eventually popped once, yielding exactly left-right-root order.

#### Complexity detail

Each node is pushed, inspected a constant number of times, and popped once, so time is $O(n)$. The stack contains at most one root-to-leaf path, or $O(h)$ nodes; the output list uses $O(n)$ required result space.

#### Alternatives and edge cases

- **Recursive DFS:** is shorter but consumes call-stack space and may overflow on deep inputs.
- **Two stacks or reversed root-right-left:** is simple but stores $O(n)$ nodes rather than $O(h)$.
- **Morris postorder:** can use constant auxiliary space but requires temporary threading and path reversal.
- An empty tree returns an empty list. A single node is visited immediately, and skewed trees work in either direction without recursion.
- Node identity, not value equality, must determine whether a right child was last visited.

</details>
