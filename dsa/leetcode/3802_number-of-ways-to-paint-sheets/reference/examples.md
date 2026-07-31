## Examples

**Example 1**

- Input: `n = 4, limit = [3,1,2]`
- Output: `6`
- Explanation:
  - For an ordered color pair `(i, j)`, color `i` covers the first `x` sheets and color `j` covers the final `4 - x` sheets. A split is valid when `1 <= x <= limit[i]` and `1 <= 4 - x <= limit[j]`.
  - The valid ordered pairs and split positions are:
    - `(0, 1)`: `x = 3`
    - `(0, 2)`: `x = 2, 3`
    - `(1, 0)`: `x = 1`
    - `(2, 0)`: `x = 1, 2`
  - These choices give `1 + 2 + 1 + 2 = 6` paintings.

**Example 2**

- Input: `n = 3, limit = [1,2]`
- Output: `2`
- Explanation:
  - For ordered pair `(i, j)`, a split `x` is valid when `1 <= x <= limit[i]` and `1 <= 3 - x <= limit[j]`.
  - The valid choices are `(0, 1)` with `x = 1` and `(1, 0)` with `x = 2`.
  - Therefore there are `2` valid paintings.

**Example 3**

- Input: `n = 3, limit = [2,2]`
- Output: `4`
- Explanation:
  - The same split conditions apply to each ordered pair of different colors.
  - Pair `(0, 1)` permits `x = 1, 2`, and pair `(1, 0)` also permits `x = 1, 2`.
  - Therefore there are `4` valid paintings.
