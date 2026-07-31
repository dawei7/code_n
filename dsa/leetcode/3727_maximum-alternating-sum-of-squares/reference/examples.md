## Examples

**Example 1**

- Input: `nums = [1,2,3]`
- Output: `12`
- Explanation: One maximizing rearrangement is `[2,1,3]`. Its alternating score is

  $$
  2^2 - 1^2 + 3^2 = 4 - 1 + 9 = 12.
  $$

**Example 2**

- Input: `nums = [1,-1,2,-2,3,-3]`
- Output: `16`
- Explanation: One maximizing rearrangement is `[-3,-1,-2,1,3,2]`. Its alternating score is

  $$
  (-3)^2 - (-1)^2 + (-2)^2 - 1^2 + 3^2 - 2^2
  = 9 - 1 + 4 - 1 + 9 - 4
  = 16.
  $$
