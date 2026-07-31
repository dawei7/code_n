## Examples

**Example 1**

- Input: `grid = [[0,1],[2,0]], k = 1`
- Output: `2`
- Explanation:

  The optimal path proceeds through the following cells:

  | Cell | `grid[i][j]` | Score | Total Score | Cost | Total Cost |
  |---|---:|---:|---:|---:|---:|
  | `(0,0)` | `0` | `0` | `0` | `0` | `0` |
  | `(1,0)` | `2` | `2` | `2` | `1` | `1` |
  | `(1,1)` | `0` | `0` | `2` | `0` | `1` |

  Therefore, the maximum possible score is `2`.

**Example 2**

- Input: `grid = [[0,1],[1,2]], k = 1`
- Output: `-1`
- Explanation: No path can reach `(1,1)` without making its total cost exceed `k`. Therefore, the answer is `-1`.
