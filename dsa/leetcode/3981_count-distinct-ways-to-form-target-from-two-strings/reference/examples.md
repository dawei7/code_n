## Examples

**Example 1**

- Input: `word1 = "abc", word2 = "bac", target = "abc"`
- Output: `5`
- **Explanation:** Exactly these five selections form `target`:
  - `word1[0] = 'a'`, `word1[1] = 'b'`, `word2[2] = 'c'`
  - `word1[0] = 'a'`, `word2[0] = 'b'`, `word1[2] = 'c'`
  - `word1[0] = 'a'`, `word2[0] = 'b'`, `word2[2] = 'c'`
  - `word2[1] = 'a'`, `word1[1] = 'b'`, `word1[2] = 'c'`
  - `word2[1] = 'a'`, `word1[1] = 'b'`, `word2[2] = 'c'`

  Every selection keeps indices strictly increasing inside each word and uses both words.

**Example 2**

- Input: `word1 = "cd", word2 = "cd", target = "ccd"`
- Output: `4`
- **Explanation:** The four selections are:
  - `word1[0] = 'c'`, `word2[0] = 'c'`, `word1[1] = 'd'`
  - `word1[0] = 'c'`, `word2[0] = 'c'`, `word2[1] = 'd'`
  - `word2[0] = 'c'`, `word1[0] = 'c'`, `word1[1] = 'd'`
  - `word2[0] = 'c'`, `word1[0] = 'c'`, `word2[1] = 'd'`

  The first two target characters must take one `'c'` from each source, while the final `'d'` may come from either source.

**Example 3**

- Input: `word1 = "xy", word2 = "xy", target = "xyxy"`
- Output: `2`
- **Explanation:** There are two valid constructions:
  - `word1[0] = 'x'`, `word1[1] = 'y'`, `word2[0] = 'x'`, `word2[1] = 'y'`
  - `word2[0] = 'x'`, `word2[1] = 'y'`, `word1[0] = 'x'`, `word1[1] = 'y'`

  Each `"xy"` block comes entirely from one word.

**Example 4**

- Input: `word1 = "ab", word2 = "cde", target = "ace"`
- Output: `1`
- **Explanation:** The only construction selects `word1[0] = 'a'`, `word2[0] = 'c'`, and `word2[2] = 'e'`.
