## Examples

**Example 1**

- Input: `s1 = "great", s2 = "rgeat"`
- Output: `true`
- Explanation: One valid scenario first divides `"great"` as `"gr/eat"` and keeps those parts in order. Recursively split that state as `"g/r / e/at"`, swap only `"g/r"` to obtain `"r/g / e/at"`, then divide `"at"` as `"a/t"` and keep it in order. The leaves concatenate as `"rgeat"`, so this scenario reaches `s2`.

**Example 2**

- Input: `s1 = "abcde", s2 = "caebd"`
- Output: `false`

**Example 3**

- Input: `s1 = "a", s2 = "a"`
- Output: `true`
