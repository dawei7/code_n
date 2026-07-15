# Smallest Subtree with all the Deepest Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 865 |
| Difficulty | Medium |
| Topics | Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/) |

## Problem Description
### Goal
Given the root of a binary tree, define a node's depth as its shortest distance in edges from the root. A deepest node is any node whose depth is as large as possible in the entire tree. Find the smallest subtree that contains every deepest node.

The subtree rooted at a node consists of that node and all its descendants. Return the root node of the qualifying subtree. If only one node is deepest, its one-node subtree is the answer; when deepest nodes lie in different branches, the answer is their lowest shared ancestor.

### Function Contract
**Inputs**

- `root`: the root of a non-empty binary tree containing $n$ nodes, where $1 \leq n \leq 500$.

Every node value is unique and lies in $[0,500]$. Let $h$ be the tree height measured as the maximum number of nodes on a root-to-leaf path.

**Return value**

Return the `TreeNode` that roots the smallest subtree containing all nodes at maximum depth.

### Examples
**Example 1**

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4]`
- Output: `[2,7,4]`

Nodes `7` and `4` are deepest, and node `2` roots their smallest common subtree.

**Example 2**

- Input: `root = [1]`
- Output: `[1]`

**Example 3**

- Input: `root = [0,1,3,null,2]`
- Output: `[2]`

Node `2` is the only deepest node, so its own subtree is smallest.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Summarize each subtree after its children**

For every node, a postorder traversal returns two values: the height of that node's subtree and the root of the smallest subtree containing all deepest nodes within it. A missing child has height zero and no answer node; a leaf consequently receives height one and selects itself.

Suppose the left summary has height $L$ and the right summary has height $R$. If $L>R$, every deepest descendant of the current subtree lies on the left, so the left answer remains the smallest valid root. The right case is symmetric. The returned height is one plus the larger child height.

**Equal heights meet at the current node**

When $L=R$, both child sides reach the same deepest level. If the height is positive, deepest descendants occur in both branches and no proper descendant can contain them all; the current node is their lowest common ancestor. For a leaf, both missing-child heights are zero and selecting the current node gives the same rule.

Inductively, each child summary is correct for its subtree. The height comparison either preserves the only side containing deepest descendants or chooses the first node joining equally deep sides. Therefore the root returned for the whole tree is exactly the smallest subtree containing every globally deepest node.

#### Complexity detail

Postorder visits each of the $n$ nodes once and performs constant work per node, so time is $O(n)$. The recursive call stack holds at most one frame per node on a root-to-leaf path, using $O(h)$ auxiliary space.

#### Alternatives and edge cases

- **Compute subtree heights repeatedly:** Descending toward the deeper side is correct, but recomputing both heights at every level takes $O(n^2)$ time on a skewed tree.
- **Collect deepest nodes and find their lowest common ancestor:** This is correct, but it needs extra depth, parent, or ancestor structures and multiple passes.
- **Breadth-first search plus parent climbing:** The last level identifies deepest nodes, after which their ancestor sets can be intersected; it uses $O(n)$ additional storage.
- **Single node:** Both child heights tie at zero, so the root itself is returned.
- **One deepest node:** Every height comparison follows its branch until that node is selected.
- **Deepest nodes in both root branches:** Equal heights select the original root and therefore the whole tree.
- **Deepest nodes share a lower ancestor:** Equal heights first occur at that lower node, preventing an unnecessarily large subtree.

</details>
