## Examples

**Example 1**

- **Input:** `peaks = [[2, 2], [6, 3], [5, 4]]`
- **Output:** `2`
- **Explanation:**
  - Peak `(2, 2)` interval: `[0, 4]`.
  - Peak `(6, 3)` interval: `[3, 9]`.
  - Peak `(5, 4)` interval: `[1, 9]`.
  - Peak `(6, 3)` lies on the border of mountain `(5, 4)` because its interval `[3, 9]` is contained within `[1, 9]`.
  - Peaks `(2, 2)` and `(5, 4)` are not contained by any other mountain, so 2 mountains are visible.

**Example 2**

- **Input:** `peaks = [[1, 3], [1, 3]]`
- **Output:** `0`
- **Explanation:** The two mountains completely overlap. Each peak lies on the border of the other, making both invisible.
