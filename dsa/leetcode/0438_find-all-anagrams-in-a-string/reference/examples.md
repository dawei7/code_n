## Examples

**Example 1**

- Input: `s = "cbaebabacd", p = "abc"`
- Output: `[0,6]`
- Explanation:
  1. The substring `"cba"` starts at index `0` and is an anagram of `"abc"`.
  2. The substring `"bac"` starts at index `6` and is also an anagram of `"abc"`.

**Example 2**

- Input: `s = "abab", p = "ab"`
- Output: `[0,1,2]`
- Explanation:
  1. The substring at index `0` is `"ab"`.
  2. The substring at index `1` is `"ba"`.
  3. The substring at index `2` is `"ab"`.
  Each of these substrings is an anagram of `"ab"`.
