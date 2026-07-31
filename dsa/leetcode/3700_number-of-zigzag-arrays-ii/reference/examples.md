## Examples

**Example 1**

- Input: `n = 3, l = 4, r = 5`
- Output: `2`
- Explanation: Using only the values in `[4, 5]`, exactly these two length-three arrays satisfy every ZigZag condition:

  - `[4, 5, 4]`
  - `[5, 4, 5]`

**Example 2**

- Input: `n = 3, l = 1, r = 3`
- Output: `10`
- Explanation: There are ten valid length-three arrays over `[1, 3]`:

  - `[1, 2, 1]`, `[1, 3, 1]`, `[1, 3, 2]`
  - `[2, 1, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[2, 3, 2]`
  - `[3, 1, 2]`, `[3, 1, 3]`, `[3, 2, 3]`

  Every array in the list meets the ZigZag conditions.
