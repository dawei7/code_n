## Examples

**Example 1**

- Input: `nums = [1,-1,0,2], k = 1`
- Output: `3`
- **Explanation:** Swap the values at indices `1` and `3`, producing `[1, 2, 0, -1]`. The subarray `[1, 2]` then has sum `3`, which is the maximum attainable value.

**Example 2**

- Input: `nums = [4,3,2,4], k = 2`
- Output: `13`
- **Explanation:** The entire array is already a subarray with sum `4 + 3 + 2 + 4 = 13`. No swap can improve on the sum of all four positive elements, so zero swaps are optimal.

**Example 3**

- Input: `nums = [-1,-2], k = 0`
- Output: `-1`
- **Explanation:** No swap is allowed. The nonempty subarrays have sums `-1`, `-2`, and `-3`, so the one-element subarray `[-1]` is best.
