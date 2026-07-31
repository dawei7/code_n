## Examples

**Example 1**

- Input: `n = 25`
- Output: `27`
- Explanation:
  - Reversing the digits gives `reverse(25) = 52`.
  - Therefore, the mirror distance is $\lvert 25 - 52\rvert = 27$.

**Example 2**

- Input: `n = 10`
- Output: `9`
- Explanation:
  - Reversal gives the digit sequence `01`, which represents the integer `1`.
  - Therefore, the mirror distance is $\lvert 10 - 1\rvert = 9$.

**Example 3**

- Input: `n = 7`
- Output: `0`
- Explanation:
  - A one-digit number is unchanged, so `reverse(7) = 7`.
  - Therefore, the mirror distance is $\lvert 7 - 7\rvert = 0$.
