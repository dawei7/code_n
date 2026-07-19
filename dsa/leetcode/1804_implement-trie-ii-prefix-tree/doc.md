# Implement Trie II (Prefix Tree)

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/implement-trie-ii-prefix-tree/) |
| Frontend ID | 1804 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Design, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Design a trie that stores a multiset of lowercase words. Inserting the same word repeatedly creates multiple occurrences rather than leaving a single membership flag. The structure must report both exact-word multiplicity and the number of stored words sharing a requested prefix.

It must also erase one occurrence of a supplied word. Every erase call is guaranteed to name a word currently present, possibly with other occurrences remaining. Erasing one word must update all of its prefix counts without changing unrelated words.

### Function Contract

**Inputs**

- `Trie()` creates an empty word multiset.
- `insert(word)` adds one occurrence of a nonempty lowercase word.
- `countWordsEqualTo(word)` returns the number of stored occurrences exactly equal to `word`.
- `countWordsStartingWith(prefix)` returns the number of stored occurrences whose words begin with `prefix`.
- `erase(word)` removes one occurrence; that occurrence is guaranteed to exist.
- At most $Q=3\cdot10^4$ method calls are made, and each word or prefix has length $L$ between 1 and 2000.
- Let $S$ be the number of character nodes created for all distinct stored prefixes.

**Return value**

- Construction, insertion, and erasure return no value.
- Each count method returns a nonnegative integer.
- In the app-local sequence interface, return one result per operation and use `null` for methods with no return value.

### Examples

**Example 1**

- Operations: `["Trie","insert","insert","countWordsEqualTo","countWordsStartingWith","erase","countWordsEqualTo"]`
- Arguments: `[[],["apple"],["apple"],["apple"],["app"],["apple"],["apple"]]`
- Output: `[null,null,null,2,2,null,1]`

Two equal insertions contribute two exact and prefix occurrences; one erase removes only one.

**Example 2**

- Operations: insert `"app"` and `"apple"`, erase `"app"`, then query exact `"app"` and prefix `"app"`
- Output: `0` and `1`

Removing the shorter word does not remove the longer word that passes through the same nodes.

**Example 3**

- Operations: insert `"apple"` and `"apply"`, then count prefix `"appl"` and exact word `"app"`
- Output: `2` and `0`

A path may be a shared prefix without representing a complete stored word.
