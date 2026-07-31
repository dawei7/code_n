## Examples

**Example 1**

- Input: `nums = [1,-2,3,4,-5], k = 2`
- Output: `14`
- **Explanation:** Multiply the operation subarray `[3,4]` by `2`, producing `[1,-2,6,8,-5]`. In that resulting array, the maximum-sum subarray is `[6,8]`, whose sum is `6 + 8 = 14`.

**Example 2**

- Input: `nums = [-5,-4,-3], k = 2`
- Output: `-1`
- **Explanation:** Divide the one-element operation subarray `[-3]` by `2`. Rounding the negative quotient toward zero changes the array to `[-5,-4,-1]`. Its maximum-sum nonempty subarray is `[-1]`, so the result is `-1`.
