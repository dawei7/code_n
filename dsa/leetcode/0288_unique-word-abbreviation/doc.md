# Unique Word Abbreviation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 288 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-word-abbreviation/) |

## Problem Description
### Goal
Construct a `ValidWordAbbr` index from a dictionary of words. A standard abbreviation keeps short words unchanged; for longer words it combines the first character, the count of omitted middle characters, and the last character. Different words can therefore share one abbreviation.

For `isUnique(word)`, return `True` when no distinct dictionary word has the same abbreviation as the query. It is also unique when all dictionary entries with that abbreviation are exactly the query word itself, including repeated copies. Return `False` when any different word collides. Process multiple queries against the same indexed dictionary without changing its contents.

### Function Contract
**Inputs**

- `dictionary`: words used to construct the abbreviation index
- `words`: offline app queries passed to `isUnique`

**Return value**

One boolean per query. Native `ValidWordAbbr(dictionary).isUnique(word)` is true when no distinct dictionary word shares the query abbreviation.

### Examples
**Example 1**

- Input: `dictionary = ["deer","door","cake","card"], words = ["dear","cart","cane","make"]`
- Output: `[false,true,false,true]`

**Example 2**

- Input: `dictionary = ["hello"], words = ["hello"]`
- Output: `[true]`

**Example 3**

- Input: `dictionary = ["a","a"], words = ["a","b"]`
- Output: `[true,true]`
