# Check If Two String Arrays are Equivalent

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1662 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-if-two-string-arrays-are-equivalent](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/).

### Goal
Check whether two arrays of string fragments concatenate to the same final
string.

### Function Contract
**Inputs**

- `word1`: first list of string fragments.
- `word2`: second list of string fragments.

**Return value**

`true` if both concatenations are equal; otherwise `false`.

### Examples
**Example 1**

- Input: `word1 = ["ab", "c"], word2 = ["a", "bc"]`
- Output: `true`

**Example 2**

- Input: `word1 = ["a", "cb"], word2 = ["ab", "c"]`
- Output: `false`

**Example 3**

- Input: `word1 = ["abc", "d", "defg"], word2 = ["abcddefg"]`
- Output: `true`

---

## Solution
### Approach
The simple method joins each fragment list and compares the two resulting
strings. A streaming two-pointer comparison can avoid building the full
concatenations, but both follow the same equality check.

### Complexity Analysis
- **Time Complexity**: `O(total characters)`.
- **Space Complexity**: `O(total characters)` when joining, or `O(1)` with streaming comparison.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
