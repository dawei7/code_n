### 1. Description

You are given a 2D integer array `grid` of size `m × n`, and an integer `k`.

In one operation, you can:

- Select any `k x k` **submatrix** of `grid`, and

- Increment **all elements** inside that **submatrix** by 1.

Return the **minimum** number of operations required to make all elements in the grid **equal**. If it is not possible, return -1.

A submatrix `(x1, y1, x2, y2)` is a matrix that forms by choosing all cells $\text{matrix}[x][y]$ where $x1 \le x \le x2$ and $y1 \le y \le y2$.

### 2. Function Contract

**Inputs**

- `grid`: A nonempty rectangular matrix of integers.
- `k`: The common height and width of every submatrix that one operation increments.

Let $m=\lvert\texttt{grid}\rvert$ and $n=\lvert\texttt{\text{grid}[0]}\rvert$. Operations may overlap, and a submatrix may be selected repeatedly. Values can only increase.

**Return value**

Return the minimum number of $k \times k$ increments needed to make all $mn$ entries equal, or `-1` if equality is impossible.

### 3. Examples

#### Example 1

- **Input:** grid = [[3,3,5],[3,3,5]], k = 2

- **Output:** 2

- **Explanation:** Choose the left `2 x 2` submatrix (covering the first two columns) and apply the operation twice.

- After 1 operation: `[[4, 4, 5], [4, 4, 5]]`

- After 2 operations: `[[5, 5, 5], [5, 5, 5]]`

All elements become equal to 5. Thus, the minimum number of operations is 2.

#### Example 2

- **Input:** grid = [[1,2],[2,3]], k = 1

- **Output:** 4

- **Explanation:** Since $k = 1$, each operation increments a single cell $\text{grid}[i][j]$ by 1. To make all elements equal, the final value must be 3.

- Increase $\text{grid}[0][0] = 1$ to 3, requiring 2 operations.

- Increase $\text{grid}[0][1] = 2$ to 3, requiring 1 operation.

- Increase $\text{grid}[1][0] = 2$ to 3, requiring 1 operation.

Thus, the minimum number of operations is $2 + 1 + 1 + 0 = 4$.

### 4. Constraints

- $1 \le m = \text{grid.length} \le 1000$

- $1 \le n = \text{grid}[i].length \le 1000$

- $-10^{5} \le \text{grid}[i][j] \le 10^{5}$

- $1 \le k \le min(m, n)$
