## Examples

**Example 1**

- Input: `s = "aaa"`
- Output: `"aaa"`

- **Explanation:** Encoding this short repetition would not reduce its length, so the literal string is already
shortest.

**Example 2**

- Input: `s = "aaaaa"`
- Output: `"5[a]"`

- **Explanation:** The five equal characters compress to four characters, one fewer than the original string.

**Example 3**

- Input: `s = "aaaaaaaaaa"`
- Output: `"10[a]"`

- **Explanation:** The alternatives `"a9[a]"` and `"9[a]a"` are valid as well. Each of these encodings, including the
displayed output, has length five and is therefore an acceptable shortest answer.
