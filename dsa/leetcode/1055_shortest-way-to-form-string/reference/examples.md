## Examples

**Example 1**

- Input: `source = "abc", target = "abcbc"`
- Output: `2`
- Explanation: Concatenate `"abc"` and `"bc"`. Each piece is a subsequence of the source string `"abc"`, and together they form `"abcbc"`.

**Example 2**

- Input: `source = "abc", target = "acdbc"`
- Output: `-1`
- Explanation: Construction is impossible because target contains `"d"`, which does not occur in source.

**Example 3**

- Input: `source = "xyz", target = "xzyxz"`
- Output: `3`
- Explanation: The required concatenation is `"xz" + "y" + "xz"`.
