# Implement Magic Dictionary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 676 |
| Difficulty | Medium |
| Topics | Hash Table, String, Depth-First Search, Design, Trie |
| Official Link | [LeetCode](https://leetcode.com/problems/implement-magic-dictionary/) |

## Problem Description
### Goal
Design a `MagicDictionary` initialized with a list of distinct lowercase words through `buildDict(dictionary)`. For each `search(searchWord)` call, determine whether changing exactly one character of the query can make it equal to a stored word.

Return `True` only when such a one-position replacement exists. The replacement preserves the query's length and every other character, so insertion, deletion, swapping positions, or changing more than one character does not qualify. An exact stored word also returns `False` unless a different stored word of the same length is exactly one character away.

### Function Contract
**Inputs**

- `operations`: constructor, `buildDict`, and `search` calls in execution order
- `arguments`: the argument list paired with each operation; `buildDict` receives a word list and each `search` receives one word

**Return value**

- A result list aligned with the operations: `null` for construction and dictionary building, and a boolean for each search

### Examples
**Example 1**

- Input: `buildDict(["hello","leetcode"]); search("hello")`
- Output: `false`

**Example 2**

- Input: `buildDict(["hello","leetcode"]); search("hhllo")`
- Output: `true`

**Example 3**

- Input: `buildDict(["hello","leetcode"]); search("hell")`
- Output: `false`
