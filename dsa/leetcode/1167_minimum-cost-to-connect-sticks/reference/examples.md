## Examples

**Example 1**

- Input: `sticks = [2,4,3]`
- Output: `14`
- Explanation: Begin with `[2,4,3]`. Connect `2` and `3` for cost `5`, leaving `[5,4]`. Then connect `5` and `4` for cost `9`, leaving `[9]`. The total cost is `5 + 9 = 14`.

**Example 2**

- Input: `sticks = [1,8,3,5]`
- Output: `30`
- Explanation: Begin with `[1,8,3,5]`. Connect `1` and `3` for cost `4`, leaving `[4,8,5]`; connect `4` and `5` for cost `9`, leaving `[9,8]`; then connect `9` and `8` for cost `17`, leaving `[17]`. The total is `4 + 9 + 17 = 30`.

**Example 3**

- Input: `sticks = [5]`
- Output: `0`
- Explanation: One stick is already the required final state, so no connection is necessary and the total cost is `0`.
