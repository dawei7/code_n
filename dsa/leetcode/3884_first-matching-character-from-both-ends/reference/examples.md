## Examples

**Example 1**

- Input: `s = "abcacbd"`
- Output: `1`
- Explanation: At index `1`, the compared positions are `1` and `5`, and both contain `'b'`. Index `0` does not match its mirror, so `1` is the smallest qualifying index.

**Example 2**

- Input: `s = "abc"`
- Output: `1`
- Explanation: For index `1`, the mirror is also index `1`; the two compared positions coincide on `'b'`. Index `0` fails, making `1` the first match.

**Example 3**

- Input: `s = "abcdab"`
- Output: `-1`
- Explanation: At every index `i`, `s[i]` differs from `s[n - i - 1]`. Because no mirrored pair matches, the required fallback is `-1`.
