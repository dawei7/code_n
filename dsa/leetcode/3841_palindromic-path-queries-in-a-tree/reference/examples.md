## Examples

**Example 1**

- Input: `n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]`
- Output: `[true,false]`
- Explanation:
  - For `"query 0 2"`, path `0 → 1 → 2` spells `"aac"`. Its letters can be rearranged as the palindrome `"aca"`, so `answer[0] = true`.
  - Operation `"update 1 b"` changes node `1` to `'b'`, making the current string `s = "abc"`.
  - The next `"query 0 2"` sees path letters `"abc"`. They cannot form a palindrome under any rearrangement, so `answer[1] = false`.

Thus, `answer = [true, false]`.

**Example 2**

- Input: `n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]`
- Output: `[false,false,true]`
- Explanation:
  - For `"query 1 2"`, path `1 → 0 → 2` spells `"bac"`, whose three distinct letters cannot be rearranged into a palindrome. Hence `answer[0] = false`.
  - Operation `"update 0 b"` changes the root character to `'b'`, so the current assignment is `s = "bbca"`.
  - For `"query 2 3"`, path `2 → 0 → 3` spells `"cba"`. It cannot form a palindrome, giving `answer[1] = false`.
  - Operation `"update 3 a"` assigns `'a'` to node `3`; that node already has `'a'`, so `s` remains `"bbca"`.
  - Finally, `"query 1 3"` sees `"bba"` along path `1 → 0 → 3`. Rearranging it as `"bab"` forms a palindrome, so `answer[2] = true`.

Thus, `answer = [false, false, true]`.
