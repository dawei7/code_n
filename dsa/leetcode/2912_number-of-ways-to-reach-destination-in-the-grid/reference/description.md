### 1. Description

You are given two integers `n` and `m` which represent the size of a **1-indexed **grid. You are also given an integer `k`, a **1-indexed** integer array `source` and a **1-indexed** integer array `dest`, where `source` and `dest` are in the form `[x, y]` representing a cell on the given grid.

You can move through the grid in the following way:

- You can go from cell `[x_1, y_1]` to cell `[x_2, y_2]` if either $x_{1} = x_{2}$ or $y_{1} = y_{2}$.

- Note that you **can't** move to the cell you are already in e.g. $x_{1} = x_{2}$ and $y_{1} = y_{2}$.

Return *the number of ways you can reach* `dest` *from* `source` *by moving through the grid* **exactly** `k` *times.*

Since the answer may be very large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

- **Input:** $n = 3, m = 2, k = 2, source = [1,1], dest = [2,2]$
- **Output:** `2`
- **Explanation:** There are 2 possible sequences of reaching [2,2] from [1,1]:
- [1,1] -> [1,2] -> [2,2]
- [1,1] -> [2,1] -> [2,2]

#### Example 2

- **Input:** $n = 3, m = 4, k = 3, source = [1,2], dest = [2,3]$
- **Output:** `9`
- **Explanation:** There are 9 possible sequences of reaching [2,3] from [1,2]:
- [1,2] -> [1,1] -> [1,3] -> [2,3]
- [1,2] -> [1,1] -> [2,1] -> [2,3]
- [1,2] -> [1,3] -> [3,3] -> [2,3]
- [1,2] -> [1,4] -> [1,3] -> [2,3]
- [1,2] -> [1,4] -> [2,4] -> [2,3]
- [1,2] -> [2,2] -> [2,1] -> [2,3]
- [1,2] -> [2,2] -> [2,4] -> [2,3]
- [1,2] -> [3,2] -> [2,2] -> [2,3]
- [1,2] -> [3,2] -> [3,3] -> [2,3]

### 4. Constraints

- $2 \le n, m \le 10^{9}$

- $1 \le k \le 10^{5}$

- $\text{source.length} = \text{dest.length} = 2$

- $1 \le \text{source}[1], \text{dest}[1] \le n$

- $1 \le \text{source}[2], \text{dest}[2] \le m$
