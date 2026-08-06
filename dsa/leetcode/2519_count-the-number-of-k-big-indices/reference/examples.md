## Examples

**Example 1**

- **Input:** `nums = [2, 3, 6, 5, 2, 3], k = 2`
- **Output:** `2`
- **Explanation:**
  - Index 2 (`nums[2] = 6`): Left side has 2 values strictly smaller (`nums[0] = 2`, `nums[1] = 3`). Right side has 3 values strictly smaller (`nums[4] = 2`, `nums[5] = 3`, `nums[3] = 5`). Both sides have $\ge 2$ smaller values.
  - Index 3 (`nums[3] = 5`): Left side has 2 values strictly smaller (`nums[0] = 2`, `nums[1] = 3`). Right side has 2 values strictly smaller (`nums[4] = 2`, `nums[5] = 3`). Both sides have $\ge 2$ smaller values.
  - Total `2`-big indices = 2.

**Example 2**

- **Input:** `nums = [1, 1, 1], k = 3`
- **Output:** `0`
- **Explanation:** Equal values are not strictly smaller, so no index has 3 strictly smaller elements on both sides.
