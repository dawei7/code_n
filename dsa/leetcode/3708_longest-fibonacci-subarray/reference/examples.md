## Examples

**Example 1**

- Input: `nums = [1, 1, 1, 1, 2, 3, 5, 1]`
- Output: `5`
- Explanation: The longest qualifying subarray is `nums[2..6] = [1, 1, 2, 3, 5]`. It is Fibonacci because `1 + 1 = 2`, `1 + 2 = 3`, and `2 + 3 = 5`.

**Example 2**

- Input: `nums = [5, 2, 7, 9, 16]`
- Output: `5`
- Explanation: The full array `nums[0..4] = [5, 2, 7, 9, 16]` qualifies: `5 + 2 = 7`, `2 + 7 = 9`, and `7 + 9 = 16`.

**Example 3**

- Input: `nums = [1000000000, 1000000000, 1000000000]`
- Output: `2`
- Explanation: A longest qualifying choice is `nums[1..2] = [1000000000, 1000000000]`. Its length is `2`, so it is Fibonacci without needing to satisfy a third-term equation.
