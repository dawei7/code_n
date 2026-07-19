# Maximum Number of Non-Overlapping Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1520 |
| Difficulty | Hard |
| Topics | Hash Table, String, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/) |

## Problem Description
### Goal

Choose a collection of nonempty, pairwise non-overlapping substrings from a lowercase string `s`. Whenever a selected substring contains a character, it must contain every occurrence of that character in the entire source string; a substring cannot capture only some copies of one of its letters.

First maximize how many substrings are selected. Among collections attaining that maximum count, minimize the sum of their lengths. The minimum-total-length optimum is guaranteed to be unique, although its substrings may be returned in any order.

### Function Contract
**Inputs**

- `s`: A lowercase English string of length $n$, where $1 \leq n \leq 10^5$.

**Return value**

Return the unique minimum-total-length collection among all maximum-cardinality collections of valid, disjoint substrings. The app-local implementation returns them in left-to-right source order.

### Examples
**Example 1**

- Input: `s = "adefaddaccc"`
- Output: `["e", "f", "ccc"]`
- Explanation: Selecting `e` and `f` separately is better than the combined `ef`, and the independent `ccc` interval adds a third substring.

**Example 2**

- Input: `s = "abbaccd"`
- Output: `["bb", "cc", "d"]`
- Explanation: `abba` is valid, but replacing it with `bb` preserves three selected substrings while reducing total length.

**Example 3**

- Input: `s = "abcd"`
- Output: `["a", "b", "c", "d"]`
- Explanation: Every character occurs once, so each single-character substring is independently valid.
