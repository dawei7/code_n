## Examples

**Example 1**

- Input: `capacity = [9,3,3,3,9]`
- Output: `2`
- Explanation:

  - `[9,3,3,3,9]` is stable: both boundary values are `9`, and the interior sum is `3 + 3 + 3 = 9`.
  - `[3,3,3]` is also stable: both boundary values and its single interior value are `3`.

**Example 2**

- Input: `capacity = [1,2,3,4,5]`
- Output: `0`
- Explanation: No subarray of length at least 3 has equal first and last elements, so no stable subarray exists.

**Example 3**

- Input: `capacity = [-4,4,0,0,-8,-4]`
- Output: `1`
- Explanation: The complete subarray `[-4,4,0,0,-8,-4]` is stable. Its two boundary values are `-4`, and the values strictly inside it sum to `4 + 0 + 0 + (-8) = -4`.
