## Examples

**Example 1**

- **Input:** `books = [8, 5, 2, 7, 9]`
- **Output:** `19`
- **Explanation:** Select contiguous section from shelf 1 to 4 ($l=1, r=4$), taking `[1, 2, 7, 9]` books respectively ($1 < 2 < 7 < 9$, and $1 \le 5, 2 \le 2, 7 \le 7, 9 \le 9$). Total books $= 1 + 2 + 7 + 9 = 19$.

**Example 2**

- **Input:** `books = [7, 0, 3, 4, 5]`
- **Output:** `12`
- **Explanation:** Select shelves 2 to 4 ($l=2, r=4$), taking `[3, 4, 5]` books. Total $= 3 + 4 + 5 = 12$.

**Example 3**

- **Input:** `books = [8, 2, 3, 7, 3, 4, 0, 1, 4, 3]`
- **Output:** `13`
- **Explanation:** Select shelves 0 to 3 ($l=0, r=3$), taking `[1, 2, 3, 7]` books. Total $= 1 + 2 + 3 + 7 = 13$.
