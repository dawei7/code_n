## Examples

**Example 1**

- Input: `s = "barfoothefoobarman", words = ["foo", "bar"]`
- Output: `[0, 9]`
- Explanation: At index 0, `"barfoo"` concatenates `["bar", "foo"]`. At index 9, `"foobar"` concatenates `["foo", "bar"]`. Both word orders are permutations of `words`.

**Example 2**

- Input: `s = "wordgoodgoodgoodbestword", words = ["word", "good", "best", "word"]`
- Output: `[]`
- Explanation: No substring contains exactly the required multiset of words, including two copies of `"word"`.

**Example 3**

- Input: `s = "barfoofoobarthefoobarman", words = ["bar", "foo", "the"]`
- Output: `[6, 9, 12]`
- Explanation: The three matches are:

  - Index 6: `"foobarthe"` is `["foo", "bar", "the"]`.
  - Index 9: `"barthefoo"` is `["bar", "the", "foo"]`.
  - Index 12: `"thefoobar"` is `["the", "foo", "bar"]`.
