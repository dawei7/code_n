## Examples

**Example 1**

- Input: `nums = [1,2,3]`
- Output: `3`
- Explanation: The full strength is `1 OR 2 OR 3 = 3`. The effective subsequences are:
  - Removing `[1,3]` leaves `[2]`, whose OR is `2`.
  - Removing `[2,3]` leaves `[1]`, whose OR is `1`.
  - Removing `[1,2,3]` leaves `[]`, whose OR is `0`.
  Thus, there are `3` effective subsequences.

**Example 2**

- Input: `nums = [7,4,6]`
- Output: `4`
- Explanation: The full strength is `7 OR 4 OR 6 = 7`. The effective subsequences are:
  - Removing `[7]` leaves `[4,6]`, whose OR is `6`.
  - Removing `[7,4]` leaves `[6]`, whose OR is `6`.
  - Removing `[7,6]` leaves `[4]`, whose OR is `4`.
  - Removing `[7,4,6]` leaves `[]`, whose OR is `0`.
  The total is therefore `4`.

**Example 3**

- Input: `nums = [8,8]`
- Output: `1`
- Explanation: The original OR is `8 OR 8 = 8`. Removing only one occurrence still leaves an `8`, so the sole effective subsequence is `[8,8]`; its removal leaves `[]` with OR `0`. Hence the answer is `1`.

**Example 4**

- Input: `nums = [2,2,1]`
- Output: `5`
- Explanation: The full strength is `2 OR 2 OR 1 = 3`. The effective subsequences are:
  - `[1]`, leaving `[2,2]` with OR `2`.
  - `[2,1]` using `nums[0]` and `nums[2]`, leaving `[2]` with OR `2`.
  - `[2,1]` using `nums[1]` and `nums[2]`, leaving `[2]` with OR `2`.
  - `[2,2]`, leaving `[1]` with OR `1`.
  - `[2,2,1]`, leaving `[]` with OR `0`.
  Therefore, the two index-distinct `[2,1]` choices contribute separately and the total is `5`.
