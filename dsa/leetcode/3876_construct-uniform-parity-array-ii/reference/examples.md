## Examples

**Example 1**

- Input: `nums1 = [1,4,7]`
- Output: `true`

- **Explanation:** Keep the first value, so `nums2[0] = nums1[0] = 1`. For index `1`, use `nums2[1] = nums1[1] - nums1[0] = 4 - 1 = 3`. Keep the last value with `nums2[2] = nums1[2] = 7`. The resulting array is `[1, 3, 7]`, and every entry is odd, so the construction succeeds.

**Example 2**

- Input: `nums1 = [2,3]`
- Output: `false`

- **Explanation:** No set of legal choices can make both constructed elements share one parity, so the required `nums2` cannot be formed.

**Example 3**

- Input: `nums1 = [4,6]`
- Output: `true`

- **Explanation:** Keep both values: `nums2[0] = nums1[0] = 4` and `nums2[1] = nums1[1] = 6`. The resulting array is `[4, 6]`, whose elements are all even, so the construction succeeds.
