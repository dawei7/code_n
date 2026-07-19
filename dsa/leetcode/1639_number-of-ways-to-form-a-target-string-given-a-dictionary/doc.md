# Number of Ways to Form a Target String Given a Dictionary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1639 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/) |

## Problem Description
### Goal
You are given a list `words` whose strings all have the same length and a string `target`. Form `target` from left to right by choosing characters from the dictionary.

To form `target[i]`, choose a character `words[j][k]` equal to it. After using column `k`, no character at column $k$ or any earlier column may be used again from any word; the next chosen column must therefore be strictly larger. Different word choices at the same selected columns count as different ways, and multiple chosen characters may come from the same word.

Return the number of valid ways modulo $10^9+7$.

### Function Contract
**Inputs**

- `words`: an array of $W$ lowercase English strings, where $1 \le W \le 1000$.
- Every word has the same length $L$, where $1 \le L \le 1000$.
- `target`: a lowercase English string of length $T$, where $1 \le T \le 1000$.

**Return value**

Return the number of sequences of strictly increasing dictionary columns and matching word choices that spell `target`, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `words = ["acca","bbbb","caca"], target = "aba"`
- Output: `6`

For example, columns 0, 1, and 3 can supply `a`, `b`, and `a`; the multiplicities of matching characters in those columns create several distinct word choices.

**Example 2**

- Input: `words = ["abba","baab"], target = "bab"`
- Output: `4`

**Example 3**

- Input: `words = ["abcd"], target = "abcd"`
- Output: `1`

The single word supplies each character from the next column.
