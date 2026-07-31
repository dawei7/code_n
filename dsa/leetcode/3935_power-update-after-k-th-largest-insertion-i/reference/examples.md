## Examples

**Example 1**

- Input: `nums = [2], p = 4, queries = [[3,1],[1,2]]`
- Output: `[64,4096]`
- Explanation: The first insertion makes `3` the largest value, so it is the exponent applied to `4`. The next insertion requests rank two from `[2,3,1]`, selecting `2` and applying it to the previously produced state `64`. The complete progression is:

| `i` | `val_i` | Current `nums` | `k_i` | `k_i`th largest | Prior `p` | New `p = p^x mod (10^9 + 7)` |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 3 | `[2,3]` | 1 | 3 | 4 | $4^3\bmod(10^9+7)=64$ |
| 1 | 1 | `[2,3,1]` | 2 | 2 | 64 | $64^2\bmod(10^9+7)=4096$ |

Thus `ans = [64,4096]`.

**Example 2**

- Input: `nums = [7,5], p = 6, queries = [[4,3],[7,2]]`
- Output: `[1296,220296870]`
- Explanation: Inserting `4` makes it the third-largest element and produces `6^4 = 1296`. After inserting another `7`, the second-largest element is `7`; that exponent is applied to the updated state. The complete progression is:

| `i` | `val_i` | Current `nums` | `k_i` | `k_i`th largest | Prior `p` | New `p = p^x mod (10^9 + 7)` |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 4 | `[7,5,4]` | 3 | 4 | 6 | $6^4\bmod(10^9+7)=1296$ |
| 1 | 7 | `[7,5,4,7]` | 2 | 7 | 1296 | $1296^7\bmod(10^9+7)=220296870$ |

Thus `ans = [1296,220296870]`.
