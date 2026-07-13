# Match Substring After Replacement

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2301 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, String, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [match-substring-after-replacement](https://leetcode.com/problems/match-substring-after-replacement/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/match-substring-after-replacement/).

### Goal
Determine whether `sub` can match some contiguous substring of `s` after independently replacing any characters of `sub` according to allowed directed mappings. Characters may also remain unchanged.

### Function Contract
**Inputs**

- `s`: the text to search.
- `sub`: the pattern.
- `mappings`: directed pairs `[old, new]` permitted when transforming pattern characters.

**Return value**

`true` if some aligned substring matches under the rules; otherwise `false`.

### Examples
**Example 1**

- Input: `s = "fool3e7bar"`, `sub = "leet"`, `mappings = [["e", "3"], ["t", "7"], ["t", "8"]]`
- Output: `true`

**Example 2**

- Input: `s = "fooleetbar"`, `sub = "f00l"`, `mappings = [["o", "0"]]`
- Output: `false`

**Example 3**

- Input: `s = "abc"`, `sub = "bc"`, `mappings = []`
- Output: `true`

---

## Solution
### Approach
Store allowed replacements as directed character pairs. Try every text window of `sub`'s length. An aligned position is valid when the characters are equal or the pair `(pattern_character, text_character)` is allowed; accept the first window valid at every position.

### Complexity Analysis
- **Time Complexity**: `O((|s| - |sub| + 1) * |sub|)`
- **Space Complexity**: `O(|mappings|)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
