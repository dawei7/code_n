## Examples

**Example 1**

- Input: `n = 2`
- Output: `[0, 1, 3, 2]`
- Explanation: The binary sequence is `[00, 01, 11, 10]`: `00 ↔ 01`, `01 ↔ 11`, `11 ↔ 10`, and the wraparound pair `10 ↔ 00` each differ in exactly one bit. Another valid answer is `[0, 2, 3, 1]`, whose binary forms `[00, 10, 11, 01]` likewise differ by one bit for `00 ↔ 10`, `10 ↔ 11`, `11 ↔ 01`, and `01 ↔ 00`.

**Example 2**

- Input: `n = 1`
- Output: `[0, 1]`
