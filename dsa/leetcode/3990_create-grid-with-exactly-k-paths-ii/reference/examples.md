## Examples

**Example 1**

- Input: `k = 2`
- Output: `["..#","#..","#.."]`
- **Explanation:** The returned strings describe this $3 \times 3$ grid:

  | Row / column | `0` | `1` | `2` |
  |---|---|---|---|
  | `0` | `.` | `.` | `#` |
  | `1` | `#` | `.` | `.` |
  | `2` | `#` | `.` | `.` |

  It has exactly two valid paths:

  - `(0, 0) -> (0, 1) -> (1, 1) -> (1, 2) -> (2, 2)`
  - `(0, 0) -> (0, 1) -> (1, 1) -> (2, 1) -> (2, 2)`

**Example 2**

- Input: `k = 3`
- Output: `["...","#..","#.."]`
- **Explanation:** This construction differs only by opening the top-right cell:

  | Row / column | `0` | `1` | `2` |
  |---|---|---|---|
  | `0` | `.` | `.` | `.` |
  | `1` | `#` | `.` | `.` |
  | `2` | `#` | `.` | `.` |

  The grid therefore has exactly these three valid paths:

  - `(0, 0) -> (0, 1) -> (0, 2) -> (1, 2) -> (2, 2)`
  - `(0, 0) -> (0, 1) -> (1, 1) -> (1, 2) -> (2, 2)`
  - `(0, 0) -> (0, 1) -> (1, 1) -> (2, 1) -> (2, 2)`
