# Sentence Screen Fitting

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 418 |
| Difficulty | Medium |
| Topics | Array, String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/sentence-screen-fitting/) |

## Problem Description
### Goal
Given an ordered list of words, repeatedly write the sentence on a screen with `rows` rows and `cols` character columns. Words must remain intact, appear in sentence order, and be separated by one space when adjacent on the same row.

When the next word does not fit in the current row, continue it at the beginning of the next row without carrying a leading space. After the last sentence word, begin another copy when space remains. Return the number of complete sentence repetitions placed after all rows are filled. Partial final copies do not count, and no word may be split across rows.

### Function Contract
**Inputs**

- `sentence`: the nonempty ordered list of words to repeat
- `rows`: the screen height
- `cols`: the number of character columns per row

**Return value**

- Return the number of complete sentence repetitions placed after filling rows from left to right with one space between adjacent words.

### Examples
**Example 1**

- Input: `sentence = ["hello","world"], rows = 2, cols = 8`
- Output: `1`

**Example 2**

- Input: `sentence = ["a","bcd","e"], rows = 3, cols = 6`
- Output: `2`

**Example 3**

- Input: `sentence = ["i","had","apple","pie"], rows = 4, cols = 5`
- Output: `1`
