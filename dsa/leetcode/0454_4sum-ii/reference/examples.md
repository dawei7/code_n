## Examples

**Example 1**

- Input: `nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]`
- Output: `2`
- **Explanation:** Exactly two index tuples work:
  1. `(0, 0, 0, 1)`, because `nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0`.
  2. `(1, 1, 0, 0)`, because `nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0`.

**Example 2**

- Input: `nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]`
- Output: `1`
