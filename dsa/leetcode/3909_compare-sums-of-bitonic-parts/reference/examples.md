## Examples

**Example 1**

- Input: `nums = [1,3,2,1]`
- Output: `1`
- Explanation: The peak is `nums[1] = 3`. The ascending part `[1,3]` sums to `1 + 3 = 4`, while the descending part `[3,2,1]` sums to `3 + 2 + 1 = 6`. The descending sum is larger, so the result is `1`.

**Example 2**

- Input: `nums = [2,4,5,2]`
- Output: `0`
- Explanation: The peak is `nums[2] = 5`. The ascending part `[2,4,5]` has sum `2 + 4 + 5 = 11`; the descending part `[5,2]` has sum `5 + 2 = 7`. The ascending sum is larger, so the result is `0`.

**Example 3**

- Input: `nums = [1,2,4,3]`
- Output: `-1`
- Explanation: The peak is `nums[2] = 4`. The ascending part `[1,2,4]` sums to `1 + 2 + 4 = 7`, and the descending part `[4,3]` also sums to `4 + 3 = 7`. Equal sums produce `-1`.
