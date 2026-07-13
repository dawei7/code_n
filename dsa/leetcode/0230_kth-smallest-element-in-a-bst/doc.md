# Kth Smallest Element in a BST

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 230 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) |

## Problem Description
### Goal
Given the root of a nonempty binary search tree with distinct values and a valid one-based integer `k`, consider all node values in ascending order. The tree property places every left-subtree value below its node and every right-subtree value above it.

Return the value at rank `k` in that sorted sequence. Thus $k = 1$ selects the minimum node, while `k` equal to the number of nodes selects the maximum. Count tree nodes rather than levels, and return only the selected value—not the node object, a traversal list, or its original structural position.

### Function Contract
**Inputs**

- `root`: the root of a non-empty binary search tree with distinct values
- `k`: a one-based rank between one and the number of tree nodes

**Return value**

The `k`-th smallest value in the tree.

### Examples
**Example 1**

- Input: `root = [3, 1, 4, null, 2], k = 1`
- Output: `1`

**Example 2**

- Input: `root = [5, 3, 6, 2, 4, null, null, 1], k = 3`
- Output: `3`

**Example 3**

- Input: `root = [2, 1, 3], k = 2`
- Output: `2`

### Required Complexity

- **Time:** $O(h + k)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Inorder position is the desired rank**

An inorder traversal visits every binary search tree value in strictly increasing order. The desired value is therefore the `k`-th node visited by inorder traversal.

**Materialize only the unfinished left paths**

Push the path of left children from the root. Pop the next smallest node, decrement `k`, and return its value when `k` reaches zero. Before the next pop, push the left path beginning at the popped node's right child.

Immediately before each pop, the top of the stack is the smallest unvisited node, while every smaller node has already been visited. The stack also preserves the ancestors needed to continue inorder traversal without revisiting nodes.

**The `k`-th pop is the `k`-th smallest value**

For `[3,1,4,null,2]`, the initial stack contains `3,1`. Popping `1` produces rank one. If a later rank were requested, its right child `2` would be pushed before returning to `3`.

The stack procedure is exactly inorder traversal, and BST inorder order is ascending. Decrementing once per popped node counts ranks in that order, so the node returned when the counter reaches zero has rank `k`.

#### Complexity detail

Reaching the first value costs at most $O(h)$, and at most `k` nodes are popped before the answer, for $O(h + k)$ time. The stack holds at most one root-to-leaf path, or $O(h)$ nodes.

#### Alternatives and edge cases

- **Full inorder list:** is simple but always takes $O(n)$ time and space even for small `k`.
- **Augmented subtree sizes:** support repeated rank queries in $O(h)$ each, but require maintained metadata.
- Skewed trees have $h = n$; $k = 1$ and $k = n$ select the extreme values.

</details>
