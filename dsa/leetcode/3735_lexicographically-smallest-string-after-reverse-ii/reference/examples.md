## Examples

**Example 1**

- Input: `s = "dcab"`
- Output: `"acdb"`
- Explanation:

  - Choose `k = 3` and reverse the first three characters.
  - Reversing `"dca"` to `"acd"` produces `"acdb"`, the lexicographically smallest achievable string.

**Example 2**

- Input: `s = "abba"`
- Output: `"aabb"`
- Explanation:

  - Choose `k = 3` and reverse the last three characters.
  - Reversing `"bba"` to `"abb"` produces `"aabb"`, the lexicographically smallest achievable string.

**Example 3**

- Input: `s = "zxy"`
- Output: `"xzy"`
- Explanation:

  - Choose `k = 2` and reverse the first two characters.
  - Reversing `"zx"` to `"xz"` produces `"xzy"`, the lexicographically smallest achievable string.
