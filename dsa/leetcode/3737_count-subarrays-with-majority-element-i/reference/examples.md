## Examples

**Example 1**

- Input: `nums = [1,2,2,3], target = 2`
- Output: `5`
- Explanation:

  The subarrays in which `target = 2` is the majority element are:

  - `nums[1..1] = [2]`
  - `nums[2..2] = [2]`
  - `nums[1..2] = [2,2]`
  - `nums[0..2] = [1,2,2]`
  - `nums[1..3] = [2,2,3]`

  Therefore, exactly `5` subarrays qualify.

**Example 2**

- Input: `nums = [1,1,1,1], target = 1`
- Output: `10`
- Explanation: All `10` subarrays have `1` as their majority element.

**Example 3**

- Input: `nums = [1,2,3], target = 4`
- Output: `0`
- Explanation: The value `target = 4` does not occur anywhere in `nums`, so it cannot be the majority element of any subarray. The answer is therefore `0`.
