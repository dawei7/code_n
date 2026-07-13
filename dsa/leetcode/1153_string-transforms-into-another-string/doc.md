# String Transforms Into Another String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1153 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [string-transforms-into-another-string](https://leetcode.com/problems/string-transforms-into-another-string/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/string-transforms-into-another-string/).

### Goal
Decide whether `str1` can be transformed into `str2` by repeatedly choosing one lowercase letter and changing all of its current occurrences into another lowercase letter.

### Function Contract
**Inputs**

- `str1`: Starting lowercase string.
- `str2`: Desired lowercase string of the same length.

**Return value**

Boolean indicating whether the transformation is possible.

### Examples
**Example 1**

- Input: `str1 = "aabcc"`, `str2 = "ccdee"`
- Output: `true`

**Example 2**

- Input: `str1 = "leetcode"`, `str2 = "codeleet"`
- Output: `false`

**Example 3**

- Input: `str1 = "abcdefghijklmnopqrstuvwxyz"`, `str2 = "bcdefghijklmnopqrstuvwxyza"`
- Output: `false`

---

## Solution
### Approach
Each source character must always map to one target character, so first build that mapping and reject contradictions.

If the strings are already equal, no conversion is needed. Otherwise, cycles can only be broken if at least one lowercase letter is unused in `str2`, giving a temporary spare letter. Therefore, after the mapping is consistent, the answer is true exactly when `str2` does not use all 26 letters.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the string length.
- **Space Complexity**: `O(1)`, since the alphabet size is fixed.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
