# Unique Morse Code Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 804 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-morse-code-words/) |

## Problem Description

### Goal

International Morse Code maps each lowercase English letter to its fixed sequence of dots and dashes. Transform a word by replacing every letter with that code and concatenating the pieces without separators.

Given an array `words`, return the number of distinct Morse transformations produced. Different words can have the same concatenated representation and then count only once, while repeated input words do not create additional distinct transformations.

### Function Contract

**Inputs**

- `words`: a nonempty list of lowercase English words.

**Return value**

- The number of distinct Morse-code strings produced by the words.

### Examples

**Example 1**

- Input: `words = ["gin","zen","gig","msg"]`
- Output: `2`
- Explanation: `gin` and `zen` share one transformation, while `gig` and `msg` share another.

**Example 2**

- Input: `words = ["a","et"]`
- Output: `1`
- Explanation: Both words concatenate to `.-` because transformation boundaries do not preserve letter separators.

**Example 3**

- Input: `words = ["abc","def","ghi"]`
- Output: `3`
- Explanation: The three resulting Morse strings are different.
