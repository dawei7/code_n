## Examples

**Example 1**

- Input: `nums = [1,100,1], x = 1`
- Output: `4`
- **Explanation:** Four intervals qualify: `nums[0..0]` has sum `1`; `nums[0..1]` has sum `1 + 100 = 101`; `nums[1..2]` has sum `100 + 1 = 101`; and `nums[2..2]` has sum `1`. Every listed sum begins and ends with `1`, so the answer is `4`.

**Example 2**

- Input: `nums = [1], x = 2`
- Output: `0`
- **Explanation:** The only subarray is `nums[0..0]`, whose sum is `1`. It does not meet the required digit conditions for `x = 2`, leaving no valid subarray.
