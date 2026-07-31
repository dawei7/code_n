## Examples

**Example 1**

- Input: `matrix = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,2,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]`
- Output: `1`
- Explanation: The only nonzero cell is the `2` at `(3, 3)`. Its distance-two square is shown below. The four positions marked `X` have row distance and column distance both equal to `2`, so they are ignored. Every other in-bounds position inside the square is considered and contains `0`; the outer border is outside this cell's neighborhood. No considered value exceeds `2`, so this cell is the single local maximum.

| row \ column | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | outside | outside | outside | outside | outside | outside | outside |
| 1 | outside | X | 0 | 0 | 0 | X | outside |
| 2 | outside | 0 | 0 | 0 | 0 | 0 | outside |
| 3 | outside | 0 | 0 | **2** | 0 | 0 | outside |
| 4 | outside | 0 | 0 | 0 | 0 | 0 | outside |
| 5 | outside | X | 0 | 0 | 0 | X | outside |
| 6 | outside | outside | outside | outside | outside | outside | outside |

**Example 2**

- Input: `matrix = [[1,2],[3,4]]`
- Output: `1`
- Explanation: The cell containing `4` has no considered value greater than itself. Each of the other three nonzero cells sees a strictly greater value in its considered neighborhood, so only `4` qualifies.

**Example 3**

- Input: `matrix = [[1,0,1],[0,1,0],[1,0,1]]`
- Output: `5`
- Explanation: Each `1` uses radius one. The diagonal positions are the four excluded corners, so only the cell itself and its in-bounds horizontal and vertical neighbors are considered. Those positions contain only `0` or `1`, and all five cells containing `1` are local maxima.

**Example 4**

- Input: `matrix = [[1,1],[1,1]]`
- Output: `4`
- Explanation: A local maximum is disqualified only by a strictly greater value. Since every entry equals `1`, each of the four cells qualifies.
