## Examples

**Example 1**

- Input: `intervals = [[1,2]]`
- Output: `[-1]`
- Explanation: The collection has only one interval, and no start reaches its end, so the result is `-1`.

**Example 2**

- Input: `intervals = [[3,4],[2,3],[1,2]]`
- Output: `[-1,0,1]`
- Explanation:
  1. `[3,4]` has no right interval.
  2. For `[2,3]`, index `0` has start $3$, the smallest start at least its end $3$.
  3. For `[1,2]`, index `1` has start $2$, the smallest start at least its end $2$.

**Example 3**

- Input: `intervals = [[1,4],[2,3],[3,4]]`
- Output: `[-1,2,-1]`
- Explanation:
  1. Neither `[1,4]` nor `[3,4]` has a right interval.
  2. For `[2,3]`, index `2` has start $3$, the smallest start at least its end $3$.
