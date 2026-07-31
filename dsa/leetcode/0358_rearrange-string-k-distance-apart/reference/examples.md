## Examples

**Example 1**

- Input: `s = "aabbcc", k = 3`
- Output: `"abcabc"`
- Explanation: In this arrangement, consecutive copies of each letter occur three positions apart.

**Example 2**

- Input: `s = "aaabc", k = 3`
- Output: `""`
- Explanation: These character counts cannot be arranged while maintaining the required separation.

**Example 3**

- Input: `s = "aaadbbcc", k = 2`
- Output: `"abacabcd"`
- Explanation: Every repeated letter in the returned string is separated from its next occurrence by at least two positions.
