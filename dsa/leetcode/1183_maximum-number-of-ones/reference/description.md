### 1. Description

Consider a matrix `M` with dimensions $width * height$, such that every cell has value `0` or `1`, and any **square** sub-matrix of `M` of size $sideLength * sideLength$ has at most `maxOnes` ones.

Return the maximum possible number of ones that the matrix `M` can have.

### 2. Function Contract

**Inputs**

- `width`: The number of columns in `M`.
- `height`: The number of rows in `M`.
- `sideLength`: The side length of every constrained square submatrix.
- `maxOnes`: The inclusive maximum number of ones permitted in each constrained square.

Let $s = \texttt{sideLength}$. A square submatrix is contiguous in both rows and columns, has exactly $s^2$ cells, and must contain at most `maxOnes` entries equal to `1`.

**Return value**

- Return the maximum total number of ones achievable across all $width * height$ cells of `M`. Only the count is returned; no matrix construction is required.

### 3. Examples

#### Example 1

- **Input:** $width = 3, height = 3, sideLength = 2, maxOnes = 1$
- **Output:** `4`
- **Explanation:** In a 3*3 matrix, no 2*2 sub-matrix can have more than 1 one.
The best solution that has 4 ones is:
[1,0,1]
[0,0,0]
[1,0,1]

#### Example 2

- **Input:** $width = 3, height = 3, sideLength = 2, maxOnes = 2$
- **Output:** `6`
- **Explanation:** [1,0,1]
[1,0,1]
[1,0,1]

### 4. Constraints

- $1 \le width, height \le 100$

- $1 \le sideLength \le width, height$

- $0 \le maxOnes \le sideLength * sideLength$
