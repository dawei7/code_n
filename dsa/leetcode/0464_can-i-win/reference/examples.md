## Examples

**Example 1**

- Input: `maxChoosableInteger = 10, desiredTotal = 11`
- Output: `false`
- **Explanation:** The first player loses regardless of the initial choice. The available values are `1` through `10`; if the first player chooses `1`, the second chooses `10` and reaches `11`. The same complementary response exists for every other first choice, so the second player can always reach or exceed `desiredTotal` immediately.

**Example 2**

- Input: `maxChoosableInteger = 10, desiredTotal = 0`
- Output: `true`

**Example 3**

- Input: `maxChoosableInteger = 10, desiredTotal = 1`
- Output: `true`
