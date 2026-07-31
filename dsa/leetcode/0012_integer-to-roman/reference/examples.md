## Examples

**Example 1**

- Input: `num = 3749`
- Output: `"MMMDCCXLIX"`
- Explanation: Convert each decimal place independently from largest to smallest:

  - `3000 = MMM`, using `M + M + M`.
  - `700 = DCC`, using `D + C + C`.
  - `40 = XL`, placing `X` before `L` to subtract 10 from 50.
  - `9 = IX`, placing `I` before `X` to subtract 1 from 10.

  The value 49 is decomposed by decimal places as 40 and 9; it is not written by subtracting `I` directly from `L`.

**Example 2**

- Input: `num = 58`
- Output: `"LVIII"`
- Explanation: `50 = L` and `8 = VIII`, giving `LVIII`.

**Example 3**

- Input: `num = 1994`
- Output: `"MCMXCIV"`
- Explanation: The place-value conversions are `1000 = M`, `900 = CM`, `90 = XC`, and `4 = IV`.
