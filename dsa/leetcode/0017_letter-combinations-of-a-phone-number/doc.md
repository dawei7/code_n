# Letter Combinations of a Phone Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 17 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) |

## Problem Description
### Goal
The digits `2` through `9` carry their conventional telephone-keypad letter groups: `abc`, `def`, `ghi`, `jkl`, `mno`, `pqrs`, `tuv`, and `wxyz`. Given a string containing only those digits, choose exactly one mapped letter for each position.

Return every possible letter string formed by those choices while preserving the order of the input digits. Each Cartesian-product combination must appear exactly once, and the answers may be returned in any order. If the input digit string is empty, there is no nonempty selection to produce, so return an empty list.

### Function Contract
**Inputs**

- `digits`: `str` containing only characters `2` through `9`

**Return value**

A `List[str]` containing each possible letter combination exactly once.

### Examples
**Example 1**

- Input: `digits = "23"`
- Output: `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`

**Example 2**

- Input: `digits = ""`
- Output: `[]`

**Example 3**

- Input: `digits = "2"`
- Output: `["a", "b", "c"]`
