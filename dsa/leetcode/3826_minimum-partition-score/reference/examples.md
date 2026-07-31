## Examples

**Example 1**

- Input: `nums = [5,1,2,1], k = 2`
- Output: `25`
- Explanation: One optimal two-part partition is `[5]` and `[1, 2, 1]`. Their sums are `5` and `1 + 2 + 1 = 4`, so their values are `5 * 6 / 2 = 15` and `4 * 5 / 2 = 10`. The resulting score is `15 + 10 = 25`, and no valid partition has a smaller score.

**Example 2**

- Input: `nums = [1,2,3,4], k = 1`
- Output: `55`
- Explanation: Exactly one subarray is required, so the only partition is `[1, 2, 3, 4]`. Its sum is `1 + 2 + 3 + 4 = 10`, giving the value `10 * 11 / 2 = 55`. Thus the minimum score is `55`.

**Example 3**

- Input: `nums = [1,1,1], k = 3`
- Output: `3`
- Explanation: Requiring three subarrays leaves only `[1]`, `[1]`, and `[1]`. Every subarray has sum `1` and value `1 * 2 / 2 = 1`, so the score is `1 + 1 + 1 = 3`, the minimum possible.
