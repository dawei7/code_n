## Examples

**Example 1**

- Input: `nums1 = [1,3,2], nums2 = [4,5,1], k = 2`
- Output: `22`
- Explanation: Choose `(i1, j1) = (1, 0)`, contributing `3 * 4 = 12`, followed by `(i2, j2) = (2, 1)`, contributing `2 * 5 = 10`. Both index chains increase strictly, and the total is `12 + 10 = 22`.

**Example 2**

- Input: `nums1 = [-2,0,5], nums2 = [-3,4,-1,2], k = 2`
- Output: `26`
- Explanation: Choose `(i1, j1) = (0, 0)` for `-2 * -3 = 6`, then `(i2, j2) = (2, 1)` for `5 * 4 = 20`. Their sum is `6 + 20 = 26`.

**Example 3**

- Input: `nums1 = [-3,-2], nums2 = [1,2], k = 2`
- Output: `-7`
- Explanation: Exactly two pairs are required, so the only legal index chains use `(0, 0)` and `(1, 1)`. Their products are `-3 * 1 = -3` and `-2 * 2 = -4`, giving `-3 + (-4) = -7`.

