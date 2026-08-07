## Description

Given the `root` of a Binary Search Tree (BST), return *the minimum absolute difference between the values of any two different nodes in the tree*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

![](images/bst1.jpg)

- **Input:** `root = [4,2,6,1,3]`
- **Output:** `1`
#### Example 2

![](images/bst2.jpg)

- **Input:** `root = [1,0,48,null,null,12,49]`
- **Output:** `1`
### Constraints

- The number of nodes in the tree is in the range $[2, 10^{4}]$.

- $0 \le \text{Node.val} \le 10^{5}$

**Note:** This question is the same as 783: <a href="https://leetcode.com/problems/minimum-distance-between-bst-nodes/" target="_blank">https://leetcode.com/problems/minimum-distance-between-bst-nodes/</a>