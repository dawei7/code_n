## Description

Given the `root` of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`.

- The "linked list" should be in the same order as a <a href="https://en.wikipedia.org/wiki/Tree_traversal#Pre-order,_NLR" target="_blank">**pre-order**** traversal**</a> of the binary tree.
### Function Contract

**Inputs**

- `root`: The root of the binary tree, or `null` for an empty tree.

**Return value**

Return `None`; modify the tree rooted at `root` so its nodes form the required right-child chain. The app runner serializes the mutated root in level order.

### Examples
#### Example 1

![](images/flaten.jpg)

- **Input:** `root = [1,2,5,3,4,null,6]`
- **Output:** `[1,null,2,null,3,null,4,null,5,null,6]`
#### Example 2

- **Input:** `root = []`
- **Output:** `[]`
#### Example 3

- **Input:** `root = [0]`
- **Output:** `[0]`
### Constraints

- The number of nodes in the tree is in the range `[0, 2000]`.

- $-100 \le \text{Node.val} \le 100$

**Follow up:** Can you flatten the tree in-place (with `O(1)` extra space)?