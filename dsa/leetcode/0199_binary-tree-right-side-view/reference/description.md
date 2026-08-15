### 1. Description

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return *the values of the nodes you can see ordered from top to bottom*.

### 2. Function Contract

**Inputs**

- `root`: The root of a binary tree, or `null` when the tree is empty.

**Return value**

Return one visible value per occupied level, ordered from top to bottom.

### 3. Examples

#### Example 1

- **Input:** root = [1,2,3,null,5,null,4]

- **Output:** [1,3,4]

- **Explanation:** ![](images/tmpd5jn43fs-1.png)

#### Example 2

- **Input:** root = [1,2,3,4,null,null,null,5]

- **Output:** [1,3,4,5]

- **Explanation:** ![](images/tmpkpe40xeh-1.png)

#### Example 3

- **Input:** root = [1,null,3]

- **Output:** [1,3]

#### Example 4

- **Input:** root = []

- **Output:** []

### 4. Constraints

- The number of nodes in the tree is in the range `[0, 100]`.

- $-100 \le \text{Node.val} \le 100$
