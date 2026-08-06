## Function Contract

**Inputs**

- `width`: The number of columns in `M`.
- `height`: The number of rows in `M`.
- `sideLength`: The side length of every constrained square submatrix.
- `maxOnes`: The inclusive maximum number of ones permitted in each constrained square.

Let $s = \texttt{sideLength}$. A square submatrix is contiguous in both rows and columns, has exactly $s^2$ cells, and must contain at most `maxOnes` entries equal to `1`.

**Return value**

- Return the maximum total number of ones achievable across all `width * height` cells of `M`. Only the count is returned; no matrix construction is required.
