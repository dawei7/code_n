## Examples

**Example 1**

- Input: `nums = [1,2,1,1,3]`
- Output: `6`
- Explanation:

  The good tuple `(0,2,3)` attains the minimum distance.

  It is good because `nums[0] == nums[2] == nums[3] == 1`. Its distance is `abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6`.

**Example 2**

- Input: `nums = [1,1,2,3,2,1,2]`
- Output: `8`
- Explanation:

  The good tuple `(2,4,6)` attains the minimum distance.

  It is good because `nums[2] == nums[4] == nums[6] == 2`. Its distance is `abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8`.

**Example 3**

- Input: `nums = [1]`
- Output: `-1`
- Explanation: No good tuple exists, so the answer is `-1`.
