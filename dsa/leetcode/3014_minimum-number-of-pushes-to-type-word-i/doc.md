# Minimum Number of Pushes to Type Word I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3014 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/) |

## Problem Description

### Goal

A telephone keypad has eight usable keys, numbered from `2` through `9`. You may remap the lowercase English letters among those keys. Each letter must belong to exactly one key, while a key may hold any number of letters.

A letter placed first on its key costs one push, a letter placed second costs two pushes, and so on. Given a word whose letters are all distinct, choose a remapping that minimizes the total number of key pushes needed to type the entire word.

Keys `0`, `1`, `*`, and `#` do not receive letters. Return the minimum total number of pushes.

### Function Contract

**Inputs**

- `word`: A string of distinct lowercase English letters.

The source constraints guarantee $1 \le \lvert\texttt{word}\rvert \le 26$.

**Return value**

- The minimum number of pushes required after choosing the best valid remapping.

### Examples

**Example 1**

- Input: `word = "abcde"`
- Output: `5`
- Explanation: Each of the five letters can occupy the first position on a different key, so every letter costs one push.

**Example 2**

- Input: `word = "xycdefghij"`
- Output: `12`
- Explanation: Eight letters use the eight one-push positions. The remaining two letters each use a two-push position, giving $8+2+2=12$.

**Example 3**

- Input: `word = "abcdefghijklmnop"`
- Output: `24`
- Explanation: The first eight letters cost one push each and the other eight cost two pushes each.
