## Examples

**Example 1**

- **Input:** `nums = [3, 2, 4, 4, 1], costs = [3, 7, 6, 4, 2]`
- **Output:** `8`
- **Explanation:**
  - Jump from index 0 (`nums[0] = 3`) to index 2 (`nums[2] = 4`): legal because `nums[0] <= nums[2]` and intervening `nums[1] = 2 < 3`. Cost = `costs[2] = 6`.
  - Jump from index 2 (`nums[2] = 4`) to index 4 (`nums[4] = 1`): legal because `nums[2] > nums[4]` and intervening `nums[3] = 4 >= 4`. Cost = `costs[4] = 2`.
  - Total landing cost $= 6 + 2 = 8$.

**Example 2**

- **Input:** `nums = [0, 1, 2], costs = [1, 1, 1]`
- **Output:** `2`
- **Explanation:** Jump $0 \to 1$ (cost 1) then $1 \to 2$ (cost 1). Total cost $= 2$.

**Example 3**

- **Input:** `nums = [7], costs = [100]`
- **Output:** `0`
- **Explanation:** Single element array; already at index 0. Cost = 0.
