## Examples

**Example 1**

- Input: `transactions = [2, -5, 3, -1, -2]`
- Output: `4`
- Explanation: One optimal choice is `[2, 3, -1, -2]`. Its balance evolves as `0 → 2 → 5 → 4 → 2`, never dropping below zero.

**Example 2**

- Input: `transactions = [-1, -2, -3]`
- Output: `0`
- Explanation: Every transaction sends money. Performing any one as the first chosen transaction would make the zero starting balance negative.

**Example 3**

- Input: `transactions = [3, -2, 3, -2, 1, -1]`
- Output: `6`
- Explanation: All transactions can be performed in order. The complete balance trace is `0 → 3 → 1 → 4 → 2 → 3 → 2`.
