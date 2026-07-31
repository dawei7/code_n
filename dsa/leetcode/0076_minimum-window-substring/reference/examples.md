## Examples

**Example 1**

- Input: `s = "ADOBECODEBANC", t = "ABC"`
- Output: `"BANC"`
- Explanation: Window `"BANC"` contains the required `A`, `B`, and `C`, and no shorter valid window exists.

**Example 2**

- Input: `s = "a", t = "a"`
- Output: `"a"`
- Explanation: The whole one-character string is the minimum valid window.

**Example 3**

- Input: `s = "a", t = "aa"`
- Output: `""`
- Explanation: A valid window would need both copies of `a` from `t`, but `s` contains only one, so the result is empty.
