## Description

Given an `m x n` `matrix`, return *all elements of the* `matrix` *in spiral order*.
### Function Contract

**Inputs**

- `matrix`: A non-empty rectangular integer matrix.

Let $m$ be the row count and $n$ be the column count.

**Return value**

Return every matrix element once, beginning at the top-left and following a clockwise inward spiral.

### Examples
#### Example 1

![](images/spiral1.jpg)

- **Input:** $matrix = [[1,2,3],[4,5,6],[7,8,9]]$
- **Output:** `[1,2,3,6,9,8,7,4,5]`
#### Example 2

![](images/spiral.jpg)

- **Input:** $matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]$
- **Output:** `[1,2,3,4,8,12,11,10,9,5,6,7]`
### Constraints

- $m = \text{matrix.length}$

- $n = \text{matrix}[i].length$

- $1 \le m, n \le 10$

- $-100 \le \text{matrix}[i][j] \le 100$