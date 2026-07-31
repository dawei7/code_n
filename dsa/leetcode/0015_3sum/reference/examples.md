## Examples

**Example 1**

- Input: `nums = [-1, 0, 1, 2, -1, -4]`
- Output: `[[-1, -1, 2], [-1, 0, 1]]`
- Explanation: Several index combinations sum to zero:

  - `nums[0] + nums[1] + nums[2] = -1 + 0 + 1 = 0`.
  - `nums[1] + nums[2] + nums[4] = 0 + 1 - 1 = 0`.
  - `nums[0] + nums[3] + nums[4] = -1 + 2 - 1 = 0`.

  These combinations produce only two distinct value triplets: `[-1, 0, 1]` and `[-1, -1, 2]`. Either the triplets or their elements may appear in a different order.

**Example 2**

- Input: `nums = [0, 1, 1]`
- Output: `[]`
- Explanation: The only possible triplet does not sum to zero.

**Example 3**

- Input: `nums = [0, 0, 0]`
- Output: `[[0, 0, 0]]`
- Explanation: The only possible triplet sums to zero.
