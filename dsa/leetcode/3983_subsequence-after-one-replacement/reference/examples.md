## Examples

**Example 1**

- Input: `s = "cat", t = "chat"`
- Output: `true`
- **Explanation:** One valid choice replaces `s[1]` from `'a'` to `'h'`, producing `"cht"`. The characters `'c'`, `'h'`, and `'t'` then match `"chat"` in that order, so `"cht"` is a subsequence. Since the operation is optional, it is also worth observing that the original `"cat"` already matches positions for `'c'`, `'a'`, and `'t'` in order.

**Example 2**

- Input: `s = "plane", t = "apple"`
- Output: `false`
- **Explanation:** The characters `'p'`, `'l'`, and `'e'` can be matched in `t`, but the remaining characters cannot also be placed while preserving their required order. Replacing any single position of `s` still leaves no complete ordered match, so `s` cannot be made a subsequence of `t`.
