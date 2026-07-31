## Examples

**Example 1**

- Input: `nums = [1,3,5,7]`
- Output: `-4`
- Explanation:

  - The even indices are `0` and `2`, containing `nums[0] = 1` and `nums[2] = 5`; these values are added.
  - The odd indices are `1` and `3`, containing `nums[1] = 3` and `nums[3] = 7`; these values are subtracted.
  - Therefore, `nums[0] - nums[1] + nums[2] - nums[3] = 1 - 3 + 5 - 7 = -4`.

**Example 2**

- Input: `nums = [100]`
- Output: `100`
- Explanation:

  - The only element is `nums[0] = 100`, and index `0` is even.
  - No odd-indexed element exists.
  - The alternating sum is consequently just `nums[0] = 100`.
