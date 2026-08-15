### 1. Description

You are given an integer `n`. You have an `n x n` binary grid `grid` with all values initially `1`'s except for some indices given in the array `mines`. The $$i^{\text{th}}$$ element of the array `mines` is defined as $\text{mines}[i] = [x_{i}, y_{i}]$ where $grid[x_{i}][y_{i}] = 0$.

Return *the order of the largest **axis-aligned** plus sign of *1*'s contained in *`grid`. If there is none, return `0`.

An **axis-aligned plus sign** of `1`'s of order `k` has some center $\text{grid}[r][c] = 1$ along with four arms of length $k - 1$ going up, down, left, and right, and made of `1`'s. Note that there could be `0`'s or `1`'s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for `1`'s.

### 2. Function Contract

**Inputs**

- `n`: Input parameter (`int`).
- `mines`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

![](images/plus1-grid.jpg)

- **Input:** $n = 5, mines = [[4,2]]$
- **Output:** `2`
- **Explanation:** In the above grid, the largest plus sign can only be of order 2. One of them is shown.

#### Example 2

![](images/plus2-grid.jpg)

- **Input:** $n = 1, mines = [[0,0]]$
- **Output:** `0`
- **Explanation:** There is no plus sign, so return 0.

### 4. Constraints

- $1 \le n \le 500$

- $1 \le \text{mines.length} \le 5000$

- $0 \le x_{i}, y_{i} < n$

- All the pairs $(x_{i}, y_{i})$ are **unique**.
