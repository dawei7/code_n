## Examples

**Example 1**

- Input: `n = 1000`
- Output: `false`
- **Explanation:** The digits are `1`, `0`, `0`, and `0`.
  - `digitSum` is `1 + 0 + 0 + 0 = 1`.
  - `squareSum` is `1^2 + 0^2 + 0^2 + 0^2 = 1`.
  - Their difference is `1 - 1 = 0`. Because $0$ is not at least $50$, the integer is not good.

**Example 2**

- Input: `n = 19`
- Output: `true`
- **Explanation:** The digits are `1` and `9`.
  - `digitSum` is `1 + 9 = 10`.
  - `squareSum` is `1^2 + 9^2 = 1 + 81 = 82`.
  - Their difference is `82 - 10 = 72`. Because $72 \ge 50$, the integer is good.
