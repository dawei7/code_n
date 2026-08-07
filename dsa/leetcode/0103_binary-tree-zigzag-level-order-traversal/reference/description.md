## Description

Given the `root` of a binary tree, return *the zigzag level order traversal of its nodes' values*. (i.e., from left to right, then right to left for the next level and alternate between).
### Function Contract

**Inputs**

- `root`: The root of the binary tree, or `null` for an empty tree.

**Return value**

Return one value list per tree depth, ordered from top to bottom and with the reading direction alternating at each level.

### Examples
#### Example 1

![](images/tree1.jpg)

- **Input:** `root = [3,9,20,null,null,15,7]`
- **Output:** `[[3],[20,9],[15,7]]`
#### Example 2

- **Input:** `root = [1]`
- **Output:** `[[1]]`
#### Example 3

- **Input:** `root = []`
- **Output:** `[]`
### Constraints

- The number of nodes in the tree is in the range `[0, 2000]`.

- $-100 \le \text{Node.val} \le 100$