## Examples

**Example 1**

- Input: `nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3`
- Output: `[1, 2, 2, 3, 5, 6]`
- Explanation: The meaningful inputs are `[1, 2, 3]` and `[2, 5, 6]`. In the merged result, positions `1`, `2`, and `4` contain the values contributed by `nums1`; positions `3`, `5`, and `6` contain those contributed by `nums2`.

**Example 2**

- Input: `nums1 = [1], m = 1, nums2 = [], n = 0`
- Output: `[1]`
- Explanation: Merging `[1]` with an empty array leaves `[1]`.

**Example 3**

- Input: `nums1 = [0], m = 0, nums2 = [1], n = 1`
- Output: `[1]`
- Explanation: The meaningful inputs are `[]` and `[1]`, producing `[1]`. Because `m = 0`, the initial zero in `nums1` is only reserved capacity and is not an input value.
