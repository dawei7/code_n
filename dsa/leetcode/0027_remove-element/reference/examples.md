## Examples

**Example 1**

- Input: `nums = [3, 2, 2, 3], val = 3`
- Output: `2, nums = [2, 2, _, _]`
- Explanation: Return $k=2$ with two copies of `2` in the retained prefix. The underscored positions are ignored.

**Example 2**

- Input: `nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2`
- Output: `5, nums = [0, 1, 4, 0, 3, _, _, _]`
- Explanation: Return $k=5$. The first five positions must contain `0`, `0`, `1`, `3`, and `4` in any order; values after that prefix do not matter.
