# Insufficient Nodes in Root to Leaf Paths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1080 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/) |

## Problem Description

### Goal

Given the `root` of a binary tree and an integer `limit`, delete all insufficient nodes simultaneously and return the root of the resulting tree. A leaf is a node with no children in the original tree.

A node is insufficient when every root-to-leaf path intersecting that node has a sum strictly less than `limit`. Thus, a node survives exactly when it belongs to at least one original root-to-leaf path whose complete sum is at least `limit`; if no such path exists through the root, the entire tree is removed.

### Function Contract

**Inputs**

- `root`: the root of a non-empty binary tree containing $n$ nodes, represented in local cases as a level-order list; $1 \le n \le 5000$.
- `limit`: the minimum sufficient root-to-leaf path sum.

Node values range from $-10^5$ through $10^5$, and `limit` ranges from $-10^9$ through $10^9$.

**Return value**

- The root of the resulting binary tree after every node absent from all qualifying original root-to-leaf paths has been removed, or `null` if no node survives.

### Examples

**Example 1**

- Input: `root = [1, 2, 3, 4, -99, -99, 7, 8, 9, -99, -99, 12, 13, -99, 14]`, `limit = 1`
- Output: `[1, 2, 3, 4, null, null, 7, 8, 9, null, 14]`

**Example 2**

- Input: `root = [5, 4, 8, 11, null, 17, 4, 7, 1, null, null, 5, 3]`, `limit = 22`
- Output: `[5, 4, 8, 11, null, 17, 4, 7, null, null, null, 5]`

**Example 3**

- Input: `root = [1, 2, -3, -5, null, 4, null]`, `limit = -1`
- Output: `[1, null, -3, 4]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Carry the remaining requirement downward:** When visiting a node with value `node.val`, its children need to supply a path sum of at least `need - node.val`. Passing this remaining threshold avoids rebuilding the root prefix sum.

**Decide children before parents:** Use an explicit postorder stack. The first stack entry schedules the node for a later decision and then schedules its children. The later entry sees those children after any insufficient subtrees have already been detached.

**Preserve original-leaf semantics:** Record whether the node was a leaf before processing children. An original leaf survives exactly when `node.val >= need`. An original internal node survives exactly when at least one processed child survives. This distinction prevents an internal node whose children were all removed from becoming a newly sufficient leaf.

For an original leaf, the remaining-threshold comparison is equivalent to checking its complete root-to-leaf sum. Inductively, an internal node retains precisely the child subtrees containing a qualifying original leaf and survives if at least one exists. Therefore every retained node lies on a sufficient original path, while every node intersected only by insufficient paths is detached.

#### Complexity detail

Each of the $n$ nodes is pushed and resolved once, so the traversal takes $O(n)$ time. The explicit postorder stack can contain $O(n)$ entries, avoiding dependence on Python's recursion limit for a tree of height up to $n$.

#### Alternatives and edge cases

- **Recursive postorder:** The same remaining-threshold recurrence is concise and uses $O(h)$ call space, but a height-$n$ tree can exceed the language recursion limit.
- **Recompute a best suffix at every node:** It is correct, but repeated subtree scans can take $O(n^2)$ time on a skewed tree.
- **Check only the current prefix:** A low prefix may later be rescued by positive descendants, so pruning before reaching original leaves is incorrect.
- **All paths insufficient:** The returned root is `null`.
- **Negative values and limit:** Comparisons must use full path sums; neither a negative node nor a negative limit changes the recurrence.
- **One surviving child:** Keep the parent and detach only the insufficient sibling subtree.
- **Internal node losing both children:** Remove it rather than treating it as a new leaf.

</details>
