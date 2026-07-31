## Examples

**Example 1**

- Input: `nums = [3,7,5]`
- Output: `3`
- Explanation: For `k = 3`, `nonPositive(nums, k) = 6`, and $6 \le 3^2$.
  - Reduce `nums[0] = 3` once. Its value becomes `3 - 3 = 0`.
  - Reduce `nums[1] = 7` three times. Its value becomes `7 - 3 - 3 - 3 = -2`.
  - Reduce `nums[2] = 5` twice. Its value becomes `5 - 3 - 3 = -1`.

**Example 2**

- Input: `nums = [1]`
- Output: `1`
- Explanation: For `k = 1`, `nonPositive(nums, k) = 1`, and $1 \le 1^2$.
  - Reduce `nums[0] = 1` once. Its value becomes `1 - 1 = 0`.
