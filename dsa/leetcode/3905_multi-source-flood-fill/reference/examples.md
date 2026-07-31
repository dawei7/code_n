## Examples

**Example 1**

- Input: `n = 3, m = 3, sources = [[0,0,1],[2,2,2]]`
- Output: `[[1,1,2],[1,2,2],[2,2,2]]`
- Explanation:

  | Time | Grid state |
  |---:|---|
  | `0` | `[[1,0,0],[0,0,0],[0,0,2]]` |
  | `1` | `[[1,1,0],[1,0,2],[0,2,2]]` |
  | `2` | `[[1,1,2],[1,2,2],[2,2,2]]` |

  At time `2`, cells `(0, 2)`, `(1, 1)`, and `(2, 0)` receive both colors during the same step. Each therefore takes the larger competing value, `2`.

**Example 2**

- Input: `n = 3, m = 3, sources = [[0,1,3],[1,1,5]]`
- Output: `[[3,3,3],[5,5,5],[5,5,5]]`
- Explanation:

  | Time | Grid state |
  |---:|---|
  | `0` | `[[0,3,0],[0,5,0],[0,0,0]]` |
  | `1` | `[[3,3,3],[5,5,5],[0,5,0]]` |
  | `2` | `[[3,3,3],[5,5,5],[5,5,5]]` |

  The two source cells are adjacent and retain their original colors. At the first step, the lower source reaches the cells on either side of it with color `5`, while the upper source fills the remaining cells in its row with color `3`. The last two cells are reached from color `5` at time `2`.

**Example 3**

- Input: `n = 2, m = 2, sources = [[1,1,5]]`
- Output: `[[5,5],[5,5]]`
- Explanation:

  | Time | Grid state |
  |---:|---|
  | `0` | `[[0,0],[0,5]]` |
  | `1` | `[[0,5],[5,5]]` |
  | `2` | `[[5,5],[5,5]]` |

  With only one source, every reachable cell receives color `5`; the diagonally opposite corner is filled after two orthogonal steps.
