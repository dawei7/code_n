## Examples

**Example 1**

- Input: `capacity = [1,5,3,7], itemSize = 3`
- Output: `2`
- Explanation: The box at index `2` has capacity `3`, the minimum capacity
  capable of storing the item. Therefore the answer is `2`.

**Example 2**

- Input: `capacity = [3,5,4,3], itemSize = 2`
- Output: `0`
- Explanation: The minimum eligible capacity is `3`, appearing at indices `0`
  and `3`. The smaller index is `0`, so that is the result.

**Example 3**

- Input: `capacity = [4], itemSize = 5`
- Output: `-1`
- Explanation: The only box is too small for the item, so no eligible index
  exists and the answer is `-1`.
