## Examples

**Example 1**

- Input: `s = "1112"`
- Output: `"1112"`
- Explanation:
  - The original string already ends in `2` and therefore represents an even number.
  - Keeping all four digits gives the largest possible result, so no deletion is needed.

**Example 2**

- Input: `s = "221"`
- Output: `"22"`
- Explanation:
  - Deleting the final `'1'` leaves `"22"`.
  - This is the largest even integer obtainable without changing the remaining order.

**Example 3**

- Input: `s = "1"`
- Output: `""`
- Explanation:
  - The only available nonempty subsequence represents an odd number.
  - No even result can be formed, so the return value is empty.
