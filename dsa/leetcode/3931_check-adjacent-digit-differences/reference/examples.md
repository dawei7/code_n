## Examples

**Example 1**

- Input: `s = "132"`
- Output: `true`
- Explanation: The first pair, `1` and `3`, has difference `abs(1 - 3) = 2`. The second pair, `3` and `2`, has difference `abs(3 - 2) = 1`. Both values are at most $2$, so the condition holds.

**Example 2**

- Input: `s = "129"`
- Output: `false`
- Explanation: The pair `1` and `2` has difference `abs(1 - 2) = 1`, but the following pair `2` and `9` has difference `abs(2 - 9) = 7`. Because that second value is greater than $2$, the condition fails.
