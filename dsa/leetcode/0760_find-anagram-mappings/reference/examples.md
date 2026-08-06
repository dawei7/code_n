## Examples

**Example 1**

- Input: `nums1 = [12,28,46,32,50], nums2 = [50,12,32,46,28]`
- Output: `[1,4,3,2,0]`
- Explanation: `mapping[0] = 1` because the element at position `0` in `nums1` occurs at `nums2[1]`. Likewise, `mapping[1] = 4` because the element at position `1` in `nums1` occurs at `nums2[4]`; the remaining entries follow the same rule.

**Example 2**

- Input: `nums1 = [84,46], nums2 = [84,46]`
- Output: `[0,1]`
