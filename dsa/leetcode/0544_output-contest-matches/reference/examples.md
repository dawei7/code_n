## Examples

**Example 1**

- Input: `n = 4`
- Output: `"((1,4),(2,3))"`
- **Explanation:** The first round pairs teams `1` and `4`, then teams `2` and `3`, producing `(1,4)` and `(2,3)`.
  Their winners meet in the final, so one enclosing pair yields `((1,4),(2,3))`.

**Example 2**

- Input: `n = 8`
- Output: `"(((1,8),(4,5)),((2,7),(3,6)))"`
- **Explanation:** The rounds are:

  1. `(1,8)`, `(2,7)`, `(3,6)`, `(4,5)`
  2. `((1,8),(4,5))`, `((2,7),(3,6))`
  3. `(((1,8),(4,5)),((2,7),(3,6)))`

  The third round produces the final winner, so its complete pairing is the returned string.
