# Determine if Two Strings Are Close

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1657 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/determine-if-two-strings-are-close/) |

## Problem Description
### Goal
Two strings are close when either can be transformed into the other by repeating two operations. The first operation swaps any two positions, allowing arbitrary reordering. The second chooses two character values already present in the string and exchanges them everywhere: every occurrence of the first becomes the second, and every occurrence of the second becomes the first.

Given lowercase strings `word1` and `word2`, determine whether these operations can make them equal. A global character exchange cannot create a previously absent character and moves an entire occurrence count from one character label to another.

### Function Contract
**Inputs**

- `word1`: a lowercase English string of length between 1 and $10^5$.
- `word2`: another lowercase English string in the same length range.

Let $N=\lvert\texttt{word1}\rvert+\lvert\texttt{word2}\rvert$.

**Return value**

Return `true` if the strings are close under any sequence of the two allowed operations; otherwise return `false`.

### Examples
**Example 1**

- Input: `word1 = "abc", word2 = "bca"`
- Output: `true`

Position swaps alone can reorder one string into the other.

**Example 2**

- Input: `word1 = "a", word2 = "aa"`
- Output: `false`

Neither operation changes string length.

**Example 3**

- Input: `word1 = "cabbba", word2 = "abbccc"`
- Output: `true`

The strings use the same characters and have the same multiset of occurrence counts, so global exchanges can reassign those counts to the required labels before reordering.
