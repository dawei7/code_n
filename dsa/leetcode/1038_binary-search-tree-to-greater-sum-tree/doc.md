# Binary Search Tree to Greater Sum Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1038 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/) |

## Problem Description

### Goal

Given the `root` of a binary search tree, convert it to a Greater Tree. Replace every original key with that key plus the sum of all original keys that are greater than it, then return the root.

The input obeys the BST rules: every key in a node's left subtree is strictly less than the node's key, every key in its right subtree is strictly greater, and both subtrees obey the same property. All keys are unique.

### Function Contract

**Inputs**

- `root`: the root of a BST with $N$ nodes, represented in cases by a level-order array using `null` for missing children; let $H$ be the tree height.
- $1 \le N \le 100$, and every unique node value lies between $0$ and $100$.

**Return value**

- The root of the same tree after updating node values in place to their greater-sum values.

### Examples

**Example 1**

- Input: `root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]`
- Output: `[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]`

**Example 2**

- Input: `root = [0,null,1]`
- Output: `[1,null,1]`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(H)$

<details>
<summary>Approach</summary>

#### General

**Visit keys from greatest to smallest:** Ordinary inorder traversal of a BST is ascending. Reversing its order to right subtree, node, left subtree visits every original key in descending order.

**Maintain the sum already passed:** Keep `running_sum` of the original values visited so far. When a node is popped from the traversal stack, add its current original value to `running_sum`, then assign `node.val = running_sum`. At that moment, the sum contains exactly that key and every greater key.

**Use an explicit traversal stack:** Descend through right children, process the deepest pending node, then move into its left subtree. This preserves reverse inorder while avoiding dependence on the language recursion limit.

Because BST ordering makes every previously visited key greater than the current key, each assignment has exactly the required sum. Every node is reached once, and mutation occurs only after its original value has been added, so later sums still include all correct original keys.

#### Complexity detail

Each of the $N$ nodes is pushed, popped, and updated once, giving $O(N)$ time. The explicit stack holds at most one root-to-leaf path and uses $O(H)$ auxiliary space.

#### Alternatives and edge cases

- **Recursive reverse inorder:** Carry a nonlocal running sum through right-node-left recursion for the same asymptotic bounds, but a skewed tree may approach recursion limits.
- **Collect and suffix-sum:** Store all nodes in ascending order, compute suffix sums, and write values back. This is $O(N)$ time but uses $O(N)$ extra space.
- **Rescan all keys per node:** For each node, sum every original key at least as large. It is correct but takes $O(N^2)$ time.
- **Single node:** Its value is unchanged because no greater key exists.
- **Zero key:** It becomes the sum of the entire tree.
- **Skewed BST:** The reverse-inorder logic remains correct, while $H$ may equal $N$.
- **Mutation order:** Add the original node value before overwriting it.

</details>
