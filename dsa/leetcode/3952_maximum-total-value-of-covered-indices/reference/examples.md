## Examples

**Example 1**

- Input: `nums = [9,2,6,1], s = "0101"`
- Output: `15`
- Explanation:
  - Tokens begin at indices `1` and `3`.
  - Move the token at index `3` to index `2`, and move the token at index `1` to index `0`.
  - The covered indices become `[0, 2]`, whose total is `nums[0] + nums[2] = 9 + 6 = 15`.

**Example 2**

- Input: `nums = [5,1,4], s = "001"`
- Output: `4`
- Explanation:
  - The only token begins at index `2`.
  - Leaving it at index `2` is optimal.
  - The sole covered value is `nums[2] = 4`.

**Example 3**

- Input: `nums = [9,3,5], s = "011"`
- Output: `14`
- Explanation:
  - Tokens begin at indices `1` and `2`.
  - Move the token at index `1` to index `0` and leave the other token at index `2`.
  - The covered indices `[0, 2]` contribute `nums[0] + nums[2] = 9 + 5 = 14`.
