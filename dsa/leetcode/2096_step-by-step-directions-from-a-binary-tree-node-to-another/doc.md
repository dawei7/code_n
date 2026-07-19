# Step-By-Step Directions From a Binary Tree Node to Another

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2096 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/) |

## Problem Description

### Goal

You are given the root of a binary tree with $n$ nodes. Every node has a unique value from $1$ through $n$. Two different values identify a starting node and a destination node.

Return directions for the unique shortest path from start to destination. Each `"L"` moves to a left child, each `"R"` moves to a right child, and each `"U"` moves to a parent. The output string must list these moves in traversal order.

### Function Contract

**Inputs**

- `root`: the root of a binary tree containing $n$ uniquely valued nodes, where $2 \le n \le 10^5$.
- `startValue`: the value of the starting node.
- `destValue`: the distinct value of the destination node.

Both requested values occur in the tree.

**Return value**

Return the shortest direction string over `"L"`, `"R"`, and `"U"` from `startValue` to `destValue`.

### Examples

**Example 1**

- Input: `root = [5,1,2,3,null,6,4]`, `startValue = 3`, `destValue = 6`
- Output: `"UURL"`
- Explanation: The node sequence is `3 -> 1 -> 5 -> 2 -> 6`.

**Example 2**

- Input: `root = [2,1]`, `startValue = 2`, `destValue = 1`
- Output: `"L"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Recording how every node was reached**

Traverse the tree once from the root. For every child value, record its parent value and whether the parent reaches it with `"L"` or `"R"`. Unique node values make these records unambiguous, and an explicit stack avoids recursion-depth failure on a tree of height $10^5$.

**Finding the shared turning point**

Walk from `startValue` through parent records to collect all of its ancestors. Then walk upward from `destValue` until the first collected value is reached. That first intersection is the lowest common ancestor of the two requested nodes. While moving upward from the destination, save each parent-to-child direction encountered.

**Constructing the shortest directions**

The path from start to the lowest common ancestor consists entirely of `"U"` moves. Count those parent steps. The saved destination-side directions were collected from bottom to top, so reverse them to obtain the downward suffix. Concatenating the upward prefix and downward suffix follows the unique simple tree path.

No shorter route can exist: every path between nodes in a tree must pass through their lowest common ancestor. Every returned move follows a real parent-child edge, and the two segments meet exactly once at that ancestor.

#### Complexity detail

The initial traversal visits all $n$ nodes once. The two ancestor walks are bounded by the tree height and therefore by $n$, giving $O(n)$ total time. Parent records, the traversal stack, and the ancestor set use $O(n)$ space; the output may also have length $O(n)$.

#### Alternatives and edge cases

- **Root-to-node paths:** Find `"L"`/`"R"` paths from the root to both targets, remove their common prefix, replace the remaining start suffix by `"U"` characters, and append the destination suffix.
- **Lowest common ancestor recursion:** A recursive LCA plus separate path searches is correct, but an unbalanced tree may exceed the language recursion limit.
- **Undirected breadth-first search:** Adding parent edges and searching from the start also finds the shortest route, with similar $O(n)$ time and space.
- If start is an ancestor of destination, the result contains only downward `"L"` and `"R"` moves.
- If destination is an ancestor of start, the result contains only `"U"` moves.
- The two values are guaranteed distinct, so the answer is never empty.

</details>
