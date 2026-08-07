## Description

Given the `root` of a binary tree, return *the sum of all left leaves.*

A **leaf** is a node with no children. A **left leaf** is a leaf that is the left child of another node.
### Function Contract

**Inputs**

- `root`: The root of a nonempty binary tree, represented by level-order values in cOde(n) cases.

**Return value**

Return the sum of values belonging to leaf nodes reached through a parent's left edge.

### Examples
#### Example 1

![](images/leftsum-tree.jpg)

- **Input:** `root = [3,9,20,null,null,15,7]`
- **Output:** `24`
- **Explanation:** There are two left leaves in the binary tree, with values 9 and 15 respectively.
#### Example 2

- **Input:** `root = [1]`
- **Output:** `0`
### Constraints

- The number of nodes in the tree is in the range `[1, 1000]`.

- $-1000 \le \text{Node.val} \le 1000$