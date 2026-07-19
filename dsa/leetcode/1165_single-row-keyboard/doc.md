# Single-Row Keyboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1165 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/single-row-keyboard/) |

## Problem Description

### Goal

A special keyboard places all $26$ lowercase English letters in one row. The string `keyboard` gives their left-to-right layout at indices `0` through `25`, with every letter appearing exactly once. A finger begins at index `0`.

To type a character, move the finger from its current index $i$ to that character's index $j$. This movement takes $\lvert i-j \rvert$ time, and the finger remains at $j$ for the next character. Given `word`, calculate the total time required to type the entire string with that one finger.

### Function Contract

**Inputs**

- `keyboard`: A length-$26$ permutation of the lowercase English letters.
- `word`: A lowercase English string of length $m$, where $1 \le m \le 10^4$.

**Return value**

- The sum of the finger-movement times needed to type `word`, starting from keyboard index `0`.

### Examples

**Example 1**

- Input: `keyboard = "abcdefghijklmnopqrstuvwxyz"`, `word = "cba"`
- Output: `4`

The finger moves from index `0` to `2`, then to `1`, and finally back to `0`, costing `2 + 1 + 1`.

**Example 2**

- Input: `keyboard = "pqrstuvwxyzabcdefghijklmno"`, `word = "leetcode"`
- Output: `73`
