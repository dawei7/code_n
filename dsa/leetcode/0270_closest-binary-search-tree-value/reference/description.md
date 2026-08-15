### 1. Description

Given the `root` of a binary search tree and a `target` value, return *the value in the BST that is closest to the* `target`. If there are multiple answers, print the smallest.

### 2. Function Contract

**Inputs**

- `root`: The nonempty root of a binary search tree.
- `target`: The numeric value to approximate with a value from the tree.

Let $n$ be the number of nodes in the tree, and let $h$ be its height.

**Return value**

Return the node value with minimum absolute distance from `target`, choosing the smaller value if there is a tie.

### 3. Examples

#### Example 1

![](images/closest1-1-tree.jpg)

- **Input:** `root = [4,2,5,1,3], target = 3.714286`
- **Output:** `4`

#### Example 2

- **Input:** `root = [1], target = 4.428571`
- **Output:** `1`

### 4. Constraints

- The number of nodes in the tree is in the range $[1, 10^{4}]$.

- $0 \le \text{Node.val} \le 10^{9}$

- $-10^{9} \le target \le 10^{9}$
