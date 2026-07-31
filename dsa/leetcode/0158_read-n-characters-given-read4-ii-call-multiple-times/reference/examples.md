## Examples

**Example 1**

- Input: `file = "abc", queries = [1,2,1]`
- Output: `[1,2,0]`
- Explanation: The first call copies `"a"` and returns `1`. The second continues from the same file position, copies `"bc"`, and returns `2`. The third call is already at end of file, so it copies nothing and returns `0`. The destination is assumed to have room for all file characters.

**Example 2**

- Input: `file = "abc", queries = [4,1]`
- Output: `[3,0]`
- Explanation: The first request asks for four characters but only `"abc"` remains, so it copies three and returns `3`. The next request finds the reader at end of file and returns `0`.
