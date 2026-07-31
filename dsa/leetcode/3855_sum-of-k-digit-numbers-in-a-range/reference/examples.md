## Examples

**Example 1**

- Input: `l = 1, r = 2, k = 2`
- Output: `66`
- Explanation:
  - Choosing two digits from `[1, 2]` produces `11, 12, 21, 22`.
  - Their sum is `11 + 12 + 21 + 22 = 66`.

**Example 2**

- Input: `l = 0, r = 1, k = 3`
- Output: `444`
- Explanation:
  - The eight three-digit sequences are `000, 001, 010, 011, 100, 101, 110, 111`.
  - Without displaying leading zeros, their integer values are `0, 1, 10, 11, 100, 101, 110, 111`.
  - These values sum to `444`.

**Example 3**

- Input: `l = 5, r = 5, k = 10`
- Output: `555555520`
- Explanation:
  - Only the ten-digit sequence `5555555555` can be formed from `[5, 5]`.
  - Reducing its value gives `5555555555 % (10^9 + 7) = 555555520`.
