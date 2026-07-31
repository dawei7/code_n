## Examples

**Example 1**

- Input: `grid = [[3,3,5],[3,3,5]], k = 2`
- Output: `2`
- Explanation: Select the left $2 \times 2$ submatrix, which covers the first two columns, twice. After the first operation the grid is `[[4,4,5],[4,4,5]]`; after the second it is `[[5,5,5],[5,5,5]]`. All cells now equal $5$, and two operations are minimal.

**Example 2**

- Input: `grid = [[1,2],[2,3]], k = 1`
- Output: `4`
- Explanation: A $1 \times 1$ operation changes only its selected cell, so the smallest possible common value is the current maximum, $3$. Raising the entries requires respectively $2$, $1$, $1$, and $0$ operations, for $2+1+1+0=4$ in total.
