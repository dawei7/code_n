## Examples

**Example 1**

- Input: `nums = [-1,1,0]`
- Output: `5`
- Explanation:
  - Every single-element subarray is centered: `[-1]`, `[1]`, and `[0]` each has a sum equal to its only element.
  - Subarray `[1,0]` has sum `1`, and `1` occurs inside it.
  - Subarray `[-1,1,0]` has sum `0`, and `0` occurs inside it.
  - These are the five centered subarrays, so the answer is `5`.

**Example 2**

- Input: `nums = [2,-3]`
- Output: `2`
- Explanation:
  - Only the two single-element subarrays `[2]` and `[-3]` are centered.
