## Description

Given the `root` of a binary tree, return *the level order traversal of its nodes' values*. (i.e., from left to right, level by level).
### Function Contract

**Inputs**

- `root`: The root of the binary tree, or `null` for an empty tree.

**Return value**

Return a list containing one list of values for each depth, ordered from the root level downward. Values at the same depth appear from left to right.

### Examples

#### Example 1

![](images/tree1.jpg)

- **Input:** `root = [3,9,20,null,null,15,7]`
- **Output:** `[[3],[9,20],[15,7]]`
#### Example 2

- **Input:** `root = [1]`
- **Output:** `[[1]]`
#### Example 3

- **Input:** `root = []`
- **Output:** `[]`
### Constraints

- The number of nodes in the tree is in the range `[0, 2000]`.

- $-1000 \le \text{Node.val} \le 1000$