## Examples

**Example 1**

- Input: `nums = [2,5,4,3]`
- Output: `4`
- Explanation: The result follows from the full array.
  - The longest balanced subarray is `[2,5,4,3]`.
  - Its distinct even values are `[2,4]`, and its distinct odd values are `[5,3]`. Both counts are `2`, so its length is `4`.

**Example 2**

- Input: `nums = [3,2,2,5,4]`
- Output: `5`
- Explanation: The result again uses the full array.
  - The longest balanced subarray is `[3,2,2,5,4]`.
  - Its distinct even values are `[2,4]`, while its distinct odd values are `[3,5]`. Each group has `2` values, giving length `5`; the repeated `2` does not increase the even count.

**Example 3**

- Input: `nums = [1,2,3,2]`
- Output: `3`
- Explanation: The balanced portion is a proper subarray.
  - The longest balanced subarray is `[2,3,2]`.
  - It has one distinct even value, `[2]`, and one distinct odd value, `[3]`. Therefore its length is `3`.
