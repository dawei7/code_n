## Examples

**Example 1**

- Input: `nums = [2,1,2]`
- Output: `1`
- Explanation: At index `1`, the left sum is `nums[0] = 2` and the right
  product is `nums[2] = 2`. The values are equal, and no smaller index is
  balanced, so the result is `1`.

**Example 2**

- Input: `nums = [2,8,2,2,5]`
- Output: `2`
- Explanation: At index `2`, the left sum is `2 + 8 = 10` and the right
  product is `2 * 5 = 10`. Equality holds there, and no earlier index satisfies
  the condition, so the answer is `2`.

**Example 3**

- Input: `nums = [1]`
- Output: `-1`
- Explanation: The only candidate is index `0`. Its empty left side has sum
  $0$, while its empty right side has product $1$. Since those values differ,
  no balanced index exists and the result is `-1`.
