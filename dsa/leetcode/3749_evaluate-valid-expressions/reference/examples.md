## Examples

**Example 1**

- Input: `expression = "add(2,3)"`
- Output: `5`
- Explanation: `add(2,3)` represents the calculation `2 + 3 = 5`.

**Example 2**

- Input: `expression = "-42"`
- Output: `-42`
- Explanation: This expression is already a single integer literal, so its value is `-42`.

**Example 3**

- Input: `expression = "div(mul(4,sub(9,5)),add(1,1))"`
- Output: `8`
- Explanation:

  1. Evaluate the inner subtraction: `sub(9,5) = 9 - 5 = 4`.
  2. Use that result in the multiplication: `mul(4,4) = 4 * 4 = 16`.
  3. Evaluate the right-hand addition: `add(1,1) = 1 + 1 = 2`.
  4. Divide the two main results: `div(16,2) = 16 / 2 = 8`.

  Therefore, the complete expression evaluates to `8`.
