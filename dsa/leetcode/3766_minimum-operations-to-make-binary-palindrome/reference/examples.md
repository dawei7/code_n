## Examples

**Example 1**

- Input: `nums = [1,2,4]`
- Output: `[0,1,1]`
- Explanation: One optimal choice for every element is shown below.

| `nums[i]` | Binary(`nums[i]`) | Nearest Palindrome | Binary (Palindrome) | Operations Required | `ans[i]` |
|---:|---|---:|---|---|---:|
| 1 | `1` | 1 | `1` | Already a palindrome | 0 |
| 2 | `10` | 3 | `11` | Increase by 1 | 1 |
| 4 | `100` | 3 | `11` | Decrease by 1 | 1 |

Therefore, `ans = [0, 1, 1]`.

**Example 2**

- Input: `nums = [6,7,12]`
- Output: `[1,0,3]`
- Explanation: One optimal choice for every element is shown below.

| `nums[i]` | Binary(`nums[i]`) | Nearest Palindrome | Binary (Palindrome) | Operations Required | `ans[i]` |
|---:|---|---:|---|---|---:|
| 6 | `110` | 5 | `101` | Decrease by 1 | 1 |
| 7 | `111` | 7 | `111` | Already a palindrome | 0 |
| 12 | `1100` | 15 | `1111` | Increase by 3 | 3 |

Therefore, `ans = [1, 0, 3]`.
