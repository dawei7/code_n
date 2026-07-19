# Make The String Great

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1544 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/make-the-string-great/) |

## Problem Description
### Goal
A string is considered good when it has no adjacent pair formed by the same English letter in opposite cases. In other words, a lowercase letter directly beside its uppercase version, in either order, makes the string invalid.

You may repeatedly remove any such adjacent pair. Continue until no invalid pair remains, then return the resulting good string. The input contains only uppercase and lowercase English letters, and the removal process is guaranteed to lead to a unique final string.

### Function Contract
**Inputs**

- `s`: a string of length $n$, where $1 \le n \le 100$, containing only uppercase and lowercase English letters.

**Return value**

The unique good string obtained after repeatedly deleting adjacent equal letters whose cases differ. The answer may be empty.

### Examples
**Example 1**

- Input: `s = "leEeetcode"`
- Output: `"leetcode"`
- Explanation: Removing the adjacent `"eE"` leaves a string with no opposite-case equal neighbors.

**Example 2**

- Input: `s = "abBAcC"`
- Output: `""`
- Explanation: Removing `"bB"` makes `"aA"` adjacent, and the final `"cC"` also disappears.

**Example 3**

- Input: `s = "s"`
- Output: `"s"`
- Explanation: A one-character string cannot contain an invalid adjacent pair.
