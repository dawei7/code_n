### 1. Description

Given a `m x n` matrix `mat` and an integer `k`, return *a matrix* `answer` *where each* $\text{answer}[i][j]$ *is the sum of all elements* $\text{mat}[r][c]$ *for*:

- $i - k \le r \le i + k,$

- $j - k \le c \le j + k$, and

- `(r, c)` is a valid position in the matrix.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1$
- **Output:** `[[12,21,16],[27,45,33],[24,39,28]]`
#### Example 2

- **Input:** $mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2$
- **Output:** `[[45,45,45],[45,45,45],[45,45,45]]`

### 4. Constraints

- $m = \text{mat.length}$

- $n = \text{mat}[i].length$

- $1 \le m, n, k \le 100$

- $1 \le \text{mat}[i][j] \le 100$