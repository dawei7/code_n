## Examples

**Example 1**

- Input: `nums = [1,4,7], queries = [[0,2,1],[1,1,2],[0,0,3]]`
- Output: `[2,6,6]`
- **Explanation:** The table applies each removal independently. It yields `ans = [2, 6, 6]`.

| `i` | `queries[i]` | `nums[l_i..r_i]` | Removed Evens | Remaining Evens | `k_i` | `ans[i]` |
|---:|---|---|---|---|---:|---:|
| 0 | `[0, 2, 1]` | `[1, 4, 7]` | `[4]` | `2, 6, 8, ...` | 1 | 2 |
| 1 | `[1, 1, 2]` | `[4]` | `[4]` | `2, 6, 8, ...` | 2 | 6 |
| 2 | `[0, 0, 3]` | `[1]` | `[]` | `2, 4, 6, ...` | 3 | 6 |

**Example 2**

- Input: `nums = [2,5,8], queries = [[0,1,2],[1,2,1],[0,2,4]]`
- Output: `[6,2,12]`
- **Explanation:** Each row removes only the even values inside its own inclusive subarray. The resulting array is `ans = [6, 2, 12]`.

| `i` | `queries[i]` | `nums[l_i..r_i]` | Removed Evens | Remaining Evens | `k_i` | `ans[i]` |
|---:|---|---|---|---|---:|---:|
| 0 | `[0, 1, 2]` | `[2, 5]` | `[2]` | `4, 6, 8, ...` | 2 | 6 |
| 1 | `[1, 2, 1]` | `[5, 8]` | `[8]` | `2, 4, 6, ...` | 1 | 2 |
| 2 | `[0, 2, 4]` | `[2, 5, 8]` | `[2, 8]` | `4, 6, 10, 12, ...` | 4 | 12 |

**Example 3**

- Input: `nums = [3,6], queries = [[0,1,1],[1,1,3]]`
- Output: `[2,8]`
- **Explanation:** Removing `6` leaves `2, 4, 8, ...` in both queries, so the requested ranks produce `ans = [2, 8]`.

| `i` | `queries[i]` | `nums[l_i..r_i]` | Removed Evens | Remaining Evens | `k_i` | `ans[i]` |
|---:|---|---|---|---|---:|---:|
| 0 | `[0, 1, 1]` | `[3, 6]` | `[6]` | `2, 4, 8, ...` | 1 | 2 |
| 1 | `[1, 1, 3]` | `[6]` | `[6]` | `2, 4, 8, ...` | 3 | 8 |
