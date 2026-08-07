## Description

You are given an `m x n` integer matrix `mat` and an integer `k`. The matrix rows are 0-indexed.

The following proccess happens `k` times:

- **Even-indexed** rows (0, 2, 4, ...) are cyclically shifted to the left.

![](images/lshift.jpg)

- **Odd-indexed** rows (1, 3, 5, ...) are cyclically shifted to the right.

![](images/rshift-stlone.jpg)

Return `true` if the final modified matrix after `k` steps is identical to the original matrix, and `false` otherwise.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4

**Output:** false

**Explanation:**

In each step left shift is applied to rows 0 and 2 (even indices), and right shift to row 1 (odd index).

![](images/t1-2.jpg)

</div>
#### Example 2

<div class="example-block">
**Input:** mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2

**Output:** true

**Explanation:**

![](images/t1-3.jpg)

</div>
#### Example 3

<div class="example-block">
**Input:** mat = [[2,2],[2,2]], k = 3

**Output:** true

**Explanation:**

As all the values are equal in the matrix, even after performing cyclic shifts the matrix will remain the same.

</div>
### Constraints

- $1 \le \text{mat.length} \le 25$

- $1 \le \text{mat}[i].length \le 25$

- $1 \le \text{mat}[i][j] \le 25$

- $1 \le k \le 50$