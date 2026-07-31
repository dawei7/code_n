## Examples

**Example 1**

- Input: `nums = [1,2,4,2,3,2]`
- Output: `[1,2,4,3,2]`
- **Explanation:** The endpoint values at indices `0` and `5` are always valid. Values at indices `1` and `2` are strictly greater than everything to their left, while `nums[4]` is strictly greater than everything to its right. Therefore the result is `[1, 2, 4, 3, 2]`.

**Example 2**

- Input: `nums = [5,5,5,5]`
- Output: `[5,5]`
- **Explanation:** The endpoints are valid automatically. Each interior `5` has an equal value on both sides, so it is not strictly greater than all values on either side. The result is `[5, 5]`.

**Example 3**

- Input: `nums = [1]`
- Output: `[1]`
- **Explanation:** The only element is both the first and last element, so it is valid and the result is `[1]`.
