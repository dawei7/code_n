## Examples

**Example 1**

- Input: `requests = [[1,1],[2,1],[1,7],[2,8]], k = 1, window = 4`
- Output: `4`
- Explanation:
  - User 1 has request times `[1, 7]`; their difference is `6`, which is greater than `window = 4`.
  - User 2 has request times `[1, 8]`; their difference is `7`, also greater than `window = 4`.
  - Thus no inclusive interval of span `window` contains more than `k = 1` request for either user, so all four records may remain.

**Example 2**

- Input: `requests = [[1,2],[1,5],[1,2],[1,6]], k = 2, window = 5`
- Output: `2`
- Explanation:
  - User 1's times are `[2, 2, 5, 6]`. The inclusive interval `[2, 7]`, whose span is `window = 5`, contains all four requests.
  - Because four is strictly greater than `k = 2`, at least two records must be removed.
  - After removing any two, every inclusive interval of the given span contains at most two retained requests.
  - Therefore, two is the maximum number that can remain.

**Example 3**

- Input: `requests = [[1,1],[2,5],[1,2],[3,9]], k = 1, window = 1`
- Output: `3`
- Explanation:
  - User 1's times are `[1, 2]`. Their difference equals `window = 1`.
  - The inclusive interval `[1, 2]` contains both, so its count is two and exceeds `k = 1`; one of those records must be removed.
  - Users 2 and 3 each have a single request and cannot violate the limit. Hence three records can remain in total.
