## Description

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called `root`.

Besides the `root`, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if **two directly-linked houses were broken into on the same night**.

Given the `root` of the binary tree, return *the maximum amount of money the thief can rob **without alerting the police***.
### Function Contract

**Inputs**

- `root`: The root of the binary tree of houses; app cases serialize the tree in level order.

**Return value**

Return the maximum sum of values from houses chosen so that no selected node is directly connected to another selected node.

### Examples

#### Example 1

![](images/rob1-tree.jpg)

- **Input:** `root = [3,2,3,null,3,null,1]`
- **Output:** `7`
- **Explanation:** Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
#### Example 2

![](images/rob2-tree.jpg)

- **Input:** `root = [3,4,5,1,3,null,1]`
- **Output:** `9`
- **Explanation:** Maximum amount of money the thief can rob = 4 + 5 = 9.
### Constraints

- The number of nodes in the tree is in the range $[1, 10^{4}]$.

- $0 \le \text{Node.val} \le 10^{4}$