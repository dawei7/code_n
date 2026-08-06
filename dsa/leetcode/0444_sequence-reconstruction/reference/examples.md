## Examples

**Example 1**

- **Input:** `nums = [1,2,3], sequences = [[1,2],[1,3]]`
- **Output:** `false`
- **Explanation:** Both `[1,2,3]` and `[1,3,2]` are possible shortest supersequences. The row `[1,2]` is a subsequence of each one, and `[1,3]` is also a subsequence of each one. Because `nums` is not the only shortest supersequence, the result is `false`.

**Example 2**

- **Input:** `nums = [1,2,3], sequences = [[1,2]]`
- **Output:** `false`
- **Explanation:** The shortest possible supersequence is `[1,2]`, which contains the sole row `[1,2]` as a subsequence. Therefore `nums = [1,2,3]` is not shortest, so the result is `false`.

**Example 3**

- **Input:** `nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]`
- **Output:** `true`
- **Explanation:** The only shortest supersequence is `[1,2,3]`. Each supplied row—`[1,2]`, `[1,3]`, and `[2,3]`—is a subsequence of it. Because this unique shortest supersequence equals `nums`, the result is `true`.
