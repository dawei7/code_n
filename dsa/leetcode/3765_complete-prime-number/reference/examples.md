## Examples

**Example 1**

- Input: `num = 23`
- Output: `true`
- Explanation:
  - The prefixes are 2 and 23, and both are prime.
  - The suffixes are 3 and 23, and both are prime.
  - Because every member of both collections is prime, 23 is a Complete Prime Number and the result is `true`.

**Example 2**

- Input: `num = 39`
- Output: `false`
- Explanation:
  - Its prefixes are 3 and 39. Although 3 is prime, 39 is not.
  - Its suffixes are 9 and 39; neither value is prime.
  - At least one required truncation is nonprime, so 39 is not a Complete Prime Number and the result is `false`.

**Example 3**

- Input: `num = 7`
- Output: `true`
- Explanation: The one-digit value 7 is prime. Its sole prefix and sole suffix are therefore prime, so the result is `true`.
