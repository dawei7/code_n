## Examples

**Example 1**

- Input: `nums = [1,4,3,5], colors = [1,1,2,2]`
- Output: `9`
- Explanation:
  - Choose house `i = 1`, which contributes `nums[1] = 4`, and house `i = 3`, which contributes `nums[3] = 5`. These houses are non-adjacent.
  - The resulting total is `4 + 5 = 9`.

**Example 2**

- Input: `nums = [3,1,2,4], colors = [2,3,2,2]`
- Output: `8`
- Explanation:
  - Choose houses `i = 0`, `i = 1`, and `i = 3`, worth `3`, `1`, and `4` respectively.
  - Houses `i = 0` and `i = 1` are an allowed adjacent pair because their colors differ. House `i = 3` is non-adjacent to the previously chosen house `i = 1`.
  - Their total is `3 + 1 + 4 = 8`.

**Example 3**

- Input: `nums = [10,1,3,9], colors = [1,1,1,2]`
- Output: `22`
- Explanation:
  - Choose houses `i = 0`, `i = 2`, and `i = 3`, whose values are `10`, `3`, and `9`.
  - Houses `i = 0` and `i = 2` are non-adjacent. Houses `i = 2` and `i = 3` are adjacent but have different colors, so that pair is also valid.
  - The maximum total is `10 + 3 + 9 = 22`.
