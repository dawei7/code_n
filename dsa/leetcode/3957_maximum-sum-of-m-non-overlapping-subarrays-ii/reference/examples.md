## Examples

**Example 1**

- Input: `nums = [4,1,-5,2], m = 2, l = 1, r = 3`
- Output: `7`
- Explanation:
  - Select `[4, 1]`, whose sum is `4 + 1 = 5`, and the separate subarray `[2]`, whose sum is `2`.
  - Both lengths lie in `[1, 3]`, and the total `5 + 2 = 7` is the best attainable with at most two subarrays.

**Example 2**

- Input: `nums = [1,0,3,4], m = 2, l = 1, r = 2`
- Output: `8`
- Explanation:
  - Choose `[1]` for a sum of `1` and `[3, 4]` for a sum of `3 + 4 = 7`.
  - Both subarrays have permitted lengths, and their maximum total is `1 + 7 = 8`.

**Example 3**

- Input: `nums = [-1,7,-4], m = 1, l = 2, r = 3`
- Output: `6`
- Explanation:
  - The subarray `[-1, 7]` has an allowed length and sum `-1 + 7 = 6`.
  - No other choice of at most one permitted subarray produces a larger total.

**Example 4**

- Input: `nums = [-3,-4,-1], m = 2, l = 1, r = 2`
- Output: `-1`
- Explanation:
  - Every legal subarray has a negative sum, but at least one must be selected.
  - Choosing the one-element subarray `[-1]` loses the least, so `-1` is optimal even though up to two subarrays are allowed.
