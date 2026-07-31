## Examples

**Example 1**

- Input: `nums = [-5,-2,3], queries = [[0,2],[2,0],[1,2]]`
- Output: `[6,2,5]`
- **Explanation:** The closest indices are `[1, 0, 1]`. For `[0, 2]`, moving `0 -> 1` uses the discounted closest move for `1`, then `1 -> 2` costs `|-2 - 3| = 5`, totaling `6`. For `[2, 0]`, both moves along `2 -> 1 -> 0` are closest moves, so the total is `2`. For `[1, 2]`, the optimal direct move costs `|-2 - 3| = 5`. Therefore the three answers are `[6, 2, 5]`.

**Example 2**

- Input: `nums = [0,2,3,9], queries = [[3,0],[1,2],[2,0]]`
- Output: `[4,1,3]`
- **Explanation:** The closest indices are `[1, 2, 1, 2]`. For `[3, 0]`, the moves `3 -> 2` and `2 -> 1` each cost `1`, while `1 -> 0` costs `|2 - 0| = 2`, for a total of `4`. Query `[1, 2]` is one closest move and costs `1`. For `[2, 0]`, the closest move `2 -> 1` costs `1` and the move `1 -> 0` costs `2`, totaling `3`. Thus the result is `[4, 1, 3]`.
