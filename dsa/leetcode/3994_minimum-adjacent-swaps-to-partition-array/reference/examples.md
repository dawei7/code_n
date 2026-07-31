## Examples

**Example 1**

- Input: `nums = [1,3,2,4,5,6], a = 3, b = 4`
- Output: `1`
- **Explanation:** Swap neighboring values `nums[1]` and `nums[2]` to obtain `[1,2,3,4,5,6]`. This array is good with parts `[1,2]`, `[3,4]`, and `[5,6]`.

**Example 2**

- Input: `nums = [9,7,5,3], a = 4, b = 8`
- Output: `5`
- **Explanation:** One optimal sequence uses these five adjacent swaps:
  1. Swap `nums[2]` with `nums[3]`, producing `[9,7,3,5]`.
  2. Swap `nums[1]` with `nums[2]`, producing `[9,3,7,5]`.
  3. Swap `nums[0]` with `nums[1]`, producing `[3,9,7,5]`.
  4. Swap `nums[1]` with `nums[2]`, producing `[3,7,9,5]`.
  5. Swap `nums[2]` with `nums[3]`, producing `[3,7,5,9]`.

  The result is good with parts `[3]`, `[7,5]`, and `[9]`.

**Example 3**

- Input: `nums = [3,7,5,9], a = 4, b = 8`
- Output: `0`
- **Explanation:** The array is already good, so no swaps are necessary.
