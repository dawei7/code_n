### 1. Description

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in place</a>.

### 2. Function Contract

**Inputs**

- `matrix`: The rectangular integer matrix to modify.

**Return value**

Return `None`; mutate `matrix` in place so every row and column containing an original zero is filled with zeroes.

### 3. Examples

#### Example 1

![](images/mat1.jpg)

- **Input:** $matrix = [[1,1,1],[1,0,1],[1,1,1]]$
- **Output:** `[[1,0,1],[0,0,0],[1,0,1]]`
#### Example 2

![](images/mat2.jpg)

- **Input:** $matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]$
- **Output:** `[[0,0,0,0],[0,4,5,0],[0,3,1,0]]`

### 4. Constraints

- $m = \text{matrix.length}$

- $n = \text{matrix}[0].length$

- $1 \le m, n \le 200$

- $-2^{31} \le \text{matrix}[i][j] \le 2^{31} - 1$

**Follow up:**

- A straightforward solution using `O(mn)` space is probably a bad idea.

- A simple improvement uses $O(m + n)$ space, but still not the best solution.

- Could you devise a constant space solution?