## Examples

**Example 1**

- Input: `n = 3`
- Output: `127`
- Explanation:
  - Block 1 is `1`.
  - Block 2 is `2 * 3 = 6`.
  - Block 3 is `4 * 5 * 6 = 120`.
  - Thus, `F(3) = 1 + 6 + 120 = 127`.

**Example 2**

- Input: `n = 7`
- Output: `6997165`
- Explanation:
  - Block 1 is `1`.
  - Block 2 is `2 * 3 = 6`.
  - Block 3 is `4 * 5 * 6 = 120`.
  - Block 4 is `7 * 8 * 9 * 10 = 5040`.
  - Block 5 is `11 * 12 * 13 * 14 * 15 = 360360`.
  - Block 6 is `16 * 17 * 18 * 19 * 20 * 21 = 39070080`.
  - Block 7 is `22 * 23 * 24 * 25 * 26 * 27 * 28 = 5967561600`.
  - The unreduced sum is `F(7) = 6006997207`, so `6006997207 % 1000000007 = 6997165`.
