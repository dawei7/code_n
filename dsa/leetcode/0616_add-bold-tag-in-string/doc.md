# Add Bold Tag in String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 616 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Trie, String Matching |
| Official Link | [LeetCode](https://leetcode.com/problems/add-bold-tag-in-string/) |

## Problem Description
### Goal
Given a string `s` and an array `words`, add $<b>$ and $</b>$ around every part of `s` that matches an occurrence of any word in the array. Matches may begin at any position, and all characters covered by at least one complete word occurrence must be bold.

Return the resulting string with the fewest necessary tag pairs. When covered intervals overlap or are consecutive, combine them into one bold region; leave every uncovered character unchanged. Empty gaps must not be invented, and a word that does not occur in `s` contributes no tags.

### Function Contract
**Inputs**

- `s`: the source string
- `words`: nonempty dictionary strings to locate in `s`

**Return value**

- `s` with maximal covered regions surrounded by bold tags
- Characters not covered by any word occurrence remain unchanged
- Overlapping and consecutive matches share one tag pair

### Examples
**Example 1**

- Input: `s = "abcxyz123"`, `words = ["abc", "123"]`
- Output: `"<b>abc</b>xyz<b>123</b>"`

**Example 2**

- Input: `s = "aaabbcc"`, `words = ["aaa", "aab", "bc"]`
- Output: `"<b>aaabbc</b>c"`
