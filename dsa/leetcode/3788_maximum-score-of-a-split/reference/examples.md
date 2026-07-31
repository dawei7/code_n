## Examples

**Example 1**

- Input: `nums = [10,-1,3,-4,-5]`
- Output: `17`
- Explanation:
  - The optimal split is `i = 2`.
  - Its score is `prefixSum(2) - suffixMin(2) = (10 + (-1) + 3) - (-5) = 17`.

**Example 2**

- Input: `nums = [-7,-5,3]`
- Output: `-2`
- Explanation:
  - The optimal split is `i = 0`.
  - Its score is `prefixSum(0) - suffixMin(0) = (-7) - (-5) = -2`.

**Example 3**

- Input: `nums = [1,1]`
- Output: `0`
- Explanation:
  - The only valid split is `i = 0`.
  - Its score is `prefixSum(0) - suffixMin(0) = 1 - 1 = 0`.
