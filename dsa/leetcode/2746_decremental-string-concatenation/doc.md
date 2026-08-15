# Decremental String Concatenation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2746 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/decremental-string-concatenation/) |

## Problem Description

### Goal

An array `words` contains $n$ lowercase strings in a fixed order. Define `join(x, y)` as the concatenation of `x` followed by `y`, except that when the last character of `x` equals the first character of `y`, the two matching boundary characters contribute only one character. For example, `join("ab", "ba")` is `"aba"`, whereas `join("ab", "cde")` is `"abcde"`.

Begin with `words[0]`. For each subsequent `words[i]`, preserve the array order of processing but choose whether to join the new word to the right of the current string or join it to the left. After all $n-1$ choices have been made, return the minimum possible length of the resulting string.

### Function Contract

Let $n$ be the number of words.

**Inputs**

- `words`: An array of lowercase English strings, where $1 \le n \le 1000$ and $1 \le \lvert\texttt{words[i]}\rvert \le 50$.

**Return value**

Return the minimum attainable final length after processing every word and choosing a left or right join at each step.

### Examples

#### Example 1

- **Input:** `words = ["aa","ab","bc"]`
- **Output:** `4`
- **Explanation:** Appending both later words yields `"aabc"`; each join removes one matching boundary character.

#### Example 2

- **Input:** `words = ["ab","b"]`
- **Output:** `2`
- **Explanation:** Joining the second word on the right merges the two boundary `b` characters.

#### Example 3

- **Input:** `words = ["aaa","c","aba"]`
- **Output:** `6`
- **Explanation:** One optimal sequence joins `"c"` on the right and then `"aba"` on the left.
