# Shortest Common Supersequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1092 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [shortest-common-supersequence](https://leetcode.com/problems/shortest-common-supersequence/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/shortest-common-supersequence/).

### Goal
Return a shortest string that contains both `str1` and `str2` as subsequences. If multiple shortest answers exist, any one of them is valid.

### Function Contract
**Inputs**

- `str1`: First string.
- `str2`: Second string.

**Return value**

One shortest common supersequence of the two input strings.

### Examples
**Example 1**

- Input: `str1 = "abac", str2 = "cab"`
- Output: `"cabac"`

**Example 2**

- Input: `str1 = "aaaaaaaa", str2 = "aaaaaaaa"`
- Output: `"aaaaaaaa"`

**Example 3**

- Input: `str1 = "abc", str2 = "def"`
- Output: `"abcdef"`

---

## Solution
### Approach
Compute the longest common subsequence of `str1` and `str2`. The LCS gives the shared backbone that should appear only once in the supersequence. Walk through the LCS characters; before each shared character, append the unmatched characters from both strings, then append the shared character.

After the LCS is consumed, append the remaining suffixes of both strings. This creates a shortest common supersequence because it preserves both strings while sharing as much overlap as possible.

### Complexity Analysis
- **Time Complexity**: `O(m * n)`, where `m = len(str1)` and `n = len(str2)`.
- **Space Complexity**: `O(m * n)` for the LCS dynamic programming table.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
