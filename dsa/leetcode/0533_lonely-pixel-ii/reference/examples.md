## Examples

**Example 1**

- Input: `picture = [["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","W","B","W","B","W"]], target = 3`
- Output: `6`
- **Explanation:** The six qualifying pixels are the black cells in columns `1` and `3` of rows `0`, `1`, and `2`.
  For `(r, c) = (0, 1)`, row `0` and column `1` each contain three black pixels. The other black cells in column `1`
  occur in rows `1` and `2`, and those rows are exactly equal to row `0`. The same reasoning applies to column `3`.

The first source diagram is represented below. `B*` marks a qualifying pixel.

| Row \ Column | 0 | 1 | 2 | 3 | 4 | 5 |
|---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | W | B* | W | B* | B | W |
| 1 | W | B* | W | B* | B | W |
| 2 | W | B* | W | B* | B | W |
| 3 | W | W | B | W | B | W |

**Example 2**

- Input: `picture = [["W","W","B"],["W","W","B"],["W","W","B"]], target = 1`
- Output: `0`

The second source diagram contains three black pixels in one column, so that column does not have the required count
of one.

| Row \ Column | 0 | 1 | 2 |
|---:|:---:|:---:|:---:|
| 0 | W | W | B |
| 1 | W | W | B |
| 2 | W | W | B |
