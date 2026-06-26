# Maximum Score Words Formed by Letters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1255 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, Dynamic Programming, Backtracking, Bit Manipulation, Counting, Bitmask |
| Official Link | [maximum-score-words-formed-by-letters](https://leetcode.com/problems/maximum-score-words-formed-by-letters/) |

## Problem Description & Examples
### Goal
Choose a subset of words that can be formed from the available letters and maximizes the total letter score.

### Function Contract
**Inputs**

- `words`: candidate lowercase words.
- `letters`: available letters, each usable once.
- `score`: length-26 array where `score[i]` is the value of character `chr(ord("a") + i)`.

**Return value**

The maximum score achievable by any feasible subset of words.

### Examples
**Example 1**

- Input: `words = ["dog","cat","dad","good"]`, `letters = ["a","a","c","d","d","d","g","o","o"]`, `score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]`
- Output: `23`

**Example 2**

- Input: `words = ["xxxz","ax","bx","cx"]`, `letters = ["z","a","b","c","x","x","x"]`, `score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]`
- Output: `27`

**Example 3**

- Input: `words = ["leetcode"]`, `letters = ["l","e","t","c","o","d"]`, `score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Backtracking with frequency counts.

---

## Complexity Analysis
- **Time Complexity**: `O(2^w * alphabet)` where `w` is the number of words.
- **Space Complexity**: `O(w + alphabet)` recursion and count storage.
