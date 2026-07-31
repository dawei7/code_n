# Longest Unequal Adjacent Groups Subsequence I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2900 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/) |

## Problem Description

### Goal

You are given two arrays of the same length $n$: an array of distinct strings `words` and a binary array `groups`. Each word is associated with the group value at its matching index.

Choose a subsequence of `words` whose indices remain in their original order. The subsequence is alternating when the `groups` values belonging to every two consecutive selected words are different; two consecutive selected indices may not both belong to group $0$ or both belong to group $1$.

Return a longest alternating subsequence. More than one longest answer may exist, and any one of them is valid.

### Function Contract

**Inputs**

- `words`: An array of pairwise distinct lowercase strings.
- `groups`: A binary array of the same length, assigning each word to group $0$ or group $1$.

The shared bounds are $1\le n\le100$ and $1\le\lvert\texttt{words[i]}\rvert\le10$.

**Return value**

Return any maximum-length subsequence of `words` whose corresponding adjacent group values alternate.

### Examples

**Example 1**

- Input: `words = ["e", "a", "b"], groups = [0, 0, 1]`
- Output: `["e", "b"]`
- Explanation: The selected group values are $0,1$. Choosing `["a", "b"]` would be another valid longest answer.

**Example 2**

- Input: `words = ["a", "b", "c", "d"], groups = [1, 0, 1, 1]`
- Output: `["a", "b", "c"]`
- Explanation: The selected group values are $1,0,1$. The final word belongs to the same last run as `"c"`, so replacing `"c"` by `"d"` gives another longest answer.
