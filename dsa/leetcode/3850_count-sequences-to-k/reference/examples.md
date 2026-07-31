## Examples

**Example 1**

- Input: `nums = [2,3,2], k = 6`
- Output: `2`
- Explanation: Exactly the following two action sequences finish with `val == k`.

| Sequence | Operation on `nums[0]` | Operation on `nums[1]` | Operation on `nums[2]` | Final `val` |
|---:|---|---|---|---:|
| 1 | Multiply: `val = 1 * 2 = 2` | Multiply: `val = 2 * 3 = 6` | Leave `val` unchanged | `6` |
| 2 | Leave `val` unchanged | Multiply: `val = 1 * 3 = 3` | Multiply: `val = 3 * 2 = 6` | `6` |

**Example 2**

- Input: `nums = [4,6,3], k = 2`
- Output: `2`
- Explanation: Exactly the following two action sequences finish with `val == k`. The first demonstrates that an intermediate rational value may later become the target integer.

| Sequence | Operation on `nums[0]` | Operation on `nums[1]` | Operation on `nums[2]` | Final `val` |
|---:|---|---|---|---:|
| 1 | Multiply: `val = 1 * 4 = 4` | Divide: `val = 4 / 6 = 2 / 3` | Multiply: `val = (2 / 3) * 3 = 2` | `2` |
| 2 | Leave `val` unchanged | Multiply: `val = 1 * 6 = 6` | Divide: `val = 6 / 3 = 2` | `2` |

**Example 3**

- Input: `nums = [1,5], k = 1`
- Output: `3`
- Explanation: Multiplication by `1`, division by `1`, and leaving the first value unchanged are three distinct choices, and each can be followed by leaving the second value unchanged.

| Sequence | Operation on `nums[0]` | Operation on `nums[1]` | Final `val` |
|---:|---|---|---:|
| 1 | Multiply: `val = 1 * 1 = 1` | Leave `val` unchanged | `1` |
| 2 | Divide: `val = 1 / 1 = 1` | Leave `val` unchanged | `1` |
| 3 | Leave `val` unchanged | Leave `val` unchanged | `1` |
