## Examples

**Example 1**

- Input: `grid = [[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1]]`
- Output: `1`
- Explanation: There is exactly one corner rectangle. Its four corners are `grid[1][2]`, `grid[1][4]`, `grid[3][2]`, and `grid[3][4]`.

The source image renders this matrix:

| | Column 0 | Column 1 | Column 2 | Column 3 | Column 4 |
|---|---:|---:|---:|---:|---:|
| Row 0 | 1 | 0 | 0 | 1 | 0 |
| Row 1 | 0 | 0 | 1 | 0 | 1 |
| Row 2 | 0 | 0 | 0 | 1 | 0 |
| Row 3 | 1 | 0 | 1 | 0 | 1 |

**Example 2**

- Input: `grid = [[1,1,1],[1,1,1],[1,1,1]]`
- Output: `9`
- Explanation: Four rectangles use a $2 \times 2$ span, four more use either a $2 \times 3$ or $3 \times 2$ span, and one uses the full $3 \times 3$ span.

The source image renders this matrix:

| | Column 0 | Column 1 | Column 2 |
|---|---:|---:|---:|
| Row 0 | 1 | 1 | 1 |
| Row 1 | 1 | 1 | 1 |
| Row 2 | 1 | 1 | 1 |

**Example 3**

- Input: `grid = [[1,1,1,1]]`
- Output: `0`
- Explanation: A rectangle requires four distinct corners. A single row cannot supply corners in two distinct rows.

The source image renders this matrix:

| | Column 0 | Column 1 | Column 2 | Column 3 |
|---|---:|---:|---:|---:|
| Row 0 | 1 | 1 | 1 | 1 |
