## Examples

**Example 1**

- Input: `nums = [1,2,4,3,5,6], k = 3`
- Output: `[2,1,3,4,6,5]`
- Explanation:
  - The three equal subarrays are `[1,2]`, `[4,3]`, and `[5,6]`.
  - Reversing them separately gives `[2,1]`, `[3,4]`, and `[6,5]`.
  - Concatenating those reversed blocks produces `[2,1,3,4,6,5]`.

**Example 2**

- Input: `nums = [5,4,4,2], k = 1`
- Output: `[2,4,4,5]`
- Explanation:
  - With one block, the complete array `[5,4,4,2]` is the sole subarray.
  - Reversing that block gives the final array `[2,4,4,5]`.
