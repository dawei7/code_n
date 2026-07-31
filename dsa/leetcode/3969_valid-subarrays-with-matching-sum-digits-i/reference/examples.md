## Examples

**Example 1**

- Input: `nums = [1,100,1], x = 1`
- Output: `4`
- **Explanation:** Four subarrays qualify: `nums[0..0]` has sum `1`, `nums[0..1]` has sum `1 + 100 = 101`, `nums[1..2]` has sum `100 + 1 = 101`, and `nums[2..2]` has sum `1`. Each listed sum starts and ends with `1`, so the count is `4`.

**Example 2**

- Input: `nums = [1], x = 2`
- Output: `0`
- **Explanation:** The only subarray is `nums[0..0]`, whose sum is `1`. That sum does not satisfy either boundary-digit requirement for `x = 2`, so no valid subarray exists.
