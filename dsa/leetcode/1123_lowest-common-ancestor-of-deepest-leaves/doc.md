# Lowest Common Ancestor of Deepest Leaves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1123 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/) |

## Problem Description

### Goal

Given the `root` of a binary tree, return the lowest common ancestor of all its deepest leaves. A node is a leaf exactly when it has no children. The root has depth $0$, and each child has depth one greater than its parent, so the deepest leaves are those whose depth is maximum among every leaf in the tree.

For a set $S$ of nodes, its lowest common ancestor is the node of greatest depth whose rooted subtree contains every node in $S$. Apply that definition to the complete set of deepest leaves. If only one leaf reaches the maximum depth, that leaf is its own lowest common ancestor. Node values are unique, but the result must be the tree node itself rather than only its value.

### Function Contract

**Inputs**

- `root`: the root of a nonempty binary tree containing $n$ nodes, where $1 \le n \le 1000$; every node value is unique and lies in $[0, 1000]$. cOde(n) serializes the tree as a level-order array with `null` for missing children.

Let $h$ be the tree height measured in nodes on the longest root-to-leaf path.

**Return value**

The `TreeNode` that is the lowest common ancestor of every deepest leaf. cOde(n) serializes the returned node's entire subtree in level order.

### Examples

**Example 1**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4]`
- Output: `[2,7,4]`
- Explanation: Leaves `7` and `4` are at depth $3$, deeper than leaves `6`, `0`, and `8`; their lowest common ancestor is node `2`.

**Example 2**

- Input: `root = [1]`
- Output: `[1]`
- Explanation: The root is the only and therefore deepest leaf, so it is its own lowest common ancestor.

**Example 3**

- Input: `root = [0,1,3,null,2]`
- Output: `[2]`
- Explanation: Node `2` is the unique deepest leaf.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Ask each subtree for one complete summary.** A postorder traversal computes two facts for every node: the height of its deepest leaf and the lowest common ancestor of all leaves that reach that height. The empty subtree returns height $0$ and no candidate. A real node combines the already-computed summaries of its left and right children.

**Propagate the uniquely deeper side.** If the left summary has greater height, every deepest leaf below the current node lies in the left subtree. The left candidate therefore remains the answer, and the combined height is one greater. The symmetric rule applies when the right subtree is deeper.

**Join equal-depth sides at the current node.** When the child heights are equal, both sides contain leaves at the same maximum depth. If the height is zero, the current node itself is a leaf; otherwise, deepest leaves occur in both child subtrees. In either case the current node is the deepest node whose subtree contains all of them, so it is exactly their lowest common ancestor. By induction from leaves to the root, the root summary covers every deepest leaf in the whole tree.

#### Complexity detail

Each of the $n$ nodes is visited once and performs constant work, giving $O(n)$ time. Postorder recursion holds at most one root-to-leaf path, so auxiliary space is $O(h)$; this is $O(n)$ for a skewed tree and $O(\log n)$ for a height-balanced tree.

#### Alternatives and edge cases

- **Breadth-first search plus parent links:** BFS can identify the deepest level, then repeatedly move those nodes to their parents until they meet, but it stores $O(n)$ parent and frontier data.
- **Repeated height computation:** Descending toward the deeper child while recomputing subtree heights is correct, but a skewed tree makes it $O(n^2)$.
- **Singleton tree:** Its root has no children and is both the only deepest leaf and the returned ancestor.
- **One uniquely deepest leaf:** The candidate propagates unchanged from that leaf to the root, so the returned subtree is just that leaf.
- **Deepest leaves on both root sides:** Equal child heights make the root the answer even when shallower leaves occur elsewhere.

</details>
