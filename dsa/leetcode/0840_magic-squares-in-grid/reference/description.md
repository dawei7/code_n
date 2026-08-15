### 1. Description

A `3 x 3` **magic square** is a `3 x 3` grid filled with distinct numbers **from **1** to **9 such that each row, column, and both diagonals all have the same sum.

Given a `row x col` `grid` of integers, how many `3 x 3` magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, `grid` may contain numbers up to 15.

### 2. Function Contract

**Inputs**

- `grid`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

![](images/magic_main.jpg)

- **Input:** `grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]`
- **Output:** `1`
- **Explanation:** The following subgrid is a 3 x 3 magic square:
![](images/magic_valid.jpg)
while this one is not:
![](images/magic_invalid.jpg)
In total, there is only one magic square inside the given grid.

#### Example 2

- **Input:** `grid = [[8]]`
- **Output:** `0`

### 4. Constraints

- $row = \text{grid.length}$

- $col = \text{grid}[i].length$

- $1 \le row, col \le 10$

- $0 \le \text{grid}[i][j] \le 15$
