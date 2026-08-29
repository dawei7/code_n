### 1. Description

You are given a 2D integer matrix `grid` of size `n x m`, an integer array `limits` of length `n`, and an integer `k`. The task is to find the **maximum sum** of **at most** `k` elements from the matrix `grid` such that:

- The number of elements taken from the $i^{\text{th}}$ row of `grid` does not exceed $\text{limits}[i]$.

Return the **maximum sum**.

### 2. Function Contract

**Inputs**

- `grid`: Input parameter (`List[List[int]]`).
- `limits`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** grid = [[1,2],[3,4]], limits = [1,2], k = 2

- **Output:** 7

- **Explanation:** 

- From the second row, we can take at most 2 elements. The elements taken are 4 and 3.

- The maximum possible sum of at most 2 selected elements is $4 + 3 = 7$.

#### Example 2

- **Input:** grid = [[5,3,7],[8,2,6]], limits = [2,2], k = 3

- **Output:** 21

- **Explanation:** 

- From the first row, we can take at most 2 elements. The element taken is 7.

- From the second row, we can take at most 2 elements. The elements taken are 8 and 6.

- The maximum possible sum of at most 3 selected elements is $7 + 8 + 6 = 21$.

### 4. Constraints

- $n = \text{grid.length} = \text{limits.length}$

- $m = \text{grid}[i].length$

- $1 \le n, m \le 500$

- $0 \le \text{grid}[i][j] \le 10^{5}$

- $0 \le \text{limits}[i] \le m$

- $0 \le k \le min(n * m, sum(limits))$
