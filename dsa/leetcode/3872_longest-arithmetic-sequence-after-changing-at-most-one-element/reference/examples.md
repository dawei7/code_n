## Examples

**Example 1**

- Input: `nums = [9,7,5,10,1]`
- Output: `5`

- **Explanation:** Replace `nums[3]`, whose old value is `10`, with `3`. The array becomes `[9, 7, 5, 3, 1]`. Selecting the complete array gives consecutive differences of `-2`, so all five elements form one arithmetic subarray.

**Example 2**

- Input: `nums = [1,2,6,7]`
- Output: `3`

- **Explanation:** Replace `nums[0]`, whose old value is `1`, with `-2`, producing `[-2, 2, 6, 7]`. The prefix `[-2, 2, 6]` has common difference `4`, so a length-three arithmetic subarray is attainable.
