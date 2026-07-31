## Examples

**Example 1**

- Input: `nums = [1,2,3]`
- Output: `[1,2,3,3,2,1]`
- Explanation: The first three result positions copy `nums`, and the final three positions read it from right to left.

The first half is `[1, 2, 3]`. For the reversed half:

- `ans[3] = nums[2] = 3`
- `ans[4] = nums[1] = 2`
- `ans[5] = nums[0] = 1`

Combining the two halves gives `[1, 2, 3, 3, 2, 1]`.

**Example 2**

- Input: `nums = [1]`
- Output: `[1,1]`
- Explanation: Reversing a one-element array leaves its order unchanged, so the value appears once in each half of the result.
