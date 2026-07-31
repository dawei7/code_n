## Examples

**Example 1**

- Input: `s = "abab"`
- Output: `2`
- Explanation: Split `"abab"` into `"a"` and `"bab"`. Their starting characters are the distinct letters `'a'` and `'b'`, so two substrings are achievable.

**Example 2**

- Input: `s = "abcd"`
- Output: `4`
- Explanation: Split the string into `"a"`, `"b"`, `"c"`, and `"d"`. Every piece starts with a different character, giving the maximum of four.

**Example 3**

- Input: `s = "aaaa"`
- Output: `1`
- Explanation: Every character is `'a'`, so at most one substring can start with that letter. Keeping the complete string as one piece attains the answer `1`.
