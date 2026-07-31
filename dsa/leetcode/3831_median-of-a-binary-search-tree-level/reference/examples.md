## Examples

**Example 1**

![A BST path from 4 through its right child 5 to node 7 at level 2.](../assets/example-1-bst.svg)

- Input: `root = [4,null,5,null,7], level = 2`
- Output: `7`
- Explanation: Level `2` contains only `[7]`, whose sole value is its median.

**Example 2**

![A three-node BST rooted at 6, with 3 and 8 highlighted at level 1.](../assets/example-2-bst.svg)

- Input: `root = [6,3,8], level = 1`
- Output: `8`
- Explanation: The values at level `1` are `[3,8]`. With two middle candidates, the upper median is the larger one, `8`.

**Example 3**

![A BST rooted at 2 with left child 1 and an empty level 2.](../assets/example-3-bst.svg)

- Input: `root = [2,1], level = 2`
- Output: `-1`
- Explanation: The tree has no node at level `2`, so the required result is `-1`.
