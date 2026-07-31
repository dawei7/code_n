## Examples

**Example 1**

- Input: `nums1 = [10,20], nums2 = [20,10]`
- Output: `0`

- **Explanation:** Exchange `nums2[0] = 20` and `nums2[1] = 10`. This is a free swap within `nums2`, which becomes `[10,20]`. The arrays are then identical, so the total cost is `0`.

**Example 2**

- Input: `nums1 = [10,10], nums2 = [20,20]`
- Output: `1`

- **Explanation:** First exchange `nums1[0] = 10` with `nums2[0] = 20`. The arrays become `[20,10]` and `[10,20]`, and this between-array operation costs `1`. Next, freely exchange `nums2[0] = 10` and `nums2[1] = 20`, making `nums2` equal to `[20,10]`. Both arrays are now identical, with total cost `1`.

**Example 3**

- Input: `nums1 = [10,20], nums2 = [30,40]`
- Output: `-1`

- **Explanation:** The available values cannot be distributed so that both arrays contain the same multiset. Therefore, making the arrays identical is impossible and the result is `-1`.
