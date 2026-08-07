## Description

Given the `root` of a binary tree, return all **duplicate subtrees**.

For each kind of duplicate subtrees, you only need to return the root node of any **one** of them.

Two trees are **duplicate** if they have the **same structure** with the **same node values**.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

![](images/e1.jpg)

- **Input:** `root = [1,2,3,4,null,2,4,null,null,4]`
- **Output:** `[[2,4],[4]]`
#### Example 2

![](images/e2.jpg)

- **Input:** `root = [2,1,1]`
- **Output:** `[[1]]`
#### Example 3

![](images/e33.jpg)

- **Input:** `root = [2,2,2,3,null,3,null]`
- **Output:** `[[2,3],[3]]`
### Constraints

- The number of the nodes in the tree will be in the range `[1, 5000]`

- $-200 \le \text{Node.val} \le 200$