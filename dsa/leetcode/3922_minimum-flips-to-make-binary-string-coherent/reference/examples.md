## Examples

**Example 1**

- Input: `s = "1010"`
- Output: `1`
- **Explanation:** Flip `s[0]` from `'1'` to `'0'`. The resulting string is `"0010"`, which has neither forbidden subsequence.

**Example 2**

- Input: `s = "0110"`
- Output: `1`
- **Explanation:** Flip `s[1]` from `'1'` to `'0'`. This again produces `"0010"` and removes every `"011"` and `"110"` subsequence.

**Example 3**

- Input: `s = "1000"`
- Output: `0`
- **Explanation:** The original string already contains neither `"011"` nor `"110"` as a subsequence, so no operation is necessary.
