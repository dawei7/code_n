## Examples

**Example 1**

- Input: `prices = [3, 3, 5, 0, 0, 3, 1, 4]`
- Output: `6`
- Explanation: Buy on day 4 for `0` and sell on day 6 for `3`, earning `3`. Then buy on day 7 for `1` and sell on day 8 for `4`, earning another `3`.

**Example 2**

- Input: `prices = [1, 2, 3, 4, 5]`
- Output: `4`
- Explanation: Buy on day 1 for `1` and sell on day 5 for `5`, earning `4`. Buying again while already holding a share would overlap transactions and is not permitted; a sale must precede the next purchase.

**Example 3**

- Input: `prices = [7, 6, 4, 3, 1]`
- Output: `0`
- Explanation: No transaction is profitable, so making none gives the maximum profit of `0`.
