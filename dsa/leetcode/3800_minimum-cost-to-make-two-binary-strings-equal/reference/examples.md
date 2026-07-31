## Examples

**Example 1**

- Input: `s = "01000", t = "10111", flipCost = 10, swapCost = 2, crossCost = 2`
- Output: `16`
- Explanation:
  1. Swap `s[0]` and `s[1]` for a cost of `2`. The strings become `s = "10000"` and `t = "10111"`.
  2. Cross-swap `s[2]` and `t[2]` for another cost of `2`. They become `s = "10100"` and `t = "10011"`.
  3. Swap `s[2]` and `s[3]` for a further cost of `2`. They become `s = "10010"` and `t = "10011"`.
  4. Flip `s[4]` for a cost of `10`, leaving `s = t = "10011"`.
  5. The total cost is `2 + 2 + 2 + 10 = 16`.

**Example 2**

- Input: `s = "001", t = "110", flipCost = 2, swapCost = 100, crossCost = 100`
- Output: `6`
- Explanation:
  - Flip all three bits of `s`. The result is `"110"`, which equals `t`.
  - The total is `3 * flipCost = 3 * 2 = 6`.

**Example 3**

- Input: `s = "1010", t = "1010", flipCost = 5, swapCost = 5, crossCost = 5`
- Output: `0`
- Explanation:
  - The strings are equal initially, so no operation is necessary.
