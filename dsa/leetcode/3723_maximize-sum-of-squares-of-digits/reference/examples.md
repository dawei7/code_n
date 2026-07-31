## Examples

**Example 1**

- Input: `num = 2, sum = 3`
- Output: `"30"`
- Explanation: Exactly three two-digit good integers exist: `12`, `21`, and `30`.
  - For `12`, the score is $1^2 + 2^2 = 5$.
  - For `21`, the score is $2^2 + 1^2 = 5$.
  - For `30`, the score is $3^2 + 0^2 = 9$.

  The greatest score is $9$, attained by `30`, so the returned string is `"30"`.

**Example 2**

- Input: `num = 2, sum = 17`
- Output: `"98"`
- Explanation: The only good integers are `89` and `98`.
  - For `89`, the score is $8^2 + 9^2 = 145$.
  - For `98`, the score is $9^2 + 8^2 = 145$.

  Both scores are maximal at $145$. The numerically greater tied integer is `98`, so the result is `"98"`.

**Example 3**

- Input: `num = 1, sum = 10`
- Output: `""`
- Explanation: No one-digit integer can have digits totaling `10`; consequently, no good integer exists and the result is empty.
