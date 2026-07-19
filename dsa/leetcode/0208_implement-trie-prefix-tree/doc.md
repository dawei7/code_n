# Implement Trie (Prefix Tree)

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 208 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Design, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/) |

## Problem Description
### Goal
Implement a prefix tree that stores lowercase words over a sequence of operations. `insert(word)` adds the complete word to the structure; inserting one word must also make its character prefixes navigable without automatically treating those prefixes as inserted words.

`search(word)` returns whether that exact complete word has previously been inserted, while `startsWith(prefix)` returns whether at least one inserted word begins with the supplied prefix. Repeated insertions do not change query truth, and words sharing prefixes must coexist without overwriting one another. Process all commands against the same persistent trie state, producing boolean results only for the two query operations.

### Function Contract
**Inputs**

- `operations`: app-local commands `["insert", value]`, `["search", value]`, or `["startsWith", value]`

**Return value**

Boolean results for query operations in command order; insertion produces no result.

### Examples
**Example 1**

- Operations: insert `apple`, search `apple`
- Output: `[True]`

**Example 2**

- Operations: insert `apple`, search `app`, query prefix `app`
- Output: `[False, True]`

**Example 3**

- Queries on an empty trie
- Output: `False` for each query
