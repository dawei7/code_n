## Examples

**Example 1**

- Input: `nums = [1,2,3,4,5]`
- Output: `true`
- Explanation: Every choice of indices satisfying $i<j<k$ also has increasing values in this array.

**Example 2**

- Input: `nums = [5,4,3,2,1]`
- Output: `false`
- Explanation: There is no increasing triplet.

**Example 3**

- Input: `nums = [2,1,5,0,4,6]`
- Output: `true`
- Explanation: Indices `(1,4,5)` are one valid choice because `nums[1] == 1 < nums[4] == 4 < nums[5] == 6`.
