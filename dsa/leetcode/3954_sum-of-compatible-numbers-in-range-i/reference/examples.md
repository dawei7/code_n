## Examples

**Example 1**

- Input: `n = 2, k = 3`
- Output: `10`
- Explanation:
  - The compatible values are `1`, `4`, and `5`.
  - Their distances from `2` are `1`, `2`, and `3`, respectively, and each has bitwise AND zero with `2`.
  - Their sum is `1 + 4 + 5 = 10`.

**Example 2**

- Input: `n = 5, k = 1`
- Output: `0`
- Explanation:
  - The distance condition restricts `x` to the interval `[4, 6]`.
  - None of those integers has bitwise AND zero with `5`, so there are no compatible values to add.
