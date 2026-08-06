## Examples

**Example 1**

- Input: `colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]`
- Output: `[3,0,3]`
- Explanation: For query `[1,3]`, the nearest `3` is at position `4`, three steps away. Query `[2,2]` already points to a `2`, so its distance is zero. For `[6,1]`, the nearest `1` is at position `3`, also three steps away.

**Example 2**

- Input: `colors = [1,2], queries = [[0,3]]`
- Output: `[-1]`
- Explanation: The array contains no occurrence of color `3`.
