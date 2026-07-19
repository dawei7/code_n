# Contains Duplicate

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 217 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/contains-duplicate/) |

## Problem Description
### Goal
Given an integer array `nums`, determine whether any value appears at least twice. Equal values count as duplicates regardless of how far apart their indices are or how many other values occur between them.

Return `True` when the array contains a repeated value and `False` when every element is distinct. Negative integers and zero follow the same equality rule as positive integers. An array with one element contains no duplicate pair, while a value appearing three or more times still produces the same boolean result rather than a count or a set of indices.

### Function Contract
**Inputs**

- `nums`: an integer list

**Return value**

`True` when a duplicate occurrence exists; otherwise `False`.

### Examples
**Example 1**

- Input: `[1,2,3,1]`
- Output: `True`

**Example 2**

- Input: `[1,2,3,4]`
- Output: `False`

**Example 3**

- Input: `[5,5]`
- Output: `True`
