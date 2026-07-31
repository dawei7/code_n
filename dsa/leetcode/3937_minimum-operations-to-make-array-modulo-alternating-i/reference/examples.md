## Examples

**Example 1**

- Input: `nums = [1,4,2,8], k = 3`
- Output: `2`
- Explanation: Choose `x = 1` for the even indices and `y = 2` for the odd indices. Increment the value at index `1` from `4` to `5`, producing `[1,5,2,8]`. Then decrement the value at index `2` from `2` to `1`, producing `[1,5,1,8]`. The even-indexed values now have residue one and the odd-indexed values have residue two, using two operations in total.

**Example 2**

- Input: `nums = [1,1,1], k = 3`
- Output: `1`
- Explanation: Increment the middle value once to obtain `[1,2,1]`. The even indices then use residue `x = 1` and the odd index uses the distinct residue `y = 2`, so one operation is sufficient and minimal.
