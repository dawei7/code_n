# Largest Merge Of Two Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1754 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-merge-of-two-strings/) |

## Problem Description

### Goal

You are given two strings, `word1` and `word2`. Build a new string by repeatedly choosing either nonempty word, taking its first character, appending that character to the merge, and deleting it from the chosen word.

Characters taken from either word must therefore retain their original relative order, although characters from the two words may be interleaved. Continue until both words are empty, and return the lexicographically largest merge obtainable through these choices.

### Function Contract

**Inputs**

- `word1`: a string of lowercase English letters with $1 \le \lvert\texttt{word1}\rvert \le 3000$.
- `word2`: a string of lowercase English letters with $1 \le \lvert\texttt{word2}\rvert \le 3000$.

Let $m=\lvert\texttt{word1}\rvert$, $n=\lvert\texttt{word2}\rvert$, and $S=m+n$.

**Return value**

- Return the lexicographically largest length-$S$ string that can be formed by interleaving the two inputs while preserving each input's character order.

### Examples

**Example 1**

- Input: `word1 = "cabaa", word2 = "bcaaa"`
- Output: `"cbcabaaaaa"`
- Explanation: Choosing `c` from `word1`, then `b` and `c` from the appropriate remaining prefixes, produces the largest possible beginning and ultimately the displayed merge.

**Example 2**

- Input: `word1 = "abcabc", word2 = "abdcaba"`
- Output: `"abdcabcabcaba"`
- Explanation: The equal initial `a` characters require comparing what follows; taking the `a` from `word2` preserves its larger suffix beginning with `b`, then `d`.

**Example 3**

- Input: `word1 = "zz", word2 = "a"`
- Output: `"zza"`
- Explanation: Both leading `z` characters are larger than `a`, so they must precede it.
