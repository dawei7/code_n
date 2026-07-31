## Examples

**Example 1**

- Input: `nums = [1,3,-1,-3,5,3,6,7], k = 3`
- Output: `[3,3,5,5,6,7]`
- Explanation: Each row shows the visible three-value window and its maximum.

| Window position | Maximum |
|---|---:|
| `[1,3,-1] -3 5 3 6 7` | `3` |
| `1 [3,-1,-3] 5 3 6 7` | `3` |
| `1 3 [-1,-3,5] 3 6 7` | `5` |
| `1 3 -1 [-3,5,3] 6 7` | `5` |
| `1 3 -1 -3 [5,3,6] 7` | `6` |
| `1 3 -1 -3 5 [3,6,7]` | `7` |

**Example 2**

- Input: `nums = [1], k = 1`
- Output: `[1]`
