# Count the Number of Vowel Strings in Range

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2586 |
| Difficulty | Easy |
| Topics | Array, String, Counting |
| Official Link | [count-the-number-of-vowel-strings-in-range](https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/) |

## Problem Description & Examples
### Goal
Given a list of strings and a specified inclusive index range [left, right], determine how many strings within that range start and end with a vowel (a, e, i, o, u).

### Function Contract
**Inputs**

- `words`: A list of strings consisting of lowercase English letters.
- `left`: An integer representing the starting index of the range.
- `right`: An integer representing the ending index of the range.

**Return value**

- An integer representing the count of strings that satisfy the vowel condition.

### Examples
**Example 1**

- Input: `words = ["are","amy","u"], left = 0, right = 2`
- Output: `2`

**Example 2**

- Input: `words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4`
- Output: `3`

**Example 3**

- Input: `words = ["a","b","c","d","e"], left = 0, right = 4`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem utilizes a linear scan (iteration) over a subset of an array. By defining a set of vowels for O(1) lookup, we check the first and last character of each string within the specified bounds.

---

## Complexity Analysis
- **Time Complexity**: O(N), where N is the number of strings in the range [left, right]. Each string check is O(1) because we only inspect the first and last characters.
- **Space Complexity**: O(1), as we only use a constant amount of extra space for the vowel set and the counter.
