# Can Make Palindrome from Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1177 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Bit Manipulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/can-make-palindrome-from-substring/) |

## Problem Description

### Goal

You are given a lowercase English string `s` and queries of the form `[left, right, k]`. For each query independently, take the inclusive substring `s[left:right + 1]`. You may rearrange its characters in any order and then replace at most `k` individual characters with any lowercase English letters.

Decide whether those operations can turn the queried substring into a palindrome. Return the Boolean answers in query order. Each replacement affects one character occurrence, and no query changes the original string used by any other query.

### Function Contract

**Inputs**

- `s`: A lowercase English string with $1 \leq \lvert s\rvert \leq 10^5$.
- `queries`: Between $1$ and $10^5$ triples `[left, right, k]`, where $0 \leq \texttt{left} \leq \texttt{right} < \lvert s\rvert$ and $0 \leq \texttt{k} \leq \lvert s\rvert$.
- Let $n=\lvert s\rvert$ and $q=\lvert\texttt{queries}\rvert$.

**Return value**

- A length-$q$ Boolean array whose entry $i$ is `True` exactly when query $i$ can produce a palindrome using at most its replacement budget.

### Examples

**Example 1**

- Input: `s = "abcda"`, `queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]`
- Output: `[true,false,false,true,true]`

For `[0,3,2]`, the four distinct letters require two replacements; for `[0,4,1]`, changing one of the three unpaired character types is enough.

**Example 2**

- Input: `s = "lyb"`, `queries = [[0,1,0],[2,2,1]]`
- Output: `[false,true]`

**Example 3**

- Input: `s = "aaa"`, `queries = [[0,2,0],[0,2,2]]`
- Output: `[true,true]`
