## Examples

**Example 1**

- Input: `s = "aa", p = "a"`
- Output: `false`
- Explanation: Pattern `"a"` covers only one character, not the complete string `"aa"`.

**Example 2**

- Input: `s = "aa", p = "*"`
- Output: `true`
- Explanation: The `*` wildcard can match the entire two-character sequence.

**Example 3**

- Input: `s = "cb", p = "?a"`
- Output: `false`
- Explanation: The `?` can match `c`, but the pattern's `a` does not match the remaining `b`.
