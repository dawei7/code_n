## Description

You are given the `root` of a **binary tree** that consists of exactly `3` nodes: the root, its left child, and its right child.

Return `true` *if the value of the root is equal to the **sum** of the values of its two children, or *`false`* otherwise*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

![](images/graph3drawio.png)

- **Input:** `root = [10,4,6]`
- **Output:** `true`
- **Explanation:** The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
10 is equal to 4 + 6, so we return true.
#### Example 2

![](images/graph3drawio-1.png)

- **Input:** `root = [5,3,1]`
- **Output:** `false`
- **Explanation:** The values of the root, its left child, and its right child are 5, 3, and 1, respectively.
5 is not equal to 3 + 1, so we return false.
### Constraints

- The tree consists only of the root, its left child, and its right child.

- $-100 \le \text{Node.val} \le 100$