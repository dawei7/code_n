## Examples

**Example 1**

- Input: `n = 101, x = 0`
- Output: `true`
- Explanation: The digit `0` occurs at index `1`, while the number begins with `1`. Both validity conditions therefore hold.

**Example 2**

- Input: `n = 232, x = 2`
- Output: `false`
- Explanation: Although `2` occurs in the number, it is also the first digit. Starting with `x` violates the second condition.

**Example 3**

- Input: `n = 5, x = 1`
- Output: `false`
- Explanation: The only digit is `5`, so the required digit `1` never occurs.
