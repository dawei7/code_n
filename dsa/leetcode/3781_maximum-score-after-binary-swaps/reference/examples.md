## Examples

**Example 1**

- Input: `nums = [2,1,5,2,3], s = "01010"`
- Output: `7`
- Explanation:
  - Swap at `i = 0`, changing `"01010"` into `"10010"`.
  - Then swap at `i = 2`, changing `"10010"` into `"10100"`.
  - The ones now occupy positions `0` and `2`, so they contribute `nums[0] + nums[2] = 2 + 5 = 7`.
  - No reachable arrangement has a greater score.

**Example 2**

- Input: `nums = [4,7,2,9], s = "0000"`
- Output: `0`
- Explanation:
  - The string contains no `'1'` character, so no legal swap exists and no position contributes to the score.
  - The score remains `0`.
