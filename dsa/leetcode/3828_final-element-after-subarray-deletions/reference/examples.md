## Examples

**Example 1**

- Input: `nums = [1,5,2]`
- Output: `2`
- Explanation: One valid optimal strategy:
  - Alice removes `[1]`, producing `[5, 2]`.
  - Bob then removes `[5]`, producing `[2]`. The final value is therefore `2`.

**Example 2**

- Input: `nums = [3,7]`
- Output: `7`
- Explanation: Alice removes `[3]` and leaves `[7]`. The game has already reached one element, so Bob has no turn and the answer is `7`.
