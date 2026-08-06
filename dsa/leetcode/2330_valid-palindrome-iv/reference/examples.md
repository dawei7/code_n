## Examples

**Example 1**

- **Input:** `s = "abcdba"`
- **Output:** `true`
- **Explanation:** Only 1 pair of mirrored characters differs (`'c'` vs `'d'`). Replacing `'c'` with `'d'` or vice versa makes `"abddba"` or `"abcba"`, taking 1 operation.

**Example 2**

- **Input:** `s = "aa"`
- **Output:** `true`
- **Explanation:** `"aa"` is already a palindrome. Changing both `'a'`s to `'b'` produces `"bb"` in 2 operations.

**Example 3**

- **Input:** `s = "abcdef"`
- **Output:** `false`
- **Explanation:** All 3 mirrored pairs (`'a'` vs `'f'`, `'b'` vs `'e'`, `'c'` vs `'d'`) differ, requiring at least 3 operations.
