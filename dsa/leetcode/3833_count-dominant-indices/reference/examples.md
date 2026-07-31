## Examples

**Example 1**

- Input: `nums = [5,4,3]`
- Output: `2`
- Explanation: At index `0`, the value `5` is greater than the average of `[4,3]`, since $(4+3)/2=3.5$. At index `1`, the value `4` is greater than the sole value `3` to its right. Index `2` has an empty right suffix and therefore is not dominant. Exactly two indices qualify.

**Example 2**

- Input: `nums = [4,1,2]`
- Output: `1`
- Explanation: The value `4` at index `0` is greater than the average of `[1,2]`. The value `1` at index `1` is not greater than the following value `2`, and index `2` has no element to its right. Thus only one index is dominant.

