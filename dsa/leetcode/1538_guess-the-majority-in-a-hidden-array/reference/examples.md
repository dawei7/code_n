## Examples

**Example 1**

- **Input:** `nums = [0, 0, 1, 0, 1, 1, 1, 1]`
- **Output:** `5`
- **Explanation:** Ones occur 5 times (indices 2, 4, 5, 6, 7) and zeros occur 3 times (indices 0, 1, 3). Ones form the majority, so returning any index of 1, such as 5, is valid.

**Example 2**

- **Input:** `nums = [0, 0, 1, 1, 0]`
- **Output:** `0`
- **Explanation:** Zeros occur 3 times (indices 0, 1, 4) and ones occur 2 times (indices 2, 3). Zeros form the majority, and index 0 contains a zero.

**Example 3**

- **Input:** `nums = [1, 0, 1, 0, 1, 0, 1, 0]`
- **Output:** `-1`
- **Explanation:** Each bit value occurs 4 times. Since there is no majority bit, the return value is -1.
