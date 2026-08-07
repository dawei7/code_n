## Description

You are given a `root`, which is the root of a **special** binary tree with `n` nodes. The nodes of the special binary tree are numbered from `1` to `n`. Suppose the tree has `k` leaves in the following order: $b_{1} <_ b_{2} < ... < b_{k}$.

The leaves of this tree have a **special** property! That is, for every leaf $b_{i}$, the following conditions hold:

- The right child of $b_{i}$ is $b_{i} + 1$ if `i < k`, and $b_{1}$ otherwise.

- The left child of $b_{i}$ is $b_{i} - 1$ if `i > 1`, and $b_{k}$ otherwise.

Return* the height of the given tree.*

**Note:** The height of a binary tree is the length of the **longest path** from the root to any other node.
### Function Contract

- Refer to method signature.

### Examples
#### Example 1

- **Input:** `root = [1,2,3,null,null,4,5]`
- **Output:** `2`
- **Explanation:** The given tree is shown in the following picture. Each leaf's left child is the leaf to its left (shown with the blue edges). Each leaf's right child is the leaf to its right (shown with the red edges). We can see that the graph has a height of 2.

![](images/1.png)
#### Example 2

- **Input:** `root = [1,2]`
- **Output:** `1`
- **Explanation:** The given tree is shown in the following picture. There is only one leaf, so it doesn't have any left or right child. We can see that the graph has a height of 1.

![](images/2.png)
#### Example 3

- **Input:** `root = [1,2,3,null,null,4,null,5,6]`
- **Output:** `3`
- **Explanation:** The given tree is shown in the following picture. Each leaf's left child is the leaf to its left (shown with the blue edges). Each leaf's right child is the leaf to its right (shown with the red edges). We can see that the graph has a height of 3.

![](images/3.png)
### Constraints

- $n = number of nodes in the tree$

- $2 \le n \le 10^{4}$

- $1 \le \text{node.val} \le n$

- The input is generated such that each `node.val` is unique.