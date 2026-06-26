# Stream of Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1032 |
| Difficulty | Hard |
| Topics | Array, String, Design, Trie, Data Stream |
| Official Link | [stream-of-characters](https://leetcode.com/problems/stream-of-characters/) |

## Problem Description & Examples
### Goal
Design a stream checker. After each queried character, return whether any configured word is a suffix of the stream seen so far.

### Function Contract
**Inputs**

- `words`: List[str] dictionary initialized once
- `letter`: str passed to each `query`

**Return value**

bool - whether the current stream ends with at least one dictionary word

### Examples
**Example 1**

- Input: `words = ["cd", "f", "kl"], queries = ["a","b","c","d"]`
- Output: `[False, False, False, True]`

**Example 2**

- Input: `words = ["cd", "f", "kl"], queries = ["f"]`
- Output: `[True]`

**Example 3**

- Input: `words = ["ab", "ba"], queries = ["a","b","a"]`
- Output: `[False, True, True]`

---

## Underlying Base Algorithm(s)
Reversed trie for suffix matching.

---

## Complexity Analysis
- **Time Complexity**: `O(L)` per query, where `L` is the maximum word length
- **Space Complexity**: `O(total dictionary characters + L)`
