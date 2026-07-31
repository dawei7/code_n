## Examples

**Example 1**

- Input: `words = ["able","area","echo","also"]`
- Output: `[["able","area","echo","also"],["area","able","also","echo"]]`
- Explanation:
  - Exactly two word squares can be formed.
  - For `["able","area","echo","also"]`, the corner letters agree because `able[0] = area[0] = 'a'`, `able[3] = echo[0] = 'e'`, `also[0] = area[3] = 'a'`, and `also[3] = echo[3] = 'o'`.
  - The transposed arrangement `["area","able","also","echo"]` also satisfies all four corner conditions: its matching letters are `'a'`, `'a'`, `'e'`, and `'o'`, respectively.
  - The two arrays appear in ascending lexicographic order.

**Example 2**

- Input: `words = ["code","cafe","eden","edge"]`
- Output: `[]`
- Explanation:
  - No ordering of four distinct words from the input satisfies all four corner equalities, so there is no word square to return.
