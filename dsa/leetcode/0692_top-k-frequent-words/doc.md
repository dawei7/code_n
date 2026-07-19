# Top K Frequent Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 692 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Trie, Sorting, Heap (Priority Queue), Bucket Sort, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/top-k-frequent-words/) |

## Problem Description
### Goal
Given an array of strings `words` and an integer `k`, count how often every distinct word occurs and select the `k` most frequent words.

Return the selected words sorted from highest frequency to lowest. When two words have the same frequency, place the lexicographically smaller word first. The output contains exactly `k` distinct words; repeated occurrences affect frequency but do not appear as duplicate output entries.

### Function Contract
**Inputs**

- `words`: a nonempty list of lowercase words
- `k`: the number of distinct ranked words to return

**Return value**

- The top `k` distinct words ordered by decreasing count and then increasing lexical value

### Examples
**Example 1**

- Input: `words = ["i","love","leetcode","i","love","coding"], k = 2`
- Output: `["i","love"]`

**Example 2**

- Input: `words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4`
- Output: `["the","is","sunny","day"]`

**Example 3**

- Input: `words = ["b","a","c","b","a","c"], k = 2`
- Output: `["a","b"]`
