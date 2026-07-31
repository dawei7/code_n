# Find the K-th Character in String Game I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3304 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Bit Manipulation, Recursion, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/) |

## Problem Description

### Goal

Begin with `word = "a"`. In every operation, make a transformed copy of the entire current word by replacing each letter with the next English letter, wrapping `z` to `a`, and append that copy to the unchanged original word. Thus one operation changes `"a"` into `"ab"`, and the next changes it into `"abbc"`.

Repeat until the word contains at least `k` characters, then return its $k$-th character using one-based indexing. The requested position is at most 500, so the relevant generated letters never reach the alphabet wraparound.

### Function Contract

**Inputs**

- `k`: A one-based position from 1 through 500 in the infinite construction.

**Return value**

- The lowercase character at position `k` after enough doubling operations.

### Examples

**Example 1**

- Input: `k = 5`
- Output: `"b"`
- Explanation: After three operations the word begins `"abbcbccd"`, whose fifth character is `b`.

**Example 2**

- Input: `k = 10`
- Output: `"c"`
- Explanation: The character at the tenth one-based position has been shifted twice from `a`.
