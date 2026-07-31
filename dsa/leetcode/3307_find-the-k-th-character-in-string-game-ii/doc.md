# Find the K-th Character in String Game II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3307 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Bit Manipulation, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/) |

## Problem Description

### Goal

Alice begins with `word = "a"` and performs every value in the binary array `operations` from left to right. Operation `0` appends an unchanged copy of the current word. Operation `1` instead makes a copy in which every letter advances once through the English alphabet, with `z` wrapping to `a`, and appends that transformed copy to the unchanged original.

Each operation therefore doubles the word's length. Given a positive one-based position `k`, determine the character occupying that position after the full sequence has been applied. The input guarantees that the final word is long enough, even though constructing it explicitly may be impossible because `k` can be as large as $10^{14}$.

### Function Contract

**Inputs**

- `k`: The one-based character position to inspect, where $1\leq k\leq10^{14}$.
- `operations`: An array of between 1 and 100 integers, each equal to `0` or `1`.

After all operations, the generated word is guaranteed to contain at least `k` characters.

**Return value**

Return the single lowercase English character at position `k` in the final word.

### Examples

**Example 1**

- Input: `k = 5, operations = [0, 0, 0]`
- Output: `"a"`

Every operation copies the word unchanged, producing `"aaaaaaaa"` after three steps.

**Example 2**

- Input: `k = 10, operations = [0, 1, 0, 1]`
- Output: `"b"`

The successive words are `"aa"`, `"aabb"`, `"aabbaabb"`, and `"aabbaabbbbccbbcc"`; its tenth character is `b`.
