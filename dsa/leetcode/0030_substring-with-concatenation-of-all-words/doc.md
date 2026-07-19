# Substring with Concatenation of All Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 30 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) |

## Problem Description
### Goal
You are given a string `s` and a nonempty list `words` whose entries all have the same positive length. Form a target block by concatenating every listed word exactly once in any ordering, with no characters inserted between words.

Return every zero-based index where a substring of `s` equals one such complete block. Duplicate words in the list are separate required occurrences, so a candidate must match their exact multiplicities. Valid blocks may overlap, and the returned start indices may appear in any order; return an empty list when none exists.

### Function Contract
**Inputs**

- `s`: `str`
- `words`: non-empty `List[str]` of equal-length strings

**Return value**

A `List[int]` containing all valid start indices in any order.

### Examples
**Example 1**

- Input: `s = "barfoothefoobarman", words = ["foo", "bar"]`
- Output: `[0, 9]`

**Example 2**

- Input: `s = "wordgoodgoodgoodbestword", words = ["word", "good", "best", "word"]`
- Output: `[]`

**Example 3**

- Input: `s = "barfoofoobarthefoobarman", words = ["bar", "foo", "the"]`
- Output: `[6, 9, 12]`
