## Examples

**Example 1**

- Input: `heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]`
- Output: `[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]`
- Explanation: Each returned cell has a non-increasing route to both oceans. The table gives one route to each;
  other valid routes may also exist.

| Cell | One route to the Pacific | One route to the Atlantic |
|---|---|---|
| `[0,4]` | Directly across the top edge | Directly across the right edge |
| `[1,3]` | `[1,3]` to `[0,3]` | `[1,3]` to `[1,4]` |
| `[1,4]` | `[1,4]` to `[1,3]` to `[0,3]` | Directly across the right edge |
| `[2,2]` | `[2,2]` to `[1,2]` to `[0,2]` | `[2,2]` to `[2,3]` to `[2,4]` |
| `[3,0]` | Directly across the left edge | `[3,0]` to `[4,0]` |
| `[3,1]` | `[3,1]` to `[3,0]` | `[3,1]` to `[4,1]` |
| `[4,0]` | Directly across the left edge | Directly across the bottom edge |

**Example 2**

- Input: `heights = [[1]]`
- Output: `[[0,0]]`
- Explanation: The only cell touches boundaries of both the Pacific and Atlantic oceans.
