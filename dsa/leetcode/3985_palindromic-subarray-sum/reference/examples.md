## Examples

**Example 1**

- Input: `nums = [10,10]`
- Output: `20`
- **Explanation:** The complete array is a palindrome, and its sum is `10 + 10 = 20`, which is the maximum.

**Example 2**

- Input: `nums = [1,2,3,2,1,5,6]`
- Output: `9`
- **Explanation:** The contiguous prefix `[1,2,3,2,1]` reads the same in both directions. Its sum is `1 + 2 + 3 + 2 + 1 = 9`, and no palindromic subarray has a larger sum.

**Example 3**

- Input: `nums = [7,1,2,1,7,3,4,3,4]`
- Output: `18`
- **Explanation:** The subarray `[7,1,2,1,7]` is palindromic and sums to `7 + 1 + 2 + 1 + 7 = 18`. This is the greatest attainable palindromic sum.

**Example 4**

- Input: `nums = [1,2,3,4,5]`
- Output: `5`
- **Explanation:** No contiguous range of length at least two is a palindrome. Every singleton is palindromic, so the largest element, `5`, supplies the answer.

**Example 5**

- Input: `nums = [1000]`
- Output: `1000`
- **Explanation:** The sole one-element subarray is a palindrome, and its sum is `1000`.
