## Examples

**Example 1**

- Input: `nums = [1,3], n = 6`
- Output: `1`
- Explanation: Before any patch, the selections `[1]`, `[3]`, and `[1,3]` produce sums `1`, `3`, and `4`. Adding `2` makes `[1]`, `[2]`, `[3]`, `[1,3]`, `[2,3]`, and `[1,2,3]` available, with sums covering every value from `1` through `6`. Thus one patch is sufficient.

**Example 2**

- Input: `nums = [1,5,10], n = 20`
- Output: `2`
- Explanation: Adding `2` and `4` supplies the required coverage with two patches.

**Example 3**

- Input: `nums = [1,2,2], n = 5`
- Output: `0`
