## Examples

**Example 1**

- Input: `operations = ["MovingAverage","next","next","next","next"], arguments = [[3],[1],[10],[3],[5]]`
- Output: `[null,1.0,5.5,4.66667,6.0]`
- Explanation:
  - Construct `MovingAverage(3)`.
  - `next(1)` returns `1.0 = 1 / 1`.
  - `next(10)` returns `5.5 = (1 + 10) / 2`.
  - `next(3)` returns approximately `4.66667 = (1 + 10 + 3) / 3`.
  - `next(5)` drops the oldest value and returns `6.0 = (10 + 3 + 5) / 3`.
