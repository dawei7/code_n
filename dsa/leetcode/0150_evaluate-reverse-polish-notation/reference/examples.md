## Examples

**Example 1**

- Input: `tokens = ["2", "1", "+", "3", "*"]`
- Output: `9`
- Explanation: The expression evaluates as `((2 + 1) * 3) = 9`.

**Example 2**

- Input: `tokens = ["4", "13", "5", "/", "+"]`
- Output: `6`
- Explanation: The expression evaluates as `(4 + (13 / 5)) = 6`.

**Example 3**

- Input: `tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]`
- Output: `22`
- Explanation: Applying the operators in postfix order gives:

  `((10 * (6 / ((9 + 3) * -11))) + 17) + 5`

  `= ((10 * (6 / (12 * -11))) + 17) + 5`

  `= ((10 * (6 / -132)) + 17) + 5`

  `= ((10 * 0) + 17) + 5`

  `= (0 + 17) + 5`

  `= 17 + 5`

  `= 22`
