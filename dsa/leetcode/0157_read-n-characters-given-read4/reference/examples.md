## Examples

**Example 1**

- Input: `file = "abc"`, `n = 4`
- Output: `3`
- Explanation: After calling your read method, `buf` should contain `"abc"`. We read a total of 3 characters from the file, so return 3. Note that `n = 4`, but the file only has 3 characters.

**Example 2**

- Input: `file = "abcde"`, `n = 5`
- Output: `5`
- Explanation: After calling your read method, `buf` should contain `"abcde"`. We read a total of 5 characters from the file, so return 5.

**Example 3**

- Input: `file = "abcdABCD1234"`, `n = 12`
- Output: `12`
- Explanation: After calling your read method, `buf` should contain `"abcdABCD1234"`. We read a total of 12 characters from the file, so return 12.
