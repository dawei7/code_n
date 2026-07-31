## Examples

**Example 1**

- Input: `nums = [3,8,3,6,5,8]`
- Output: `1`
- Explanation:
  - Remove the first three values in the first operation. The remaining array is `[6,5,8]`.
  - Those three values are distinct, so processing stops after one operation.

**Example 2**

- Input: `nums = [2,2]`
- Output: `1`
- Explanation:
  - Fewer than three values are present, so one operation removes both of them.
  - The resulting empty array satisfies the stopping condition.

**Example 3**

- Input: `nums = [4,3,5,1,2]`
- Output: `0`
- Explanation:
  - Every value is already distinct, so no removal operation is performed.
