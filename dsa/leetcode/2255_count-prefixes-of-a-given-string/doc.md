# Count Prefixes of a Given String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2255 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-prefixes-of-a-given-string](https://leetcode.com/problems/count-prefixes-of-a-given-string/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-prefixes-of-a-given-string/).

### Goal
Count words that are prefixes of a given string. Duplicate words count separately.

### Function Contract
**Inputs**

- `words`: a list of lowercase words.
- `s`: the string whose prefixes are tested.

**Return value**

The number of word occurrences that match the beginning of `s`.

### Examples
**Example 1**

- Input: `words = ["a", "b", "c", "ab", "bc", "abc"]`, `s = "abc"`
- Output: `3`

**Example 2**

- Input: `words = ["a", "a"]`, `s = "aa"`
- Output: `2`

**Example 3**

- Input: `words = ["hello", "hell", "world"]`, `s = "hello"`
- Output: `2`

---

## Solution
### Approach
Scan the words and increment the result whenever `s` starts with the current word. A word longer than `s` automatically fails.

### Complexity Analysis
- **Time Complexity**: `O(L)`, where `L` is the total number of compared characters
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
