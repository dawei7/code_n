## Examples

**Example 1**

- Input: `words = ["leetcode","leetcode","codeforces"]`
- Output: `3`
- Explanation: The words at indices `0` and `2` differ. Their distance is `2 - 0 + 1 = 3`, and no pair can span farther.

**Example 2**

- Input: `words = ["a","b","c","a","a"]`
- Output: `4`
- Explanation: Indices `1` and `4` contain unequal words and have distance `4 - 1 + 1 = 4`, the largest attainable value.

**Example 3**

- Input: `words = ["z","z","z"]`
- Output: `0`
- Explanation: Every entry contains the same word, so there is no valid unequal pair and the answer is zero.
