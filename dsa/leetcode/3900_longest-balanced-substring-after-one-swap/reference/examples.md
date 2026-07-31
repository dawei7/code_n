## Examples

**Example 1**

- Input: `s = "100001"`
- Output: `4`
- Explanation:
  - Exchange the third character, which is `'0'`, with the final character, which is `'1'`. The complete string becomes `"101000"`.
  - Select its leading substring `"1010"`. That substring contains two zeros and two ones, so it is balanced and has length $4$.

**Example 2**

- Input: `s = "111"`
- Output: `0`
- Explanation:
  - Use no swap.
  - The empty substring contains zero zeros and zero ones, so it is balanced. No non-empty substring can be balanced because the complete string contains no zero.
