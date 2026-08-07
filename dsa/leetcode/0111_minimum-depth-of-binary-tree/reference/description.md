## Description

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Note:** A leaf is a node with no children.
### Function Contract

**Inputs**

- `root`: The root of the binary tree, or `null` for an empty tree.

**Return value**

Return the number of nodes on the shortest root-to-leaf path. Return `0` for an empty tree.

### Examples
#### Example 1

![](images/ex_depth.jpg)

- **Input:** `root = [3,9,20,null,null,15,7]`
- **Output:** `2`
#### Example 2

- **Input:** `root = [2,null,3,null,4,null,5,null,6]`
- **Output:** `5`
### Constraints

- The number of nodes in the tree is in the range $[0, 10^{5}]$.

- $-1000 \le \text{Node.val} \le 1000$