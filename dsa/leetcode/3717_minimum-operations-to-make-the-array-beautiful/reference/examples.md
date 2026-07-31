## Examples

**Example 1**

- Input: `nums = [3,7,9]`
- Output: `2`
- Explanation: Increment `nums[1]` twice. The resulting array `[3,9,9]` is beautiful because $9$ is divisible by $3$ and the final $9$ is divisible by the preceding $9$.

**Example 2**

- Input: `nums = [1,1,1]`
- Output: `0`
- Explanation: Every adjacent divisibility condition already holds, so no operation is necessary.

**Example 3**

- Input: `nums = [4]`
- Output: `0`
- Explanation: A one-element array has no index $i > 0$ to check, so it is already beautiful.
