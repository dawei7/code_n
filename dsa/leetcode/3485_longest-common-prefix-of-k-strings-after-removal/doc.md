# Longest Common Prefix of K Strings After Removal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3485 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/) |

## Problem Description

### Goal

You are given an array `words` and an integer `k`. Consider removing each array element in turn. After removing `words[i]`, choose any `k` strings at distinct remaining indices and measure their longest common prefix.

For every original index `i`, determine the greatest prefix length achievable by some such selection of `k` remaining strings. The chosen strings may differ from one removal to the next, and equal string values at different indices still count as distinct choices.

Return one answer per removed index. If fewer than `k` strings remain after a removal, the corresponding answer is zero.

### Function Contract

**Inputs**

- `words`: A list of non-empty strings consisting only of lowercase English letters.
- `k`: The exact number of remaining strings whose common prefix is considered.

Let $n=\lvert\texttt{words}\rvert$ and define the total input length

$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert.
$$

The constraints are $1\le k\le n\le10^5$, $1\le\lvert\texttt{words[i]}\rvert\le10^4$, and $S\le10^5$.

**Return value**

Return a list `answer` of length $n$. For each index `i`, `answer[i]` is the maximum longest-common-prefix length among any `k` distinct remaining indices after removing `words[i]`, or zero when fewer than `k` strings remain.

### Examples

**Example 1**

- Input: `words = ["jump", "run", "run", "jump", "run"]`, `k = 2`
- Output: `[3, 4, 4, 3, 4]`

Removing a `jump` leaves at least two copies of `run`, whose common prefix has length 3. Removing a `run` leaves two copies of `jump`, giving length 4.

**Example 2**

- Input: `words = ["dog", "racer", "car"]`, `k = 2`
- Output: `[0, 0, 0]`

After any removal, the two remaining strings begin with different letters.

**Example 3**

- Input: `words = ["a", "ab", "abc"]`, `k = 2`
- Output: `[2, 1, 1]`

Removing `a` leaves two strings sharing `ab`; either other removal leaves a best common prefix of `a`.
