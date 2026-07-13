# Binary Tree Pruning

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 814 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-tree-pruning/) |

## Problem Description

### Goal

You are given the root of a binary tree in which every node stores either `0` or `1`. A subtree consists of a node together with all descendants reachable below it. Such a subtree is eligible for removal when none of those nodes contains `1`.

Prune every eligible subtree and return the root of what remains. Removing a subtree deletes its top node as well as all descendants, so pruning lower branches can make an all-zero ancestor removable too. The entire tree may disappear, in which case the returned root is `None`; surviving nodes keep their original relative structure.

### Function Contract

**Inputs**

- `root`: the root of a binary tree whose node values are `0` or `1`, or `None`.

**Return value**

- The root after pruning every all-zero subtree; this may be `None` when the whole tree is removed.

### Examples

**Example 1**

- Input: `root = [1,null,0,0,1]`
- Output: `[1,null,0,null,1]`
- Explanation: The zero leaf below the right child is removed, while the zero node with a `1` descendant remains.

**Example 2**

- Input: `root = [1,0,1,0,0,0,1]`
- Output: `[1,null,1,null,1]`
- Explanation: The entire left subtree and the zero leaf under the right subtree contain no `1` and are pruned.

**Example 3**

- Input: `root = [0,0,0]`
- Output: `[]`
- Explanation: No node in the tree has value `1`, so the root is also removed.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Decide only after pruning descendants**

Traverse in postorder. Recursively replace the left child with its pruned result, then do the same for the right child. At that point, a current node with value `0` represents an all-zero subtree exactly when both child references are `None`; return `None` for it. Otherwise, return the node.

For a leaf, the rule keeps `1` and removes `0`, which is correct. Inductively, each returned child is present exactly when its original subtree contained a `1`. The current subtree therefore contains a `1` exactly when the current value is `1` or at least one pruned child remains, matching the return condition. Applying this at the original root prunes precisely the required subtrees.

**Reuse the existing nodes**

Assign pruned children back to their parent rather than constructing a second tree. The returned structure preserves every surviving node and edge while releasing references to removed branches.

#### Complexity detail

Each of the `n` nodes is visited once and performs constant work, giving $O(n)$ time. Recursive calls occupy $O(h)$ stack space for tree height `h`; no additional tree-sized structure is created.

#### Alternatives and edge cases

- **Return a contains-one flag:** A helper can return both the pruned node and whether a `1` was found; postorder child references already encode that flag.
- **Iterative postorder:** An explicit stack avoids recursion depth limits but needs visitation state for each node.
- **Repeated subtree scans:** Calling a separate `contains_one` traversal before pruning each node is correct but can take $O(n^2)$ time on a skewed tree.
- **Empty tree:** Return `None` immediately.
- **All-zero tree:** Every leaf prunes, then each ancestor becomes childless and prunes in turn.
- **Zero ancestor of one:** It must remain because its subtree contains a `1`.
- **Root pruning:** The result may be an empty tree even though the input root existed.

</details>
