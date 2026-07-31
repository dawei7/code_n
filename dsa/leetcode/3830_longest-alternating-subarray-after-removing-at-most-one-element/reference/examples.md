## Examples

**Example 1**

- Input: `nums = [2,1,3,2]`
- Output: `4`
- Explanation:
  - Do not remove any element.
  - Select the entire array `[2,1,3,2]`. It is alternating because `2 > 1 < 3 > 2`.

**Example 2**

- Input: `nums = [3,2,1,2,3,2,1]`
- Output: `4`
- Explanation:
  - Remove `nums[3]`, the fourth value `2`. The array becomes `[3,2,1,3,2,1]`.
  - Select its middle subarray `[2,1,3,2]`, which has length `4`.

**Example 3**

- Input: `nums = [100000,100000]`
- Output: `1`
- Explanation:
  - Do not remove either element.
  - Select one value—for example, the second `100000`. Equal adjacent values cannot belong to a longer alternating subarray.
