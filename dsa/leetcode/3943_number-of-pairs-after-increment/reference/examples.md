## Examples

**Example 1**

- Input: `nums1 = [1,2], nums2 = [3,4], queries = [[2,5],[1,0,0,2],[2,5]]`
- Output: `[2,1]`
- Explanation:
  - For `[2,5]`, the valid pairs use `1 + 4 = 5` and `2 + 3 = 5`, so the first answer is `2`.
  - Query `[1,0,0,2]` adds `2` only to `nums2[0]`, changing `nums2` to `[5,4]`.
  - For the final `[2,5]`, only `1 + 4 = 5` remains valid, so the second answer is `1`.
  - Therefore the returned answer is `[2,1]`.

**Example 2**

- Input: `nums1 = [1,1], nums2 = [2,2,3], queries = [[2,4],[1,0,1,1],[2,4]]`
- Output: `[2,6]`
- Explanation:
  - Initially, each of the two positions containing `1` in `nums1` pairs with the `3` in `nums2`, giving `2` pairs whose sum is `4`.
  - Query `[1,0,1,1]` adds `1` to the first two positions of `nums2`, producing `[3,3,3]`.
  - Every one of the two `nums1` positions now pairs with every one of the three `nums2` positions because `1 + 3 = 4`. The resulting count is `2 * 3 = 6`.
  - Therefore the returned answer is `[2,6]`.

**Example 3**

- Input: `nums1 = [2,5,8,4], nums2 = [1,3,8], queries = [[2,9],[1,1,2,1],[2,10]]`
- Output: `[1,0]`
- Explanation:
  - For `[2,9]`, the only valid pair is `nums1[2] + nums2[0] = 8 + 1 = 9`, so the first count is `1`.
  - Query `[1,1,2,1]` adds `1` to `nums2[1]` and `nums2[2]`, changing `nums2` to `[1,4,9]`.
  - No pair formed from `nums1` and the updated `nums2` sums to `10`, so the final count is `0`.
  - Therefore the returned answer is `[1,0]`.
