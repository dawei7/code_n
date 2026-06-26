# Count the Number of Consistent Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1684 |
| Difficulty | Easy |
| Topics | Array, Hash Table, String, Bit Manipulation, Counting |
| Official Link | [count-the-number-of-consistent-strings](https://leetcode.com/problems/count-the-number-of-consistent-strings/) |

## Problem Description & Examples
### Goal
Count how many words use only characters from a given allowed character set.

### Function Contract
**Inputs**

- `allowed`: a string of distinct lowercase letters.
- `words`: a list of lowercase words.

**Return value**

Return the number of consistent words.

### Examples
**Example 1**

- Input: `allowed = "ab", words = ["ad","bd","aaab","baa","badab"]`
- Output: `2`

**Example 2**

- Input: `allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]`
- Output: `7`

**Example 3**

- Input: `allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]`
- Output: `4`

---

## Underlying Base Algorithm(s)
Convert `allowed` to a set or bitmask. For each word, verify every character is present in the allowed representation and count the words that pass.

---

## Complexity Analysis
- **Time Complexity**: `O(total characters in words)`
- **Space Complexity**: `O(1)` because the alphabet size is fixed
