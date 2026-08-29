### 1. Description

You are given a 2D integer array `grid` of size $m * n$.

You start at the **top-left** cell `(0, 0)` and want to reach the **bottom-right** cell $(m - 1, n - 1)$.

At each step, you **may** move either **right or down**.

The **cost** of a path is defined as the **bitwise XOR** of all the values in the cells along that path, **including** the start and end cells.

Return the **minimum** possible XOR value among all valid paths from `(0, 0)` to $(m - 1, n - 1)$.

### 2. Function Contract

**Inputs**

- `grid`: A non-empty rectangular matrix of nonnegative integers.

Let $m=\lvert\texttt{grid}\rvert$, let $n=\lvert\texttt{\text{grid}[0]}\rvert$, and let $b=10$. Every legal cell value and every XOR formed from them belongs to $[0,2^b)$.

Every path contains exactly $m+n-1$ cells and may use only right and down moves. The start and destination values both participate in its XOR.

**Return value**

Return the minimum integer among the XOR costs of all valid paths from `(0, 0)` to $(m - 1, n - 1)$.

### 3. Examples

#### Example 1

- **Input:** grid = [[1,2],[3,4]]

- **Output:** 6

- **Explanation:** There are two valid paths:

- `(0, 0) → (0, 1) → (1, 1)` with XOR: $1 XOR 2 XOR 4 = 7$

- `(0, 0) → (1, 0) → (1, 1)` with XOR: $1 XOR 3 XOR 4 = 6$

The minimum XOR value among all valid paths is 6.

#### Example 2

- **Input:** grid = [[6,7],[5,8]]

- **Output:** 9

- **Explanation:** There are two valid paths:

- `(0, 0) → (0, 1) → (1, 1)` with XOR: $6 XOR 7 XOR 8 = 9$

- `(0, 0) → (1, 0) → (1, 1)` with XOR: $6 XOR 5 XOR 8 = 11$

The minimum XOR value among all valid paths is 9.

#### Example 3

- **Input:** grid = [[2,7,5]]

- **Output:** 0

- **Explanation:** There is only one valid path:

- `(0, 0) → (0, 1) → (0, 2)` with XOR: $2 XOR 7 XOR 5 = 0$

The XOR value of this path is 0, which is the minimum possible.

### 4. Constraints

- $1 \le m = \text{grid.length} \le 1000$

- $1 \le n = \text{grid}[i].length \le 1000$

- $m * n \le 1000$

- $0 \le \text{grid}[i][j] \le 1023$
