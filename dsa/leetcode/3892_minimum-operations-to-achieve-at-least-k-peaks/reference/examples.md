## Examples

**Example 1**

- Input: `nums = [2,1,2], k = 1`
- Output: `1`
- Explanation: Increase `nums[2]` from $2$ to $3$. Its circular neighbors are `nums[1] = 1` and `nums[0] = 2`, so index $2$ is then strictly greater than both. This attains one peak using the minimum of one operation.

**Example 2**

- Input: `nums = [4,5,3,6], k = 2`
- Output: `0`
- Explanation: The original array already has two peaks. Index $1$ holds $5$, which exceeds its neighbors $4$ and $3$; index $3$ holds $6$, which exceeds its neighbors $3$ and the wrapped value $4$. No operation is required.

**Example 3**

- Input: `nums = [3,7,3], k = 2`
- Output: `-1`
- Explanation: A circular array of length three cannot contain two nonadjacent peaks, so reaching at least two peaks is impossible.
