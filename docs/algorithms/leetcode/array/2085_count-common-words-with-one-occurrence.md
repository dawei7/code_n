# Count Common Words With One Occurrence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2085 |
| Difficulty | Easy |
| Topics | Array, Hash Table, String, Counting |
| Official Link | [count-common-words-with-one-occurrence](https://leetcode.com/problems/count-common-words-with-one-occurrence/) |

## Problem Description & Examples
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

## Underlying Base Algorithm(s)
Count word frequencies in both arrays, then sum words whose count is exactly one in both maps.

---

## Complexity Analysis
- **Time Complexity**: `O(n + m)`
- **Space Complexity**: `O(n + m)`
