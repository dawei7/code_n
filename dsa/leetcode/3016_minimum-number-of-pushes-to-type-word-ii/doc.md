# Minimum Number of Pushes to Type Word II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3016 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Greedy, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/) |

## Problem Description

### Goal

A telephone keypad has eight usable keys, numbered from `2` through `9`. You may replace their usual letter layout by assigning lowercase English letters to those keys. Every letter must be assigned to exactly one key, and a key may hold any number of letters.

Typing the first assigned letter on a key takes one push, the second takes two pushes, and each later position costs one additional push. Given a lowercase string `word`, whose letters may repeat, choose a valid remapping that minimizes the total number of pushes needed to type every character in order.

Keys `0`, `1`, `*`, and `#` do not receive letters. Return the minimum total push count.

### Function Contract

**Inputs**

- `word`: A nonempty string of lowercase English letters.

The source constraints allow $1 \le N \le 10^5$, where $N=\lvert\texttt{word}\rvert$.

**Return value**

- The minimum total number of key pushes after an optimal remapping.

### Examples

**Example 1**

- Input: `word = "abcde"`
- Output: `5`
- Explanation: The five used letters can each occupy a one-push position.

**Example 2**

- Input: `word = "xyzxyzxyzxyz"`
- Output: `12`
- Explanation: Only three letters occur, so each can be placed first on its own key and every character costs one push.

**Example 3**

- Input: `word = "abcdefghijklmnopqrstuvwxyz"`
- Output: `56`
- Explanation: Eight letters cost one push, eight cost two, eight cost three, and the final two cost four.
