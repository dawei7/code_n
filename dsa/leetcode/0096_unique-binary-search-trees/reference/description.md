### 1. Description

Given an integer `n`, return *the number of structurally unique **BST'**s (binary search trees) which has exactly *`n`* nodes of unique values from* `1` *to* `n`.

### 2. Function Contract

**Inputs**

- `n`: The number of nodes and the greatest value used in every BST.

**Return value**

Return the count of structurally unique BSTs that use every value from `1` through `n` exactly once.

### 3. Examples

#### Example 1

![](images/uniquebstn3.jpg)

- **Input:** $n = 3$
- **Output:** `5`
#### Example 2

- **Input:** $n = 1$
- **Output:** `1`

### 4. Constraints

- $1 \le n \le 19$