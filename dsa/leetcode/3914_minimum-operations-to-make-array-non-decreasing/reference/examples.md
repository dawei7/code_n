## Examples

**Example 1**

- Input: `nums = [3,3,2,1]`
- Output: `2`
- **Explanation:** First add `x = 1` to subarray `[2..3]`, producing `[3, 3, 3, 2]`. Then add `x = 1` to `[3..3]`, producing `[3, 3, 3, 3]`. The final array is non-decreasing and the chosen values sum to `1 + 1 = 2`, which is optimal.

**Example 2**

- Input: `nums = [5,1,2,3]`
- Output: `4`
- **Explanation:** Add `x = 4` to subarray `[1..3]`. The array becomes `[5, 5, 6, 7]`, which is non-decreasing, and the total cost is `4`.
