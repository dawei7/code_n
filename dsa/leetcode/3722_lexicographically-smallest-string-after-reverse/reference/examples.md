## Examples

**Example 1**

- Input: `s = "dcab"`
- Output: `"acdb"`
- Explanation: A prefix reversal gives the minimum result.
  - Choose `k = 3` and reverse the first three characters.
  - Reversing `"dca"` to `"acd"` produces `"acdb"`, the lexicographically smallest achievable string.

**Example 2**

- Input: `s = "abba"`
- Output: `"aabb"`
- Explanation: A suffix reversal gives the minimum result.
  - Choose `k = 3` and reverse the last three characters.
  - Reversing `"bba"` to `"abb"` produces `"aabb"`, the lexicographically smallest achievable string.

**Example 3**

- Input: `s = "zxy"`
- Output: `"xzy"`
- Explanation: The best choice reverses a shorter prefix.
  - Choose `k = 2` and reverse the first two characters.
  - Reversing `"zx"` to `"xz"` produces `"xzy"`, the lexicographically smallest achievable string.
