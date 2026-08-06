## Examples

**Example 1**

- Input: `words = ["ab","bc"], s = "aabcd"`
- Output: `"a<b>abc</b>d"`
- Explanation: The appearances of `"ab"` and `"bc"` overlap, so their covered letters use one bold range. Returning `"a<b>a<b>b</b>c</b>d"` would use more tags and is therefore incorrect.

**Example 2**

- Input: `words = ["ab","cb"], s = "aabcd"`
- Output: `"a<b>ab</b>cd"`
