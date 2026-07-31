## Examples

**Example 1**

- Input: `nums = [1,4,7], k = 3, queries = [[0,1],[0,2]]`
- Output: `[1,2]`
- Explanation: One optimal choice of operations for each query is shown below.

| `i` | `[l_i, r_i]` | `nums[l_i..r_i]` | Possible | Operations | Final `nums[l_i..r_i]` | `ans[i]` |
|---:|---|---|---|---|---|---:|
| 0 | `[0,1]` | `[1,4]` | Yes | `nums[0] + k = 1 + 3 = 4 = nums[1]` | `[4,4]` | 1 |
| 1 | `[0,2]` | `[1,4,7]` | Yes | `nums[0] + k = 1 + 3 = 4 = nums[1]`<br>`nums[2] - k = 7 - 3 = 4 = nums[1]` | `[4,4,4]` | 2 |

Thus, `ans = [1,2]`.

**Example 2**

- Input: `nums = [1,2,4], k = 2, queries = [[0,2],[0,0],[1,2]]`
- Output: `[-1,0,1]`
- Explanation: One optimal choice of operations for each possible query is shown below.

| `i` | `[l_i, r_i]` | `nums[l_i..r_i]` | Possible | Operations | Final `nums[l_i..r_i]` | `ans[i]` |
|---:|---|---|---|---|---|---:|
| 0 | `[0,2]` | `[1,2,4]` | No | `-` | `[1,2,4]` | -1 |
| 1 | `[0,0]` | `[1]` | Yes | Already equal | `[1]` | 0 |
| 2 | `[1,2]` | `[2,4]` | Yes | `nums[1] + k = 2 + 2 = 4 = nums[2]` | `[4,4]` | 1 |

Thus, `ans = [-1,0,1]`.
