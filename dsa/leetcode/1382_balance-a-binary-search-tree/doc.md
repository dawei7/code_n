# Balance a Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1382 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Divide and Conquer, Greedy, Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/balance-a-binary-search-tree/) |

## Problem Description

### Goal

Given the root of a binary search tree, construct and return a balanced binary search tree containing exactly the same node values. A binary tree is balanced when, at every node, the heights of its left and right subtrees differ by no more than one.

The input can be highly skewed, and more than one balanced shape may satisfy the requirement. The returned tree must preserve the binary-search-tree ordering while redistributing the values into any valid balanced structure.

### Function Contract

**Inputs**

- `root`: the root node of a binary search tree containing $N$ distinct values, where $1 \le N \le 10^4$.

**Return value**

- The root node of any height-balanced binary search tree containing exactly the input values.

### Examples

**Example 1**

- Input: `root = [1,null,2,null,3,null,4]`
- Output: `[2,1,3,null,null,null,4]`

**Example 2**

- Input: `root = [2,1,3]`
- Output: `[2,1,3]`

**Example 3**

- Input: `root = [1]`
- Output: `[1]`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Extract the sorted node order.** An inorder traversal of a binary search tree visits its nodes in strictly increasing value order. Use an explicit stack so a chain of up to $10^4$ nodes cannot overflow the recursion limit, and store the visited node objects in an array.

**Choose medians recursively.** For any contiguous interval of the sorted array, choose its middle node as the subtree root. Build the left subtree from the values before the midpoint and the right subtree from the values after it, replacing the node's old child links with these balanced children.

Every value appears in exactly one interval and is therefore used once. All left-interval values are smaller than their midpoint and all right-interval values are larger, establishing the BST property. Splitting each interval near its middle makes the two subtree sizes differ by at most one, which inductively keeps their heights within one.

#### Complexity detail

The iterative inorder traversal and balanced reconstruction each process all $N$ nodes once, giving $O(N)$ time. The node array uses $O(N)$ space; the reconstruction depth is $O(\log N)$.

#### Alternatives and edge cases

- **Create new nodes from sorted values:** It has the same bounds and result semantics, but allocates a second set of node objects instead of reusing the input nodes.
- **Repeated list concatenation:** Growing the inorder array by copying it at every visit can take $O(N^2)$ time.
- **Tree rotations:** Day-Stout-Warren balancing can achieve $O(N)$ time with $O(1)$ auxiliary space, but it is more intricate to implement correctly.
- **Already balanced:** Rebuilding is still valid even if the returned shape differs from the input.
- **Single node:** It is already balanced and remains the sole root.
- **Deep chain:** Keep the input traversal iterative; only the reconstruction recurses, and its depth is logarithmic.
- **Multiple valid answers:** Correctness depends on inorder values and height balance, not on matching one serialized shape.

</details>
