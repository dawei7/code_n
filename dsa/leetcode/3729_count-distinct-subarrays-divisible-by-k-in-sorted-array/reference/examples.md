## Examples

**Example 1**

- Input: `nums = [1,2,3], k = 3`
- Output: `3`
- Explanation: The good subarrays are `[1,2]`, `[3]`, and `[1,2,3]`. For instance, the last sequence sums to `1 + 2 + 3 = 6`, and `6 % k = 6 % 3 = 0`.

**Example 2**

- Input: `nums = [2,2,2,2,2,2], k = 6`
- Output: `2`
- Explanation: The good subarrays are `[2,2,2]` and `[2,2,2,2,2,2]`. The first sequence sums to `2 + 2 + 2 = 6`, and `6 % k = 6 % 6 = 0`. Although `[2,2,2]` occurs at several positions, its identical value sequence is counted only once.
