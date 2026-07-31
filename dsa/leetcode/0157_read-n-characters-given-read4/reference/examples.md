## Examples

**Example 1**

- Input: `file = "abc", n = 4`
- Output: `3`
- Explanation: `read` copies `"abc"` into the destination `buf`. Only three characters exist, so it returns `3`. The input file content and the output buffer are separate: the implementation must write these characters into `buf`.

**Example 2**

- Input: `file = "abcde", n = 5`
- Output: `5`
- Explanation: All five characters are copied into `buf`, so the returned count is `5`.

**Example 3**

- Input: `file = "abcdABCD1234", n = 12`
- Output: `12`
- Explanation: The entire twelve-character file is copied into `buf`, and `read` returns `12`.
