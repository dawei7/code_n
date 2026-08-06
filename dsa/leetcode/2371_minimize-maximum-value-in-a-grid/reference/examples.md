## Examples

**Example 1**

- **Input:** `grid = [[3, 1], [2, 5]]`
- **Output:** `[[2, 1], [1, 2]]`
- **Explanation:**
  - Row 0: `3 > 1` -> output `2 > 1`.
  - Row 1: `2 < 5` -> output `1 < 2`.
  - Col 0: `3 > 2` -> output `2 > 1`.
  - Col 1: `1 < 5` -> output `1 < 2`.
  - Maximum value in result matrix is 2, which is optimal.

**Example 2**

- **Input:** `grid = [[10]]`
- **Output:** `[[1]]`
- **Explanation:** Single element matrix; 1 is the minimum positive integer.
