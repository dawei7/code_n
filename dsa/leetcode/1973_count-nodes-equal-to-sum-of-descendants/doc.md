# Count Nodes Equal to Sum of Descendants

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1973 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/) |

## Problem Description
### Goal
Given the root of a nonempty binary tree, count the nodes whose stored value
equals the sum of the values stored in all of their descendants. A descendant
is any node strictly below the current node on a path toward a leaf; the
current node itself is not included.

A leaf has no descendants, so its descendant sum is defined as zero. It
therefore contributes to the answer exactly when its own value is `0`.

### Function Contract
**Inputs**

- `root`: the root of a binary tree containing $N$ nodes, where
  $1 \le N \le 10^5$.
- Every node value is an integer in the inclusive range from `0` through
  $10^5$.

**Return value**

- The number of nodes whose value equals the sum of all strict descendants in
  that node's subtree.

### Examples
**Example 1**

- Input: `root = [10, 3, 4, 2, 1]`
- Output: `2`

**Example 2**

- Input: `root = [2, 3, null, 2, null]`
- Output: `0`

**Example 3**

- Input: `root = [0]`
- Output: `1`

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Process children before their parent**

Use an explicit stack of `(node, visited)` pairs to perform postorder
traversal. The first time a node is popped, push it back as visited and then
push its children. When the visited entry is later popped, both child subtree
sums are already available.

For a node, add the complete subtree sums of its left and right children. This
quantity is exactly the sum of all strict descendants, because those two
subtrees are disjoint and contain every node below the current one. Compare it
with the current value, increment the answer on equality, and store the
current subtree's total as `node.val + descendant_sum`.

**Why every node is counted correctly**

An absent child contributes zero. By postorder induction, every stored child
total equals the sum of all values in that child's subtree. Their sum is
therefore precisely the current node's descendant sum, neither omitting a
descendant nor including the current node. The comparison is consequently
correct for that node. Since the traversal reaches each tree node once, the
final counter includes exactly all qualifying nodes.

#### Complexity detail

Each of the $N$ nodes is pushed a constant number of times and processed once,
so the running time is $O(N)$. The explicit stack and subtree-sum map may each
hold $O(N)$ entries. This iterative form also avoids depending on a recursion
limit for a tree whose height can reach $N$.

#### Alternatives and edge cases

- **Recursive postorder:** Return each subtree sum while updating a shared
  counter. This is concise and also $O(N)$ time, but a chain of up to $10^5$
  nodes can overflow the call stack.
- **Recompute each subtree:** For every node, launch a separate traversal to
  sum its descendants. A skewed tree makes this take $O(N^2)$ time.
- A leaf qualifies only when its value is zero because its descendant sum is
  zero.
- Zero-valued internal nodes qualify when every descendant value is also zero.
- Repeated values are independent; qualification depends on subtree position,
  not value uniqueness.
- The comparison uses the sum of all descendant levels, not merely the
  immediate children.

</details>
