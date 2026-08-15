### 1. Description

You are given an `m x n` integer matrix `matrix` with the following two properties:

- Each row is sorted in non-decreasing order.

- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` *if* `target` *is in* `matrix` *or* `false` *otherwise*.

You must write a solution in $O(log(m * n))$ time complexity.

### 2. Function Contract

**Inputs**

- `matrix`: A rectangular matrix satisfying the row and cross-row ordering rules.
- `target`: The integer to locate.

**Return value**

Return `true` if any matrix cell equals `target`; otherwise return `false`.

### 3. Examples

#### Example 1

![](images/mat.jpg)

- **Input:** $matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3$
- **Output:** `true`

#### Example 2

![](images/mat2.jpg)

- **Input:** $matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13$
- **Output:** `false`

### 4. Constraints

- $m = \text{matrix.length}$

- $n = \text{matrix}[i].length$

- $1 \le m, n \le 100$

- $-10^{4} \le \text{matrix}[i][j], target \le 10^{4}$
