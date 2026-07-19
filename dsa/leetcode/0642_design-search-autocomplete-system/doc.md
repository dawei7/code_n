# Design Search Autocomplete System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 642 |
| Difficulty | Hard |
| Topics | String, Depth-First Search, Design, Trie, Sorting, Heap (Priority Queue), Data Stream |
| Official Link | [LeetCode](https://leetcode.com/problems/design-search-autocomplete-system/) |

## Problem Description
### Goal
Design a search autocomplete system initialized with historical sentences and the number of times each sentence was previously entered. As a user types lowercase letters or spaces, maintain the complete current prefix and return up to three historical sentences that begin with it.

Rank matching sentences by decreasing historical frequency and then by ASCII lexicographical order when frequencies tie. The character `#` finishes the current sentence: add one to that sentence's frequency, clear the prefix for the next search, and return no suggestions. Each ordinary input character extends rather than replaces the prefix established by earlier calls.

### Function Contract
**Inputs**

- `operations`: a sequence beginning with `AutocompleteSystem`, followed by `input` calls
- `arguments`: constructor sentence/frequency arrays, then one typed character per call
- Ordinary lowercase letters and spaces extend the current prefix
- `#` finishes the current sentence, increments its historical frequency, resets the prefix, and returns no suggestions

**Return value**

- Each ordinary input returns at most three matching sentences ordered by descending frequency, then lexicographically for equal frequencies
- Construction returns null and `#` returns an empty list

### Examples
**Example 1**

- Input history: `"i love you"` five times, `"island"` three times, and two other `i` sentences twice; type `i`
- Output: `["i love you","island","i love leetcode"]`

**Example 2**

- Input: continue the same prefix with a space
- Output: `["i love you","i love leetcode"]`

**Example 3**

- Input: type a previously unseen sentence, terminate it with `#`, then type its first character again
- Output: the learned sentence can now appear among matching suggestions
