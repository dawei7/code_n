## Examples

**Example 1**

- Input: `nums = [7, 2, 5, 10, 8], k = 2`
- Output: `18`
- Explanation: There are four ways to place the single boundary. The optimal split is `[7, 2, 5]` and `[10, 8]`;
  its two sums are $14$ and $18$, so its largest sum is only $18$.

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5], k = 2`
- Output: `9`
- Explanation: Among the four possible boundary placements, the best split is `[1, 2, 3]` and `[4, 5]`. Both
  subarrays sum to $6$ and $9$, making the largest sum $9$.
