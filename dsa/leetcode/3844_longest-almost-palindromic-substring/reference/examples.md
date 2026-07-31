## Examples

**Example 1**

- Input: `s = "abca"`
- Output: `4`
- Explanation:
  - Choose the complete substring `"abca"`.
  - Remove its third character, `c`.
  - The remaining string is `"aba"`, which is a palindrome, so `"abca"` is almost-palindromic.

**Example 2**

- Input: `s = "abba"`
- Output: `4`
- Explanation:
  - Choose the complete substring `"abba"`.
  - Remove the second character, one of the two middle `b` characters.
  - The remaining string is `"aba"`, which is a palindrome, so `"abba"` is almost-palindromic.

**Example 3**

- Input: `s = "zzabba"`
- Output: `5`
- Explanation:
  - Choose the substring `"zabba"`, beginning at the second character of `s`.
  - Remove the leading `z` from that chosen substring.
  - The remaining string is `"abba"`, which is a palindrome, so `"zabba"` is almost-palindromic.
