## Examples

**Example 1**

- Input: `nums = [5,4,5,6], k = 2`
- Output: `7`
- Explanation:
  - Select the contiguous subarray `[4,5,6]`.
  - Its maximum-minus-minimum difference is `6 - 4 = 2`, which does not exceed `k`.
  - Its value is `4 XOR 5 XOR 6 = 7`.

**Example 2**

- Input: `nums = [5,4,5,6], k = 1`
- Output: `6`
- Explanation:
  - Select the one-element subarray `[6]`.
  - Its maximum and minimum are both `6`, so the difference is `6 - 6 = 0`, which does not exceed `k`.
  - The XOR value of that subarray is `6`.
