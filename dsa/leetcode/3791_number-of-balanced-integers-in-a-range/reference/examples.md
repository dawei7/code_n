## Examples

**Example 1**

- Input: `low = 1, high = 100`
- Output: `9`
- Explanation:
  - The balanced integers in the range are `11`, `22`, `33`, `44`, `55`, `66`, `77`, `88`, and `99`.
  - There are `9` such integers.

**Example 2**

- Input: `low = 120, high = 129`
- Output: `1`
- Explanation:
  - Only `121` is balanced: its even-position digit sum is `2`, and its odd-position sum is `1 + 1 = 2`.

**Example 3**

- Input: `low = 1234, high = 1234`
- Output: `0`
- Explanation:
  - For `1234`, the odd-position sum is `1 + 3 = 4`, while the even-position sum is `2 + 4 = 6`.
  - The sums differ, so `1234` is not balanced.
