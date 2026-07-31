## Examples

**Example 1**

- Input: `nums = [3,6,2]`
- Output: `7`
- Explanation: The value `6` is divisible by the existing value `2`, so replace the middle element and obtain `[3,2,2]`. No remaining replacement can lower the sum below `3 + 2 + 2 = 7`.

**Example 2**

- Input: `nums = [4,2,8,3]`
- Output: `9`
- Explanation: Use the element equal to `2` as the donor for both divisible values. Replacing `4` and `8` produces `[2,2,2,3]`, whose sum is `9`; no further valid operation reduces it.

**Example 3**

- Input: `nums = [7,5,9]`
- Output: `21`
- Explanation: No value at one position divides the value at another position. The array therefore cannot be reduced, and its original sum is `21`.
