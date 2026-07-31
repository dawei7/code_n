## Examples

**Example 1**

- Input: `m = 2, n = 3, k = 2`
- Output: `["...","#.."]`
- **Explanation:** The first source visual depicts this grid:

  | Row / column | `0` | `1` | `2` |
  |---|---|---|---|
  | `0` | `.` | `.` | `.` |
  | `1` | `#` | `.` | `.` |

  It has exactly these two valid paths from `(0, 0)` to `(1, 2)`:

  - `(0, 0) → (0, 1) → (0, 2) → (1, 2)`
  - `(0, 0) → (0, 1) → (1, 1) → (1, 2)`

**Example 2**

- Input: `m = 3, n = 3, k = 4`
- Output: `["..#","...","#.."]`
- **Explanation:** The second source visual depicts this grid:

  | Row / column | `0` | `1` | `2` |
  |---|---|---|---|
  | `0` | `.` | `.` | `#` |
  | `1` | `.` | `.` | `.` |
  | `2` | `#` | `.` | `.` |

  It has exactly these four valid paths from `(0, 0)` to `(2, 2)`:

  - `(0, 0) → (0, 1) → (1, 1) → (1, 2) → (2, 2)`
  - `(0, 0) → (0, 1) → (1, 1) → (2, 1) → (2, 2)`
  - `(0, 0) → (1, 0) → (1, 1) → (1, 2) → (2, 2)`
  - `(0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2)`

**Example 3**

- Input: `m = 1, n = 4, k = 2`
- Output: `[]`
- **Explanation:** A one-row grid can have only one positive right/down path count, so no grid of these dimensions can provide exactly two valid paths.
