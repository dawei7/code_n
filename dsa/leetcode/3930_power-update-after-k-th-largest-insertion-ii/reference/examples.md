## Examples

**Example 1**

- Input: `nums = [2], p = 4, queries = [[3,1],[1,2]]`
- Output: `[64,4096]`
- Explanation: The two queries update the growing array and state as follows.

| `i` | Inserted `val_i` | Current `nums` | `k_i` | `k_i`th largest $x$ | Old `p` | New `p = p^x mod (10^9 + 7)` |
|---:|---:|---|---:|---:|---:|---:|
| 0 | 3 | `[2, 3]` | 1 | 3 | 4 | `4^3 mod (10^9 + 7) = 64` |
| 1 | 1 | `[2, 3, 1]` | 2 | 2 | 64 | `64^2 mod (10^9 + 7) = 4096` |

The recorded states are therefore `ans = [64, 4096]`.

**Example 2**

- Input: `nums = [7,5], p = 6, queries = [[4,3],[7,2]]`
- Output: `[1296,220296870]`
- Explanation: The first insertion selects the smallest current value, while the duplicate `7` inserted next changes the second-largest rank.

| `i` | Inserted `val_i` | Current `nums` | `k_i` | `k_i`th largest $x$ | Old `p` | New `p = p^x mod (10^9 + 7)` |
|---:|---:|---|---:|---:|---:|---:|
| 0 | 4 | `[7, 5, 4]` | 3 | 4 | 6 | `6^4 mod (10^9 + 7) = 1296` |
| 1 | 7 | `[7, 5, 4, 7]` | 2 | 7 | 1296 | `1296^7 mod (10^9 + 7) = 220296870` |

Thus the returned list is `ans = [1296, 220296870]`.
