# Remove Vowels from a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1119 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [remove-vowels-from-a-string](https://leetcode.com/problems/remove-vowels-from-a-string/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/remove-vowels-from-a-string/).

### Goal
Return a copy of the input string with every lowercase vowel removed.

### Function Contract
**Inputs**

- `s`: Lowercase English string.

**Return value**

String formed by deleting all `a`, `e`, `i`, `o`, and `u` characters from `s`.

### Examples
**Example 1**

- Input: `s = "leetcodeisacommunityforcoders"`
- Output: `"ltcdscmmntyfrcdrs"`

**Example 2**

- Input: `s = "aeiou"`
- Output: `""`

**Example 3**

- Input: `s = "rhythm"`
- Output: `"rhythm"`

---

## Solution
### Approach
Scan the string and append each character that is not in the vowel set. Joining those kept characters produces the result.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of `s`.
- **Space Complexity**: `O(n)` for the returned string.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
