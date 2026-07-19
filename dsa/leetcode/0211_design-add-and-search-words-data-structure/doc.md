# Design Add and Search Words Data Structure

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 211 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Depth-First Search, Design, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-add-and-search-words-data-structure/) |

## Problem Description
### Goal
Implement a stateful dictionary that receives lowercase words through `addWord(word)` and answers full-pattern queries through `search(pattern)`. Added words remain available for all later operations, and words with common prefixes or different lengths must coexist independently.

Within a search pattern, a lowercase letter must match that exact character, while each dot `.` matches any one character. Dots do not match zero or several characters, so a successful word must have exactly the same length as the pattern. Return whether at least one stored word matches the entire pattern; matching only a prefix is insufficient. Produce booleans for searches and no result for additions.

### Function Contract
**Inputs**

- `operations`: app commands `["addWord", word]` and `["search", pattern]`

**Return value**

Boolean results for searches in command order.

### Examples
**Example 1**

- Add `bad`, `dad`, `mad`; search `.ad`
- Output: `True`

**Example 2**

- Search `pad` after those additions
- Output: `False`

**Example 3**

- Search `b..` after adding `bad`
- Output: `True`
