## Examples

**Example 1**

- Input: `n = 10, restrictions = [[3,1],[8,1]], diff = [2,2,3,1,4,5,1,1,2]`
- Output: `6`
- Explanation:
  - One valid construction is `a = [0, 2, 4, 1, 2, 6, 2, 1, 1, 3]`.
  - It obeys both explicit bounds, `a[3] <= 1` and `a[8] <= 1`, as well as every neighboring `diff` limit.
  - Its largest value is `6`, which is optimal.

**Example 2**

- Input: `n = 8, restrictions = [[3,2]], diff = [3,5,2,4,2,3,1]`
- Output: `12`
- Explanation:
  - The sequence `a = [0, 3, 3, 2, 6, 8, 11, 12]` is valid and satisfies `a[3] <= 2`.
  - The maximum value in this construction is `12`, and no valid sequence can attain a larger one.
