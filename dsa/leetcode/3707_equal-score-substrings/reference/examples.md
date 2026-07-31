## Examples

**Example 1**

- Input: `s = "adcb"`
- Output: `true`
- Explanation: Split after index `1`.

  - The left substring is `s[0..1] = "ad"`, with score `1 + 4 = 5`.
  - The right substring is `s[2..3] = "cb"`, with score `3 + 2 = 5`.

  The two non-empty substrings have the same score, so this split succeeds.

**Example 2**

- Input: `s = "bace"`
- Output: `false`
- Explanation: None of the three legal split positions gives equal scores on the two sides.
