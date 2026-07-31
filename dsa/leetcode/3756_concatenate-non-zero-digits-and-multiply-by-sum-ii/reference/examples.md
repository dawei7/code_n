## Examples

**Example 1**

- Input: `s = "10203004", queries = [[0,7],[1,3],[4,6]]`
- Output: `[12340, 4, 9]`
- Explanation:
  - For `s[0..7] = "10203004"`, removing zeros gives `x = 1234`. Its digit sum is `1 + 2 + 3 + 4 = 10`, so the result is `1234 * 10 = 12340`.
  - For `s[1..3] = "020"`, the only retained digit gives `x = 2` and `sum = 2`. Therefore, the result is `2 * 2 = 4`.
  - For `s[4..6] = "300"`, the retained value is `x = 3` and its digit sum is `3`. Therefore, the result is `3 * 3 = 9`.

**Example 2**

- Input: `s = "1000", queries = [[0,3],[1,1]]`
- Output: `[1, 0]`
- Explanation:
  - For `s[0..3] = "1000"`, removing the zeros leaves `x = 1` with `sum = 1`, giving `1 * 1 = 1`.
  - For `s[1..1] = "0"`, no nonzero digit remains, so `x = 0` and `sum = 0`. The result is `0 * 0 = 0`.

**Example 3**

- Input: `s = "9876543210", queries = [[0,9]]`
- Output: `[444444137]`
- Explanation: For `s[0..9] = "9876543210"`, removing zero produces `x = 987654321`. The digit sum is `9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45`, so the unreduced product is `987654321 * 45 = 44444444445`. Reducing `44444444445` modulo $10^9+7$ gives `444444137`.
