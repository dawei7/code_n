## Examples

**Example 1**

- Input: `nums = [6, 12, 8]`
- Output: `3`
- **Explanation:** Use $6$ as the common value. Divide `nums[1] = 12` by $2$ to obtain $6$. Divide `nums[2] = 8` by $4$ to obtain $2$, then multiply that $2$ by $3$ to obtain $6$. These three operations are optimal.

**Example 2**

- Input: `nums = [5, 15, 20]`
- Output: `2`
- **Explanation:** Keep the first entry at $5$. Divide `nums[1] = 15` by $3$, and divide `nums[2] = 20` by $4$. Both changed entries become $5$, using two operations.

**Example 3**

- Input: `nums = [7, 7, 7]`
- Output: `0`
- **Explanation:** Every entry already has the same value, so no operation is necessary.
