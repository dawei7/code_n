## Examples

**Example 1**

- Input: `nums = [1,2,3]`
- Output: `0`
- Explanation:
  - Game 0 has an odd point value, so the second player becomes active and receives `nums[0] = 1` point.
  - Game 1 causes no swap, and the second player receives `nums[1] = 2` points.
  - Game 2 has an odd point value, so the first player becomes active and receives `nums[2] = 3` points.
  - The score difference is `3 - 3 = 0`.

**Example 2**

- Input: `nums = [2,4,2,1,2,1]`
- Output: `4`
- Explanation:
  - Across games 0 through 2, the first player receives `2 + 4 + 2 = 8` points.
  - Game 3 has an odd point value, so the second player becomes active and receives `nums[3] = 1` point.
  - The second player also receives `nums[4] = 2` points in game 4.
  - In game 5, the odd value causes one swap and the sixth-game rule causes another. The two swaps cancel, so the second player receives `nums[5] = 1` point.
  - The score difference is `8 - 4 = 4`.

**Example 3**

- Input: `nums = [1]`
- Output: `-1`
- Explanation:
  - Game 0 has an odd point value, so the second player becomes active and receives `nums[0] = 1` point.
  - The score difference is `0 - 1 = -1`.
