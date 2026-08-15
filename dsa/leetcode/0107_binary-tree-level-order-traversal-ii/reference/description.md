### 1. Description

Given the `root` of a binary tree, return *the bottom-up level order traversal of its nodes' values*. (i.e., from left to right, level by level from leaf to root).

### 2. Function Contract

**Inputs**

- `root`: The root of the binary tree, or `null` for an empty tree.

**Return value**

Return a list containing one left-to-right value list for each depth, ordered from the deepest level up to the root level.

### 3. Examples

#### Example 1

![](images/tree1.jpg)

- **Input:** `root = [3,9,20,null,null,15,7]`
- **Output:** `[[15,7],[9,20],[3]]`

#### Example 2

- **Input:** `root = [1]`
- **Output:** `[[1]]`

#### Example 3

- **Input:** `root = []`
- **Output:** `[]`

### 4. Constraints

- The number of nodes in the tree is in the range `[0, 2000]`.

- $-1000 \le \text{Node.val} \le 1000$
