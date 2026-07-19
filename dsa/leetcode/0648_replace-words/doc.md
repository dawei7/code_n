# Replace Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 648 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Trie |
| Official Link | [LeetCode](https://leetcode.com/problems/replace-words/) |

## Problem Description
### Goal
In English, a root can be followed by additional letters to form a longer derivative. Given a dictionary of roots and a sentence whose words are separated by spaces, replace each derivative by a dictionary root that forms its prefix.

If more than one root can replace the same word, use the root with the shortest length. Leave a word unchanged when no dictionary root is its prefix, preserve the original word order, and return the transformed sentence with its single-space separation intact.

### Function Contract
**Inputs**

- `dictionary`: a list of lowercase root words
- `sentence`: lowercase words separated by single spaces

**Return value**

- The transformed sentence with original word order and single-space separation
- If several roots prefix the same word, the shortest root must be used

### Examples
**Example 1**

- Input: `dictionary = ["cat","bat","rat"]`, `sentence = "the cattle was rattled by the battery"`
- Output: `"the cat was rat by the bat"`

**Example 2**

- Input: `dictionary = ["a","b","c"]`, `sentence = "aadsfasf absbs bbab cadsfafs"`
- Output: `"a a b c"`

**Example 3**

- Input: `dictionary = ["c","cat"]`, `sentence = "cattle"`
- Output: `"c"`
