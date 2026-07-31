## Examples

**Example 1**

- Input: `nums = [-2,-3,1,4]`
- Output: `[2,6]`
- Explanation:
  - Increase `nums[2]` by `1`, giving `nums = [-2, -3, 2, 4]`.
  - Decrease `nums[3]` by `1`, giving `nums = [-2, -3, 2, 3]`.
  - This array alternates parity. Its range is `max(nums) - min(nums) = 3 - (-3) = 6`, the smallest attainable range among parity-alternating arrays produced with exactly two operations.

**Example 2**

- Input: `nums = [0,2,-2]`
- Output: `[1,3]`
- Explanation:
  - Decrease `nums[1]` by `1`, giving `nums = [0, 1, -2]`.
  - The result alternates parity, and its range is `max(nums) - min(nums) = 1 - (-2) = 3`. No parity-alternating array obtainable in exactly one operation has a smaller range.

**Example 3**

- Input: `nums = [7]`
- Output: `[0,0]`
- Explanation: A one-element array is already parity alternating, so it needs no operation. Its maximum and minimum are both `7`, making its minimum possible range `7 - 7 = 0`.
