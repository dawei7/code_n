# Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1430 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/) |

## Problem Description

### Goal

Given the root of a binary tree and an integer array `arr`, determine whether `arr` is exactly the sequence of node values along some path that starts at the root and ends at a leaf. Consecutive array entries must correspond to parent-child steps in the tree.

Matching only a prefix or reaching an internal node when the array ends is not sufficient: the last array value must match a node with no children. Likewise, a root-to-leaf path is invalid if it ends before every array value has been consumed.

### Function Contract

**Inputs**

- `root`: the root node of a nonempty binary tree containing $N$ nodes, where $1 \le N \le 5000$.
- `arr`: an integer array of length $k$, where $1 \le k \le 5000$.
- Every tree value and array value is between $0$ and $9$.
- Let $h$ be the height of the tree.

**Return value**

- `true` if one root-to-leaf path has exactly the values in `arr` in order; otherwise `false`.

### Examples

**Example 1**

- Input: `root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]`
- Output: `true`

**Example 2**

- Input: `root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]`
- Output: `false`

**Example 3**

- Input: `root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]`
- Output: `false`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Carry the array position with the traversal.** At a node paired with index `i`, fail immediately if the node is absent, `i` is outside the array, or `node.val != arr[i]`. No descendant of that state can repair a mismatched prefix.

**Enforce the leaf endpoint.** If the current value matches and the node is a leaf, accept exactly when `i` is the final array index. This single condition enforces both sides of the contract: the array cannot stop at an internal node, and a leaf cannot be accepted while unconsumed values remain.

**Explore only matching prefixes.** For a matching non-leaf node, recursively test the left and right children with `i + 1`. A successful branch describes a connected root-to-leaf path with every value aligned. Conversely, any valid path follows one of those child branches and survives every equality and endpoint check, so the traversal finds it.

#### Complexity detail

Each reachable node is examined at most once before its branch either fails or continues, giving $O(N)$ worst-case time. Recursive calls follow at most one root-to-current path at a time, so the stack uses $O(h)$ space.

#### Alternatives and edge cases

- **Materialize all root-to-leaf paths:** Comparing `arr` after copying every path is correct but can take $O(Nh)$ time and space on deep trees.
- **Breadth-first search:** Queue pairs of nodes and array indices; it remains $O(N)$ time but can use $O(N)$ space at a wide level.
- **Array ends at an internal node:** Return `false` even if every consumed value matched.
- **Leaf reached too early:** Return `false` while array values remain.
- **Single-node tree:** Return `true` only for a one-element array equal to the root value.
- **Duplicate values:** Track structure and depth, not merely whether the values occur somewhere in the tree.

</details>
