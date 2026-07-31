## Examples

**Example 1**

- Input: `nums = [2,2,3,1], k = 4`
- Output: `2`
- Explanation:
  - The subarray `[2, 3]` has the distinct-value set `{2, 3}`.
  - Its sum is `2 + 3 = 5`, which is at least `k = 4`, so the minimum qualifying length is `2`.

**Example 2**

- Input: `nums = [3,2,3,4], k = 5`
- Output: `2`
- Explanation:
  - The subarray `[3, 2]` contributes the distinct values `{3, 2}`.
  - Their sum is exactly `3 + 2 = 5`, meeting `k = 5`, and the answer is `2`.

**Example 3**

- Input: `nums = [5,5,4], k = 5`
- Output: `1`
- Explanation:
  - The one-element subarray `[5]` has distinct-value set `{5}` and sum `5`.
  - It already meets `k = 5`, so no longer subarray can improve on length `1`.
