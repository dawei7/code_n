## Examples

**Example 1**

- Input: `s = "abca", k = 3`
- Output: `"abc"`
- Explanation:
  - The `'a'` characters at indices `i = 0` and `i = 3` are close because `3 - 0 = 3 <= k`.
  - The right `'a'` merges into the left one, producing `s = "abc"`.
  - The updated string has no other close equal characters, so merging stops.

**Example 2**

- Input: `s = "aabca", k = 2`
- Output: `"abca"`
- Explanation:
  - The `'a'` characters at indices `i = 0` and `i = 1` are close because `1 - 0 = 1 <= k`.
  - Removing the right copy while retaining the left one changes the string to `s = "abca"`.
  - The remaining `'a'` characters now occupy indices `i = 0` and `i = 3`. They are not close because `k < 3`, so no further merge is possible.

**Example 3**

- Input: `s = "yybyzybz", k = 2`
- Output: `"ybzybz"`
- Explanation:
  - The `'y'` characters at indices `i = 0` and `i = 1` are close because `1 - 0 = 1 <= k`.
  - Their merge retains the left `'y'` and produces `s = "ybyzybz"`.
  - In this updated string, the `'y'` characters at indices `i = 0` and `i = 2` are close because `2 - 0 = 2 <= k`.
  - Merging that pair produces `s = "ybzybz"`.
  - No close equal pair remains, so this string is final.
