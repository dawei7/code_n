## Examples

**Example 1**

- Input: `words = ["leetcode", "leetcode", "codeforces"]`
- Output: `3`
- Explanation: Positions `0` and `2` contain unequal words. Their inclusive distance is `2 - 0 + 1 = 3`, which is the largest possible span in this array.

**Example 2**

- Input: `words = ["a", "b", "c", "a", "a"]`
- Output: `4`
- Explanation: The words at positions `1` and `4` differ, and their distance is `4 - 1 + 1 = 4`. No valid pair has a larger distance.

**Example 3**

- Input: `words = ["z", "z", "z"]`
- Output: `0`
- Explanation: Every entry contains the same word, so no valid pair exists.
