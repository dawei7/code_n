## Description

A subsequence of a string `s` is considered a **good palindromic subsequence** if:

- It is a subsequence of `s`.
- It is a palindrome (reads the same forwards and backwards).
- It has an **even** length.
- No two consecutive characters are equal, except for the two middle characters.

For example, if `s = "abcabcabb"`, then `"abba"` is considered a good palindromic subsequence, whereas `"bcb"` (not of even length) and `"bbbb"` (contains equal consecutive characters outside the middle) are not.

Given a string `s`, return the length of the longest good palindromic subsequence in `s`.
