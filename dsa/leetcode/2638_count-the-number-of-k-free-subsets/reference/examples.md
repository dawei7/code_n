## Examples

**Example 1**

- **Input:** `nums = [5, 4, 6], k = 1`
- **Output:** `5`
- **Explanation:** The valid subsets are `[]`, `[4]`, `[5]`, `[6]`, and `[4, 6]`. (Note: `[4, 5]` and `[5, 6]` contain elements differing by 1).

**Example 2**

- **Input:** `nums = [2, 3, 5, 8], k = 5`
- **Output:** `12`
- **Explanation:** The only conflicting pair is `3` and `8`. Out of $2^4 = 16$ total subsets, 4 contain both `3` and `8`, leaving 12 valid k-Free subsets.

**Example 3**

- **Input:** `nums = [10, 5, 9, 11], k = 20`
- **Output:** `16`
- **Explanation:** No two values differ by 20, so all $2^4 = 16$ subsets are k-Free.
