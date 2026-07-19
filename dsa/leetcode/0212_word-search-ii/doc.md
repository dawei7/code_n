# Word Search II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 212 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Backtracking, Trie, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/word-search-ii/) |

## Problem Description
### Goal
Given a nonempty character board and a list of distinct candidate words, determine which words can be traced through the grid. Consecutive letters in a trace must occupy horizontally or vertically adjacent cells, and a cell cannot be used more than once within the same word.

Return every candidate that has at least one valid path, including each word at most once even when several paths spell it. Result order does not matter. Diagonal moves and jumps are forbidden, but cells may be reused independently while searching for different words. A matching prefix is not enough: the full candidate must be consumed by one continuous path.

### Function Contract
**Inputs**

- `board`: a nonempty character matrix
- `words`: distinct candidate words

**Return value**

Every candidate found on the board, returned once.

### Examples
**Example 1**

- Board: `[[o,a,a,n],[e,t,a,e],[i,h,k,r],[i,f,l,v]]`
- Words: `oath, pea, eat, rain`
- Output: `oath, eat`

**Example 2**

- A path would need one cell twice
- Output: that word is absent

**Example 3**

- No candidate begins with a board path
- Output: `[]`
