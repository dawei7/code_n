## Examples

**Example 1**

- **Input:** `nums = [1,4,5,2,3], k = 3`
- **Output:** `[5,2,3]`
- **Explanation:** The subarrays of size 3 are `[1,4,5]`, `[4,5,2]`, and `[5,2,3]`.
  Of these subarrays, `[5,2,3]` is the largest because $5 > 4$ and $5 > 1$.

**Example 2**

- **Input:** `nums = [1,4,5,2,3], k = 4`
- **Output:** `[4,5,2,3]`
- **Explanation:** The subarrays of size 4 are `[1,4,5,2]` and `[4,5,2,3]`.
  `[4,5,2,3]` is larger because $4 > 1$.

**Example 3**

- **Input:** `nums = [1,4,5,2,3], k = 1`
- **Output:** `[5]`
- **Explanation:** The single-element subarrays are `[1]`, `[4]`, `[5]`, `[2]`, and `[3]`. The largest is `[5]`.
