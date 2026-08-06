## Examples

**Example 1**

- Input: `s = "abcxyz123", words = ["abc","123"]`
- Output: `"<b>abc</b>xyz<b>123</b>"`
- Explanation: Both dictionary values occur in `s`: `"abc"` covers the first three characters and `"123"` covers the final three. The uncovered substring `"xyz"` separates those spans, so each match requires its own tag pair.

**Example 2**

- Input: `s = "aaabbb", words = ["aa","b"]`
- Output: `"<b>aaabbb</b>"`
- Explanation: The word `"aa"` occurs twice, starting at positions `0` and `1`, so those two spans overlap and combine to cover `"aaa"`. The one-character word `"b"` occurs three times and covers each of the final three positions. Those three matches are consecutive to one another and to the already covered `"aaa"` span. Their union therefore covers all of `s`, and one outer tag pair replaces any nested, overlapping, or adjacent pairs.
