# Deepest Leaves Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1302 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/deepest-leaves-sum/) |

## Problem Description
### Goal
Given the root of a nonempty binary tree, identify the leaves at the greatest depth from the root. A leaf is a node with no left or right child, and depth is measured by the number of edges from the root.

Return the sum of the values stored in all leaves at that maximum depth. Shallower leaves do not contribute, even when their values are larger.

### Function Contract
**Inputs**

- `root`: the root of a binary tree containing $n$ nodes, where $1 \le n \le 10^4$ and $1 \le \texttt{Node.val} \le 100$.
- In cOde(n) cases, the tree is serialized in level order with `null` entries for missing children.

**Return value**

The sum of the values of every leaf whose depth is greatest among all leaves in the tree.

### Examples
**Example 1**

- Input: `root = [1,2,3,4,5,null,6,7,null,null,null,null,8]`
- Output: `15`
- Explanation: The deepest leaves are 7 and 8.

**Example 2**

- Input: `root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]`
- Output: `19`
- Explanation: The deepest leaves have values 9, 1, 4, and 5.

**Example 3**

- Input: `root = [42]`
- Output: `42`
- Explanation: The root is also the only and deepest leaf.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Let the final breadth-first level overwrite earlier sums**

Perform breadth-first traversal with a queue initialized by the root. Each queue batch contains exactly one tree depth. At the beginning of a batch, reset `level_sum` to zero; then remove every node currently in the queue, add its value, and enqueue its non-null children.

After a batch finishes, `level_sum` is the sum of every node on that depth. If children were enqueued, the next iteration deliberately replaces this sum with the next level's sum. When the queue finally becomes empty, the most recently processed batch was the deepest level.

Every node on the deepest level is necessarily a leaf: if one had a child, a still-deeper level would exist. Therefore the retained sum is exactly the sum of the deepest leaves, without separately testing leaf status.

#### Complexity detail

Each of the $n$ nodes enters and leaves the queue once, so the traversal takes $O(n)$ time. The queue holds at most one level, whose width is at most $n$, giving $O(n)$ auxiliary space in the worst case.

#### Alternatives and edge cases

- **Depth-first score pair:** A postorder traversal can return both maximum subtree depth and the sum at that depth in $O(n)$ time, but recursion may use $O(n)$ stack space on a skewed tree.
- **Repeated subtree-height calculation:** Choosing a deeper branch by recomputing child heights at every node is correct, but takes $O(n^2)$ time on a chain.
- **Single node:** The root is the sole deepest leaf and its value is returned.
- **Several deepest leaves:** Sum every node on the final level, including leaves from different subtrees.
- **Shallower high-value leaf:** Its value must be ignored once a deeper level exists.
- **Skewed tree:** The only deepest leaf is the final node in the chain.

</details>
