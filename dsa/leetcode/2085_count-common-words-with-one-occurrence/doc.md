# Count Common Words With One Occurrence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2085 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-common-words-with-one-occurrence](https://leetcode.com/problems/count-common-words-with-one-occurrence/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-common-words-with-one-occurrence/).

### Goal
Count words that appear exactly once in each of two arrays.

### Function Contract
**Inputs**

- `words1`, `words2`: arrays of strings.

**Return value**

Return the number of words with frequency one in both arrays.

### Examples
**Example 1**

- Input: `words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]`
- Output: `2`

**Example 2**

- Input: `words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]`
- Output: `0`

**Example 3**

- Input: `words1 = ["a","ab"], words2 = ["a","a","a","ab"]`
- Output: `1`

---

## Solution
### Approach
Count word frequencies in both arrays, then sum words whose count is exactly one in both maps.

### Complexity Analysis
- **Time Complexity**: `O(n + m)`
- **Space Complexity**: `O(n + m)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
