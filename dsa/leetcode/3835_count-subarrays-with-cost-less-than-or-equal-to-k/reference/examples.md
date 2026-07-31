## Examples

**Example 1**

- Input: `nums = [1,3,2], k = 4`
- Output: `5`
- Explanation: The six subarrays, in source order, have these costs:
  - `nums[0..0]`: `(1 - 1) * 1 = 0`
  - `nums[0..1]`: `(3 - 1) * 2 = 4`
  - `nums[0..2]`: `(3 - 1) * 3 = 6`
  - `nums[1..1]`: `(3 - 3) * 1 = 0`
  - `nums[1..2]`: `(3 - 2) * 2 = 2`
  - `nums[2..2]`: `(2 - 2) * 1 = 0`

  Exactly five of these costs are at most `4`.

**Example 2**

- Input: `nums = [5,5,5,5], k = 0`
- Output: `10`
- Explanation: Every subarray has the same maximum and minimum, so every cost is `0` and satisfies the threshold. A length-four array has `(4 * 5) / 2 = 10` subarrays, so all ten qualify.

**Example 3**

- Input: `nums = [1,2,3], k = 0`
- Output: `3`
- Explanation: A multi-element subarray has different minimum and maximum values and therefore positive cost. Only the three single-element subarrays have cost `0`.
