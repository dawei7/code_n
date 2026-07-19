# Change Minimum Characters to Satisfy One of Three Conditions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1737 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Counting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/) |

## Problem Description

### Goal

The nonempty strings `a` and `b` contain only lowercase English letters. One operation may replace any one character in either string with any lowercase letter.

Find the minimum operations needed to make at least one of three conditions true: every character in `a` is strictly alphabetically smaller than every character in `b`; every character in `b` is strictly smaller than every character in `a`; or both strings together contain only one distinct letter. Either string may contain up to $10^5$ characters.

### Function Contract

**Inputs**

- `a`: a nonempty lowercase string.
- `b`: another nonempty lowercase string.

Let $N = \lvert a \rvert + \lvert b \rvert$.

**Return value**

- Return the minimum number of single-character replacements needed to satisfy at least one allowed condition.

### Examples

**Example 1**

- Input: `a = "aba", b = "caa"`
- Output: `2`
- Explanation: Changing `b` to `"ccc"` satisfies the first condition, while making both strings all `a` also costs two.

**Example 2**

- Input: `a = "dabadd", b = "cda"`
- Output: `3`
- Explanation: Changing `b` to `"eee"` makes every letter in `a` strictly smaller than every letter in `b`.

**Example 3**

- Input: `a = "aaaa", b = "bbbb"`
- Output: `0`
- Explanation: The first strict-order condition already holds.
