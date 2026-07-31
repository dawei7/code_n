## Examples

**Example 1**

- Input: `s = "aa", p = "a"`
- Output: `false`
- Explanation: A single `a` cannot cover the complete two-character string `"aa"`.

**Example 2**

- Input: `s = "aa", p = "a*"`
- Output: `true`
- Explanation: The `*` permits the preceding `a` to occur multiple times, so that element can cover both characters of `"aa"`.

**Example 3**

- Input: `s = "ab", p = ".*"`
- Output: `true`
- Explanation: The dot can represent any character, and the following `*` permits that element to repeat enough times to cover the entire string.
