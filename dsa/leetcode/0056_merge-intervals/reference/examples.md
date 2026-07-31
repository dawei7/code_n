## Examples

**Example 1**

- Input: `intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]`
- Output: `[[1, 6], [8, 10], [15, 18]]`
- Explanation: Intervals `[1, 3]` and `[2, 6]` overlap, so together they become `[1, 6]`.

**Example 2**

- Input: `intervals = [[1, 4], [4, 5]]`
- Output: `[[1, 5]]`
- Explanation: Because the intervals meet at endpoint `4`, `[1, 4]` and `[4, 5]` are overlapping closed intervals.

**Example 3**

- Input: `intervals = [[4, 7], [1, 4]]`
- Output: `[[1, 7]]`
- Explanation: Intervals `[1, 4]` and `[4, 7]` share endpoint `4` and therefore merge.
