## Examples

**Example 1**

- Input: `nums = [5,1,2,1], k = 2`
- Output: `25`
- Explanation: The partition `[5]` and `[1, 2, 1]` has subarray sums `5` and `4`. Their values are `5 * 6 / 2 = 15` and `4 * 5 / 2 = 10`, respectively, for a total score of `15 + 10 = 25`. No other valid two-part partition has a smaller score.

**Example 2**

- Input: `nums = [1,2,3,4], k = 1`
- Output: `55`
- Explanation: Exactly one subarray is required, so every element belongs to `[1, 2, 3, 4]`. Its sum is `1 + 2 + 3 + 4 = 10`, giving the value `10 * 11 / 2 = 55`; this is therefore the only possible score.

**Example 3**

- Input: `nums = [1,1,1], k = 3`
- Output: `3`
- Explanation: The only valid three-part partition is `[1]`, `[1]`, `[1]`. Every subarray has sum `1` and value `1 * 2 / 2 = 1`, so the partition score is `1 + 1 + 1 = 3`.
