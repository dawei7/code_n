## Examples

**Example 1**

- Input: `n = 2, s = 9`
- Output: `90`
- **Explanation:** Among integers with at most two digits whose digits total nine, `90` is the largest.

**Example 2**

- Input: `n = 2, s = 19`
- Output: `-1`
- **Explanation:** Two decimal digits can contribute at most $9+9=18$, so no integer with at most two digits can have digit sum 19.

**Example 3**

- Input: `n = 5, s = 0`
- Output: `0`
- **Explanation:** Every decimal digit is non-negative, so all digits must be zero when their sum is zero. The only non-negative integer represented by those digits is `0`.
