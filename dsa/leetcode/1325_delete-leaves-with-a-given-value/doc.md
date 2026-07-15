# Delete Leaves With a Given Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1325 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/delete-leaves-with-a-given-value/) |

## Problem Description
### Goal
Given the root of a binary tree and an integer `target`, delete every leaf whose value equals `target`.

Deletion can expose a new qualifying leaf: after its children are removed, a node with value `target` may itself have no children. Continue applying the same rule until no target-valued leaf remains, and return the resulting tree. The root may also be deleted if the cascade makes it a qualifying leaf.

### Function Contract
**Inputs**

- `root`: the root of a nonempty binary tree containing $n$ nodes, where $1\le n\le3000$ and every node value is between 1 and 1000.
- `target`: an integer between 1 and 1000.

**Return value**

The root of the tree after all target-valued leaves, including leaves created by earlier deletions, have been removed; return an empty tree if the root is deleted.

### Examples
**Example 1**

- Input: `root = [1,2,3,2,null,2,4], target = 2`
- Output: `[1,null,3,null,4]`
- Explanation: Removing the original target leaves makes the node 2 below the root a leaf, so it is removed as well.

**Example 2**

- Input: `root = [1,3,3,3,2], target = 3`
- Output: `[1,3,null,null,2]`

**Example 3**

- Input: `root = [1,2,null,2,null,2], target = 2`
- Output: `[1]`
- Explanation: The chain of 2-valued nodes disappears from the bottom upward.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Evaluate a node only after its children**

Whether a node should be deleted depends on the state of both child subtrees after their own deletions. Traverse the tree in postorder. An explicit stack stores each node together with its parent, which side links it to that parent, and whether its children have already been scheduled.

On the postorder visit, both child pointers already describe the fully processed subtrees. If they are both null and the node value is `target`, detach the node from its parent. When the node is the original root, replace the result root with null instead. Because parents are visited later, they immediately observe that deletion and can be removed in the same single postorder pass.

Every deletion required by the repeated process occurs when its node is visited: its descendants have reached their final forms, so it is a leaf exactly when the repeated bottom-up process would eventually expose it. Nodes that fail either the value or leaf condition must remain.

#### Complexity detail

Each of the $n$ nodes is pushed and processed a constant number of times, for $O(n)$ time. The explicit postorder stack can contain $O(n)$ entries on a skewed tree, giving $O(n)$ auxiliary space without relying on the language recursion limit.

#### Alternatives and edge cases

- **Recursive postorder:** Returning null for a qualifying processed node is concise and also $O(n)$, but a 3000-node skewed tree can exceed Python's recursion limit.
- **Repeated whole-tree passes:** Removing only the current leaves and rescanning until stable is correct but can take $O(n^2)$ time on a target-valued chain.
- **Root deletion:** If the final root is a target-valued leaf, the result is empty.
- **Non-target leaf:** It remains even when its parent equals `target`, preventing that parent from becoming a leaf.
- **Cascade through one child:** A parent can become a leaf after its only surviving child is removed.
- **No matching values:** The tree structure remains unchanged.

</details>
