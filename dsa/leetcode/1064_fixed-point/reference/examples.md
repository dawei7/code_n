## Examples

**Example 1**

- Input: `arr = [-10,-5,0,3,7]`
- Output: `3`
- Explanation: The values at indices `0`, `1`, `2`, and `3` are respectively `-10`, `-5`, `0`, and `3`. The first equality between a value and its index is `arr[3] == 3`, so the result is `3`.

**Example 2**

- Input: `arr = [0,2,5,8,17]`
- Output: `0`
- Explanation: The first value satisfies `arr[0] == 0`, making index `0` the required result.

**Example 3**

- Input: `arr = [-10,-5,3,4,7,9]`
- Output: `-1`
- Explanation: No index `i` in this array satisfies `arr[i] == i`, so the result is `-1`.
