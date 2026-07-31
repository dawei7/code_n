## Examples

**Example 1**

- Input: `nums = [12,21,45,33,54]`
- Output: `1`
- Explanation: There are two mirror pairs:
  - `(0,1)` because `reverse(nums[0]) = reverse(12) = 21 = nums[1]`; its distance is `abs(0 - 1) = 1`.
  - `(2,4)` because `reverse(nums[2]) = reverse(45) = 54 = nums[4]`; its distance is `abs(2 - 4) = 2`.
  The smaller of these distances is `1`.

**Example 2**

- Input: `nums = [120,21]`
- Output: `1`
- Explanation: The sole mirror pair is `(0,1)` because `reverse(nums[0]) = reverse(120) = 21 = nums[1]`. Its index distance is `1`.

**Example 3**

- Input: `nums = [21,120]`
- Output: `-1`
- Explanation: No mirror pair exists in this order, so the result is `-1`.
