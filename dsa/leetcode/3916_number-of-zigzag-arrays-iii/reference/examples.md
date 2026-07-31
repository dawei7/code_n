## Examples

**Example 1**

- Input: `n = 3, l = 4, r = 5`
- Output: `2`
- **Explanation:** The interval supplies only `4` and `5`. The two valid arrays are `[4, 5, 4]` and `[5, 4, 5]`; each changes direction after its first comparison.

**Example 2**

- Input: `n = 3, l = 1, r = 3`
- Output: `10`
- **Explanation:** The valid arrays are `[1, 2, 1]`, `[1, 3, 1]`, `[1, 3, 2]`, `[2, 1, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[2, 3, 2]`, `[3, 1, 2]`, `[3, 1, 3]`, and `[3, 2, 3]`. Each has unequal neighbors and makes its second comparison in the direction opposite to its first.
