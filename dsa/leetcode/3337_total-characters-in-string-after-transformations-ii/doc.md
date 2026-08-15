# Total Characters in String After Transformations II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3337 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, Math, String, Dynamic Programming, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/) |

## Problem Description

### Goal

You are given a lowercase English string `s`, an integer `t`, and a 26-entry array `nums`. During one transformation, every character is replaced simultaneously. A letter with alphabet index $i$ is replaced by the next `nums[i]` consecutive letters, starting immediately after it rather than including the original letter.

Successors wrap around the alphabet: for example, three successors after `y` are `"zab"`. Apply this character-dependent rule exactly `t` times to the whole evolving string. Because the materialized string can become enormous, return only its final length modulo $10^9+7$.

### Function Contract

**Inputs**

- `s`: A nonempty lowercase English string of length $n$, where $1 \le n \le 10^5$.
- `t`: The exact number of transformations, where $1 \le t \le 10^9$.
- `nums`: A 26-entry integer list. For alphabet index $i$, `nums[i]` is between $1$ and $25$ and determines how many consecutive successor letters replace that character.

Let $A=26$ denote the fixed alphabet size.

**Return value**

- The transformed string's length after exactly `t` simultaneous transformations, reduced modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `s = "abcyy", t = 2, nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]`
- **Output:** `7`
- **Explanation:** The two simultaneous transformations produce `"bcdzz"` and then `"cdeabab"`.

#### Example 2

- **Input:** `s = "azbk", t = 1, nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]`
- **Output:** `8`
- **Explanation:** Each input character contributes two successors; wrapping makes `z` become `"ab"`.

#### Example 3

- **Input:** `s = "y", t = 1, nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1]`
- **Output:** `3`
- **Explanation:** The three consecutive successors of `y` are `"zab"`.
