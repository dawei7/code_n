## Examples

**Example 1**

- Input: `costs = [4,8,5,3], capacity = [1,5,2,7], budget = 8`
- Output: `8`
- Explanation:
  - Choose machines `0` and `3`, whose costs are `costs[0] = 4` and `costs[3] = 3`.
  - Their total cost is `4 + 3 = 7`, which is strictly less than `budget = 8`.
  - Their total capacity is `capacity[0] + capacity[3] = 1 + 7 = 8`, the maximum possible value.

**Example 2**

- Input: `costs = [3,5,7,4], capacity = [2,4,3,6], budget = 7`
- Output: `6`
- Explanation:
  - Choose only machine `3`, which has `costs[3] = 4`.
  - Its total cost is `4`, strictly less than `budget = 7`.
  - The maximum total capacity is therefore `capacity[3] = 6`.

**Example 3**

- Input: `costs = [2,2,2], capacity = [3,5,4], budget = 5`
- Output: `9`
- Explanation:
  - Choose machines `1` and `2`, both of which cost `2`.
  - Their total cost is `2 + 2 = 4`, which is strictly less than `budget = 5`.
  - Their total capacity is `capacity[1] + capacity[2] = 5 + 4 = 9`, the maximum achievable total.
