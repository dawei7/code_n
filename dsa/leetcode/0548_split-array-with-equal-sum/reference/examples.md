## Examples

**Example 1**

- **Input:** `nums = [1,2,1,2,1,2,1]`
- **Output:** `true`
- **Explanation:** Choose `i = 1`, `j = 3`, and `k = 5`. The four retained sums are
  `sum(0, i - 1) = sum(0, 0) = 1`, `sum(i + 1, j - 1) = sum(2, 2) = 1`,
  `sum(j + 1, k - 1) = sum(4, 4) = 1`, and `sum(k + 1, n - 1) = sum(6, 6) = 1`.

**Example 2**

- **Input:** `nums = [1,2,1,2,1,2,1,2]`
- **Output:** `false`
