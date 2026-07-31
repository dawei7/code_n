## Examples

**Example 1**

- Input: `nums = [1, 1, 1, 2, 2, 3]`
- Output: `5, nums = [1, 1, 2, 2, 3, _]`
- Explanation: Return `k = 5`; the first five entries must be `1, 1, 2, 2, 3`. The value after that prefix is irrelevant and is shown as `_`.

**Example 2**

- Input: `nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]`
- Output: `7, nums = [0, 0, 1, 1, 2, 3, 3, _, _]`
- Explanation: Return `k = 7`; the required prefix is `0, 0, 1, 1, 2, 3, 3`. Both remaining positions may hold any values.
