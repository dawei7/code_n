# Check if a String Is an Acronym of Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2828 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [check-if-a-string-is-an-acronym-of-words](https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/) |

## Problem Description & Examples
### Goal
Determine whether a given string is a valid acronym for a provided list of words. An acronym is formed by concatenating the first character of each word in the list, in the exact order they appear.

### Function Contract
**Inputs**

- `words`: A list of strings (`List[str]`) representing the sequence of words.
- `s`: A string (`str`) representing the potential acronym.

**Return value**

- `bool`: Returns `True` if the first character of every word in `words` forms the string `s` in sequence, otherwise returns `False`.

### Examples
**Example 1**

- Input: `words = ["alice","bob","charlie"], s = "abc"`
- Output: `True`

**Example 2**

- Input: `words = ["an","apple"], s = "a"`
- Output: `False`

**Example 3**

- Input: `words = ["never","gonna","give","up","on","you"], s = "ngguoy"`
- Output: `True`

---

## Underlying Base Algorithm(s)
The problem is solved using a linear scan (iteration). We compare the length of the input list with the length of the string to perform an early exit, then iterate through the list to verify that the first character of each word matches the corresponding character in the string.

---

## Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the number of words in the list. We iterate through the list exactly once.
- **Space Complexity**: `O(1)`, as we only use a constant amount of extra space for pointers and comparisons, assuming the input string `s` is not modified.
