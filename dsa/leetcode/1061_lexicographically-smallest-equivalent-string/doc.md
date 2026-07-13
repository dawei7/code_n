# Lexicographically Smallest Equivalent String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1061 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Union-Find |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [lexicographically-smallest-equivalent-string](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/).

### Goal
Pairs of characters from `s1` and `s2` define equivalence classes over lowercase letters. Replace each character in `baseStr` with the smallest character in its equivalence class to create the lexicographically smallest possible string.

### Function Contract
**Inputs**

- `s1`: First string of equivalence-pair characters.
- `s2`: Second string of equivalence-pair characters.
- `baseStr`: String to transform.

**Return value**

Lexicographically smallest equivalent version of `baseStr`.

### Examples
**Example 1**

- Input: `s1 = "parker", s2 = "morris", baseStr = "parser"`
- Output: `"makkek"`

**Example 2**

- Input: `s1 = "hello", s2 = "world", baseStr = "hold"`
- Output: `"hdld"`

**Example 3**

- Input: `s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"`
- Output: `"aauaaaaada"`

---

## Solution
### Approach
Use union-find over the 26 lowercase letters. When merging two letters, make the representative of the merged set be the smaller representative. After processing all equivalence pairs, each character in `baseStr` maps to the representative of its set.

Because the representative is always the smallest available letter in the component, replacing every character this way gives the lexicographically smallest string.

### Complexity Analysis
- **Time Complexity**: `O(len(s1) + len(baseStr))`, with a tiny constant alphabet.
- **Space Complexity**: `O(1)`, because the union-find structure has 26 entries.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
