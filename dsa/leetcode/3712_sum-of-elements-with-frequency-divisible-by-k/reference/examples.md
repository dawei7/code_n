## Examples

**Example 1**

- Input: `nums = [1, 2, 2, 3, 3, 3, 3, 4], k = 2`
- Output: `16`
- Explanation:

  - `1` occurs once, so its frequency is odd and does not qualify.
  - `2` occurs twice, so its frequency is even.
  - `3` occurs four times, which is also even.
  - `4` occurs once and does not qualify.

  Therefore the included occurrences sum to `2 + 2 + 3 + 3 + 3 + 3 = 16`.

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5], k = 2`
- Output: `0`
- Explanation: Every value occurs once, so no frequency is divisible by `2` and the sum is `0`.

**Example 3**

- Input: `nums = [4, 4, 4, 1, 2, 3], k = 3`
- Output: `12`
- Explanation:

  - `1`, `2`, and `3` each occur once.
  - `4` occurs three times, so its frequency is divisible by `3`.

  All three copies of `4` contribute, giving `4 + 4 + 4 = 12`.
