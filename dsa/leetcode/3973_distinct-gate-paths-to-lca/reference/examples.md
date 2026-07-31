## Examples

**Example 1**

- Input: `n = 3, parent = [-1,0,0], gates = [[1,0,1],[0,1,1],[1,1,0]], queries = [[1,0,2,0],[1,1,2,0],[1,0,2,1]]`
- Output: `1`
- **Explanation:** Both people move from a child of the root to node `0` in every query. The table retains every per-query path and multiplicity from the source explanation.

| `i` | Alice `[Node, Card]` | Bob `[Node, Card]` | LCA | Alice Path | Bob Path | Alice Ways | Bob Ways | Total Ways |
| ---: | --- | --- | ---: | --- | --- | --- | --- | --- |
| 0 | `[1, 0]`: Blue | `[2, 0]`: Blue | 0 | `1 -> 0` | `2 -> 0` | 2: one blue gate plus one white gate at node `1` | 1: the blue gate at node `2` | `2 * 1 = 2` |
| 1 | `[1, 1]`: Red | `[2, 0]`: Blue | 0 | `1 -> 0` | `2 -> 0` | 1: the white gate at node `1` | 1: the blue gate at node `2` | `1 * 1 = 1` |
| 2 | `[1, 0]`: Blue | `[2, 1]`: Red | 0 | `1 -> 0` | `2 -> 0` | 2: one blue gate plus one white gate at node `1` | 1: the red gate at node `2` | `2 * 1 = 2` |

Thus the requested aggregate is `2 XOR 1 XOR 2 = 1`.

**Example 2**

- Input: `n = 3, parent = [-1,0,1], gates = [[0,1,2],[1,0,1],[0,0,3]], queries = [[2,0,1,0],[2,1,0,0],[1,1,2,1]]`
- Output: `3`
- **Explanation:** Node `2` has three separate white gates, so its first upward move has three choices even though all three choices produce the same new card color. The table retains every path, no-move case, factor, and product from the source explanation.

| `i` | Alice `[Node, Card]` | Bob `[Node, Card]` | LCA | Alice Path | Bob Path | Alice Ways | Bob Ways | Total Ways |
| ---: | --- | --- | ---: | --- | --- | --- | --- | --- |
| 0 | `[2, 0]`: Blue | `[1, 0]`: Blue | 1 | `2 -> 1` | `1` | 3: the three white gates at node `2` | 1: no move | `3 * 1 = 3` |
| 1 | `[2, 1]`: Red | `[0, 0]`: Blue | 0 | `2 -> 1 -> 0` | `0` | `3 * 1 = 3`: three white choices at node `2`, then the white gate at node `1` | 1: no move | `3 * 1 = 3` |
| 2 | `[1, 1]`: Red | `[2, 1]`: Red | 1 | `1` | `2 -> 1` | 1: no move | 3: the three white gates at node `2` | `1 * 3 = 3` |

The final value is `3 XOR 3 XOR 3 = 3`.
