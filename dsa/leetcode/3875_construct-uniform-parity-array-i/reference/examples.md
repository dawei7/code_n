## Examples

**Example 1**

- Input: `nums1 = [2,3]`
- Output: `true`

- **Explanation:** For index `0`, subtract the value at index `1`: `nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1`. For index `1`, keep the original value, so `nums2[1] = nums1[1] = 3`. The resulting array is `[-1, 3]`; both values are odd, so the construction succeeds.

**Example 2**

- Input: `nums1 = [4,6]`
- Output: `true`

- **Explanation:** Keep both original values: `nums2[0] = nums1[0] = 4` and `nums2[1] = nums1[1] = 6`. The resulting array is `[4, 6]`, whose elements are all even, so the construction succeeds.
