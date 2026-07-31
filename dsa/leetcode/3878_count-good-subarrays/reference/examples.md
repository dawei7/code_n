## Examples

**Example 1**

- Input: `nums = [4,2,3]`
- Output: `4`
- Explanation: Every subarray can be classified directly:

  | Subarray | Bitwise OR | OR present in subarray? |
  |---|---|:---:|
  | `[4]` | `4 = 4` | Yes |
  | `[2]` | `2 = 2` | Yes |
  | `[3]` | `3 = 3` | Yes |
  | `[4, 2]` | `4 \| 2 = 6` | No |
  | `[2, 3]` | `2 \| 3 = 3` | Yes |
  | `[4, 2, 3]` | `4 \| 2 \| 3 = 7` | No |

  Therefore `[4]`, `[2]`, `[3]`, and `[2, 3]` are the four good subarrays.

**Example 2**

- Input: `nums = [1,3,1]`
- Output: `6`
- Explanation: A subarray containing `3` has OR `3`, while a subarray containing only `1` values has OR `1`. In either case, the OR occurs inside that subarray, so all six non-empty subarrays are good.
